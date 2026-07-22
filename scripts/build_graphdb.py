"""
GraphDB Knowledge Graph Builder

Replaces Neo4j entirely — loads IFRS-GICS knowledge graph into
Ontotext GraphDB using RDF triples and SPARQL.

Graph structure (matches KG diagram):
    gics:Sector -[kg:PARENT_OF]-> gics:IndustryGroup
    gics:IndustryGroup -[kg:PARENT_OF]-> gics:Industry
    gics:Industry -[kg:PARENT_OF]-> gics:SubIndustry
    gics:SubIndustry -[kg:HAS_RELEVANT_TAG]-> ifrs:XBRLTag
    ifrs:XBRLTag -[kg:HAS_CHILD_TAG]-> ifrs:XBRLTag          (summation rules, weight +1.0)
    ifrs:XBRLTag -[kg:HAS_CHILD_TAG_NEGATIVE]-> ifrs:XBRLTag (summation rules, weight -1.0)

SubIndustry → XBRL tag mapping is read directly from
data/mappings/subindustry_ifrs_mapping_v3_katana.json (already computed
on Katana HPC via the two-stage FinBERT + Qwen3 mapper). This script does
not recompute the mapping — it only loads it, plus the universal tags,
into GraphDB.

Setup:
    pip install SPARQLWrapper rdflib requests
    GraphDB running at http://localhost:7200 (docker compose up -d graphdb)
    Repository 'ifrs-gics' is auto-created if missing
"""

import json
import re
import requests
import xml.etree.ElementTree as ET
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS, XSD
from SPARQLWrapper import SPARQLWrapper, JSON

from d_20230318          import definition as gics_definition
from ifrs_tags           import definition as ifrs_definition
from universal_ifrs_tags import UNIVERSAL_TAGS


# ── Config ─────────────────────────────────────────────────────────────────────
GRAPHDB_URL  = "http://localhost:7200"
REPOSITORY   = "ifrs-gics"
SPARQL_URL   = f"{GRAPHDB_URL}/repositories/{REPOSITORY}"
UPDATE_URL   = f"{GRAPHDB_URL}/repositories/{REPOSITORY}/statements"

INPUT_JSON   = "data/mappings/subindustry_ifrs_mapping_v3_katana.json"

REPO_CONFIG_TTL = f"""
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rep: <http://www.openrdf.org/config/repository#> .
@prefix sr: <http://www.openrdf.org/config/repository/sail#> .
@prefix sail: <http://www.openrdf.org/config/sail#> .
@prefix graphdb: <http://www.ontotext.com/config/graphdb#> .

[] a rep:Repository ;
    rep:repositoryID "{REPOSITORY}" ;
    rdfs:label "IFRS-GICS Knowledge Graph" ;
    rep:repositoryImpl [
        rep:repositoryType "graphdb:SailRepository" ;
        sr:sailImpl [
            sail:sailType "graphdb:Sail" ;
            graphdb:ruleset "rdfsplus-optimized" ;
            graphdb:storage-folder "storage" ;
            graphdb:base-URL "http://example.org/owlim#" ;
            graphdb:repository-type "file-repository" ;
            graphdb:check-for-inconsistencies "false" ;
            graphdb:disable-sameAs "true" ;
            graphdb:enable-context-index "false" ;
            graphdb:enablePredicateList "true" ;
            graphdb:in-memory-literal-properties "true" ;
            graphdb:enable-literal-index "true" ;
            graphdb:throw-QueryEvaluationException-on-timeout "false" ;
            graphdb:query-timeout "0" ;
            graphdb:query-limit-results "0" ;
            graphdb:read-only "false" ;
        ]
    ] .
"""


# ── RDF Namespaces ─────────────────────────────────────────────────────────────
GICS = Namespace("http://gics.msci.com/ontology/")
IFRS = Namespace("http://xbrl.ifrs.org/taxonomy/2025/")
KG   = Namespace("http://ifrs-gics.ontotext.com/ontology/")


HAS_CHILD_TAG_RULES = [
    # (parent, child, weight) — weight +1.0 for addition, -1.0 for subtraction.
    # Sourced from the IFRS Accounting Taxonomy 2025-03-27 calculation linkbases
    # (cal_ias_1_*.xml, cal_ias_7_*.xml — Statement of Financial Position, Profit or
    # Loss, Comprehensive Income, Changes in Equity, Cash Flows), not hand-typed.
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForDecreaseIncreaseInInventories", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForDecreaseIncreaseInOtherOperatingReceivables", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForDecreaseIncreaseInTradeAccountReceivable", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForDepreciationAndAmortisationExpense", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForFairValueGainsLosses", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForFinanceCosts", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLoss", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForIncomeTaxExpense", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForIncreaseDecreaseInOtherOperatingPayables", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForIncreaseDecreaseInTradeAccountPayable", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForLossesGainsOnDisposalOfNoncurrentAssets", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForProvisions", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForSharebasedPayments", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForUnrealisedForeignExchangeLossesGains", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "OtherAdjustmentsForNoncashItems", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "OtherAdjustmentsForWhichCashEffectsAreInvestingOrFinancingCashFlow", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "OtherAdjustmentsToReconcileProfitLoss", 1.0),
    ("AdjustmentsForReconcileProfitLoss", "AdjustmentsForUndistributedProfitsOfAssociates", -1.0),
    ("Assets", "BiologicalAssets", 1.0),
    ("Assets", "CashAndCashEquivalents", 1.0),
    ("Assets", "CurrentAssets", 1.0),
    ("Assets", "CurrentTaxAssets", 1.0),
    ("Assets", "DeferredTaxAssets", 1.0),
    ("Assets", "Goodwill", 1.0),
    ("Assets", "InsuranceContractsIssuedThatAreAssets", 1.0),
    ("Assets", "IntangibleAssetsOtherThanGoodwill", 1.0),
    ("Assets", "InventoriesTotal", 1.0),
    ("Assets", "InvestmentAccountedForUsingEquityMethod", 1.0),
    ("Assets", "InvestmentProperty", 1.0),
    ("Assets", "InvestmentsInSubsidiariesJointVenturesAndAssociates", 1.0),
    ("Assets", "NoncashAssetsPledgedAsCollateralForWhichTransfereeHasRightByContractOrCustomToSellOrRepledgeCollateral", 1.0),
    ("Assets", "NoncurrentAssets", 1.0),
    ("Assets", "NoncurrentAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners", 1.0),
    ("Assets", "OtherFinancialAssets", 1.0),
    ("Assets", "OtherNonfinancialAssets", 1.0),
    ("Assets", "PropertyPlantAndEquipment", 1.0),
    ("Assets", "ReinsuranceContractsHeldThatAreAssets", 1.0),
    ("Assets", "TradeAndOtherReceivables", 1.0),
    ("CashFlowsFromUsedInFinancingActivities", "OtherInflowsOutflowsOfCashClassifiedAsFinancingActivities", 1.0),
    ("CashFlowsFromUsedInFinancingActivities", "ProceedsFromBorrowingsClassifiedAsFinancingActivities", 1.0),
    ("CashFlowsFromUsedInFinancingActivities", "ProceedsFromChangesInOwnershipInterestsInSubsidiaries", 1.0),
    ("CashFlowsFromUsedInFinancingActivities", "ProceedsFromGovernmentGrantsClassifiedAsFinancingActivities", 1.0),
    ("CashFlowsFromUsedInFinancingActivities", "ProceedsFromIssuingOtherEquityInstruments", 1.0),
    ("CashFlowsFromUsedInFinancingActivities", "ProceedsFromIssuingShares", 1.0),
    ("CashFlowsFromUsedInFinancingActivities", "DividendsPaidClassifiedAsFinancingActivities", -1.0),
    ("CashFlowsFromUsedInFinancingActivities", "IncomeTaxesPaidRefundClassifiedAsFinancingActivities", -1.0),
    ("CashFlowsFromUsedInFinancingActivities", "InterestPaidClassifiedAsFinancingActivities", -1.0),
    ("CashFlowsFromUsedInFinancingActivities", "PaymentsFromChangesInOwnershipInterestsInSubsidiaries", -1.0),
    ("CashFlowsFromUsedInFinancingActivities", "PaymentsOfLeaseLiabilitiesClassifiedAsFinancingActivities", -1.0),
    ("CashFlowsFromUsedInFinancingActivities", "PaymentsOfOtherEquityInstruments", -1.0),
    ("CashFlowsFromUsedInFinancingActivities", "PaymentsToAcquireOrRedeemEntitysShares", -1.0),
    ("CashFlowsFromUsedInFinancingActivities", "RepaymentsOfBorrowingsClassifiedAsFinancingActivities", -1.0),
    ("CashFlowsFromUsedInInvestingActivities", "CashFlowsFromLosingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities", 1.0),
    ("CashFlowsFromUsedInInvestingActivities", "CashReceiptsFromFutureContractsForwardContractsOptionContractsAndSwapContractsClassifiedAsInvestingActivities", 1.0),
    ("CashFlowsFromUsedInInvestingActivities", "CashReceiptsFromRepaymentOfAdvancesAndLoansMadeToOtherPartiesClassifiedAsInvestingActivities", 1.0),
    ("CashFlowsFromUsedInInvestingActivities", "DividendsReceivedClassifiedAsInvestingActivities", 1.0),
    ("CashFlowsFromUsedInInvestingActivities", "InterestReceivedClassifiedAsInvestingActivities", 1.0),
    ("CashFlowsFromUsedInInvestingActivities", "OtherCashReceiptsFromSalesOfEquityOrDebtInstrumentsOfOtherEntitiesClassifiedAsInvestingActivities", 1.0),
    ("CashFlowsFromUsedInInvestingActivities", "OtherCashReceiptsFromSalesOfInterestsInJointVenturesClassifiedAsInvestingActivities", 1.0),
    ("CashFlowsFromUsedInInvestingActivities", "OtherInflowsOutflowsOfCashClassifiedAsInvestingActivities", 1.0),
    ("CashFlowsFromUsedInInvestingActivities", "ProceedsFromGovernmentGrantsClassifiedAsInvestingActivities", 1.0),
    ("CashFlowsFromUsedInInvestingActivities", "ProceedsFromOtherLongtermAssetsClassifiedAsInvestingActivities", 1.0),
    ("CashFlowsFromUsedInInvestingActivities", "ProceedsFromSalesOfIntangibleAssetsClassifiedAsInvestingActivities", 1.0),
    ("CashFlowsFromUsedInInvestingActivities", "ProceedsFromSalesOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities", 1.0),
    ("CashFlowsFromUsedInInvestingActivities", "CashAdvancesAndLoansMadeToOtherPartiesClassifiedAsInvestingActivities", -1.0),
    ("CashFlowsFromUsedInInvestingActivities", "CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities", -1.0),
    ("CashFlowsFromUsedInInvestingActivities", "CashPaymentsForFutureContractsForwardContractsOptionContractsAndSwapContractsClassifiedAsInvestingActivities", -1.0),
    ("CashFlowsFromUsedInInvestingActivities", "IncomeTaxesPaidRefundClassifiedAsInvestingActivities", -1.0),
    ("CashFlowsFromUsedInInvestingActivities", "InterestPaidClassifiedAsInvestingActivities", -1.0),
    ("CashFlowsFromUsedInInvestingActivities", "OtherCashPaymentsToAcquireEquityOrDebtInstrumentsOfOtherEntitiesClassifiedAsInvestingActivities", -1.0),
    ("CashFlowsFromUsedInInvestingActivities", "OtherCashPaymentsToAcquireInterestsInJointVenturesClassifiedAsInvestingActivities", -1.0),
    ("CashFlowsFromUsedInInvestingActivities", "PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities", -1.0),
    ("CashFlowsFromUsedInInvestingActivities", "PurchaseOfOtherLongtermAssetsClassifiedAsInvestingActivities", -1.0),
    ("CashFlowsFromUsedInInvestingActivities", "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities", -1.0),
    ("CashFlowsFromUsedInOperatingActivities", "CashFlowsFromUsedInOperations", 1.0),
    ("CashFlowsFromUsedInOperatingActivities", "DividendsReceivedClassifiedAsOperatingActivities", 1.0),
    ("CashFlowsFromUsedInOperatingActivities", "InterestReceivedClassifiedAsOperatingActivities", 1.0),
    ("CashFlowsFromUsedInOperatingActivities", "OtherInflowsOutflowsOfCashClassifiedAsOperatingActivities", 1.0),
    ("CashFlowsFromUsedInOperatingActivities", "DividendsPaidClassifiedAsOperatingActivities", -1.0),
    ("CashFlowsFromUsedInOperatingActivities", "IncomeTaxesPaidRefundClassifiedAsOperatingActivities", -1.0),
    ("CashFlowsFromUsedInOperatingActivities", "InterestPaidClassifiedAsOperatingActivities", -1.0),
    ("CashFlowsFromUsedInOperations", "AdjustmentsForReconcileProfitLoss", 1.0),
    ("CashFlowsFromUsedInOperations", "OtherCashReceiptsFromOperatingActivities", 1.0),
    ("CashFlowsFromUsedInOperations", "ProfitLoss", 1.0),
    ("CashFlowsFromUsedInOperations", "ReceiptsFromContractsHeldForDealingOrTradingPurpose", 1.0),
    ("CashFlowsFromUsedInOperations", "ReceiptsFromRentsAndSubsequentSalesOfSuchAssets", 1.0),
    ("CashFlowsFromUsedInOperations", "ReceiptsFromRoyaltiesFeesCommissionsAndOtherRevenue", 1.0),
    ("CashFlowsFromUsedInOperations", "ReceiptsFromSalesOfGoodsAndRenderingOfServices", 1.0),
    ("CashFlowsFromUsedInOperations", "RecoveriesOnLoansPreviouslyWrittenOff", 1.0),
    ("CashFlowsFromUsedInOperations", "OtherCashPaymentsFromOperatingActivities", -1.0),
    ("CashFlowsFromUsedInOperations", "PaymentsFromContractsHeldForDealingOrTradingPurpose", -1.0),
    ("CashFlowsFromUsedInOperations", "PaymentsRelatingToRoyaltiesFeesAndCommissions", -1.0),
    ("CashFlowsFromUsedInOperations", "PaymentsToAndOnBehalfOfEmployees", -1.0),
    ("CashFlowsFromUsedInOperations", "PaymentsToManufactureOrAcquireAssetsHeldForRentalToOthersAndSubsequentlyHeldForSale", -1.0),
    ("CashFlowsFromUsedInOperations", "PaymentsToSuppliersForGoodsAndServices", -1.0),
    ("ChangesInEquity", "ComprehensiveIncome", 1.0),
    ("ChangesInEquity", "IncreaseDecreaseThroughChangesInOwnershipInterestsInSubsidiariesThatDoNotResultInLossOfControl", 1.0),
    ("ChangesInEquity", "IncreaseDecreaseThroughOtherContributionsByOwners", 1.0),
    ("ChangesInEquity", "IncreaseDecreaseThroughSharebasedPaymentTransactions", 1.0),
    ("ChangesInEquity", "IncreaseDecreaseThroughTransfersAndOtherChangesEquity", 1.0),
    ("ChangesInEquity", "IncreaseDecreaseThroughTreasuryShareTransactions", 1.0),
    ("ChangesInEquity", "IssueOfEquity", 1.0),
    ("ChangesInEquity", "AmountRemovedFromReserveOfCashFlowHedgesAndIncludedInInitialCostOrOtherCarryingAmountOfNonfinancialAssetLiabilityOrFirmCommitmentForWhichFairValueHedgeAccountingIsApplied", -1.0),
    ("ChangesInEquity", "AmountRemovedFromReserveOfChangeInValueOfForeignCurrencyBasisSpreadsAndIncludedInInitialCostOrOtherCarryingAmountOfNonfinancialAssetLiabilityOrFirmCommitmentForWhichFairValueHedgeAccountingIsApplied", -1.0),
    ("ChangesInEquity", "AmountRemovedFromReserveOfChangeInValueOfForwardElementsOfForwardContractsAndIncludedInInitialCostOrOtherCarryingAmountOfNonfinancialAssetLiabilityOrFirmCommitmentForWhichFairValueHedgeAccountingIsApplied", -1.0),
    ("ChangesInEquity", "AmountRemovedFromReserveOfChangeInValueOfTimeValueOfOptionsAndIncludedInInitialCostOrOtherCarryingAmountOfNonfinancialAssetLiabilityOrFirmCommitmentForWhichFairValueHedgeAccountingIsApplied", -1.0),
    ("ChangesInEquity", "DividendsPaid", -1.0),
    ("ChangesInEquity", "IncreaseDecreaseThroughOtherDistributionsToOwners", -1.0),
    ("ComprehensiveIncome", "OtherComprehensiveIncome", 1.0),
    ("ComprehensiveIncome", "ProfitLoss", 1.0),
    ("CurrentAssets", "CurrentAssetsOtherThanAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners", 1.0),
    ("CurrentAssets", "NoncurrentAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners", 1.0),
    ("CurrentAssetsOtherThanAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners", "CashAndCashEquivalents", 1.0),
    ("CurrentAssetsOtherThanAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners", "CurrentBiologicalAssets", 1.0),
    ("CurrentAssetsOtherThanAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners", "CurrentNoncashAssetsPledgedAsCollateralForWhichTransfereeHasRightByContractOrCustomToSellOrRepledgeCollateral", 1.0),
    ("CurrentAssetsOtherThanAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners", "CurrentTaxAssetsCurrent", 1.0),
    ("CurrentAssetsOtherThanAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners", "Inventories", 1.0),
    ("CurrentAssetsOtherThanAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners", "OtherCurrentFinancialAssets", 1.0),
    ("CurrentAssetsOtherThanAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners", "OtherCurrentNonfinancialAssets", 1.0),
    ("CurrentAssetsOtherThanAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners", "TradeAndOtherCurrentReceivables", 1.0),
    ("CurrentLiabilities", "CurrentLiabilitiesOtherThanLiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale", 1.0),
    ("CurrentLiabilities", "LiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale", 1.0),
    ("CurrentLiabilitiesOtherThanLiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale", "CurrentProvisions", 1.0),
    ("CurrentLiabilitiesOtherThanLiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale", "CurrentTaxLiabilitiesCurrent", 1.0),
    ("CurrentLiabilitiesOtherThanLiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale", "OtherCurrentFinancialLiabilities", 1.0),
    ("CurrentLiabilitiesOtherThanLiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale", "OtherCurrentNonfinancialLiabilities", 1.0),
    ("CurrentLiabilitiesOtherThanLiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale", "TradeAndOtherCurrentPayables", 1.0),
    ("CurrentProvisions", "CurrentProvisionsForEmployeeBenefits", 1.0),
    ("CurrentProvisions", "OtherShorttermProvisions", 1.0),
    ("Equity", "EquityAttributableToOwnersOfParent", 1.0),
    ("Equity", "NoncontrollingInterests", 1.0),
    ("EquityAndLiabilities", "Equity", 1.0),
    ("EquityAndLiabilities", "Liabilities", 1.0),
    ("EquityAttributableToOwnersOfParent", "IssuedCapital", 1.0),
    ("EquityAttributableToOwnersOfParent", "OtherEquityInterest", 1.0),
    ("EquityAttributableToOwnersOfParent", "OtherReserves", 1.0),
    ("EquityAttributableToOwnersOfParent", "RetainedEarnings", 1.0),
    ("EquityAttributableToOwnersOfParent", "SharePremium", 1.0),
    ("EquityAttributableToOwnersOfParent", "TreasuryShares", -1.0),
    ("GrossProfit", "Revenue", 1.0),
    ("GrossProfit", "CostOfSales", -1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToAvailableforsaleFinancialAssetsOfOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToCashFlowHedgesOfOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToChangeInValueOfForeignCurrencyBasisSpreadsOfOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToChangeInValueOfForwardElementsOfForwardContractsOfOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToChangeInValueOfTimeValueOfOptionsOfOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToExchangeDifferencesOnTranslationOfOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToFinanceIncomeExpensesFromReinsuranceContractsHeldOfOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToHedgesOfNetInvestmentsInForeignOperationsOfOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLoss", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToChangesInFairValueOfFinancialLiabilityAttributableToChangeInCreditRiskOfLiabilityOfOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToChangesInRevaluationSurplusOfOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToExchangeDifferencesOnTranslationOtherThanTranslationOfForeignOperationsIncludedInOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToHedgesOfInvestmentsInEquityInstrumentsOfOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToInvestmentsInEquityInstrumentsOfOtherComprehensiveIncome", 1.0),
    ("IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLoss", "IncomeTaxRelatingToRemeasurementsOfDefinedBenefitPlansOfOtherComprehensiveIncome", 1.0),
    ("IncreaseDecreaseInCashAndCashEquivalents", "EffectOfExchangeRateChangesOnCashAndCashEquivalents", 1.0),
    ("IncreaseDecreaseInCashAndCashEquivalents", "IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges", 1.0),
    ("IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges", "CashFlowsFromUsedInFinancingActivities", 1.0),
    ("IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges", "CashFlowsFromUsedInInvestingActivities", 1.0),
    ("IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges", "CashFlowsFromUsedInOperatingActivities", 1.0),
    ("Liabilities", "CurrentLiabilities", 1.0),
    ("Liabilities", "CurrentTaxLiabilities", 1.0),
    ("Liabilities", "DeferredTaxLiabilities", 1.0),
    ("Liabilities", "InsuranceContractsIssuedThatAreLiabilities", 1.0),
    ("Liabilities", "LiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale", 1.0),
    ("Liabilities", "NoncurrentLiabilities", 1.0),
    ("Liabilities", "OtherFinancialLiabilities", 1.0),
    ("Liabilities", "OtherNonfinancialLiabilities", 1.0),
    ("Liabilities", "Provisions", 1.0),
    ("Liabilities", "ReinsuranceContractsHeldThatAreLiabilities", 1.0),
    ("Liabilities", "TradeAndOtherPayables", 1.0),
    ("NoncurrentAssets", "CurrentTaxAssetsNoncurrent", 1.0),
    ("NoncurrentAssets", "DeferredTaxAssets", 1.0),
    ("NoncurrentAssets", "Goodwill", 1.0),
    ("NoncurrentAssets", "IntangibleAssetsOtherThanGoodwill", 1.0),
    ("NoncurrentAssets", "InvestmentAccountedForUsingEquityMethod", 1.0),
    ("NoncurrentAssets", "InvestmentProperty", 1.0),
    ("NoncurrentAssets", "InvestmentsInSubsidiariesJointVenturesAndAssociates", 1.0),
    ("NoncurrentAssets", "NoncurrentBiologicalAssets", 1.0),
    ("NoncurrentAssets", "NoncurrentInventories", 1.0),
    ("NoncurrentAssets", "NoncurrentNoncashAssetsPledgedAsCollateralForWhichTransfereeHasRightByContractOrCustomToSellOrRepledgeCollateral", 1.0),
    ("NoncurrentAssets", "NoncurrentReceivables", 1.0),
    ("NoncurrentAssets", "OtherNoncurrentFinancialAssets", 1.0),
    ("NoncurrentAssets", "OtherNoncurrentNonfinancialAssets", 1.0),
    ("NoncurrentAssets", "PropertyPlantAndEquipment", 1.0),
    ("NoncurrentLiabilities", "CurrentTaxLiabilitiesNoncurrent", 1.0),
    ("NoncurrentLiabilities", "DeferredTaxLiabilities", 1.0),
    ("NoncurrentLiabilities", "NoncurrentPayables", 1.0),
    ("NoncurrentLiabilities", "NoncurrentProvisions", 1.0),
    ("NoncurrentLiabilities", "OtherNoncurrentFinancialLiabilities", 1.0),
    ("NoncurrentLiabilities", "OtherNoncurrentNonfinancialLiabilities", 1.0),
    ("NoncurrentProvisions", "NoncurrentProvisionsForEmployeeBenefits", 1.0),
    ("NoncurrentProvisions", "OtherLongtermProvisions", 1.0),
    ("OtherComprehensiveIncome", "OtherComprehensiveIncomeBeforeTax", 1.0),
    ("OtherComprehensiveIncome", "OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax", 1.0),
    ("OtherComprehensiveIncome", "OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossNetOfTax", 1.0),
    ("OtherComprehensiveIncome", "IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss", -1.0),
    ("OtherComprehensiveIncome", "IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLoss", -1.0),
    ("OtherComprehensiveIncome", "IncomeTaxRelatingToShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodThatWillBeReclassifiedToProfitOrLoss", -1.0),
    ("OtherComprehensiveIncome", "IncomeTaxRelatingToShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodThatWillNotBeReclassifiedToProfitOrLoss", -1.0),
    ("OtherComprehensiveIncomeBeforeTax", "OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax", 1.0),
    ("OtherComprehensiveIncomeBeforeTax", "OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", 1.0),
    ("OtherComprehensiveIncomeBeforeTaxAvailableforsaleFinancialAssets", "GainsLossesOnRemeasuringAvailableforsaleFinancialAssetsBeforeTax", 1.0),
    ("OtherComprehensiveIncomeBeforeTaxAvailableforsaleFinancialAssets", "ReclassificationAdjustmentsOnAvailableforsaleFinancialAssetsBeforeTax", -1.0),
    ("OtherComprehensiveIncomeBeforeTaxCashFlowHedges", "GainsLossesOnCashFlowHedgesBeforeTax", 1.0),
    ("OtherComprehensiveIncomeBeforeTaxCashFlowHedges", "AmountsRemovedFromEquityAndIncludedInCarryingAmountOfNonfinancialAssetLiabilityWhoseAcquisitionOrIncurrenceWasHedgedHighlyProbableForecastTransactionBeforeTax", -1.0),
    ("OtherComprehensiveIncomeBeforeTaxCashFlowHedges", "ReclassificationAdjustmentsOnCashFlowHedgesBeforeTax", -1.0),
    ("OtherComprehensiveIncomeBeforeTaxChangeInValueOfForeignCurrencyBasisSpreads", "GainsLossesOnChangeInValueOfForeignCurrencyBasisSpreadsBeforeTax", 1.0),
    ("OtherComprehensiveIncomeBeforeTaxChangeInValueOfForeignCurrencyBasisSpreads", "ReclassificationAdjustmentsOnChangeInValueOfForeignCurrencyBasisSpreadsBeforeTax", -1.0),
    ("OtherComprehensiveIncomeBeforeTaxChangeInValueOfForwardElementsOfForwardContracts", "GainsLossesOnChangeInValueOfForwardElementsOfForwardContractsBeforeTax", 1.0),
    ("OtherComprehensiveIncomeBeforeTaxChangeInValueOfForwardElementsOfForwardContracts", "ReclassificationAdjustmentsOnChangeInValueOfForwardElementsOfForwardContractsBeforeTax", -1.0),
    ("OtherComprehensiveIncomeBeforeTaxChangeInValueOfTimeValueOfOptions", "GainsLossesOnChangeInValueOfTimeValueOfOptionsBeforeTax", 1.0),
    ("OtherComprehensiveIncomeBeforeTaxChangeInValueOfTimeValueOfOptions", "ReclassificationAdjustmentsOnChangeInValueOfTimeValueOfOptionsBeforeTax", -1.0),
    ("OtherComprehensiveIncomeBeforeTaxExchangeDifferencesOnTranslation", "GainsLossesOnExchangeDifferencesOnTranslationBeforeTax", 1.0),
    ("OtherComprehensiveIncomeBeforeTaxExchangeDifferencesOnTranslation", "ReclassificationAdjustmentsOnExchangeDifferencesOnTranslationBeforeTax", -1.0),
    ("OtherComprehensiveIncomeBeforeTaxFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLoss", "FinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLossBeforeTax", 1.0),
    ("OtherComprehensiveIncomeBeforeTaxFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLoss", "ReclassificationAdjustmentsOnFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLossBeforeTax", -1.0),
    ("OtherComprehensiveIncomeBeforeTaxFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome", "GainsLossesOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeBeforeTax", 1.0),
    ("OtherComprehensiveIncomeBeforeTaxFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome", "AmountsRemovedFromEquityAndAdjustedAgainstFairValueOfFinancialAssetsOnReclassificationOutOfFairValueThroughOtherComprehensiveIncomeMeasurementCategoryBeforeTax", -1.0),
    ("OtherComprehensiveIncomeBeforeTaxFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome", "ReclassificationAdjustmentsOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeBeforeTax", -1.0),
    ("OtherComprehensiveIncomeBeforeTaxHedgesOfNetInvestmentsInForeignOperations", "GainsLossesOnHedgesOfNetInvestmentsInForeignOperationsBeforeTax", 1.0),
    ("OtherComprehensiveIncomeBeforeTaxHedgesOfNetInvestmentsInForeignOperations", "ReclassificationAdjustmentsOnHedgesOfNetInvestmentsInForeignOperationsBeforeTax", -1.0),
    ("OtherComprehensiveIncomeBeforeTaxInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLoss", "InsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLossBeforeTax", 1.0),
    ("OtherComprehensiveIncomeBeforeTaxInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLoss", "ReclassificationAdjustmentsOnInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossBeforeTax", -1.0),
    ("OtherComprehensiveIncomeNetOfTaxAvailableforsaleFinancialAssets", "GainsLossesOnRemeasuringAvailableforsaleFinancialAssetsNetOfTax", 1.0),
    ("OtherComprehensiveIncomeNetOfTaxAvailableforsaleFinancialAssets", "ReclassificationAdjustmentsOnAvailableforsaleFinancialAssetsNetOfTax", -1.0),
    ("OtherComprehensiveIncomeNetOfTaxCashFlowHedges", "GainsLossesOnCashFlowHedgesNetOfTax", 1.0),
    ("OtherComprehensiveIncomeNetOfTaxCashFlowHedges", "AdjustmentsForAmountsTransferredToInitialCarryingAmountOfHedgedItems", -1.0),
    ("OtherComprehensiveIncomeNetOfTaxCashFlowHedges", "ReclassificationAdjustmentsOnCashFlowHedgesNetOfTax", -1.0),
    ("OtherComprehensiveIncomeNetOfTaxChangeInValueOfForeignCurrencyBasisSpreads", "GainsLossesOnChangeInValueOfForeignCurrencyBasisSpreadsNetOfTax", 1.0),
    ("OtherComprehensiveIncomeNetOfTaxChangeInValueOfForeignCurrencyBasisSpreads", "ReclassificationAdjustmentsOnChangeInValueOfForeignCurrencyBasisSpreadsNetOfTax", -1.0),
    ("OtherComprehensiveIncomeNetOfTaxChangeInValueOfForwardElementsOfForwardContracts", "GainsLossesOnChangeInValueOfForwardElementsOfForwardContractsNetOfTax", 1.0),
    ("OtherComprehensiveIncomeNetOfTaxChangeInValueOfForwardElementsOfForwardContracts", "ReclassificationAdjustmentsOnChangeInValueOfForwardElementsOfForwardContractsNetOfTax", -1.0),
    ("OtherComprehensiveIncomeNetOfTaxChangeInValueOfTimeValueOfOptions", "GainsLossesOnChangeInValueOfTimeValueOfOptionsNetOfTax", 1.0),
    ("OtherComprehensiveIncomeNetOfTaxChangeInValueOfTimeValueOfOptions", "ReclassificationAdjustmentsOnChangeInValueOfTimeValueOfOptionsNetOfTax", -1.0),
    ("OtherComprehensiveIncomeNetOfTaxExchangeDifferencesOnTranslation", "GainsLossesOnExchangeDifferencesOnTranslationNetOfTax", 1.0),
    ("OtherComprehensiveIncomeNetOfTaxExchangeDifferencesOnTranslation", "ReclassificationAdjustmentsOnExchangeDifferencesOnTranslationNetOfTax", -1.0),
    ("OtherComprehensiveIncomeNetOfTaxFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLoss", "FinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLossNetOfTax", 1.0),
    ("OtherComprehensiveIncomeNetOfTaxFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLoss", "ReclassificationAdjustmentsOnFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLossNetOfTax", -1.0),
    ("OtherComprehensiveIncomeNetOfTaxFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome", "GainsLossesOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeNetOfTax", 1.0),
    ("OtherComprehensiveIncomeNetOfTaxFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome", "AmountsRemovedFromEquityAndAdjustedAgainstFairValueOfFinancialAssetsOnReclassificationOutOfFairValueThroughOtherComprehensiveIncomeMeasurementCategoryNetOfTax", -1.0),
    ("OtherComprehensiveIncomeNetOfTaxFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome", "ReclassificationAdjustmentsOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeNetOfTax", -1.0),
    ("OtherComprehensiveIncomeNetOfTaxHedgesOfNetInvestmentsInForeignOperations", "GainsLossesOnHedgesOfNetInvestmentsInForeignOperationsNetOfTax", 1.0),
    ("OtherComprehensiveIncomeNetOfTaxHedgesOfNetInvestmentsInForeignOperations", "ReclassificationAdjustmentsOnHedgesOfNetInvestmentsInForeignOperationsNetOfTax", -1.0),
    ("OtherComprehensiveIncomeNetOfTaxInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLoss", "InsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLossNetOfTax", 1.0),
    ("OtherComprehensiveIncomeNetOfTaxInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLoss", "ReclassificationAdjustmentsOnInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossNetOfTax", -1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxAvailableforsaleFinancialAssets", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxCashFlowHedges", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxChangeInValueOfForeignCurrencyBasisSpreads", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxChangeInValueOfForwardElementsOfForwardContracts", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxChangeInValueOfTimeValueOfOptions", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxExchangeDifferencesOnTranslation", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLoss", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxHedgesOfNetInvestmentsInForeignOperations", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLoss", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax", "ShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodThatWillBeReclassifiedToProfitOrLossBeforeTax", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxAvailableforsaleFinancialAssets", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxCashFlowHedges", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxChangeInValueOfForeignCurrencyBasisSpreads", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxChangeInValueOfForwardElementsOfForwardContracts", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxChangeInValueOfTimeValueOfOptions", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxExchangeDifferencesOnTranslation", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLoss", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxHedgesOfNetInvestmentsInForeignOperations", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLoss", 1.0),
    ("OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax", "ShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodThatWillBeReclassifiedToProfitOrLossNetOfTax", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxChangeInFairValueOfFinancialLiabilityAttributableToChangeInCreditRiskOfLiability", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxExchangeDifferencesOnTranslationOtherThanTranslationOfForeignOperations", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxGainsLossesFromInvestmentsInEquityInstruments", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxGainsLossesOnHedgingInstrumentsThatHedgeInvestmentsInEquityInstruments", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxGainsLossesOnRemeasurementsOfDefinedBenefitPlans", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxGainsLossesOnRevaluation", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", "OtherComprehensiveIncomeBeforeTaxInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillNotBeReclassifiedToProfitOrLoss", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax", "ShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodThatWillNotBeReclassifiedToProfitOrLossBeforeTax", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxChangeInFairValueOfFinancialLiabilityAttributableToChangeInCreditRiskOfLiability", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxExchangeDifferencesOnTranslationOtherThanTranslationOfForeignOperations", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxGainsLossesFromInvestmentsInEquityInstruments", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxGainsLossesOnHedgingInstrumentsThatHedgeInvestmentsInEquityInstruments", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxGainsLossesOnRemeasurementsOfDefinedBenefitPlans", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxGainsLossesOnRevaluation", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossNetOfTax", "OtherComprehensiveIncomeNetOfTaxInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillNotBeReclassifiedToProfitOrLoss", 1.0),
    ("OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossNetOfTax", "ShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodThatWillNotBeReclassifiedToProfitOrLossNetOfTax", 1.0),
    ("ProfitLoss", "ProfitLossFromContinuingOperations", 1.0),
    ("ProfitLoss", "ProfitLossFromDiscontinuedOperations", 1.0),
    ("ProfitLossBeforeTax", "CumulativeGainLossPreviouslyRecognisedInOtherComprehensiveIncomeArisingFromReclassificationOfFinancialAssetsOutOfFairValueThroughOtherComprehensiveIncomeIntoFairValueThroughProfitOrLossMeasurementCategory", 1.0),
    ("ProfitLossBeforeTax", "DifferenceBetweenCarryingAmountOfDividendsPayableAndCarryingAmountOfNoncashAssetsDistributed", 1.0),
    ("ProfitLossBeforeTax", "FinanceIncome", 1.0),
    ("ProfitLossBeforeTax", "FinanceIncomeExpensesFromReinsuranceContractsHeldRecognisedInProfitOrLoss", 1.0),
    ("ProfitLossBeforeTax", "GainLossArisingFromDerecognitionOfFinancialAssetsMeasuredAtAmortisedCost", 1.0),
    ("ProfitLossBeforeTax", "GainsLossesArisingFromDifferenceBetweenPreviousCarryingAmountAndFairValueOfFinancialAssetsReclassifiedAsMeasuredAtFairValue", 1.0),
    ("ProfitLossBeforeTax", "GainsLossesOnNetMonetaryPosition", 1.0),
    ("ProfitLossBeforeTax", "HedgingGainsLossesForHedgeOfGroupOfItemsWithOffsettingRiskPositions", 1.0),
    ("ProfitLossBeforeTax", "InsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedRecognisedInProfitOrLoss", 1.0),
    ("ProfitLossBeforeTax", "OtherIncomeExpenseFromSubsidiariesJointlyControlledEntitiesAndAssociates", 1.0),
    ("ProfitLossBeforeTax", "ProfitLossFromOperatingActivities", 1.0),
    ("ProfitLossBeforeTax", "ShareOfProfitLossOfAssociatesAndJointVenturesAccountedForUsingEquityMethod", 1.0),
    ("ProfitLossBeforeTax", "FinanceCosts", -1.0),
    ("ProfitLossBeforeTax", "ImpairmentLossImpairmentGainAndReversalOfImpairmentLossDeterminedInAccordanceWithIFRS9", -1.0),
    ("ProfitLossFromContinuingOperations", "ProfitLossBeforeTax", 1.0),
    ("ProfitLossFromContinuingOperations", "IncomeTaxExpenseContinuingOperations", -1.0),
    ("ProfitLossFromOperatingActivities", "GrossProfit", 1.0),
    ("ProfitLossFromOperatingActivities", "IncomeExpensesFromReinsuranceContractsHeldOtherThanFinanceIncomeExpenses", 1.0),
    ("ProfitLossFromOperatingActivities", "OtherGainsLosses", 1.0),
    ("ProfitLossFromOperatingActivities", "OtherIncome", 1.0),
    ("ProfitLossFromOperatingActivities", "OtherWorkPerformedByEntityAndCapitalised", 1.0),
    ("ProfitLossFromOperatingActivities", "Revenue", 1.0),
    ("ProfitLossFromOperatingActivities", "AdministrativeExpense", -1.0),
    ("ProfitLossFromOperatingActivities", "ChangesInInventoriesOfFinishedGoodsAndWorkInProgress", -1.0),
    ("ProfitLossFromOperatingActivities", "DepreciationAndAmortisationExpense", -1.0),
    ("ProfitLossFromOperatingActivities", "DistributionCosts", -1.0),
    ("ProfitLossFromOperatingActivities", "EmployeeBenefitsExpense", -1.0),
    ("ProfitLossFromOperatingActivities", "ImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLoss", -1.0),
    ("ProfitLossFromOperatingActivities", "InsuranceServiceExpensesFromInsuranceContractsIssued", -1.0),
    ("ProfitLossFromOperatingActivities", "OtherExpenseByFunction", -1.0),
    ("ProfitLossFromOperatingActivities", "OtherExpenseByNature", -1.0),
    ("ProfitLossFromOperatingActivities", "RawMaterialsAndConsumablesUsed", -1.0),
    ("Provisions", "OtherProvisions", 1.0),
    ("Provisions", "ProvisionsForEmployeeBenefits", 1.0),
]


# ── Helpers ────────────────────────────────────────────────────────────────────

def camel_to_sentence(name: str) -> str:
    s = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', s)
    return s.strip()


def load_ifrs_labels() -> dict:
    label_map = {}
    tree = ET.parse("data/taxonomy/lab_full_ifrs-en_2025-03-27.xml")
    root = tree.getroot()
    ns   = {"link": "http://www.xbrl.org/2003/linkbase"}
    for label in root.findall(".//link:label", ns):
        id_attr = label.get("id", "")
        text    = label.text or ""
        if (id_attr.startswith("ifrs-full_")
                and id_attr.endswith("_label")
                and text and "[" not in text):
            tag = id_attr[len("ifrs-full_"):-len("_label")]
            if tag not in label_map:
                label_map[tag] = text
    for tag in ifrs_definition:
        if tag not in label_map:
            label_map[tag] = camel_to_sentence(tag)
    return label_map


# ── GraphDB RDF loader ─────────────────────────────────────────────────────────

class GraphDBLoader:

    def __init__(self):
        self.update_url = UPDATE_URL
        self._ensure_repository()
        self.sparql = SPARQLWrapper(SPARQL_URL)
        self.sparql.setReturnFormat(JSON)
        self._test_connection()

    def _ensure_repository(self):
        """Create the repository if it doesn't already exist."""
        resp = requests.get(f"{GRAPHDB_URL}/rest/repositories")
        if resp.status_code != 200:
            raise ConnectionError(
                f"Cannot reach GraphDB at {GRAPHDB_URL}: {resp.status_code}\n"
                f"Make sure GraphDB is running (docker compose up -d graphdb)"
            )
        existing = {r["id"] for r in resp.json()}
        if REPOSITORY in existing:
            print(f"  ✓ Repository '{REPOSITORY}' already exists")
            return

        create_resp = requests.post(
            f"{GRAPHDB_URL}/rest/repositories",
            files={"config": ("repo-config.ttl", REPO_CONFIG_TTL, "text/turtle")},
        )
        if create_resp.status_code not in (200, 201):
            raise Exception(
                f"Repository creation failed: {create_resp.status_code} "
                f"{create_resp.text[:300]}"
            )
        print(f"  ✓ Repository '{REPOSITORY}' created")

    def _test_connection(self):
        try:
            self.sparql.setQuery("SELECT * WHERE { ?s ?p ?o } LIMIT 1")
            self.sparql.query()
            print(f"  ✓ Connected to GraphDB at {GRAPHDB_URL}")
            print(f"  ✓ Repository: {REPOSITORY}")
        except Exception as e:
            raise ConnectionError(f"Cannot connect to GraphDB: {e}\n"
                                  f"Make sure GraphDB is running at {GRAPHDB_URL}")

    def clear(self):
        """Clear all triples from repository."""
        response = requests.delete(UPDATE_URL)
        if response.status_code not in (200, 204):
            raise Exception(f"Clear failed: {response.status_code}")
        print("  ✓ Repository cleared")

    def _insert_triples(self, g: Graph):
        """Insert an rdflib Graph into GraphDB via REST API."""
        turtle_data = g.serialize(format="turtle")
        response    = requests.post(
            UPDATE_URL,
            data    = turtle_data.encode("utf-8"),
            headers = {"Content-Type": "text/turtle"},
        )
        if response.status_code not in (200, 204):
            raise Exception(f"GraphDB insert failed: {response.status_code} {response.text[:200]}")

    def load_ontology(self):
        """Define the ontology classes and properties."""
        g = Graph()
        g.bind("gics", GICS)
        g.bind("ifrs", IFRS)
        g.bind("kg",   KG)

        # Classes
        for cls in ["Sector", "IndustryGroup", "Industry", "SubIndustry", "XBRLTag"]:
            g.add((KG[cls], RDF.type, RDFS.Class))
            g.add((KG[cls], RDFS.label, Literal(cls)))

        # Properties
        props = {
            "PARENT_OF":       ("GICS hierarchy parent-child relationship", KG.Sector,      KG.IndustryGroup),
            "HAS_RELEVANT_TAG":("Maps a GICS SubIndustry to relevant XBRL tags", KG.SubIndustry, KG.XBRLTag),
            "HAS_CHILD_TAG":   ("XBRL summation rule (additive) — parent tag contains child tag", KG.XBRLTag, KG.XBRLTag),
            "HAS_CHILD_TAG_NEGATIVE": ("XBRL summation rule (subtractive) — parent tag subtracts child tag", KG.XBRLTag, KG.XBRLTag),
        }
        for prop, (comment, domain, range_) in props.items():
            g.add((KG[prop], RDF.type,         RDF["Property"]))
            g.add((KG[prop], RDFS.label,       Literal(prop)))
            g.add((KG[prop], RDFS.comment,     Literal(comment)))
            g.add((KG[prop], RDFS.domain,      domain))
            g.add((KG[prop], RDFS.range,       range_))

        self._insert_triples(g)
        print("  ✓ Ontology loaded")

    def load_gics_hierarchy(self):
        """Load GICS nodes and PARENT_OF relationships."""
        g = Graph()
        g.bind("gics", GICS)
        g.bind("kg",   KG)
        g.bind("rdfs", RDFS)

        counts = {2: 0, 4: 0, 6: 0, 8: 0}

        for code, data in gics_definition.items():
            name = data.get("name", "")
            desc = data.get("description", "")
            n    = len(code)

            # Determine node type
            if n == 2:
                node_type = KG.Sector
            elif n == 4:
                node_type = KG.IndustryGroup
            elif n == 6:
                node_type = KG.Industry
            elif n == 8:
                node_type = KG.SubIndustry
            else:
                continue

            uri = GICS[code]
            g.add((uri, RDF.type,           node_type))
            g.add((uri, RDFS.label,         Literal(name)))
            g.add((uri, GICS.code,          Literal(code)))

            if desc:
                g.add((uri, RDFS.comment, Literal(desc)))

            # PARENT_OF relationship
            if n > 2:
                parent_code = code[:n-2]
                parent_uri  = GICS[parent_code]
                g.add((parent_uri, KG.PARENT_OF, uri))

            counts[n] += 1

        self._insert_triples(g)
        print(f"  ✓ GICS: {counts[2]} sectors, {counts[4]} groups, "
              f"{counts[6]} industries, {counts[8]} sub-industries")
        print(f"  ✓ PARENT_OF edges: {counts[4]+counts[6]+counts[8]}")

    def load_xbrl_tags(self, label_map: dict):
        """Load all XBRL tag nodes."""
        g     = Graph()
        g.bind("ifrs", IFRS)
        g.bind("kg",   KG)
        g.bind("rdfs", RDFS)

        for name, meta in ifrs_definition.items():
            label      = label_map.get(name, camel_to_sentence(name))
            uri        = IFRS[name]
            is_univ    = name in UNIVERSAL_TAGS

            g.add((uri, RDF.type,         KG.XBRLTag))
            g.add((uri, RDFS.label,       Literal(label)))
            g.add((uri, IFRS.tagName,     Literal(name)))
            g.add((uri, IFRS.isUniversal, Literal(is_univ, datatype=XSD.boolean)))

            if meta.get("balance"):
                g.add((uri, IFRS.balance, Literal(meta["balance"])))
            if meta.get("period_type"):
                g.add((uri, IFRS.periodType, Literal(meta["period_type"])))

        self._insert_triples(g)
        print(f"  ✓ XBRLTag nodes: {len(ifrs_definition)}")

    def load_universal_tags(self):
        """
        Universal tags → HAS_RELEVANT_TAG from every SubIndustry.
        These apply to all companies regardless of sub-industry, and are
        loaded before the sub-industry-specific tags so every SubIndustry
        has at least this baseline set.
        """
        g = Graph()
        g.bind("gics", GICS)
        g.bind("ifrs", IFRS)
        g.bind("kg",   KG)

        si_codes = [c for c in gics_definition if len(c) == 8]
        count    = 0

        for si_code in si_codes:
            si_uri = GICS[si_code]
            for tag in UNIVERSAL_TAGS:
                if tag in ifrs_definition:
                    g.add((si_uri, KG.HAS_RELEVANT_TAG, IFRS[tag]))
                    count += 1

        self._insert_triples(g)
        print(f"  ✓ Universal HAS_RELEVANT_TAG: {count} triples "
              f"({len(UNIVERSAL_TAGS)} tags × {len(si_codes)} sub-industries)")

    def load_subindustry_tags(self, mapping: dict):
        """Load SubIndustry -[HAS_RELEVANT_TAG]-> XBRLTag."""
        g     = Graph()
        g.bind("gics", GICS)
        g.bind("ifrs", IFRS)
        g.bind("kg",   KG)

        total = 0
        for si_code, tags in mapping.items():
            si_uri = GICS[si_code]
            for tag in tags:
                if tag in ifrs_definition:
                    g.add((si_uri, KG.HAS_RELEVANT_TAG, IFRS[tag]))
                    total += 1

        self._insert_triples(g)
        print(f"  ✓ SubIndustry HAS_RELEVANT_TAG: {total} triples")

    def load_has_child_tag(self):
        """
        Load XBRLTag -[HAS_CHILD_TAG]-> XBRLTag summation rules (weight +1.0)
        and XBRLTag -[HAS_CHILD_TAG_NEGATIVE]-> XBRLTag (weight -1.0, e.g.
        GrossProfit = Revenue - CostOfSales). Two predicates rather than a
        single weighted edge — keeps triples flat, no reification needed.
        """
        g = Graph()
        g.bind("ifrs", IFRS)
        g.bind("kg",   KG)

        pos_count, neg_count = 0, 0
        for parent_tag, child_tag, weight in HAS_CHILD_TAG_RULES:
            if parent_tag not in ifrs_definition or child_tag not in ifrs_definition:
                continue
            if weight > 0:
                g.add((IFRS[parent_tag], KG.HAS_CHILD_TAG, IFRS[child_tag]))
                pos_count += 1
            else:
                g.add((IFRS[parent_tag], KG.HAS_CHILD_TAG_NEGATIVE, IFRS[child_tag]))
                neg_count += 1

        self._insert_triples(g)
        print(f"  ✓ HAS_CHILD_TAG summation rules: {pos_count} additive, {neg_count} subtractive")

    def verify(self):
        """Run verification SPARQL queries."""
        queries = {
            "Total triples": "SELECT (COUNT(*) AS ?c) WHERE { ?s ?p ?o }",
            "Sectors":       "SELECT (COUNT(*) AS ?c) WHERE { ?s a kg:Sector }",
            "XBRLTags":      "SELECT (COUNT(*) AS ?c) WHERE { ?s a kg:XBRLTag }",
            "SubIndustries": "SELECT (COUNT(*) AS ?c) WHERE { ?s a kg:SubIndustry }",
            "PARENT_OF":     "SELECT (COUNT(*) AS ?c) WHERE { ?s kg:PARENT_OF ?o }",
            "HAS_RELEVANT_TAG": "SELECT (COUNT(*) AS ?c) WHERE { ?s kg:HAS_RELEVANT_TAG ?o }",
            "HAS_CHILD_TAG": "SELECT (COUNT(*) AS ?c) WHERE { ?s kg:HAS_CHILD_TAG ?o }",
            "HAS_CHILD_TAG_NEGATIVE": "SELECT (COUNT(*) AS ?c) WHERE { ?s kg:HAS_CHILD_TAG_NEGATIVE ?o }",
        }

        prefixes = """
            PREFIX kg:   <http://ifrs-gics.ontotext.com/ontology/>
            PREFIX ifrs: <http://xbrl.ifrs.org/taxonomy/2025/>
            PREFIX gics: <http://gics.msci.com/ontology/>
        """

        print("\n" + "=" * 55)
        print("VERIFICATION — GraphDB triple counts")
        print("=" * 55)

        for label, query in queries.items():
            self.sparql.setQuery(prefixes + query)
            results = self.sparql.query().convert()
            count   = results["results"]["bindings"][0]["c"]["value"]
            print(f"  {label:25s}: {count}")

        # Sample Regional Banks tags
        print("\n  Sample — Regional Banks (40101015) HAS_RELEVANT_TAG:")
        self.sparql.setQuery(prefixes + """
            SELECT ?tagName ?label WHERE {
                gics:40101015 kg:HAS_RELEVANT_TAG ?tag .
                ?tag ifrs:tagName ?tagName ;
                     rdfs:label   ?label .
            }
            LIMIT 10
        """)
        results = self.sparql.query().convert()
        for r in results["results"]["bindings"]:
            print(f"    {r['tagName']['value']:50s} → {r['label']['value']}")

        # Summation rules — sample a handful of parents (323 rules total, too many to print in full)
        print("\n  Summation rules (HAS_CHILD_TAG / HAS_CHILD_TAG_NEGATIVE), sample:")
        self.sparql.setQuery(prefixes + """
            SELECT ?parent ?child ?sign WHERE {
                { ?parentTag kg:HAS_CHILD_TAG ?childTag . BIND("+" AS ?sign) }
                UNION
                { ?parentTag kg:HAS_CHILD_TAG_NEGATIVE ?childTag . BIND("-" AS ?sign) }
                ?parentTag ifrs:tagName ?parent .
                ?childTag  ifrs:tagName ?child .
            }
            ORDER BY ?parent
        """)
        results  = self.sparql.query().convert()
        parents  = {}
        for r in results["results"]["bindings"]:
            p = r["parent"]["value"]
            c = r["child"]["value"]
            sign = r["sign"]["value"]
            parents.setdefault(p, []).append(f"{sign}{c}")
        for parent, children in list(parents.items())[:8]:
            print(f"    {parent} = {' '.join(children)}")
        if len(parents) > 8:
            print(f"    ... and {len(parents) - 8} more parent totals")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("GraphDB Knowledge Graph Builder")
    print(f"  URL:        {GRAPHDB_URL}")
    print(f"  Repository: {REPOSITORY}")
    print(f"  Input:      {INPUT_JSON}")
    print("=" * 60)

    # ── Load IFRS labels ───────────────────────────────────────────────
    print("\n[1] Loading IFRS labels...")
    label_map = load_ifrs_labels()
    print(f"  {len(label_map)} labels loaded")

    # ── Load SubIndustry → XBRL tag mapping (pre-computed on Katana) ────
    print(f"\n[2] Loading SubIndustry → XBRL tag mapping from {INPUT_JSON}...")
    with open(INPUT_JSON) as f:
        si_mapping = json.load(f)

    total_si   = len(si_mapping)
    total_tags = sum(len(v) for v in si_mapping.values())
    print(f"  {total_si} sub-industries, {total_tags} edges "
          f"(avg {total_tags/total_si:.1f}/SI)")

    # ── Load into GraphDB ──────────────────────────────────────────────
    print("\n[3] Loading into GraphDB...")
    loader = GraphDBLoader()

    print("  Clearing repository...")
    loader.clear()

    print("  Loading ontology...")
    loader.load_ontology()

    print("  Loading GICS hierarchy (PARENT_OF)...")
    loader.load_gics_hierarchy()

    print("  Loading XBRL tag nodes...")
    loader.load_xbrl_tags(label_map)

    print("  Loading universal tags (HAS_RELEVANT_TAG)...")
    loader.load_universal_tags()

    print("  Loading SubIndustry tags (HAS_RELEVANT_TAG)...")
    loader.load_subindustry_tags(si_mapping)

    print("  Loading summation rules (HAS_CHILD_TAG)...")
    loader.load_has_child_tag()

    # ── Verify ────────────────────────────────────────────────────────
    loader.verify()

    print("\n" + "=" * 60)
    print("✅ Knowledge graph loaded into GraphDB!")
    print("=" * 60)
    print(f"\nOpen GraphDB at: {GRAPHDB_URL}")
    print(f"Repository:      {REPOSITORY}")
    print("\nSample SPARQL queries:")
    print("""
  # Get all tags for Regional Banks
  PREFIX kg:   <http://ifrs-gics.ontotext.com/ontology/>
  PREFIX ifrs: <http://xbrl.ifrs.org/taxonomy/2025/>
  PREFIX gics: <http://gics.msci.com/ontology/>

  SELECT ?tagName ?label WHERE {
      gics:40101015 kg:HAS_RELEVANT_TAG ?tag .
      ?tag ifrs:tagName ?tagName ;
           rdfs:label   ?label .
  }

  # Get summation rules for Assets
  SELECT ?child WHERE {
      ifrs:Assets kg:HAS_CHILD_TAG ?childTag .
      ?childTag ifrs:tagName ?child .
  }

  # Full GICS hierarchy for Financials
  SELECT ?ig ?i ?si WHERE {
      gics:40 kg:PARENT_OF ?igNode .
      ?igNode kg:PARENT_OF ?iNode .
      ?iNode  kg:PARENT_OF ?siNode .
      ?igNode rdfs:label ?ig .
      ?iNode  rdfs:label ?i .
      ?siNode rdfs:label ?si .
  }
    """)


if __name__ == "__main__":
    main()