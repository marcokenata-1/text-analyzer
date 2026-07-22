"""
IFRS Accounting Taxonomy 2025 — monetary data point tags with labels.
Sources:
  XSD:    https://xbrl.ifrs.org/taxonomy/2025-03-27/full_ifrs/full_ifrs-cor_2025-03-27.xsd
  Labels: https://xbrl.ifrs.org/taxonomy/2025-03-27/full_ifrs/labels/lab_full_ifrs-en_2025-03-27.xml

Each key is the IFRS tag name (without 'ifrs-full_' prefix).
Fields:
  label       : human-readable English label (from label file, or derived from camelCase)
  balance     : 'debit' or 'credit'
  period_type : 'instant' (balance sheet) or 'duration' (income/cash flow)
"""

definition = {
    "AccountingProfit": {
        "label":       "Accounting profit",
        "balance":     "credit",
        "period_type": "duration",
    },
    "Accruals": {
        "label":       "Accruals",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AccrualsAndDeferredIncomeIncludingContractLiabilities": {
        "label":       "Accruals and deferred income including contract liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AccrualsClassifiedAsCurrent": {
        "label":       "Accruals classified as current",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AccrualsClassifiedAsNoncurrent": {
        "label":       "Accruals classified as non-current",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AccruedIncomeIncludingContractAssets": {
        "label":       "Accrued income including contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AccruedIncomeOtherThanContractAssets": {
        "label":       "Accrued income other than contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AccumulatedChangesInFairValueOfFinancialAssetsAttributableToChangesInCreditRiskOfFinancialAssets": {
        "label":       "Accumulated increase (decrease) in fair value of financial assets designated as measured at fair value through profit or loss, attributable to changes in credit risk of financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AccumulatedChangesInFairValueOfFinancialAssetsRelatedCreditDerivativesOrSimilarInstruments": {
        "label":       "Accumulated increase (decrease) in fair value of credit derivatives or similar instruments related to financial assets designated as measured at fair value through profit or loss",
        "balance":     "None",
        "period_type": "instant",
    },
    "AccumulatedChangesInFairValueOfFinancialLiabilityAttributableToChangesInCreditRiskOfLiability": {
        "label":       "Accumulated increase (decrease) in fair value of financial liability, attributable to changes in credit risk of liability",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AccumulatedChangesInFairValueOfLoanOrReceivableAttributableToChangesInCreditRiskOfFinancialAssets": {
        "label":       "Accumulated increase (decrease) in fair value of loan or receivable, attributable to changes in credit risk of financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AccumulatedChangesInFairValueOfLoansOrReceivablesRelatedCreditDerivativesOrSimilarInstruments": {
        "label":       "Accumulated increase (decrease) in fair value of credit derivatives or similar instruments related to loans or receivables",
        "balance":     "None",
        "period_type": "instant",
    },
    "AccumulatedFairValueHedgeAdjustmentOnHedgedItemIncludedInCarryingAmountAssets": {
        "label":       "Accumulated fair value hedge adjustment on hedged item included in carrying amount, assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AccumulatedFairValueHedgeAdjustmentOnHedgedItemIncludedInCarryingAmountLiabilities": {
        "label":       "Accumulated fair value hedge adjustment on hedged item included in carrying amount, liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AccumulatedFairValueHedgeAdjustmentRemainingInStatementOfFinancialPositionForHedgedItemThatCeasedToBeAdjustedForHedgingGainsAndLossesAssets": {
        "label":       "Accumulated fair value hedge adjustment remaining in statement of financial position for hedged item that ceased to be adjusted for hedging gains and losses, assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AccumulatedFairValueHedgeAdjustmentRemainingInStatementOfFinancialPositionForHedgedItemThatCeasedToBeAdjustedForHedgingGainsAndLossesLiabilities": {
        "label":       "Accumulated fair value hedge adjustment remaining in statement of financial position for hedged item that ceased to be adjusted for hedging gains and losses, liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AccumulatedOtherComprehensiveIncome": {
        "label":       "Accumulated other comprehensive income",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AcquisitiondateFairValueOfEquityInterestInAcquireeHeldByAcquirerImmediatelyBeforeAcquisitionDate": {
        "label":       "Acquisition-date fair value of equity interest in acquiree held by acquirer immediately before acquisition date",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AcquisitiondateFairValueOfTotalConsiderationTransferred": {
        "label":       "Consideration transferred, acquisition-date fair value",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AcquisitionrelatedCostsForTransactionRecognisedSeparatelyFromAcquisitionOfAssetsAndAssumptionOfLiabilitiesInBusinessCombination": {
        "label":       "Acquisitionrelated costs for transaction recognised separately from acquisition of assets and assumption of liabilities in business combination",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AcquisitionrelatedCostsRecognisedAsExpenseForTransactionRecognisedSeparatelyFromAcquisitionOfAssetsAndAssumptionOfLiabilitiesInBusinessCombination": {
        "label":       "Acquisitionrelated costs recognised as expense for transaction recognised separately from acquisition of assets and assumption of liabilities in business combination",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AcquisitionsThroughBusinessCombinationsBiologicalAssets": {
        "label":       "Acquisitions through business combinations, biological assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AcquisitionsThroughBusinessCombinationsIntangibleAssetsAndGoodwill": {
        "label":       "Acquisitions through business combinations, intangible assets and goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AcquisitionsThroughBusinessCombinationsIntangibleAssetsOtherThanGoodwill": {
        "label":       "Acquisitions through business combinations, intangible assets other than goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AcquisitionsThroughBusinessCombinationsInvestmentProperty": {
        "label":       "Acquisitions through business combinations, investment property",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AcquisitionsThroughBusinessCombinationsOtherProvisions": {
        "label":       "Acquisitions through business combinations, other provisions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AcquisitionsThroughBusinessCombinationsPropertyPlantAndEquipment": {
        "label":       "Acquisitions through business combinations, property, plant and equipment",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AcquisitionsThroughBusinessCombinationsPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Acquisitions through business combinations, property, plant and equipment including right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AcquisitionsThroughBusinessCombinationsRightofuseAssets": {
        "label":       "Acquisitions through business combinations, right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ActualClaimsThatAriseFromContractsWithinScopeOfIFRS17": {
        "label":       "Actual claims that arise from contracts within scope of IFRS 17",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ActuarialGainsLossesArisingFromChangesInDemographicAssumptionsBeforeTaxDefinedBenefitPlans": {
        "label":       "Actuarial gains (losses) arising from changes in demographic assumptions, before tax, defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ActuarialGainsLossesArisingFromChangesInDemographicAssumptionsNetDefinedBenefitLiabilityAsset": {
        "label":       "Decrease (increase) in net defined benefit liability (asset) resulting from actuarial gains (losses) arising from changes in demographic assumptions",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ActuarialGainsLossesArisingFromChangesInDemographicAssumptionsNetOfTaxDefinedBenefitPlans": {
        "label":       "Actuarial gains (losses) arising from changes in demographic assumptions, net of tax, defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ActuarialGainsLossesArisingFromChangesInFinancialAssumptionsBeforeTaxDefinedBenefitPlans": {
        "label":       "Actuarial gains (losses) arising from changes in financial assumptions, before tax, defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ActuarialGainsLossesArisingFromChangesInFinancialAssumptionsNetDefinedBenefitLiabilityAsset": {
        "label":       "Decrease (increase) in net defined benefit liability (asset) resulting from actuarial gains (losses) arising from changes in financial assumptions",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ActuarialGainsLossesArisingFromChangesInFinancialAssumptionsNetOfTaxDefinedBenefitPlans": {
        "label":       "Actuarial gains (losses) arising from changes in financial assumptions, net of tax, defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ActuarialGainsLossesArisingFromExperienceAdjustmentsBeforeTaxDefinedBenefitPlans": {
        "label":       "Actuarial gains (losses) arising from experience adjustments, before tax, defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ActuarialGainsLossesArisingFromExperienceAdjustmentsNetDefinedBenefitLiabilityAsset": {
        "label":       "Decrease (increase) in net defined benefit liability (asset) resulting from actuarial gains (losses) arising from experience adjustments",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ActuarialGainsLossesArisingFromExperienceAdjustmentsNetOfTaxDefinedBenefitPlans": {
        "label":       "Actuarial gains (losses) arising from experience adjustments, net of tax, defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ActuarialPresentValueOfPromisedRetirementBenefits": {
        "label":       "Actuarial present value of promised retirement benefits",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AdditionalAllowanceRecognisedInProfitOrLossAllowanceAccountForCreditLossesOfFinancialAssets": {
        "label":       "Additional allowance recognised in profit or loss, allowance account for credit losses of financial assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "AdditionalLiabilitiesContingentLiabilitiesRecognisedInBusinessCombination": {
        "label":       "Additional liabilities, contingent liabilities recognised in business combination",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdditionalPaidinCapital": {
        "label":       "Additional paid-in capital",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AdditionalProvisionsOtherProvisions": {
        "label":       "Additional provisions, other provisions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdditionalRecognitionGoodwill": {
        "label":       "Additional recognition, goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdditionsFromAcquisitionsInvestmentProperty": {
        "label":       "Additions from acquisitions, investment property",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdditionsFromPurchasesBiologicalAssets": {
        "label":       "Additions from purchases, biological assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdditionsFromSubsequentExpenditureRecognisedAsAssetBiologicalAssets": {
        "label":       "Additions from subsequent expenditure recognised as asset, biological assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdditionsFromSubsequentExpenditureRecognisedAsAssetInvestmentProperty": {
        "label":       "Additions from subsequent expenditure recognised as asset, investment property",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdditionsOtherThanThroughBusinessCombinationsBiologicalAssets": {
        "label":       "Additions other than through business combinations, biological assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdditionsOtherThanThroughBusinessCombinationsIntangibleAssetsOtherThanGoodwill": {
        "label":       "Additions other than through business combinations, intangible assets other than goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdditionsOtherThanThroughBusinessCombinationsInvestmentProperty": {
        "label":       "Additions other than through business combinations, investment property",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdditionsOtherThanThroughBusinessCombinationsPropertyPlantAndEquipment": {
        "label":       "Additions other than through business combinations, property, plant and equipment",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdditionsOtherThanThroughBusinessCombinationsPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Additions other than through business combinations, property, plant and equipment including right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdditionsOtherThanThroughBusinessCombinationsRightofuseAssets": {
        "label":       "Additions other than through business combinations, right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdditionsToNoncurrentAssets": {
        "label":       "Additions to non-current assets other than financial instruments, deferred tax assets, net defined benefit assets, and rights arising under insurance contracts",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdditionsToRightofuseAssets": {
        "label":       "Additions to right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentToCarryingAmountsReportedUnderPreviousGAAP": {
        "label":       "Aggregate adjustment to carrying amounts of investments reported under previous GAAP",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AdjustmentToProfitLossForPreferenceShareDividends": {
        "label":       "Adjustment to profit (loss) for preference share dividends",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForAmortisationExpense": {
        "label":       "Adjustments for amortisation expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForAmountsTransferredToInitialCarryingAmountOfHedgedItems": {
        "label":       "Amounts removed from equity and included in carrying amount of non-financial asset (liability) whose acquisition or incurrence was hedged highly probable forecast transaction, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForCurrentTaxOfPriorPeriod": {
        "label":       "Adjustments for current tax of prior period",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInAccruedIncomeIncludingContractAssets": {
        "label":       "Adjustments for decrease (increase) in accrued income including contract assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInAccruedIncomeOtherThanContractAssets": {
        "label":       "Adjustments for decrease (increase) in accrued income other than contract assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInBiologicalAssets": {
        "label":       "Adjustments for decrease (increase) in biological assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInContractAssets": {
        "label":       "Adjustments for decrease (increase) in contract assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInDebtInstrumentsHeld": {
        "label":       "Adjustments for decrease (increase) in debt instruments held",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInDerivativeFinancialAssets": {
        "label":       "Adjustments for decrease (increase) in derivative financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInEquityInstrumentsHeld": {
        "label":       "Adjustments for decrease (increase) in equity instruments held",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInFinancialAssetsAtFairValueThroughProfitOrLossDesignatedUponInitialRecognitionOrSubsequently": {
        "label":       "Adjustments for decrease (increase) in financial assets at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInFinancialAssetsAtFairValueThroughProfitOrLossMandatorilyMeasuredAtFairValue": {
        "label":       "Adjustments for decrease (increase) in financial assets at fair value through profit or loss, mandatorily measured at fair value",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInFinancialAssetsHeldForTrading": {
        "label":       "Adjustments for decrease (increase) in financial assets held for trading",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInFinancialAssetsMeasuredAtAmortisedCost": {
        "label":       "Adjustments for decrease (increase) in financial assets measured at amortised cost",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Adjustments for decrease (increase) in financial assets measured at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInFinancialAssetsMeasuredAtFairValueThroughProfitOrLoss": {
        "label":       "Adjustments for decrease (increase) in financial assets measured at fair value through profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInInventories": {
        "label":       "Adjustments for decrease (increase) in inventories",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInLoansAndAdvances": {
        "label":       "Adjustments for decrease (increase) in loans and advances",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInLoansAndAdvancesToBanks": {
        "label":       "Adjustments for decrease (increase) in loans and advances to banks",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInLoansAndAdvancesToCentralBanks": {
        "label":       "Adjustments for decrease (increase) in loans and advances to central banks",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInLoansAndAdvancesToCustomers": {
        "label":       "Adjustments for decrease (increase) in loans and advances to customers",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInOtherAssets": {
        "label":       "Adjustments for decrease (increase) in other assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInOtherCurrentAssets": {
        "label":       "Adjustments for decrease (increase) in other current assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInOtherFinancialAssets": {
        "label":       "Adjustments for decrease (increase) in other financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInOtherOperatingReceivables": {
        "label":       "Adjustments for decrease (increase) in other operating receivables",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInPrepaidExpenses": {
        "label":       "Adjustments for decrease (increase) in prepaid expenses",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInReverseRepurchaseAgreementsAndCashCollateralOnSecuritiesBorrowed": {
        "label":       "Adjustments for decrease (increase) in reverse repurchase agreements and cash collateral on securities borrowed",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInTradeAccountReceivable": {
        "label":       "Adjustments for decrease (increase) in trade accounts receivable",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDecreaseIncreaseInTradeAndOtherReceivables": {
        "label":       "Adjustments for decrease (increase) in trade and other receivables",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDeferredTaxExpense": {
        "label":       "Adjustments for deferred tax expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDeferredTaxOfPriorPeriods": {
        "label":       "Adjustments for deferred tax of prior periods",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDepreciationAndAmortisationExpense": {
        "label":       "Adjustments for depreciation and amortisation expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDepreciationAndAmortisationExpenseAndImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLoss": {
        "label":       "Adjustments for depreciation and amortisation expense and impairment loss (reversal of impairment loss) recognised in profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDepreciationExpense": {
        "label":       "Adjustments for depreciation expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForDividendIncome": {
        "label":       "Adjustments for dividend income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForFairValueGainsLosses": {
        "label":       "Adjustments for fair value losses (gains)",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForFinanceCosts": {
        "label":       "Adjustments for finance costs",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForFinanceIncome": {
        "label":       "Adjustments for finance income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForFinanceIncomeCost": {
        "label":       "Adjustments for finance income cost",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForGainLossOnDisposalOfInvestmentsInSubsidiariesJointVenturesAndAssociates": {
        "label":       "Adjustments for gain (loss) on disposal of investments in subsidiaries, joint ventures and associates",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForGainLossOnDisposalsPropertyPlantAndEquipment": {
        "label":       "Adjustments for gain (loss) on disposals, property, plant and equipment",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForGainsLossesOnChangeInFairValueLessCostsToSellBiologicalAssets": {
        "label":       "Adjustments for gains (losses) on change in fair value less costs to sell, biological assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForGainsLossesOnChangeInFairValueOfDerivatives": {
        "label":       "Adjustments for gains (losses) on change in fair value of derivatives",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForGainsLossesOnChangeInFairValueOfFinancialAssets": {
        "label":       "Adjustments for gains (losses) on change in fair value of financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForGainsLossesOnChangeInFairValueOfFinancialLiabilities": {
        "label":       "Adjustments for gains (losses) on change in fair value of financial liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForGainsLossesOnDisposalOfFinancialAssets": {
        "label":       "Adjustments for gains (losses) on disposal of financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForGainsLossesOnFairValueAdjustmentInvestmentProperty": {
        "label":       "Adjustments for gains (losses) on fair value adjustment, investment property",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForImpairmentLossRecognisedInProfitOrLossGoodwill": {
        "label":       "Adjustments for impairment loss recognised in profit or loss, goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLoss": {
        "label":       "Adjustments for impairment loss (reversal of impairment loss) recognised in profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLossExplorationAndEvaluationAssets": {
        "label":       "Adjustments for impairment loss (reversal of impairment loss) recognised in profit or loss, exploration and evaluation assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLossInventories": {
        "label":       "Adjustments for impairment loss (reversal of impairment loss) recognised in profit or loss, inventories",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLossLoansAndAdvances": {
        "label":       "Adjustments for impairment loss (reversal of impairment loss) recognised in profit or loss, loans and advances",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLossPropertyPlantAndEquipment": {
        "label":       "Adjustments for impairment loss (reversal of impairment loss) recognised in profit or loss, property, plant and equipment",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLossTradeAndOtherReceivables": {
        "label":       "Adjustments for impairment loss (reversal of impairment loss) recognised in profit or loss, trade and other receivables",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForImpairmentLossesReversalOfImpairmentLossesRecognisedInProfitOrLossFinancialAssets": {
        "label":       "Adjustments for impairment losses (reversal of impairment losses) recognised in profit or loss, financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncomeTaxExpense": {
        "label":       "Adjustments for income tax expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInContractLiabilities": {
        "label":       "Adjustments for increase (decrease) in contract liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInDebtInstrumentsIssued": {
        "label":       "Adjustments for increase (decrease) in debt instruments issued",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInDeferredIncomeIncludingContractLiabilities": {
        "label":       "Adjustments for increase (decrease) in deferred income including contract liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInDeferredIncomeOtherThanContractLiabilities": {
        "label":       "Adjustments for increase (decrease) in deferred income other than contract liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInDeposits": {
        "label":       "Adjustments for increase (decrease) in deposits",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInDepositsFromBanks": {
        "label":       "Adjustments for increase (decrease) in deposits from banks",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInDepositsFromCustomers": {
        "label":       "Adjustments for increase (decrease) in deposits from customers",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInDerivativeFinancialLiabilities": {
        "label":       "Adjustments for increase (decrease) in derivative financial liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInEmployeeBenefitLiabilities": {
        "label":       "Adjustments for increase (decrease) in employee benefit liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInFinancialLiabilitiesAtFairValueThroughProfitOrLossDesignatedUponInitialRecognitionOrSubsequently": {
        "label":       "Adjustments for increase (decrease) in financial liabilities at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInFinancialLiabilitiesHeldForTrading": {
        "label":       "Adjustments for increase (decrease) in financial liabilities held for trading",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInFinancialLiabilitiesMeasuredAtAmortisedCost": {
        "label":       "Adjustments for increase (decrease) in financial liabilities measured at amortised cost",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInFinancialLiabilitiesMeasuredAtFairValueThroughProfitOrLoss": {
        "label":       "Adjustments for increase (decrease) in financial liabilities measured at fair value through profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInInsuranceReinsuranceAndInvestmentContractLiabilities": {
        "label":       "Adjustments for increase (decrease) in insurance, reinsurance and investment contract liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInOtherCurrentLiabilities": {
        "label":       "Adjustments for increase (decrease) in other current liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInOtherFinancialLiabilities": {
        "label":       "Adjustments for increase (decrease) in other financial liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInOtherLiabilities": {
        "label":       "Adjustments for increase (decrease) in other liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInOtherOperatingPayables": {
        "label":       "Adjustments for increase (decrease) in other operating payables",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInRepurchaseAgreementsAndCashCollateralOnSecuritiesLent": {
        "label":       "Adjustments for increase (decrease) in repurchase agreements and cash collateral on securities lent",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInTradeAccountPayable": {
        "label":       "Adjustments for increase (decrease) in trade accounts payable",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseDecreaseInTradeAndOtherPayables": {
        "label":       "Adjustments for increase (decrease) in trade and other payables",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForIncreaseInOtherProvisionsArisingFromPassageOfTime": {
        "label":       "Adjustments for increase in other provisions arising from passage of time",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForInterestExpense": {
        "label":       "Adjustments for interest expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForInterestIncome": {
        "label":       "Adjustments for interest income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForLossesGainsOnDisposalOfNoncurrentAssets": {
        "label":       "Adjustments for losses (gains) on disposal of non-current assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForProvisions": {
        "label":       "Adjustments for provisions",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForReconcileProfitLoss": {
        "label":       "Adjustments for reconcile profit loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForSharebasedPayments": {
        "label":       "Adjustments for share-based payments",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsForUndistributedProfitsOfAssociates": {
        "label":       "Adjustments for undistributed profits of associates",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForUndistributedProfitsOfInvestmentsAccountedForUsingEquityMethod": {
        "label":       "Adjustments for undistributed profits of investments accounted for using equity method",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AdjustmentsForUnrealisedForeignExchangeLossesGains": {
        "label":       "Adjustments for unrealised foreign exchange losses (gains)",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsToProfitLossForInterestAndDividendsOnEquityInstrumentsOtherThanPreferenceSharesAndParticipatingEquityInstruments": {
        "label":       "Adjustments to profit (loss) for interest and dividends on equity instruments, other than preference shares and participating equity instruments",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsToReconcileProfitLossAttributableToOwnersOfParentToNumeratorUsedInCalculatingBasicEarningsPerShare": {
        "label":       "Adjustments to reconcile profit (loss) attributable to owners of parent to numerator used in calculating basic earnings per share",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdjustmentsToReconcileProfitLossOtherThanChangesInWorkingCapital": {
        "label":       "Adjustments to reconcile profit loss other than changes in working capital",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdministrationCostsNotReflectedInReturnOnPlanAssetsDefinedBenefitPlans": {
        "label":       "Administration costs not reflected in return on plan assets defined benefit plans",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AdministrativeExpense": {
        "label":       "Administrative expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "Advances": {
        "label":       "Advances received, representing contract liabilities for performance obligations satisfied at point in time",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AdvertisingExpense": {
        "label":       "Advertising expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AggregateDifferenceBetweenFairValueAtInitialRecognitionAndAmountDeterminedUsingValuationTechniqueYetToBeRecognised": {
        "label":       "Aggregate difference between fair value at initial recognition and transaction price yet to be recognised in profit or loss",
        "balance":     "None",
        "period_type": "instant",
    },
    "Aircraft": {
        "label":       "Aircraft",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AllowanceAccountForCreditLossesOfFinancialAssets": {
        "label":       "Allowance account for credit losses of financial assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "Amortisation": {
        "label":       "Amortisation",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AmortisationAssetsRecognisedFromCostsIncurredToObtainOrFulfilContractsWithCustomers": {
        "label":       "Amortisation assets recognised from costs incurred to obtain or fulfil contracts with customers",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AmortisationExpense": {
        "label":       "Amortisation expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AmortisationIntangibleAssetsOtherThanGoodwill": {
        "label":       "Amortisation, intangible assets other than goodwill",
        "balance":     "None",
        "period_type": "duration",
    },
    "AmountByWhichFinancialAssetsRelatedCreditDerivativesOrSimilarInstrumentsMitigateMaximumExposureToCreditRisk": {
        "label":       "Amount by which credit derivatives or similar instruments related to financial assets designated as measured at fair value through profit or loss mitigate maximum exposure to credit risk",
        "balance":     "None",
        "period_type": "instant",
    },
    "AmountByWhichLoansOrReceivablesRelatedCreditDerivativesOrSimilarInstrumentsMitigateMaximumExposureToCreditRisk": {
        "label":       "Amount by which credit derivatives or similar instruments related to loans or receivables mitigate maximum exposure to credit risk",
        "balance":     "None",
        "period_type": "instant",
    },
    "AmountByWhichRegulatoryDeferralAccountCreditBalanceHasBeenReducedBecauseItIsNoLongerFullyReversible": {
        "label":       "Amount by which regulatory deferral account credit balance has been reduced because it is no longer fully reversible",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AmountByWhichRegulatoryDeferralAccountDebitBalanceHasBeenReducedBecauseItIsNoLongerFullyRecoverable": {
        "label":       "Amount by which regulatory deferral account debit balance has been reduced because it is no longer fully recoverable",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AmountByWhichUnitsRecoverableAmountExceedsItsCarryingAmount": {
        "label":       "Amount by which unit's recoverable amount exceeds its carrying amount",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AmountIncurredByEntityForProvisionOfKeyManagementPersonnelServicesProvidedBySeparateManagementEntity": {
        "label":       "Amount incurred by entity for provision of key management personnel services provided by separate management entity",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AmountOfReclassificationsOrChangesInPresentation": {
        "label":       "Amount of reclassifications or changes in presentation",
        "balance":     "None",
        "period_type": "duration",
    },
    "AmountPresentedInOtherComprehensiveIncomeRealisedAtDerecognition": {
        "label":       "Amount presented in other comprehensive income realised at derecognition of financial liability",
        "balance":     "None",
        "period_type": "duration",
    },
    "AmountRecognisedInOtherComprehensiveIncomeAndAccumulatedInEquityRelatingToNoncurrentAssetsOrDisposalGroupsHeldForSale": {
        "label":       "Amount recognised in other comprehensive income and accumulated in equity relating to non-current assets or disposal groups held for sale",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AmountRecognisedInProfitOrLossForReportingPeriodToReflectChangesInLeasePaymentsThatAriseFromRentConcessionsOccurringAsDirectConsequenceOfCovid19PandemicToWhichLesseeAppliedPracticalExpedientInParagraph46AOfIFRS16": {
        "label":       "Amount recognised in profit or loss for reporting period to reflect changes in lease payments that arise from rent concessions occurring as direct consequence of covid19 pandemic to which lessee applied practical expedient in paragraph46 a ofifrs16",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AmountRemovedFromReserveOfCashFlowHedgesAndIncludedInInitialCostOrOtherCarryingAmountOfNonfinancialAssetLiabilityOrFirmCommitmentForWhichFairValueHedgeAccountingIsApplied": {
        "label":       "Amount removed from reserve of cash flow hedges and included in initial cost or other carrying amount of non-financial asset (liability) or firm commitment for which fair value hedge accounting is applied",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AmountRemovedFromReserveOfChangeInValueOfForeignCurrencyBasisSpreadsAndIncludedInInitialCostOrOtherCarryingAmountOfNonfinancialAssetLiabilityOrFirmCommitmentForWhichFairValueHedgeAccountingIsApplied": {
        "label":       "Amount removed from reserve of change in value of foreign currency basis spreads and included in initial cost or other carrying amount of non-financial asset (liability) or firm commitment for which fair value hedge accounting is applied",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AmountRemovedFromReserveOfChangeInValueOfForwardElementsOfForwardContractsAndIncludedInInitialCostOrOtherCarryingAmountOfNonfinancialAssetLiabilityOrFirmCommitmentForWhichFairValueHedgeAccountingIsApplied": {
        "label":       "Amount removed from reserve of change in value of forward elements of forward contracts and included in initial cost or other carrying amount of non-financial asset (liability) or firm commitment for which fair value hedge accounting is applied",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AmountRemovedFromReserveOfChangeInValueOfTimeValueOfOptionsAndIncludedInInitialCostOrOtherCarryingAmountOfNonfinancialAssetLiabilityOrFirmCommitmentForWhichFairValueHedgeAccountingIsApplied": {
        "label":       "Amount removed from reserve of change in value of time value of options and included in initial cost or other carrying amount of non-financial asset (liability) or firm commitment for which fair value hedge accounting is applied",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AmountsPayableOnDemandThatAriseFromContractsWithinScopeOfIFRS17": {
        "label":       "Amounts payable on demand that arise from contracts within scope of IFRS 17",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AmountsPayableRelatedPartyTransactions": {
        "label":       "Amounts payable, related party transactions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AmountsPayableToTransfereeInRespectOfTransferredAssets": {
        "label":       "Other amounts payable to transferee in respect of transferred assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AmountsReceivableRelatedPartyTransactions": {
        "label":       "Amounts receivable, related party transactions",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AmountsRecognisedForTransactionRecognisedSeparatelyFromAcquisitionOfAssetsAndAssumptionOfLiabilitiesInBusinessCombination": {
        "label":       "Amounts recognised for transaction recognised separately from acquisition of assets and assumption of liabilities in business combination",
        "balance":     "None",
        "period_type": "duration",
    },
    "AmountsRemovedFromEquityAndAdjustedAgainstFairValueOfFinancialAssetsOnReclassificationOutOfFairValueThroughOtherComprehensiveIncomeMeasurementCategoryBeforeTax": {
        "label":       "Amounts removed from equity and adjusted against fair value of financial assets on reclassification out of fair value through other comprehensive income measurement category, before tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AmountsRemovedFromEquityAndAdjustedAgainstFairValueOfFinancialAssetsOnReclassificationOutOfFairValueThroughOtherComprehensiveIncomeMeasurementCategoryNetOfTax": {
        "label":       "Amounts removed from equity and adjusted against fair value of financial assets on reclassification out of fair value through other comprehensive income measurement category, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AmountsRemovedFromEquityAndIncludedInCarryingAmountOfNonfinancialAssetLiabilityWhoseAcquisitionOrIncurrenceWasHedgedHighlyProbableForecastTransactionBeforeTax": {
        "label":       "Amounts removed from equity and included in carrying amount of non-financial asset (liability) whose acquisition or incurrence was hedged highly probable forecast transaction, before tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AmountsSubjectToEnforceableMasterNettingArrangementOrSimilarAgreementNotSetOffAgainstFinancialAssets": {
        "label":       "Amounts subject to enforceable master netting arrangement or similar agreement not set off against financial assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AmountsSubjectToEnforceableMasterNettingArrangementOrSimilarAgreementNotSetOffAgainstFinancialLiabilities": {
        "label":       "Amounts subject to enforceable master netting arrangement or similar agreement not set off against financial liabilities",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetRecognisedForExpectedReimbursementContingentLiabilitiesInBusinessCombination": {
        "label":       "Asset recognised for expected reimbursement, contingent liabilities in business combination",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetRecognisedForExpectedReimbursementOtherProvisions": {
        "label":       "Asset recognised for expected reimbursement, other provisions",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetbackedDebtInstrumentsHeld": {
        "label":       "Asset-backed debt instruments held",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetbackedSecuritiesAmountContributedToFairValueOfPlanAssets": {
        "label":       "Asset-backed securities, amount contributed to fair value of plan assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "Assets": {
        "label":       "Assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetsAndRegulatoryDeferralAccountDebitBalances": {
        "label":       "Assets and regulatory deferral account debit balances",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetsArisingFromExplorationForAndEvaluationOfMineralResources": {
        "label":       "Assets arising from exploration for and evaluation of mineral resources",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetsForInsuranceAcquisitionCashFlows": {
        "label":       "Assets for insurance acquisition cash flows",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AssetsHeldAsCollateralPermittedToBeSoldOrRepledgedAtFairValue": {
        "label":       "Collateral held permitted to be sold or repledged in absence of default by owner of collateral, at fair value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetsLessCurrentLiabilities": {
        "label":       "Assets less current liabilities",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetsLiabilitiesOfBenefitPlan": {
        "label":       "Assets (liabilities) of benefit plan",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AssetsObtained": {
        "label":       "Assets obtained by taking possession of collateral or calling on other credit enhancements",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetsOfBenefitPlan": {
        "label":       "Assets of benefit plan",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetsOtherThanCashOrCashEquivalentsInSubsidiaryOrBusinessesAcquiredOrDisposed2013": {
        "label":       "Assets other than cash or cash equivalents in subsidiary or businesses acquired or disposed",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AssetsRecognisedFromCostsToObtainOrFulfilContractsWithCustomers": {
        "label":       "Assets recognised from costs to obtain or fulfil contracts with customers",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetsRecognisedInEntitysFinancialStatementsInRelationToStructuredEntities": {
        "label":       "Assets recognised in entity's financial statements in relation to structured entities",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetsSoldOrRepledgedAsCollateralAtFairValue": {
        "label":       "Collateral sold or repledged in absence of default by owner of collateral, at fair value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetsThatEntityContinuesToRecognise": {
        "label":       "Assets that entity continues to recognise",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetsThatEntityContinuesToRecogniseToExtentOfContinuingInvolvement": {
        "label":       "Assets that entity continues to recognise to extent of continuing involvement",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetsToWhichSignificantRestrictionsApply": {
        "label":       "Assets to which significant restrictions apply",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssetsTransferredToStructuredEntitiesAtTimeOfTransfer": {
        "label":       "Assets transferred to structured entities, at time of transfer",
        "balance":     "credit",
        "period_type": "duration",
    },
    "AssetsWithSignificantRiskOfMaterialAdjustmentsWithinNextFinancialYear": {
        "label":       "Assets with significant risk of material adjustments within next financial year",
        "balance":     "debit",
        "period_type": "instant",
    },
    "AssociatedLiabilitiesThatEntityContinuesToRecognise": {
        "label":       "Associated liabilities that entity continues to recognise",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AssociatedLiabilitiesThatEntityContinuesToRecogniseToExtentOfContinuingInvolvement": {
        "label":       "Associated liabilities that entity continues to recognise to extent of continuing involvement",
        "balance":     "credit",
        "period_type": "instant",
    },
    "AuditorsRemuneration": {
        "label":       "Auditors remuneration",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AuditorsRemunerationForAuditServices": {
        "label":       "Auditors remuneration for audit services",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AuditorsRemunerationForOtherServices": {
        "label":       "Auditors remuneration for other services",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AuditorsRemunerationForTaxServices": {
        "label":       "Auditors remuneration for tax services",
        "balance":     "debit",
        "period_type": "duration",
    },
    "AuthorisedCapitalCommitmentsButNotContractedFor": {
        "label":       "Authorised capital commitments but not contracted for",
        "balance":     "credit",
        "period_type": "instant",
    },
    "BalancesOnCurrentAccountsFromCustomers": {
        "label":       "Balances on current accounts from customers",
        "balance":     "credit",
        "period_type": "instant",
    },
    "BalancesOnDemandDepositsFromCustomers": {
        "label":       "Balances on demand deposits from customers",
        "balance":     "credit",
        "period_type": "instant",
    },
    "BalancesOnOtherDepositsFromCustomers": {
        "label":       "Balances on other deposits from customers",
        "balance":     "credit",
        "period_type": "instant",
    },
    "BalancesOnTermDepositsFromCustomers": {
        "label":       "Balances on term deposits from customers",
        "balance":     "credit",
        "period_type": "instant",
    },
    "BalancesWithBanks": {
        "label":       "Balances with banks",
        "balance":     "debit",
        "period_type": "instant",
    },
    "BasicEarningsLossPerShare": {
        "label":       "Basic earnings (loss) per share",
        "balance":     "",
        "period_type": "duration",
    },
    "BankAcceptanceAssets": {
        "label":       "Bank acceptance assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "BankAcceptanceLiabilities": {
        "label":       "Bank acceptance liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "BankAndSimilarCharges": {
        "label":       "Bank and similar charges",
        "balance":     "debit",
        "period_type": "duration",
    },
    "BankBalancesAtCentralBanksOtherThanMandatoryReserveDeposits": {
        "label":       "Bank balances at central banks other than mandatory reserve deposits",
        "balance":     "debit",
        "period_type": "instant",
    },
    "BankBorrowingsUndiscountedCashFlows": {
        "label":       "Bank borrowings, undiscounted cash flows",
        "balance":     "credit",
        "period_type": "instant",
    },
    "BankDebtInstrumentsHeld": {
        "label":       "Bank debt instruments held",
        "balance":     "debit",
        "period_type": "instant",
    },
    "BankOverdraftsClassifiedAsCashEquivalents": {
        "label":       "Bank overdrafts",
        "balance":     "credit",
        "period_type": "instant",
    },
    "BankingArrangementsClassifiedAsCashEquivalents": {
        "label":       "Other banking arrangements, classified as cash equivalents",
        "balance":     "debit",
        "period_type": "instant",
    },
    "BearerPlants": {
        "label":       "Bearer plants",
        "balance":     "debit",
        "period_type": "instant",
    },
    "BenefitsPaidOrPayable": {
        "label":       "Benefits paid or payable",
        "balance":     "debit",
        "period_type": "duration",
    },
    "BestEstimateAtAcquisitionDateOfContractualCashFlowsNotExpectedToBeCollectedForAcquiredReceivables": {
        "label":       "Best estimate at acquisition date of contractual cash flows not expected to be collected for acquired receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "BiologicalAssets": {
        "label":       "Biological assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "BiologicalAssetsPledgedAsSecurityForLiabilities": {
        "label":       "Biological assets pledged as security for liabilities",
        "balance":     "debit",
        "period_type": "instant",
    },
    "BiologicalAssetsWhoseTitleIsRestricted": {
        "label":       "Biological assets whose title is restricted",
        "balance":     "debit",
        "period_type": "instant",
    },
    "BondsIssued": {
        "label":       "Bonds issued",
        "balance":     "credit",
        "period_type": "instant",
    },
    "BondsIssuedUndiscountedCashFlows": {
        "label":       "Bonds issued, undiscounted cash flows",
        "balance":     "credit",
        "period_type": "instant",
    },
    "BorrowingCostsCapitalised": {
        "label":       "Borrowing costs capitalised",
        "balance":     "None",
        "period_type": "duration",
    },
    "BorrowingCostsIncurred": {
        "label":       "Borrowing costs incurred",
        "balance":     "None",
        "period_type": "duration",
    },
    "BorrowingCostsRecognisedAsExpense": {
        "label":       "Borrowing costs recognised as expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "Borrowings": {
        "label":       "Borrowings",
        "balance":     "credit",
        "period_type": "instant",
    },
    "BorrowingsRecognisedAsOfAcquisitionDate": {
        "label":       "Borrowings recognised as of acquisition date",
        "balance":     "credit",
        "period_type": "instant",
    },
    "BrandNames": {
        "label":       "Brand names",
        "balance":     "debit",
        "period_type": "instant",
    },
    "BrokerageFeeExpense": {
        "label":       "Brokerage fee expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "BrokerageFeeIncome": {
        "label":       "Brokerage fee income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "Buildings": {
        "label":       "Buildings",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CancellationOfTreasuryShares": {
        "label":       "Cancellation of treasury shares",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CapitalCommitments": {
        "label":       "Capital commitments",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CapitalRedemptionReserve": {
        "label":       "Capital redemption reserve",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CapitalReserve": {
        "label":       "Capital reserve",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CarryingAmountOfAssetsAffectedByCurrencyNotBeingExchangeable": {
        "label":       "Carrying amount of assets affected by currency not being exchangeable",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CarryingAmountOfAssetsExposedToRisk": {
        "label":       "Carrying amount of assets exposed to risk",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CarryingAmountOfLiabilitiesAffectedByCurrencyNotBeingExchangeable": {
        "label":       "Carrying amount of liabilities affected by currency not being exchangeable",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CarryingAmountOfLiabilitiesExposedToRisk": {
        "label":       "Carrying amount of liabilities exposed to risk",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CarryingAmountOfNoncurrentLiabilitiesWithCovenants": {
        "label":       "Carrying amount of non-current liabilities with covenants",
        "balance":     "credit",
        "period_type": "instant",
    },
    "Cash": {
        "label":       "Cash",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CashAdvancesAndLoansFromRelatedParties": {
        "label":       "Cash advances and loans from related parties",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashAdvancesAndLoansMadeToOtherPartiesClassifiedAsInvestingActivities": {
        "label":       "Cash advances and loans made to other parties, classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CashAdvancesAndLoansMadeToRelatedParties": {
        "label":       "Cash advances and loans made to related parties",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CashAndBankBalancesAtCentralBanks": {
        "label":       "Cash and bank balances at central banks",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CashAndCashEquivalents": {
        "label":       "Cash and cash equivalents",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CashAndCashEquivalentsAmountContributedToFairValueOfPlanAssets": {
        "label":       "Cash and cash equivalents, amount contributed to fair value of plan assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CashAndCashEquivalentsClassifiedAsPartOfDisposalGroupHeldForSale": {
        "label":       "Cash and cash equivalents classified as part of disposal group held for sale",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CashAndCashEquivalentsHeldByEntityUnavailableForUseByGroup": {
        "label":       "Cash and cash equivalents held by entity unavailable for use by group",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CashAndCashEquivalentsIfDifferentFromStatementOfFinancialPosition": {
        "label":       "Cash and cash equivalents if different from statement of financial position",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CashAndCashEquivalentsInSubsidiaryOrBusinessesAcquiredOrDisposed2013": {
        "label":       "Cash and cash equivalents in subsidiary or businesses acquired or disposed",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashAndCashEquivalentsRecognisedAsOfAcquisitionDate": {
        "label":       "Cash and cash equivalents recognised as of acquisition date",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CashCollateralPledgedSubjectToEnforceableMasterNettingArrangementOrSimilarAgreementNotSetOffAgainstFinancialLiabilities": {
        "label":       "Cash collateral pledged subject to enforceable master netting arrangement or similar agreement not set off against financial liabilities",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CashCollateralReceivedSubjectToEnforceableMasterNettingArrangementOrSimilarAgreementNotSetOffAgainstFinancialAssets": {
        "label":       "Cash collateral received subject to enforceable master netting arrangement or similar agreement not set off against financial assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CashEquivalents": {
        "label":       "Cash equivalents",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CashFlowsFromLosingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities": {
        "label":       "Cash flows from losing control of subsidiaries or other businesses, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInDecreaseIncreaseInRestrictedCashAndCashEquivalents": {
        "label":       "Cash flows from (used in) decrease (increase) in restricted cash and cash equivalents",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInDecreaseIncreaseInShorttermDepositsAndInvestments": {
        "label":       "Cash flows from (used in) decrease (increase) in short-term deposits and investments",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInExplorationForAndEvaluationOfMineralResourcesClassifiedAsInvestingActivities": {
        "label":       "Cash flows from (used in) exploration for and evaluation of mineral resources, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInExplorationForAndEvaluationOfMineralResourcesClassifiedAsOperatingActivities": {
        "label":       "Cash flows from (used in) exploration for and evaluation of mineral resources, classified as operating activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInFinancingActivities": {
        "label":       "Cash flows from (used in) financing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInFinancingActivitiesContinuingOperations": {
        "label":       "Cash flows from (used in) financing activities, continuing operations",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInFinancingActivitiesDiscontinuedOperations": {
        "label":       "Cash flows from (used in) financing activities, discontinued operations",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInIncreaseDecreaseInCurrentBorrowings": {
        "label":       "Cash flows from (used in) increase (decrease) in current borrowings",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInIncreasesInOperatingCapacity": {
        "label":       "Cash flows from (used in) increases in operating capacity",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInInvestingActivities": {
        "label":       "Cash flows from (used in) investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInInvestingActivitiesContinuingOperations": {
        "label":       "Cash flows from (used in) investing activities, continuing operations",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInInvestingActivitiesDiscontinuedOperations": {
        "label":       "Cash flows from (used in) investing activities, discontinued operations",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInMaintainingOperatingCapacity": {
        "label":       "Cash flows from (used in) maintaining operating capacity",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInOperatingActivities": {
        "label":       "Cash flows from (used in) operating activities",
        "balance":     "None",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInOperatingActivitiesContinuingOperations": {
        "label":       "Cash flows from (used in) operating activities, continuing operations",
        "balance":     "None",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInOperatingActivitiesDiscontinuedOperations": {
        "label":       "Cash flows from (used in) operating activities, discontinued operations",
        "balance":     "None",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInOperations": {
        "label":       "Cash flows from (used in) operations",
        "balance":     "None",
        "period_type": "duration",
    },
    "CashFlowsFromUsedInOperationsBeforeChangesInWorkingCapital": {
        "label":       "Cash flows from (used in) operations before changes in working capital",
        "balance":     "None",
        "period_type": "duration",
    },
    "CashFlowsUsedInExplorationAndDevelopmentActivities": {
        "label":       "Cash flows used in exploration and development activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities": {
        "label":       "Cash flows used in obtaining control of subsidiaries or other businesses, classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CashOnHand": {
        "label":       "Cash on hand",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CashOutflowForLeases": {
        "label":       "Cash outflow for leases",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CashPaymentsForFutureContractsForwardContractsOptionContractsAndSwapContractsClassifiedAsInvestingActivities": {
        "label":       "Cash payments for futures contracts, forward contracts, option contracts and swap contracts, classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CashReceiptsFromFutureContractsForwardContractsOptionContractsAndSwapContractsClassifiedAsInvestingActivities": {
        "label":       "Cash receipts from futures contracts, forward contracts, option contracts and swap contracts, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashReceiptsFromRepaymentOfAdvancesAndLoansMadeToOtherPartiesClassifiedAsInvestingActivities": {
        "label":       "Cash receipts from repayment of advances and loans made to other parties, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashReceiptsFromRepaymentOfAdvancesAndLoansMadeToRelatedParties": {
        "label":       "Cash receipts from repayment of advances and loans made to related parties",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CashRepaymentsOfAdvancesAndLoansFromRelatedParties": {
        "label":       "Cash repayments of advances and loans from related parties",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CashTransferred": {
        "label":       "Cash transferred",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ChangeInAmountRecognisedForPreacquisitionDeferredTaxAsset": {
        "label":       "Increase (decrease) in amount recognised for pre-acquisition deferred tax asset",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ChangesInBiologicalAssets": {
        "label":       "Increase (decrease) in biological assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ChangesInEquity": {
        "label":       "Increase (decrease) in equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ChangesInFairValueOfFinancialAssetsAttributableToChangesInCreditRiskOfFinancialAssets": {
        "label":       "Increase (decrease) in fair value of financial assets designated as measured at fair value through profit or loss, attributable to changes in credit risk of financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ChangesInFairValueOfFinancialAssetsRelatedCreditDerivativesOrSimilarInstruments": {
        "label":       "Increase (decrease) in fair value of credit derivatives or similar instruments related to financial assets designated as measured at fair value through profit or loss",
        "balance":     "None",
        "period_type": "duration",
    },
    "ChangesInFairValueOfFinancialLiabilityAttributableToChangesInCreditRiskOfLiability": {
        "label":       "Increase (decrease) in fair value of financial liability, attributable to changes in credit risk of liability",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ChangesInFairValueOfLoansOrReceivablesAttributableToChangesInCreditRiskOfFinancialAssets": {
        "label":       "Increase (decrease) in fair value of loans or receivables, attributable to changes in credit risk of financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ChangesInFairValueOfLoansOrReceivablesRelatedCreditDerivativesOrSimilarInstruments": {
        "label":       "Increase (decrease) in fair value of credit derivatives or similar instruments related to loans or receivables",
        "balance":     "None",
        "period_type": "duration",
    },
    "ChangesInGoodwill": {
        "label":       "Increase (decrease) in goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ChangesInIntangibleAssetsOtherThanGoodwill": {
        "label":       "Increase (decrease) in intangible assets other than goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ChangesInInventoriesOfFinishedGoodsAndWorkInProgress": {
        "label":       "Changes in inventories of finished goods and work in progress",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ChangesInInvestmentProperty": {
        "label":       "Increase (decrease) in investment property",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ChangesInOtherProvisions": {
        "label":       "Increase (decrease) in other provisions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ChangesInPropertyPlantAndEquipment": {
        "label":       "Increase (decrease) in property, plant and equipment",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ChangesInReimbursementRightsAtFairValue": {
        "label":       "Increase (decrease) in reimbursement rights related to defined benefit obligation, at fair value",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CirculationRevenue": {
        "label":       "Circulation revenue",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CommercialPapersIssued": {
        "label":       "Commercial papers issued",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CommitmentsForDevelopmentOrAcquisitionOfBiologicalAssets": {
        "label":       "Commitments for development or acquisition of biological assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CommitmentsInRelationToJointVentures": {
        "label":       "Commitments in relation to joint ventures",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CommitmentsMadeByEntityRelatedPartyTransactions": {
        "label":       "Commitments made by entity, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "CommitmentsMadeOnBehalfOfEntityRelatedPartyTransactions": {
        "label":       "Commitments made on behalf of entity, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "CommunicationExpense": {
        "label":       "Communication expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CompensationFromThirdPartiesForItemsOfPropertyPlantAndEquipment": {
        "label":       "Compensation from third parties for items of property plant and equipment",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ComprehensiveIncome": {
        "label":       "Comprehensive income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ComprehensiveIncomeAttributableToNoncontrollingInterests": {
        "label":       "Comprehensive income, attributable to non-controlling interests",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ComprehensiveIncomeAttributableToOwnersOfParent": {
        "label":       "Comprehensive income, attributable to owners of parent",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ComprehensiveIncomeFromContinuingOperations": {
        "label":       "Comprehensive income from continuing operations",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ComprehensiveIncomeFromContinuingOperationsAttributableToNoncontrollingInterests": {
        "label":       "Comprehensive income from continuing operations, attributable to non-controlling interests",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ComprehensiveIncomeFromContinuingOperationsAttributableToOwnersOfParent": {
        "label":       "Comprehensive income from continuing operations, attributable to owners of parent",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ComprehensiveIncomeFromDiscontinuedOperations": {
        "label":       "Comprehensive income from discontinued operations",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ComprehensiveIncomeFromDiscontinuedOperationsAttributableToNoncontrollingInterests": {
        "label":       "Comprehensive income from discontinued operations, attributable to non-controlling interests",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ComprehensiveIncomeFromDiscontinuedOperationsAttributableToOwnersOfParent": {
        "label":       "Comprehensive income from discontinued operations, attributable to owners of parent",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ComputerSoftware": {
        "label":       "Computer software",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ConsiderationPaidReceived": {
        "label":       "Consideration paid (received)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ConstructionInProgress": {
        "label":       "Construction in progress",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ConsumerLoans": {
        "label":       "Loans to consumers",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ContingentConsiderationRecognisedAsOfAcquisitionDate": {
        "label":       "Contingent consideration recognised as of acquisition date",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ContingentLiabilitiesIncurredByVenturerInRelationToInterestsInJointVentures": {
        "label":       "Contingent liabilities incurred in relation to interests in joint ventures",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ContingentLiabilitiesIncurredInRelationToInterestsInAssociates": {
        "label":       "Contingent liabilities incurred in relation to interests in associates",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ContingentLiabilitiesRecognisedAsOfAcquisitionDate": {
        "label":       "Contingent liabilities recognised as of acquisition date",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ContingentLiabilitiesRecognisedInBusinessCombination": {
        "label":       "Contingent liabilities recognised in business combination",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ContractAssets": {
        "label":       "Contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ContractLiabilities": {
        "label":       "Contract liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ContractLiabilitiesForPerformanceObligationsSatisfiedOverTime": {
        "label":       "Contract liabilities for performance obligations satisfied over time",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ContractLiabilitiesRecognisedAsOfAcquisitionDate": {
        "label":       "Contract liabilities recognised as of acquisition date",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ContractualAmountsToBeExchangedInDerivativeFinancialInstrumentForWhichGrossCashFlowsAreExchanged": {
        "label":       "Contractual amounts to be exchanged in derivative financial instrument for which gross cash flows are exchanged",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ContractualCapitalCommitments": {
        "label":       "Contractual capital commitments",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ContractualCommitmentsForAcquisitionOfIntangibleAssets": {
        "label":       "Contractual commitments for acquisition of intangible assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ContractualCommitmentsForAcquisitionOfPropertyPlantAndEquipment": {
        "label":       "Contractual commitments for acquisition of property, plant and equipment",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ContractualServiceMargin": {
        "label":       "Contractual service margin",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ContributionsToPlanByEmployerNetDefinedBenefitLiabilityAsset": {
        "label":       "Decrease (increase) in net defined benefit liability (asset) resulting from resulting from contributions to plan by employer",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ContributionsToPlanByPlanParticipantsNetDefinedBenefitLiabilityAsset": {
        "label":       "Decrease (increase) in net defined benefit liability (asset) resulting from contributions to plan by plan participants",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ContributionsToPlanNetDefinedBenefitLiabilityAsset": {
        "label":       "Decrease (increase) in net defined benefit liability (asset) resulting from contributions to plan",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CopyrightsPatentsAndOtherIndustrialPropertyRightsServiceAndOperatingRights": {
        "label":       "Copyrights, patents and other industrial property rights, service and operating rights",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CorporateDebtInstrumentsHeld": {
        "label":       "Corporate debt instruments held",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CorporateLoans": {
        "label":       "Loans to corporate entities",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CostIncludedInProfitOrLossInAccordanceWithParagraph20AOfIAS16ThatRelatesToItemsProducedThatAreNotOutputOfEntitysOrdinaryActivities": {
        "label":       "Cost included in profit or loss in accordance with paragraph20 a ofias16 that relates to items produced that are not output of entitys ordinary activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CostOfInventoriesRecognisedAsExpenseDuringPeriod": {
        "label":       "Cost of inventories recognised as expense during period",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CostOfMerchandiseSold": {
        "label":       "Cost of merchandise sold",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CostOfPurchasedEnergySold": {
        "label":       "Cost of purchased energy sold",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CostOfSales": {
        "label":       "Cost of sales",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CostOfSalesFoodAndBeverage": {
        "label":       "Cost of sales food and beverage",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CostOfSalesHotelOperations": {
        "label":       "Cost of sales hotel operations",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CostOfSalesRoomOccupancyServices": {
        "label":       "Cost of sales room occupancy services",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CreditCardLoans": {
        "label":       "Credit card loans",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CreditDerivativeFairValue": {
        "label":       "Credit derivative, fair value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CreditDerivativeNominalAmount": {
        "label":       "Credit derivative, nominal amount",
        "balance":     "None",
        "period_type": "instant",
    },
    "CreditExposure": {
        "label":       "Credit exposure",
        "balance":     "None",
        "period_type": "instant",
    },
    "CreditrelatedFeeAndCommissionIncome": {
        "label":       "Creditrelated fee and commission income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CumulativeChangeInFairValueRecognisedInProfitOrLossOnSalesOfInvestmentPropertyBetweenPoolsOfAssetsMeasuredUsingDifferentModels": {
        "label":       "Cumulative change in fair value recognised in profit or loss on sales of investment property between pools of assets measured using different models",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CumulativeGainLossOnDisposalOfInvestmentsInEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Cumulative gain (loss) on disposal of investments in equity instruments designated at fair value through other comprehensive income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CumulativeGainLossPreviouslyRecognisedInOtherComprehensiveIncomeArisingFromReclassificationOfFinancialAssetsOutOfFairValueThroughOtherComprehensiveIncomeIntoFairValueThroughProfitOrLossMeasurementCategory": {
        "label":       "Cumulative gain (loss) previously recognised in other comprehensive income arising from reclassification of financial assets out of fair value through other comprehensive income into fair value through profit or loss measurement category",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CumulativeGainLossPreviouslyRecognisedInOtherComprehensiveIncomeArisingFromReclassificationOfFinancialAssetsOutOfFairValueThroughOtherComprehensiveIncomeIntoFairValueThroughProfitOrLossMeasurementCategoryInvesting": {
        "label":       "Cumulative gain loss previously recognised in other comprehensive income arising from reclassification of financial assets out of fair value through other comprehensive income into fair value through profit or loss measurement category investing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CumulativeGainLossPreviouslyRecognisedInOtherComprehensiveIncomeArisingFromReclassificationOfFinancialAssetsOutOfFairValueThroughOtherComprehensiveIncomeIntoFairValueThroughProfitOrLossMeasurementCategoryOperating": {
        "label":       "Cumulative gain loss previously recognised in other comprehensive income arising from reclassification of financial assets out of fair value through other comprehensive income into fair value through profit or loss measurement category operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CumulativePreferenceDividendsNotRecognised": {
        "label":       "Cumulative preference dividends not recognised",
        "balance":     "None",
        "period_type": "duration",
    },
    "CumulativeUnrecognisedShareOfLossesOfAssociates": {
        "label":       "Cumulative unrecognised share of losses of associates",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CumulativeUnrecognisedShareOfLossesOfJointVentures": {
        "label":       "Cumulative unrecognised share of losses of joint ventures",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CumulativeUnrecognisedShareOfLossesOfJointVenturesTransitionFromProportionateConsolidationToEquityMethod": {
        "label":       "Cumulative unrecognised share of losses of joint ventures, transition from proportionate consolidation to equity method",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentAccrualsAndCurrentDeferredIncomeIncludingCurrentContractLiabilities": {
        "label":       "Current accruals and current deferred income including current contract liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentAccruedExpensesAndOtherCurrentLiabilities": {
        "label":       "Current accrued expenses and other current liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentAccruedIncomeIncludingCurrentContractAssets": {
        "label":       "Current accrued income including current contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentAccruedIncomeOtherThanCurrentContractAssets": {
        "label":       "Current accrued income other than current contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentAdvances": {
        "label":       "Current advances received, representing current contract liabilities for performance obligations satisfied at point in time",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentAdvancesToSuppliers": {
        "label":       "Current advances to suppliers",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentAgriculturalProduce": {
        "label":       "Current agricultural produce",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentAndDeferredTaxRelatingToItemsChargedOrCreditedDirectlyToEquity": {
        "label":       "Current and deferred tax relating to items credited (charged) directly to equity",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CurrentAssets": {
        "label":       "Current assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentAssetsLiabilities": {
        "label":       "Current assets (liabilities)",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentAssetsOtherThanAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners": {
        "label":       "Current assets other than non-current assets or disposal groups classified as held for sale or as held for distribution to owners",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentAssetsRecognisedAsOfAcquisitionDate": {
        "label":       "Current assets recognised as of acquisition date",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentBiologicalAssets": {
        "label":       "Current biological assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentBondsIssuedAndCurrentPortionOfNoncurrentBondsIssued": {
        "label":       "Current bonds issued and current portion of non-current bonds issued",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentBorrowingsAndCurrentPortionOfNoncurrentBorrowings": {
        "label":       "Current borrowings and current portion of non-current borrowings",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentCommercialPapersIssuedAndCurrentPortionOfNoncurrentCommercialPapersIssued": {
        "label":       "Current commercial papers issued and current portion of non-current commercial papers issued",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentContractAssets": {
        "label":       "Current contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentContractLiabilities": {
        "label":       "Current contract liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentContractLiabilitiesForPerformanceObligationsSatisfiedOverTime": {
        "label":       "Current contract liabilities for performance obligations satisfied over time",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentCrudeOil": {
        "label":       "Current crude oil",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentDebtInstrumentsIssued": {
        "label":       "Current debt instruments issued",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentDeferredIncomeIncludingCurrentContractLiabilities": {
        "label":       "Current deferred income including current contract liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentDeferredIncomeOtherThanCurrentContractLiabilities": {
        "label":       "Current deferred income other than current contract liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentDepositsFromCustomers": {
        "label":       "Current deposits from customers",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentDerivativeFinancialAssets": {
        "label":       "Current derivative financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentDerivativeFinancialLiabilities": {
        "label":       "Current derivative financial liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentDividendPayables": {
        "label":       "Current dividend payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentExciseTaxPayables": {
        "label":       "Current excise tax payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentFinanceLeaseReceivables": {
        "label":       "Current finance lease receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentFinancialAssets": {
        "label":       "Current financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentFinancialAssetsAtAmortisedCost": {
        "label":       "Current financial assets at amortised cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentFinancialAssetsAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Current financial assets at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentFinancialAssetsAtFairValueThroughProfitOrLoss": {
        "label":       "Current financial assets at fair value through profit or loss",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentFinancialAssetsAtFairValueThroughProfitOrLossClassifiedAsHeldForTrading": {
        "label":       "Current financial assets at fair value through profit or loss, classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentFinancialAssetsAtFairValueThroughProfitOrLossDesignatedUponInitialRecognition": {
        "label":       "Current financial assets at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentFinancialAssetsAtFairValueThroughProfitOrLossMandatorilyMeasuredAtFairValue": {
        "label":       "Current financial assets at fair value through profit or loss, mandatorily measured at fair value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentFinancialAssetsAtFairValueThroughProfitOrLossMeasuredAsSuchInAccordanceWithExemptionForReacquisitionOfOwnEquityInstruments": {
        "label":       "Current financial assets at fair value through profit or loss, measured as such in accordance with exemption for reacquisition of own equity instruments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentFinancialAssetsAtFairValueThroughProfitOrLossMeasuredAsSuchInAccordanceWithExemptionForRepurchaseOfOwnFinancialLiabilities": {
        "label":       "Current financial assets at fair value through profit or loss, measured as such in accordance with exemption for repurchase of own financial liabilities",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentFinancialAssetsAvailableforsale": {
        "label":       "Current financial assets available-for-sale",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Current financial assets measured at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentFinancialLiabilities": {
        "label":       "Current financial liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentFinancialLiabilitiesAtAmortisedCost": {
        "label":       "Current financial liabilities at amortised cost",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentFinancialLiabilitiesAtFairValueThroughProfitOrLoss": {
        "label":       "Current financial liabilities at fair value through profit or loss",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentFinancialLiabilitiesAtFairValueThroughProfitOrLossClassifiedAsHeldForTrading": {
        "label":       "Current financial liabilities at fair value through profit or loss, classified as held for trading",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentFinancialLiabilitiesAtFairValueThroughProfitOrLossDesignatedUponInitialRecognition": {
        "label":       "Current financial liabilities at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentFoodAndBeverage": {
        "label":       "Current food and beverage",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentFuel": {
        "label":       "Current fuel",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentGovernmentGrants": {
        "label":       "Current government grants",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentHeldtomaturityInvestments": {
        "label":       "Current held-to-maturity investments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentInterestPayable": {
        "label":       "Current interest payable",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentInterestReceivable": {
        "label":       "Current interest receivable",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentInventoriesHeldForSale": {
        "label":       "Current inventories held for sale",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentInventoriesInTransit": {
        "label":       "Current inventories in transit",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentInvestments": {
        "label":       "Current investments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentInvestmentsInEquityInstrumentsDesignatedAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Current investments in equity instruments designated at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentLeaseLiabilities": {
        "label":       "Current lease liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentLiabilities": {
        "label":       "Current liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentLiabilitiesOtherThanLiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale": {
        "label":       "Current liabilities other than liabilities included in disposal groups classified as held for sale",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentLiabilitiesRecognisedAsOfAcquisitionDate": {
        "label":       "Current liabilities recognised as of acquisition date",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentLoansAndReceivables": {
        "label":       "Current loans and receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentLoansReceivedAndCurrentPortionOfNoncurrentLoansReceived": {
        "label":       "Current loans received and current portion of non-current loans received",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentMaterialsAndSuppliesToBeConsumedInProductionProcessOrRenderingServices": {
        "label":       "Current materials and supplies to be consumed in production process or rendering services",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentNaturalGas": {
        "label":       "Current natural gas",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentNoncashAssetsPledgedAsCollateralForWhichTransfereeHasRightByContractOrCustomToSellOrRepledgeCollateral": {
        "label":       "Current non-cash assets pledged as collateral for which transferee has right by contract or custom to sell or repledge collateral",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentNotesAndDebenturesIssuedAndCurrentPortionOfNoncurrentNotesAndDebenturesIssued": {
        "label":       "Current notes and debentures issued and current portion of non-current notes and debentures issued",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentOreStockpiles": {
        "label":       "Current ore stockpiles",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentPackagingAndStorageMaterials": {
        "label":       "Current packaging and storage materials",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentPayablesForPurchaseOfEnergy": {
        "label":       "Current payables for purchase of energy",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentPayablesForPurchaseOfNoncurrentAssets": {
        "label":       "Current payables for purchase of non-current assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentPayablesOnSocialSecurityAndTaxesOtherThanIncomeTax": {
        "label":       "Current payables on social security and taxes other than income tax",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentPetroleumAndPetrochemicalProducts": {
        "label":       "Current petroleum and petrochemical products",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentPortionOfLongtermBorrowings": {
        "label":       "Current portion of non-current borrowings",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentPrepaidExpenses": {
        "label":       "Current prepaid expenses",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentPrepayments": {
        "label":       "Current prepayments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentPrepaymentsAndCurrentAccruedIncomeIncludingCurrentContractAssets": {
        "label":       "Current prepayments and current accrued income including current contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentPrepaymentsAndCurrentAccruedIncomeOtherThanCurrentContractAssets": {
        "label":       "Current prepayments and current accrued income other than current contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentPrepaymentsAndOtherCurrentAssets": {
        "label":       "Current prepayments and other current assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentProgrammingAssets": {
        "label":       "Current programming assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentProvisions": {
        "label":       "Current provisions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentProvisionsForEmployeeBenefits": {
        "label":       "Current provisions for employee benefits",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentRawMaterialsAndCurrentProductionSupplies": {
        "label":       "Current raw materials and current production supplies",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentReceivablesDueFromAssociates": {
        "label":       "Current receivables due from associates",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentReceivablesDueFromJointVentures": {
        "label":       "Current receivables due from joint ventures",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentReceivablesFromContractsWithCustomers": {
        "label":       "Current receivables from contracts with customers",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentReceivablesFromRentalOfProperties": {
        "label":       "Current receivables from rental of properties",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentReceivablesFromSaleOfProperties": {
        "label":       "Current receivables from sale of properties",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentReceivablesFromTaxesOtherThanIncomeTax": {
        "label":       "Current receivables from taxes other than income tax",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentRecognisedAssetsDefinedBenefitPlan": {
        "label":       "Current net defined benefit asset",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentRecognisedLiabilitiesDefinedBenefitPlan": {
        "label":       "Current net defined benefit liability",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentRefundsProvision": {
        "label":       "Current refunds provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentRestrictedCashAndCashEquivalents": {
        "label":       "Current restricted cash and cash equivalents",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentRetentionPayables": {
        "label":       "Current retention payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentSecuredBankLoansReceivedAndCurrentPortionOfNoncurrentSecuredBankLoansReceived": {
        "label":       "Current secured bank loans received and current portion of non-current secured bank loans received",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentServiceCostDefinedBenefitPlans": {
        "label":       "Current service cost defined benefit plans",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CurrentServiceCostNetDefinedBenefitLiabilityAsset": {
        "label":       "Increase in net defined benefit liability (asset) resulting from current service cost",
        "balance":     "credit",
        "period_type": "duration",
    },
    "CurrentTaxAssets": {
        "label":       "Current tax assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentTaxAssetsCurrent": {
        "label":       "Current tax assets, current",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentTaxAssetsNoncurrent": {
        "label":       "Current tax assets, non-current",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentTaxExpenseIncome": {
        "label":       "Current tax expense income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CurrentTaxExpenseIncomeAndAdjustmentsForCurrentTaxOfPriorPeriods": {
        "label":       "Current tax expense income and adjustments for current tax of prior periods",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CurrentTaxExpenseIncomeRelatedToPillarTwoIncomeTaxes": {
        "label":       "Current tax expense (income), related to Pillar Two income taxes",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CurrentTaxLiabilities": {
        "label":       "Current tax liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentTaxLiabilitiesCurrent": {
        "label":       "Current tax liabilities, current",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentTaxLiabilitiesNoncurrent": {
        "label":       "Current tax liabilities, non-current",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentTaxRelatingToItemsChargedOrCreditedDirectlyToEquity": {
        "label":       "Current tax relating to items credited (charged) directly to equity",
        "balance":     "debit",
        "period_type": "duration",
    },
    "CurrentTradeReceivables": {
        "label":       "Current trade receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentUnsecuredBankLoansReceivedAndCurrentPortionOfNoncurrentUnsecuredBankLoansReceived": {
        "label":       "Current unsecured bank loans received and current portion of non-current unsecured bank loans received",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentValueAddedTaxPayables": {
        "label":       "Current value added tax payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CurrentValueAddedTaxReceivables": {
        "label":       "Current value added tax receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "CurrentWarrantLiability": {
        "label":       "Current warrant liability",
        "balance":     "credit",
        "period_type": "instant",
    },
    "CustomerrelatedIntangibleAssetsRecognisedAsOfAcquisitionDate": {
        "label":       "Customer-related intangible assets recognised as of acquisition date",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DatedSubordinatedLiabilities": {
        "label":       "Dated subordinated liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DebtInstrumentsAmountContributedToFairValueOfPlanAssets": {
        "label":       "Debt instruments, amount contributed to fair value of plan assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DebtInstrumentsHeld": {
        "label":       "Debt instruments held",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DebtInstrumentsHeldAtAmortisedCost": {
        "label":       "Debt instruments held at amortised cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DebtInstrumentsHeldAtFairValueThroughProfitOrLossClassifiedAsHeldForTrading": {
        "label":       "Debt instruments held at fair value through profit or loss, classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DebtInstrumentsHeldAtFairValueThroughProfitOrLossMandatorilyMeasuredAtFairValueOtherThanThoseClassifiedAsHeldForTrading": {
        "label":       "Debt instruments held at fair value through profit or loss, mandatorily measured at fair value, other than those classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DebtInstrumentsHeldMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Debt instruments held measured at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DebtInstrumentsIssuedAtAmortisedCost": {
        "label":       "Debt instruments issued at amortised cost",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DebtInstrumentsIssuedAtFairValueThroughProfitOrLossDesignatedUponInitialRecognitionOrSubsequently": {
        "label":       "Debt instruments issued at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DebtSecurities": {
        "label":       "Debt instruments issued",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DecreaseDueToHarvestBiologicalAssets": {
        "label":       "Decrease due to harvest, biological assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsAssets": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsEntitysOwnEquityInstruments": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, entity's own equity instruments",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsLiabilities": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInOtherComprehensiveIncomeAfterTaxAssets": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in other comprehensive income, after tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInOtherComprehensiveIncomeAfterTaxEntitysOwnEquityInstruments": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in other comprehensive income, after tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInOtherComprehensiveIncomeAfterTaxLiabilities": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in other comprehensive income, after tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInOtherComprehensiveIncomeBeforeTaxAssets": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in other comprehensive income, before tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInOtherComprehensiveIncomeBeforeTaxEntitysOwnEquityInstruments": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in other comprehensive income, before tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInOtherComprehensiveIncomeBeforeTaxLiabilities": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in other comprehensive income, before tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInProfitOrLossAfterTaxAssets": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in profit or loss, after tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInProfitOrLossAfterTaxEntitysOwnEquityInstruments": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in profit or loss, after tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInProfitOrLossAfterTaxLiabilities": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in profit or loss, after tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInProfitOrLossBeforeTaxAssets": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in profit or loss, before tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInProfitOrLossBeforeTaxEntitysOwnEquityInstruments": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in profit or loss, before tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "DecreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInProfitOrLossBeforeTaxLiabilities": {
        "label":       "Decrease in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in profit or loss, before tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "DecreaseIncreaseThroughTaxOnSharebasedPaymentTransactions": {
        "label":       "Decrease (increase) through tax on share-based payment transactions, equity",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DecreaseThroughBalancesRecoveredInCurrentPeriodRegulatoryDeferralAccountDebitBalances": {
        "label":       "Decrease through balances recovered in current period, regulatory deferral account debit balances",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughBalancesReversedInCurrentPeriodRegulatoryDeferralAccountCreditBalances": {
        "label":       "Decrease through balances reversed in current period, regulatory deferral account credit balances",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DecreaseThroughBenefitsPaidReimbursementRightsAtFairValue": {
        "label":       "Decrease in reimbursement rights related to defined benefit obligation, resulting from benefits paid",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughClassifiedAsHeldForSaleBiologicalAssets": {
        "label":       "Decrease through classified as held for sale, biological assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughClassifiedAsHeldForSaleGoodwill": {
        "label":       "Decrease through classified as held for sale, goodwill",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughClassifiedAsHeldForSaleIntangibleAssetsAndGoodwill": {
        "label":       "Decrease through classified as held for sale, intangible assets and goodwill",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughClassifiedAsHeldForSaleIntangibleAssetsOtherThanGoodwill": {
        "label":       "Decrease through classified as held for sale, intangible assets other than goodwill",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughClassifiedAsHeldForSaleInvestmentProperty": {
        "label":       "Decrease through classified as held for sale, investment property",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughClassifiedAsHeldForSalePropertyPlantAndEquipment": {
        "label":       "Decrease through classified as held for sale, property, plant and equipment",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughClassifiedAsHeldForSalePropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Decrease through classified as held for sale, property, plant and equipment including right-of-use assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughClassifiedAsHeldForSaleRightofuseAssets": {
        "label":       "Decrease through classified as held for sale, right-of-use assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughDerecognitionExposureToCreditRiskOnLoanCommitmentsAndFinancialGuaranteeContracts": {
        "label":       "Decrease through derecognition, exposure to credit risk on loan commitments and financial guarantee contracts",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DecreaseThroughDerecognitionFinancialAssets": {
        "label":       "Decrease through derecognition, financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughDisposalsRegulatoryDeferralAccountCreditBalances": {
        "label":       "Decrease through disposals, regulatory deferral account credit balances",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DecreaseThroughDisposalsRegulatoryDeferralAccountDebitBalances": {
        "label":       "Decrease through disposals, regulatory deferral account debit balances",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughImpairmentContractAssets": {
        "label":       "Decrease through impairment, contract assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughImpairmentLossesAssetsForInsuranceAcquisitionCashFlows": {
        "label":       "Decrease through impairment losses, assets for insurance acquisition cash flows",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughImpairmentsRegulatoryDeferralAccountDebitBalances": {
        "label":       "Decrease through impairments, regulatory deferral account debit balances",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughLossOfControlOfSubsidiaryIntangibleAssetsAndGoodwill": {
        "label":       "Decrease through loss of control of subsidiary, intangible assets and goodwill",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughLossOfControlOfSubsidiaryIntangibleAssetsOtherThanGoodwill": {
        "label":       "Decrease through loss of control of subsidiary, intangible assets other than goodwill",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughLossOfControlOfSubsidiaryOtherProvisions": {
        "label":       "Decrease through loss of control of subsidiary, other provisions",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DecreaseThroughLossOfControlOfSubsidiaryPropertyPlantAndEquipment": {
        "label":       "Decrease through loss of control of subsidiary, property, plant and equipment",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughLossOfControlOfSubsidiaryPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Decrease through loss of control of subsidiary, property, plant and equipment including right-of-use assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughLossOfControlOfSubsidiaryRightofuseAssets": {
        "label":       "Decrease through loss of control of subsidiary, right-of-use assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughPerformanceObligationBeingSatisfiedContractLiabilities": {
        "label":       "Decrease through performance obligation being satisfied, contract liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DecreaseThroughRightToConsiderationBecomingUnconditionalContractAssets": {
        "label":       "Decrease through right to consideration becoming unconditional, contract assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DecreaseThroughTransferToLiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSaleOtherProvisions": {
        "label":       "Decrease through transfer to liabilities included in disposal groups classified as held for sale, other provisions",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DecreaseThroughWriteoffFinancialAssets": {
        "label":       "Decrease through write-off, financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DeductibleTemporaryDifferencesForWhichNoDeferredTaxAssetIsRecognised": {
        "label":       "Deductible temporary differences for which no deferred tax asset is recognised",
        "balance":     "None",
        "period_type": "instant",
    },
    "DeemedCostOfInvestmentsForWhichDeemedCostIsFairValue": {
        "label":       "Aggregate deemed cost of investments for which deemed cost is fair value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DeemedCostOfInvestmentsForWhichDeemedCostIsPreviousGAAPCarryingAmount": {
        "label":       "Aggregate deemed cost of investments for which deemed cost is previous GAAP carrying amount",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DeferredIncomeIncludingContractLiabilities": {
        "label":       "Deferred income including contract liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DeferredIncomeIncludingContractLiabilitiesRecognisedAsOfAcquisitionDate": {
        "label":       "Deferred income including contract liabilities recognised as of acquisition date",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DeferredIncomeOtherThanContractLiabilities": {
        "label":       "Deferred income other than contract liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DeferredIncomeOtherThanContractLiabilitiesRecognisedAsOfAcquisitionDate": {
        "label":       "Deferred income other than contract liabilities recognised as of acquisition date",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DeferredTaxAssetAssociatedWithRegulatoryDeferralAccountBalances": {
        "label":       "Deferred tax asset associated with regulatory deferral account balances",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DeferredTaxAssetWhenUtilisationIsDependentOnFutureTaxableProfitsInExcessOfProfitsFromReversalOfTaxableTemporaryDifferencesAndEntityHasSufferedLossInJurisdictionToWhichDeferredTaxAssetRelates": {
        "label":       "Deferred tax asset when utilisation is dependent on future taxable profits in excess of profits from reversal of taxable temporary differences and entity has suffered loss in jurisdiction to which deferred tax asset relates",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DeferredTaxAssets": {
        "label":       "Deferred tax assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DeferredTaxAssetsRecognisedAsOfAcquisitionDate": {
        "label":       "Deferred tax assets recognised as of acquisition date",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DeferredTaxExpenseArisingFromWritedownOrReversalOfWritedownOfDeferredTaxAsset": {
        "label":       "Deferred tax expense arising from writedown or reversal of writedown of deferred tax asset",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DeferredTaxExpenseIncome": {
        "label":       "Deferred tax expense (income)",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DeferredTaxExpenseIncomeRecognisedInProfitOrLoss": {
        "label":       "Deferred tax expense income recognised in profit or loss",
        "balance":     "None",
        "period_type": "duration",
    },
    "DeferredTaxExpenseIncomeRelatingToOriginationAndReversalOfTemporaryDifferences": {
        "label":       "Deferred tax expense income relating to origination and reversal of temporary differences",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DeferredTaxExpenseIncomeRelatingToTaxRateChangesOrImpositionOfNewTaxes": {
        "label":       "Deferred tax expense income relating to tax rate changes or imposition of new taxes",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DeferredTaxLiabilities": {
        "label":       "Deferred tax liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DeferredTaxLiabilitiesRecognisedAsOfAcquisitionDate": {
        "label":       "Deferred tax liabilities recognised as of acquisition date",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DeferredTaxLiabilityAsset": {
        "label":       "Deferred tax liability (asset)",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DeferredTaxLiabilityAssociatedWithRegulatoryDeferralAccountBalances": {
        "label":       "Deferred tax liability associated with regulatory deferral account balances",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DeferredTaxRelatingToItemsChargedOrCreditedDirectlyToEquity": {
        "label":       "Deferred tax relating to items credited (charged) directly to equity",
        "balance":     "None",
        "period_type": "duration",
    },
    "DefinedBenefitObligationAtPresentValue": {
        "label":       "Defined benefit obligation, at present value",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DepositLiabilities": {
        "label":       "Deposit liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DepositsAtAmortisedCost": {
        "label":       "Deposits at amortised cost",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DepositsAtFairValueThroughProfitOrLossDesignatedUponInitialRecognitionOrSubsequently": {
        "label":       "Deposits at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DepositsAtFairValueThroughProfitOrLossThatMeetDefinitionOfHeldForTrading": {
        "label":       "Deposits at fair value through profit or loss that meet definition of held for trading",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DepositsFromBanks": {
        "label":       "Deposits from banks",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DepositsFromBanksAtAmortisedCost": {
        "label":       "Deposits from banks at amortised cost",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DepositsFromBanksAtFairValueThroughProfitOrLossDesignatedUponInitialRecognitionOrSubsequently": {
        "label":       "Deposits from banks at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DepositsFromBanksAtFairValueThroughProfitOrLossThatMeetDefinitionOfHeldForTrading": {
        "label":       "Deposits from banks at fair value through profit or loss that meet definition of held for trading",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DepositsFromCustomers": {
        "label":       "Deposits from customers",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DepositsFromCustomersAtAmortisedCost": {
        "label":       "Deposits from customers at amortised cost",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DepositsFromCustomersAtFairValueThroughProfitOrLossDesignatedUponInitialRecognitionOrSubsequently": {
        "label":       "Deposits from customers at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DepositsFromCustomersAtFairValueThroughProfitOrLossThatMeetDefinitionOfHeldForTrading": {
        "label":       "Deposits from customers at fair value through profit or loss that meet definition of held for trading",
        "balance":     "credit",
        "period_type": "instant",
    },
    "Depreciation": {
        "label":       "Depreciation",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DepreciationAmortisationAndImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLoss": {
        "label":       "Depreciation amortisation and impairment loss reversal of impairment loss recognised in profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DepreciationAmortisationAndImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLossInvesting": {
        "label":       "Depreciation amortisation and impairment loss reversal of impairment loss recognised in profit or loss investing",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DepreciationAndAmortisationExpense": {
        "label":       "Depreciation and amortisation expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DepreciationAndAmortisationExpenseOperating": {
        "label":       "Depreciation and amortisation expense operating",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DepreciationBiologicalAssets": {
        "label":       "Depreciation biological assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "DepreciationExpense": {
        "label":       "Depreciation expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DepreciationInvestmentProperty": {
        "label":       "Depreciation, investment property",
        "balance":     "None",
        "period_type": "duration",
    },
    "DepreciationPropertyPlantAndEquipment": {
        "label":       "Depreciation property plant and equipment",
        "balance":     "None",
        "period_type": "duration",
    },
    "DepreciationPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Depreciation property plant and equipment including rightofuse assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "DepreciationRightofuseAssets": {
        "label":       "Depreciation, right-of-use assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "DerivativeFinancialAssets": {
        "label":       "Derivative financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DerivativeFinancialAssetsHeldForHedging": {
        "label":       "Derivative financial assets held for hedging",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DerivativeFinancialAssetsHeldForTrading": {
        "label":       "Derivative financial assets held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DerivativeFinancialLiabilities": {
        "label":       "Derivative financial liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DerivativeFinancialLiabilitiesHeldForHedging": {
        "label":       "Derivative financial liabilities held for hedging",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DerivativeFinancialLiabilitiesHeldForTrading": {
        "label":       "Derivative financial liabilities held for trading",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DerivativeFinancialLiabilitiesUndiscountedCashFlows": {
        "label":       "Derivative financial liabilities, undiscounted cash flows",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DerivativesAmountContributedToFairValueOfPlanAssets": {
        "label":       "Derivatives, amount contributed to fair value of plan assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DescriptionOfAmountsOfEntitysOwnFinancialInstrumentsIncludedInFairValueOfPlanAssets": {
        "label":       "Entity's own financial instruments included in fair value of plan assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DescriptionOfAmountsOfOtherAssetsUsedByEntityIncludedInFairValueOfPlanAssets": {
        "label":       "Other assets used by entity included in fair value of plan assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DescriptionOfAmountsOfPropertyOccupiedByEntityIncludedInFairValueOfPlanAssets": {
        "label":       "Property occupied by entity included in fair value of plan assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DifferenceBetweenCarryingAmountOfDividendsPayableAndCarryingAmountOfNoncashAssetsDistributed": {
        "label":       "Difference between carrying amount of dividends payable and carrying amount of noncash assets distributed",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DifferenceBetweenCarryingAmountOfFinancialLiabilityAndAmountContractuallyRequiredToPayAtMaturityToHolderOfObligation": {
        "label":       "Difference between carrying amount of financial liability and amount contractually required to pay at maturity to holder of obligation",
        "balance":     "None",
        "period_type": "instant",
    },
    "DirectOperatingExpenseFromInvestmentProperty": {
        "label":       "Direct operating expense from investment property",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DirectOperatingExpenseFromInvestmentPropertyGeneratingRentalIncome": {
        "label":       "Direct operating expense from investment property generating rental income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DirectOperatingExpenseFromInvestmentPropertyNotGeneratingRentalIncome": {
        "label":       "Direct operating expense from investment property not generating rental income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DirectorsRemunerationExpense": {
        "label":       "Directors remuneration expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DilutedEarningsLossPerShare": {
        "label":       "Diluted earnings (loss) per share",
        "balance":     "",
        "period_type": "duration",
    },
    "DiscountedUnguaranteedResidualValueOfAssetsSubjectToFinanceLease": {
        "label":       "Discounted unguaranteed residual value of assets subject to finance lease",
        "balance":     "debit",
        "period_type": "instant",
    },
    "DisposalsAndRetirementsIntangibleAssetsAndGoodwill": {
        "label":       "Disposals and retirements, intangible assets and goodwill",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DisposalsAndRetirementsIntangibleAssetsOtherThanGoodwill": {
        "label":       "Disposals and retirements, intangible assets other than goodwill",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DisposalsAndRetirementsPropertyPlantAndEquipment": {
        "label":       "Disposals and retirements, property, plant and equipment",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DisposalsAndRetirementsPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Disposals and retirements, property, plant and equipment including right-of-use assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DisposalsAndRetirementsRightofuseAssets": {
        "label":       "Disposals and retirements, right-of-use assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DisposalsBiologicalAssets": {
        "label":       "Disposals, biological assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DisposalsIntangibleAssetsAndGoodwill": {
        "label":       "Disposals, intangible assets and goodwill",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DisposalsIntangibleAssetsOtherThanGoodwill": {
        "label":       "Disposals, intangible assets other than goodwill",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DisposalsInvestmentProperty": {
        "label":       "Disposals, investment property",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DisposalsPropertyPlantAndEquipment": {
        "label":       "Disposals, property, plant and equipment",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DisposalsPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Disposals, property, plant and equipment including right-of-use assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DisposalsRightofuseAssets": {
        "label":       "Disposals, right-of-use assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DistributionAndAdministrativeExpense": {
        "label":       "Distribution and administrative expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DistributionCosts": {
        "label":       "Distribution costs",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendPayables": {
        "label":       "Dividend payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DividendsClassifiedAsExpense": {
        "label":       "Dividends classified as expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsClassifiedAsExpenseOperating": {
        "label":       "Dividends classified as expense operating",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsPaid": {
        "label":       "Dividends recognised as distributions to owners",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsPaidClassifiedAsFinancingActivities": {
        "label":       "Dividends paid, classified as financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DividendsPaidClassifiedAsOperatingActivities": {
        "label":       "Dividends paid classified as operating activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DividendsPaidOrdinaryShares": {
        "label":       "Dividends paid, ordinary shares",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsPaidOtherShares": {
        "label":       "Dividends paid, other shares",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsPaidToEquityHoldersOfParentClassifiedAsFinancingActivities": {
        "label":       "Dividends paid to equity holders of parent, classified as financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DividendsPaidToNoncontrollingInterests": {
        "label":       "Dividends paid to non-controlling interests",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DividendsPaidToNoncontrollingInterestsClassifiedAsFinancingActivities": {
        "label":       "Dividends paid to non-controlling interests, classified as financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DividendsPayable": {
        "label":       "Dividends payable, non-cash assets distributions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "DividendsProposedOrDeclaredBeforeFinancialStatementsAuthorisedForIssueButNotRecognisedAsDistributionToOwners": {
        "label":       "Dividends proposed or declared before financial statements authorised for issue but not recognised as distribution to owners",
        "balance":     "None",
        "period_type": "duration",
    },
    "DividendsReceived": {
        "label":       "Dividends received",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsReceivedClassifiedAsInvestingActivities": {
        "label":       "Dividends received, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsReceivedClassifiedAsOperatingActivities": {
        "label":       "Dividends received, classified as operating activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsReceivedFromAssociatesClassifiedAsInvestingActivities": {
        "label":       "Dividends received from associates, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsReceivedFromInvestmentsAccountedForUsingEquityMethodClassifiedAsInvestingActivities": {
        "label":       "Dividends received from investments accounted for using equity method, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsReceivedFromJointVenturesClassifiedAsInvestingActivities": {
        "label":       "Dividends received from joint ventures, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsRecognisedAsDistributionsToNoncontrollingInterests": {
        "label":       "Dividends recognised as distributions to non-controlling interests",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsRecognisedAsDistributionsToOwnersOfParent": {
        "label":       "Dividends recognised as distributions to owners of parent",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsRecognisedAsDistributionsToOwnersOfParentRelatingToCurrentYear": {
        "label":       "Dividends recognised as distributions to owners of parent, relating to current year",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsRecognisedAsDistributionsToOwnersOfParentRelatingToPriorYears": {
        "label":       "Dividends recognised as distributions to owners of parent, relating to prior years",
        "balance":     "debit",
        "period_type": "duration",
    },
    "DividendsRecognisedForInvestmentsInEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeDerecognisedDuringPeriod": {
        "label":       "Dividends recognised for investments in equity instruments designated at fair value through other comprehensive income, derecognised during period",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DividendsRecognisedForInvestmentsInEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncomeHeldAtEndOfReportingPeriod": {
        "label":       "Dividends recognised for investments in equity instruments designated at fair value through other comprehensive income, held at end of reporting period",
        "balance":     "credit",
        "period_type": "duration",
    },
    "DonationsAndSubsidiesExpense": {
        "label":       "Donations and subsidies expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "EffectOfExchangeRateChangesOnCashAndCashEquivalents": {
        "label":       "Effect of exchange rate changes on cash and cash equivalents",
        "balance":     "debit",
        "period_type": "duration",
    },
    "EffectOnAdjustmentToContractualServiceMarginOfChoiceNotToAdjustContractualServiceMarginForSomeChangesInFulfilmentCashFlowsForContractsWithDirectParticipationFeatures": {
        "label":       "Effect on adjustment to contractual service margin of choice not to adjust contractual service margin for some changes in fulfilment cash flows for contracts with direct participation features",
        "balance":     "credit",
        "period_type": "duration",
    },
    "EmployeeBenefitsExpense": {
        "label":       "Employee benefits expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "EmployeeContributions": {
        "label":       "Employee contributions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "EmployerContributions": {
        "label":       "Employer contributions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "EnergyExpense": {
        "label":       "Energy expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "EnergyTransmissionCharges": {
        "label":       "Energy transmission charges",
        "balance":     "debit",
        "period_type": "duration",
    },
    "Equity": {
        "label":       "Equity",
        "balance":     "credit",
        "period_type": "instant",
    },
    "EquityAndLiabilities": {
        "label":       "Equity and liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "EquityAttributableToOwnersOfParent": {
        "label":       "Equity attributable to owners of parent",
        "balance":     "credit",
        "period_type": "instant",
    },
    "EquityInstrumentsAmountContributedToFairValueOfPlanAssets": {
        "label":       "Equity instruments, amount contributed to fair value of plan assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "EquityInstrumentsHeld": {
        "label":       "Equity instruments held",
        "balance":     "debit",
        "period_type": "instant",
    },
    "EquityInstrumentsHeldAtFairValueThroughProfitOrLossClassifiedAsHeldForTrading": {
        "label":       "Equity instruments held at fair value through profit or loss, classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "EquityInstrumentsHeldAtFairValueThroughProfitOrLossMandatorilyMeasuredAtFairValueOtherThanThoseClassifiedAsHeldForTrading": {
        "label":       "Equity instruments held at fair value through profit or loss, mandatorily measured at fair value, other than those classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "EquityInterestsOfAcquirer": {
        "label":       "Equity interests of acquirer",
        "balance":     "credit",
        "period_type": "instant",
    },
    "EquityLiabilitiesAndRegulatoryDeferralAccountCreditBalances": {
        "label":       "Equity, liabilities and regulatory deferral account credit balances",
        "balance":     "credit",
        "period_type": "instant",
    },
    "EquityReclassifiedIntoFinancialLiabilities": {
        "label":       "Equity reclassified into financial liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "EstimateOfBenefitPaymentsExpectedToBePaidFromDefinedBenefitPlan": {
        "label":       "Estimate of benefit payments expected to be paid from defined benefit plan",
        "balance":     "credit",
        "period_type": "duration",
    },
    "EstimateOfContributionsExpectedToBePaidToPlan": {
        "label":       "Estimate of contributions expected to be paid to plan for next annual reporting period",
        "balance":     "credit",
        "period_type": "duration",
    },
    "EstimateOfUndiscountedClaimsThatAriseFromContractsWithinScopeOfIFRS17": {
        "label":       "Estimate of undiscounted claims that arise from contracts within scope of IFRS 17",
        "balance":     "credit",
        "period_type": "instant",
    },
    "EstimatedCashFlowsOfFinancialAssetsReclassifiedOutOfAvailableforsaleFinancialAssets": {
        "label":       "Estimated cash flows of financial assets reclassified out of available-for-sale financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "EstimatedCashFlowsOfFinancialAssetsReclassifiedOutOfFinancialAssetsAtFairValueThroughProfitOrLoss": {
        "label":       "Estimated cash flows of financial assets reclassified out of financial assets at fair value through profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "EstimatedFinancialEffectContingentLiabilitiesInBusinessCombination": {
        "label":       "Estimated financial effect, contingent liabilities in business combination",
        "balance":     "credit",
        "period_type": "instant",
    },
    "EstimatedFinancialEffectOfContingentAssets": {
        "label":       "Estimated financial effect of contingent assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "EstimatedFinancialEffectOfContingentLiabilities": {
        "label":       "Estimated financial effect of contingent liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "EstimatedFutureCashFlowsFromBuyingElectricityUnderContractsForReceiptOfNaturedependentElectricity": {
        "label":       "Estimated future cash flows from buying electricity under contracts for receipt of nature-dependent electricity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "EstimatesOfPresentValueOfFutureCashOutflowsInflowsThatAriseFromContractsWithinScopeOfIFRS17ThatAreLiabilities": {
        "label":       "Estimates of present value of future cash outflows (inflows) that arise from contracts within scope of IFRS 17 that are liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ExciseTaxPayables": {
        "label":       "Excise tax payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ExpectedCashOutflowOnRedemptionOrRepurchaseOfPuttableFinancialInstruments": {
        "label":       "Expected cash outflow on redemption or repurchase of puttable financial instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ExpectedDividendShareOptionsGranted": {
        "label":       "Expected dividend, share options granted",
        "balance":     "None",
        "period_type": "duration",
    },
    "ExpectedReimbursementContingentLiabilitiesInBusinessCombination": {
        "label":       "Expected reimbursement, contingent liabilities in business combination",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ExpectedReimbursementOtherProvisions": {
        "label":       "Expected reimbursement, other provisions",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ExpenseArisingFromExplorationForAndEvaluationOfMineralResources": {
        "label":       "Expense arising from exploration for and evaluation of mineral resources",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpenseByNature": {
        "label":       "Expense by nature",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpenseDueToUnwindingOfDiscountOnProvisions": {
        "label":       "Expense due to unwinding of discount on provisions",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpenseFromCashsettledSharebasedPaymentTransactionsInWhichGoodsOrServicesReceivedDidNotQualifyForRecognitionAsAssets": {
        "label":       "Expense from cashsettled sharebased payment transactions in which goods or services received did not qualify for recognition as assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpenseFromContinuingInvolvementInDerecognisedFinancialAssets": {
        "label":       "Expense from continuing involvement in derecognised financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpenseFromContinuingInvolvementInDerecognisedFinancialAssetsCumulativelyRecognised": {
        "label":       "Expense from continuing involvement in derecognised financial assets cumulatively recognised",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ExpenseFromEquitysettledSharebasedPaymentTransactionsInWhichGoodsOrServicesReceivedDidNotQualifyForRecognitionAsAssets": {
        "label":       "Expense from equitysettled sharebased payment transactions in which goods or services received did not qualify for recognition as assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpenseFromSharebasedPaymentTransactionsInWhichGoodsOrServicesReceivedDidNotQualifyForRecognitionAsAssets": {
        "label":       "Expense from sharebased payment transactions in which goods or services received did not qualify for recognition as assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpenseFromSharebasedPaymentTransactionsWithEmployees": {
        "label":       "Expense from sharebased payment transactions with employees",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpenseFromSharebasedPaymentTransactionsWithPartiesOtherThanEmployees": {
        "label":       "Expense from sharebased payment transactions with parties other than employees",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpenseOfRestructuringActivities": {
        "label":       "Expense of restructuring activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpenseRecognisedDuringPeriodForBadAndDoubtfulDebtsForRelatedPartyTransaction": {
        "label":       "Expense recognised during period for bad and doubtful debts for related party transaction",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpenseRelatingToLeasesOfLowvalueAssetsForWhichRecognitionExemptionHasBeenUsed": {
        "label":       "Expense relating to leases of lowvalue assets for which recognition exemption has been used",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpenseRelatingToShorttermLeasesForWhichRecognitionExemptionHasBeenUsed": {
        "label":       "Expense relating to shortterm leases for which recognition exemption has been used",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpenseRelatingToVariableLeasePaymentsNotIncludedInMeasurementOfLeaseLiabilities": {
        "label":       "Expense relating to variable lease payments not included in measurement of lease liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpensesFromAllocationOfPremiumsPaidToReinsurer": {
        "label":       "Expenses from allocation of premiums paid to reinsurer",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpensesOnFinancialAssetsReclassifiedOutOfAvailableforsaleFinancialAssetsRecognisedInOtherComprehensiveIncome": {
        "label":       "Expenses on financial assets reclassified out of available-for-sale financial assets recognised in profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExpensesOnFinancialAssetsReclassifiedOutOfFinancialAssetsAtFairValueThroughProfitOrLossRecognisedInProfitOrLoss": {
        "label":       "Expenses on financial assets reclassified out of financial assets at fair value through profit or loss recognised in profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ExposureToCreditRiskOnLoanCommitmentsAndFinancialGuaranteeContracts": {
        "label":       "Exposure to credit risk on loan commitments and financial guarantee contracts",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ExposureToRiskThatArisesFromContractsWithinScopeOfIFRS17": {
        "label":       "Exposure to risk that arises from contracts within scope of IFRS 17",
        "balance":     "None",
        "period_type": "instant",
    },
    "FairValueGainLossThatWouldHaveBeenRecognisedInOtherComprehensiveIncomeIfFinancialAssetsHadNotBeenReclassified": {
        "label":       "Fair value gain (loss) that would have been recognised in other comprehensive income if financial assets had not been reclassified",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FairValueGainLossThatWouldHaveBeenRecognisedInProfitOrLossIfFinancialAssetsHadNotBeenReclassifiedOutOfFairValueThroughProfitOrLossAndIntoFairValueThroughOtherComprehensiveIncomeInitialApplicationOfIFRS9": {
        "label":       "Fair value gain (loss) that would have been recognised in profit or loss if financial assets had not been reclassified out of fair value through profit or loss and into fair value through other comprehensive income, initial application of IFRS 9",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FairValueGainLossThatWouldHaveBeenRecognisedInProfitOrLossOrOtherComprehensiveIncomeIfFinancialAssetsHadNotBeenReclassifiedFirstApplicationOfIFRS9": {
        "label":       "Fair value gain (loss) that would have been recognised in profit or loss or other comprehensive income if financial assets had not been reclassified as measured at amortised cost, initial application of IFRS 9",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FairValueGainLossThatWouldHaveBeenRecognisedInProfitOrLossOrOtherComprehensiveIncomeIfFinancialLiabilitiesHadNotBeenReclassifiedFirstApplicationOfIFRS9": {
        "label":       "Fair value gain (loss) that would have been recognised in profit or loss or other comprehensive income if financial liabilities had not been reclassified as measured at amortised cost, initial application of IFRS 9",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FairValueGainsLossesOnFinancialAssetsReclassifiedOutOfAvailableforsaleFinancialAssetsNotRecognisedInOtherComprehensiveIncome": {
        "label":       "Fair value gains (losses) on financial assets reclassified out of available-for-sale financial assets not recognised in other comprehensive income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FairValueGainsLossesOnFinancialAssetsReclassifiedOutOfAvailableforsaleFinancialAssetsRecognisedInOtherComprehensiveIncome": {
        "label":       "Fair value gains (losses) on financial assets reclassified out of available-for-sale financial assets recognised in other comprehensive income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FairValueGainsLossesOnFinancialAssetsReclassifiedOutOfFinancialAssetsAtFairValueThroughProfitOrLossNotRecognisedInProfitOrLoss": {
        "label":       "Fair value gains (losses) on financial assets reclassified out of financial assets at fair value through profit or loss not recognised in profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FairValueGainsLossesOnFinancialAssetsReclassifiedOutOfFinancialAssetsAtFairValueThroughProfitOrLossRecognisedInProfitOrLoss": {
        "label":       "Fair value gains (losses) on financial assets reclassified out of financial assets at fair value through profit or loss recognised in profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FairValueGainsOrLossThatWouldHaveBeenRecognisedInProfitOrLossIfFinancialAssetsHadNotBeenReclassified": {
        "label":       "Fair value gain (loss) that would have been recognised in profit or loss if financial assets had not been reclassified",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FairValueOfAcquiredReceivables": {
        "label":       "Fair value of acquired receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfAssetsRepresentingContinuingInvolvementInDerecognisedFinancialAssets": {
        "label":       "Fair value of assets representing continuing involvement in derecognised financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfAssociatedFinancialLiabilities": {
        "label":       "Fair value of associated financial liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FairValueOfFinancialAssetsReclassifiedAsMeasuredAtAmortisedCost": {
        "label":       "Fair value of financial assets reclassified out of fair value through profit or loss category into amortised cost or fair value through other comprehensive income category",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfFinancialAssetsReclassifiedAsMeasuredAtAmortisedCostFirstApplicationOfIFRS9": {
        "label":       "Fair value of financial assets reclassified as measured at amortised cost, initial application of IFRS 9",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfFinancialAssetsReclassifiedOutOfFairValueThroughOtherComprehensiveIncomeCategoryIntoAmortisedCostCategory": {
        "label":       "Fair value of financial assets reclassified out of fair value through other comprehensive income category into amortised cost category",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfFinancialAssetsReclassifiedOutOfFairValueThroughProfitOrLossAndIntoFairValueThroughOtherComprehensiveIncomeInitialApplicationOfIFRS9": {
        "label":       "Fair value of financial assets reclassified out of fair value through profit or loss and into fair value through other comprehensive income, initial application of IFRS 9",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfFinancialInstrumentOnDiscontinuationOfMeasurementAtFairValueThroughProfitOrLossBecauseCreditDerivativeIsUsedToManageCreditRiskAssets": {
        "label":       "Fair value of financial instrument on discontinuation of measurement at fair value through profit or loss because credit derivative is used to manage credit risk, assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfFinancialInstrumentOnDiscontinuationOfMeasurementAtFairValueThroughProfitOrLossBecauseCreditDerivativeIsUsedToManageCreditRiskLiabilities": {
        "label":       "Fair value of financial instrument on discontinuation of measurement at fair value through profit or loss because credit derivative is used to manage credit risk, liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FairValueOfFinancialLiabilitiesReclassifiedAsMeasuredAtAmortisedCostFirstApplicationOfIFRS9": {
        "label":       "Fair value of financial liabilities reclassified as measured at amortised cost, initial application of IFRS 9",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FairValueOfInvestmentInJointVenturesWherePriceQuotationsPublished": {
        "label":       "Fair value of investments in joint ventures for which there are quoted market prices",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfInvestmentPropertyWhenEntityAppliesCostModel": {
        "label":       "Fair value of investment property when entity applies cost model",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfInvestmentsInAssociatesWherePriceQuotationsPublished": {
        "label":       "Fair value of investments in associates for which there are quoted market prices",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfInvestmentsInEquityInstrumentsDesignatedAsMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Investments in equity instruments designated at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfInvestmentsInEquityInstrumentsMeasuredAtFairValueThroughOtherComprehensiveIncomeAtDateOfDerecognition": {
        "label":       "Fair value of investments in equity instruments designated at fair value through other comprehensive income at date of derecognition",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfLiabilitiesRepresentingContinuingInvolvementInDerecognisedFinancialAssets": {
        "label":       "Fair value of liabilities representing continuing involvement in derecognised financial assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FairValueOfPropertyPlantAndEquipmentMateriallyDifferentFromCarryingAmount": {
        "label":       "Fair value of property, plant and equipment materially different from carrying amount",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfSubsidiariesThatCeaseToBeConsolidatedAsOfDateOfChangeOfInvestmentEntityStatus": {
        "label":       "Fair value of subsidiaries that cease to be consolidated as of date of change of investment entity status",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfTransferredFinancialAssetsAssociatedFinancialLiabilitiesThatAreNotDerecognisedInTheirEntirety": {
        "label":       "Fair value of transferred financial assets (associated financial liabilities) that are not derecognised in their entirety",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfTransferredFinancialAssetsThatAreNotDerecognisedInTheirEntirety": {
        "label":       "Fair value of transferred financial assets that are not derecognised in their entirety",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FairValueOfUnderlyingItemsForContractsWithDirectParticipationFeatures": {
        "label":       "Fair value of underlying items for contracts with direct participation features",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FeeAndCommissionExpense": {
        "label":       "Fee and commission expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "FeeAndCommissionIncome": {
        "label":       "Fee and commission income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FeeAndCommissionIncomeExpense": {
        "label":       "Fee and commission income expense",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FeeExpenseArisingFromFinancialLiabilitiesNotAtFairValueThroughProfitOrLoss": {
        "label":       "Fee expense arising from financial liabilities not at fair value through profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "FeeIncomeArisingFromFinancialAssetsMeasuredAtAmortisedCost": {
        "label":       "Fee income arising from financial assets measured at amortised cost",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FeeIncomeExpenseArisingFromFinancialAssetsOrFinancialLiabilitiesNotAtFairValueThroughProfitOrLoss": {
        "label":       "Fee income (expense) arising from financial assets or financial liabilities not at fair value through profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FeeIncomeExpenseArisingFromTrustAndFiduciaryActivities": {
        "label":       "Fee income expense arising from trust and fiduciary activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FinanceCosts": {
        "label":       "Finance costs",
        "balance":     "debit",
        "period_type": "duration",
    },
    "FinanceCostsPaidClassifiedAsOperatingActivities": {
        "label":       "Finance costs paid classified as operating activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FinanceIncome": {
        "label":       "Finance income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FinanceIncomeCost": {
        "label":       "Finance income cost",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLossBeforeTax": {
        "label":       "Finance income (expenses) from reinsurance contracts held excluded from profit or loss, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLossNetOfTax": {
        "label":       "Finance income (expenses) from reinsurance contracts held excluded from profit or loss, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FinanceIncomeExpensesFromReinsuranceContractsHeldRecognisedInProfitOrLoss": {
        "label":       "Finance income expenses from reinsurance contracts held recognised in profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FinanceIncomeOnNetInvestmentInFinanceLease": {
        "label":       "Finance income on net investment in finance lease",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FinanceIncomeReceivedClassifiedAsOperatingActivities": {
        "label":       "Finance income received classified as operating activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "FinanceLeaseReceivables": {
        "label":       "Finance lease receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssets": {
        "label":       "Financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAffectedByAmendmentsToApplicationGuidanceToSectionOnClassificationOfFinancialAssetsCarryingAmountImmediatelyAfterApplyingAmendments": {
        "label":       "Financial assets affected by amendments to Application Guidance to section on classification of financial assets, carrying amount immediately after applying amendments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAffectedByAmendmentsToApplicationGuidanceToSectionOnClassificationOfFinancialAssetsCarryingAmountImmediatelyBeforeApplyingAmendments": {
        "label":       "Financial assets affected by amendments to Application Guidance to section on classification of financial assets, carrying amount immediately before applying amendments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAffectedByAmendmentsToIFRS9ForPrepaymentFeaturesWithNegativeCompensationCarryingAmountAfterApplyingAmendments": {
        "label":       "Financial assets affected by amendments to IFRS 9 for prepayment features with negative compensation, carrying amount after applying amendments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAffectedByAmendmentsToIFRS9ForPrepaymentFeaturesWithNegativeCompensationCarryingAmountImmediatelyBeforeApplyingAmendments": {
        "label":       "Financial assets affected by amendments to IFRS 9 for prepayment features with negative compensation, carrying amount immediately before applying amendments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAffectedByAmendmentsToIFRS9MadeByIFRS17CarryingAmountAfterApplyingAmendments": {
        "label":       "Financial assets affected by amendments to IFRS 9 made by IFRS 17, carrying amount after applying amendments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAffectedByAmendmentsToIFRS9MadeByIFRS17CarryingAmountImmediatelyBeforeApplyingAmendments": {
        "label":       "Financial assets affected by amendments to IFRS 9 made by IFRS 17, carrying amount immediately before applying amendments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAffectedByRedesignationAtDateOfInitialApplicationOfIFRS17CarryingAmountAfterRedesignation": {
        "label":       "Financial assets affected by redesignation at date of initial application of IFRS 17, carrying amount after redesignation",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAffectedByRedesignationAtDateOfInitialApplicationOfIFRS17CarryingAmountImmediatelyBeforeRedesignation": {
        "label":       "Financial assets affected by redesignation at date of initial application of IFRS 17, carrying amount immediately before redesignation",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAtAmortisedCost": {
        "label":       "Financial assets at amortised cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAtFairValue": {
        "label":       "Financial assets, at fair value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Financial assets at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAtFairValueThroughProfitOrLoss": {
        "label":       "Financial assets at fair value through profit or loss",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAtFairValueThroughProfitOrLossClassifiedAsHeldForTrading": {
        "label":       "Financial assets at fair value through profit or loss, classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAtFairValueThroughProfitOrLossDesignatedAsUponInitialRecognition": {
        "label":       "Financial assets at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAtFairValueThroughProfitOrLossMandatorilyMeasuredAtFairValue": {
        "label":       "Financial assets at fair value through profit or loss, mandatorily measured at fair value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAtFairValueThroughProfitOrLossMandatorilyMeasuredAtFairValueOtherThanThoseClassifiedAsHeldForTrading": {
        "label":       "Financial assets at fair value through profit or loss, mandatorily measured at fair value, other than those classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAtFairValueThroughProfitOrLossMeasuredAsSuchInAccordanceWithExemptionForReacquisitionOfOwnEquityInstruments": {
        "label":       "Financial assets at fair value through profit or loss, measured as such in accordance with exemption for reacquisition of own equity instruments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAtFairValueThroughProfitOrLossMeasuredAsSuchInAccordanceWithExemptionForRepurchaseOfOwnFinancialLiabilities": {
        "label":       "Financial assets at fair value through profit or loss, measured as such in accordance with exemption for repurchase of own financial liabilities",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsAvailableforsale": {
        "label":       "Financial assets available-for-sale",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsCarryingAmountImmediatelyAfterInitialApplicationOfIFRS9": {
        "label":       "Financial assets, carrying amount immediately after initial application of IFRS 9",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsCarryingAmountImmediatelyBeforeInitialApplicationOfIFRS9": {
        "label":       "Financial assets, carrying amount immediately before initial application of IFRS 9",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsHeldForManagingLiquidityRisk": {
        "label":       "Financial assets held for managing liquidity risk",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Financial assets measured at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsPledgedAsCollateralForLiabilitiesOrContingentLiabilities": {
        "label":       "Financial assets pledged as collateral for liabilities or contingent liabilities",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsPreviouslyDesignatedAtFairValueThroughProfitOrLossButNoLongerSoDesignatedFirstApplicationOfIFRS9": {
        "label":       "Financial assets previously designated at fair value through profit or loss but no longer so designated, initial application of IFRS 9",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsPreviouslyDesignatedAtFairValueThroughProfitOrLossReclassifiedDueToRequirementsOfIFRS9FirstApplicationOfIFRS9": {
        "label":       "Financial assets previously designated at fair value through profit or loss reclassified due to requirements of IFRS 9, initial application of IFRS 9",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsPreviouslyDesignatedAtFairValueThroughProfitOrLossReclassifiedVoluntarilyFirstApplicationOfIFRS9": {
        "label":       "Financial assets previously designated at fair value through profit or loss reclassified voluntarily, initial application of IFRS 9",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsReclassifiedOutOfAvailableforsaleFinancialAssetsAtFairValue": {
        "label":       "Financial assets reclassified out of available-for-sale financial assets, at fair value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsReclassifiedOutOfAvailableforsaleFinancialAssetsCarryingAmount": {
        "label":       "Financial assets reclassified out of available-for-sale financial assets, carrying amount",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsReclassifiedOutOfFinancialAssetsAtFairValueThroughProfitOrLossAtFairValue": {
        "label":       "Financial assets reclassified out of financial assets at fair value through profit or loss, at fair value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsReclassifiedOutOfFinancialAssetsAtFairValueThroughProfitOrLossCarryingAmount": {
        "label":       "Financial assets reclassified out of financial assets at fair value through profit or loss, carrying amount",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsRecognisedAsOfAcquisitionDate": {
        "label":       "Financial assets recognised as of acquisition date",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsSubjectToContractualTermsBasedOnContingentEventThatCouldChangeAmountOfContractualCashFlowsGrossCarryingAmount": {
        "label":       "Financial assets subject to contractual terms based on contingent event that could change amount of contractual cash flows, gross carrying amount",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsThatAreIndividuallyDeterminedToBeImpairedFairValueOfCollateralHeldAndOtherCreditEnhancements": {
        "label":       "Financial assets that are individually determined to be impaired, fair value of collateral held and other credit enhancements",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsThatWereDesignatedAsMeasuredAtFairValueThroughProfitOrLossBeforeApplicationOfAmendmentsToIFRS9ForPrepaymentFeaturesWithNegativeCompensationThatAreNoLongerSoDesignated": {
        "label":       "Financial assets that were designated as measured at fair value through profit or loss before application of amendments to IFRS 9 for prepayment features with negative compensation that are no longer so designated",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsThatWereDesignatedAsMeasuredAtFairValueThroughProfitOrLossBeforeApplicationOfIFRS17ThatAreNoLongerSoDesignated": {
        "label":       "Financial assets that were designated as measured at fair value through profit or loss before application of IFRS 17 that are no longer so designated",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsWhoseContractualCashFlowCharacteristicsHaveBeenAssessedBasedOnFactsAndCircumstancesAtInitialRecognitionWithoutTakingIntoAccountExceptionForPrepaymentFeatures": {
        "label":       "Financial assets whose contractual cash flow characteristics have been assessed based on facts and circumstances at initial recognition without taking into account exception for prepayment features",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsWhoseContractualCashFlowCharacteristicsHaveBeenAssessedBasedOnFactsAndCircumstancesAtInitialRecognitionWithoutTakingIntoAccountRequirementsRelatedToModificationOfTimeValueOfMoneyElement": {
        "label":       "Financial assets whose contractual cash flow characteristics have been assessed based on facts and circumstances at initial recognition without taking into account requirements related to modification of time value of money element",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsWithContractualCashFlowsModifiedDuringReportingPeriodWhileLossAllowanceMeasuredAtLifetimeExpectedCreditLossesAmortisedCostBeforeModification": {
        "label":       "Financial assets with contractual cash flows modified during reporting period while loss allowance measured at lifetime expected credit losses, amortised cost before modification",
        "balance":     "debit",
        "period_type": "duration",
    },
    "FinancialAssetsWithContractualCashFlowsModifiedDuringReportingPeriodWhileLossAllowanceMeasuredAtLifetimeExpectedCreditLossesModificationGainLoss": {
        "label":       "Financial assets with contractual cash flows modified during reporting period while loss allowance measured at lifetime expected credit losses, modification gain (loss)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FinancialAssetsWithModifiedContractualCashFlowsWhileLossAllowanceMeasuredAtLifetimeExpectedCreditLossesForWhichLossAllowanceChangedDuringReportingPeriodTo12monthExpectedCreditLossesGrossCarryingAmount": {
        "label":       "Financial assets with modified contractual cash flows while loss allowance measured at lifetime expected credit losses for which loss allowance changed during reporting period to 12-month expected credit losses, gross carrying amount",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialAssetsWrittenOffDuringReportingPeriodAndStillSubjectToEnforcementActivityContractualAmountOutstanding": {
        "label":       "Financial assets written off during reporting period and still subject to enforcement activity, contractual amount outstanding",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialInstrumentsDesignatedAsHedgingInstrumentsAtFairValue": {
        "label":       "Financial instruments designated as hedging instruments, at fair value",
        "balance":     "None",
        "period_type": "instant",
    },
    "FinancialInstrumentsSubjectToEnforceableMasterNettingArrangementOrSimilarAgreementNotSetOffAgainstFinancialAssets": {
        "label":       "Financial instruments subject to enforceable master netting arrangement or similar agreement not set off against financial assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialInstrumentsSubjectToEnforceableMasterNettingArrangementOrSimilarAgreementNotSetOffAgainstFinancialLiabilities": {
        "label":       "Financial instruments subject to enforceable master netting arrangement or similar agreement not set off against financial liabilities",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FinancialInstrumentsWhoseFairValuePreviouslyCouldNotBeReliablyMeasuredAtTimeOfDerecognition": {
        "label":       "Financial instruments whose fair value previously could not be reliably measured at time of derecognition",
        "balance":     "None",
        "period_type": "instant",
    },
    "FinancialLiabilities": {
        "label":       "Financial liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesAffectedByAmendmentsToIFRS9ForPrepaymentFeaturesWithNegativeCompensationCarryingAmountAfterApplyingAmendments": {
        "label":       "Financial liabilities affected by amendments to IFRS 9 for prepayment features with negative compensation, carrying amount after applying amendments",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesAffectedByAmendmentsToIFRS9ForPrepaymentFeaturesWithNegativeCompensationCarryingAmountImmediatelyBeforeApplyingAmendments": {
        "label":       "Financial liabilities affected by amendments to IFRS 9 for prepayment features with negative compensation, carrying amount immediately before applying amendments",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesAffectedByAmendmentsToIFRS9MadeByIFRS17CarryingAmountAfterApplyingAmendments": {
        "label":       "Financial liabilities affected by amendments to IFRS 9 made by IFRS 17, carrying amount after applying amendments",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesAffectedByAmendmentsToIFRS9MadeByIFRS17CarryingAmountImmediatelyBeforeApplyingAmendments": {
        "label":       "Financial liabilities affected by amendments to IFRS 9 made by IFRS 17, carrying amount immediately before applying amendments",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesAtAmortisedCost": {
        "label":       "Financial liabilities at amortised cost",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesAtFairValue": {
        "label":       "Financial liabilities, at fair value",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesAtFairValueThroughProfitOrLoss": {
        "label":       "Financial liabilities at fair value through profit or loss",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesAtFairValueThroughProfitOrLossClassifiedAsHeldForTrading": {
        "label":       "Financial liabilities at fair value through profit or loss that meet definition of held for trading",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesAtFairValueThroughProfitOrLossDesignatedAsUponInitialRecognition": {
        "label":       "Financial liabilities at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesCarryingAmountImmediatelyAfterInitialApplicationOfIFRS9": {
        "label":       "Financial liabilities, carrying amount immediately after initial application of IFRS 9",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesCarryingAmountImmediatelyBeforeInitialApplicationOfIFRS9": {
        "label":       "Financial liabilities, carrying amount immediately before initial application of IFRS 9",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesPreviouslyDesignatedAtFairValueThroughProfitOrLossButNoLongerSoDesignatedFirstApplicationOfIFRS9": {
        "label":       "Financial liabilities previously designated at fair value through profit or loss but no longer so designated, initial application of IFRS 9",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesPreviouslyDesignatedAtFairValueThroughProfitOrLossReclassifiedDueToRequirementsOfIFRS9FirstApplicationOfIFRS9": {
        "label":       "Financial liabilities previously designated at fair value through profit or loss reclassified due to requirements of IFRS 9, initial application of IFRS 9",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesPreviouslyDesignatedAtFairValueThroughProfitOrLossReclassifiedVoluntarilyFirstApplicationOfIFRS9": {
        "label":       "Financial liabilities previously designated at fair value through profit or loss reclassified voluntarily, initial application of IFRS 9",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesReclassifiedIntoEquity": {
        "label":       "Financial liabilities reclassified into equity",
        "balance":     "None",
        "period_type": "duration",
    },
    "FinancialLiabilitiesRecognisedAsOfAcquisitionDate": {
        "label":       "Financial liabilities recognised as of acquisition date",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesSubjectToContractualTermsBasedOnContingentEventThatCouldChangeAmountOfContractualCashFlowsAmortisedCost": {
        "label":       "Financial liabilities subject to contractual terms based on contingent event that could change amount of contractual cash flows, amortised cost",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesThatWereDesignatedAsMeasuredAtFairValueThroughProfitOrLossBeforeApplicationOfAmendmentsToIFRS9ForPrepaymentFeaturesWithNegativeCompensationThatAreNoLongerSoDesignated": {
        "label":       "Financial liabilities that were designated as measured at fair value through profit or loss before application of amendments to IFRS 9 for prepayment features with negative compensation that are no longer so designated",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialLiabilitiesThatWereDesignatedAsMeasuredAtFairValueThroughProfitOrLossBeforeApplicationOfAmendmentsToIFRS9MadeByIFRS17ButAreNoLongerSoDesignated": {
        "label":       "Financial liabilities that were designated as measured at fair value through profit or loss before application of amendments to IFRS 9 made by IFRS 17 but are no longer so designated",
        "balance":     "credit",
        "period_type": "instant",
    },
    "FinancialResultOperating": {
        "label":       "Financial result operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FinishedGoods": {
        "label":       "Current finished goods",
        "balance":     "debit",
        "period_type": "instant",
    },
    "FixturesAndFittings": {
        "label":       "Fixtures and fittings",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ForeignExchangeGain": {
        "label":       "Foreign exchange gain",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ForeignExchangeLoss": {
        "label":       "Foreign exchange loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "FranchiseFeeIncome": {
        "label":       "Franchise fee income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "FuelAndEnergyExpense": {
        "label":       "Fuel and energy expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "FuelExpense": {
        "label":       "Fuel expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "GainLossArisingFromDerecognitionOfFinancialAssetsMeasuredAtAmortisedCost": {
        "label":       "Gain (loss) arising from derecognition of financial assets measured at amortised cost",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossArisingFromDerecognitionOfFinancialAssetsMeasuredAtAmortisedCostInvesting": {
        "label":       "Gain loss arising from derecognition of financial assets measured at amortised cost investing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossArisingFromDerecognitionOfFinancialAssetsMeasuredAtAmortisedCostOperating": {
        "label":       "Gain loss arising from derecognition of financial assets measured at amortised cost operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossArisingFromDifferenceBetweenCarryingAmountOfFinancialLiabilityExtinguishedAndConsiderationPaid": {
        "label":       "Gain (loss) arising from difference between carrying amount of financial liability extinguished and consideration paid",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossArisingFromDifferenceBetweenCarryingAmountOfFinancialLiabilityExtinguishedAndConsiderationPaidOperating": {
        "label":       "Gain loss arising from difference between carrying amount of financial liability extinguished and consideration paid operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossOfDerecognisedFinancialAssetsAtDateOfTransfer": {
        "label":       "Gain (loss) of derecognised financial assets at date of transfer",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossOfDerecognisedFinancialAssetsRepresentingGreatestTransferActivity": {
        "label":       "Gain (loss) from transfer activity during period representing greatest transfer activity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossOnCessationOfConsolidationOfSubsidiariesDueToChangeOfInvestmentEntityStatus": {
        "label":       "Gain loss on cessation of consolidation of subsidiaries due to change of investment entity status",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossOnChangeInFairValueOfHedgedItemUsedAsBasisForRecognisingHedgeIneffectiveness": {
        "label":       "Gain (loss) on change in fair value of hedged item used as basis for recognising hedge ineffectiveness",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossOnChangeInFairValueOfHedgingInstrumentUsedAsBasisForRecognisingHedgeIneffectiveness": {
        "label":       "Gain (loss) on change in fair value of hedging instrument used as basis for recognising hedge ineffectiveness",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossOnChangesInEffectOfLimitingNetDefinedBenefitAssetToAssetCeiling": {
        "label":       "Decrease (increase) in net defined benefit liability (asset) resulting from gain (loss) on changes in effect of limiting net defined benefit asset to asset ceiling excluding interest income or expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "GainLossOnChangesInEffectOfLimitingReimbursementRightsToAssetCeiling": {
        "label":       "Increase (decrease) in reimbursement rights related to defined benefit obligation, resulting from gain (loss) on changes in effect of limiting reimbursement rights to asset ceiling excluding interest income or expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "GainLossOnDesignationOfFinancialInstrumentAsMeasuredAtFairValueThroughProfitOrLossBecauseCreditDerivativeIsUsedToManageCreditRisk": {
        "label":       "Gain (loss) on designation of financial instrument as measured at fair value through profit or loss because credit derivative is used to manage credit risk",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossOnHedgeIneffectiveness": {
        "label":       "Gain (loss) on hedge ineffectiveness",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossOnHedgeIneffectivenessRecognisedInOtherComprehensiveIncome": {
        "label":       "Gain (loss) on hedge ineffectiveness recognised in other comprehensive income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossOnHedgeIneffectivenessRecognisedInProfitOrLoss": {
        "label":       "Gain (loss) on hedge ineffectiveness recognised in profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossOnRemeasurementOfNetDefinedBenefitLiabilityAsset": {
        "label":       "Decrease (increase) in net defined benefit liability (asset) resulting from gain (loss) on remeasurement in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "GainLossOnRemeasurementOfReimbursementRights": {
        "label":       "Increase (decrease) in reimbursement rights related to defined benefit obligation, resulting from gain (loss) on remeasurement",
        "balance":     "debit",
        "period_type": "duration",
    },
    "GainLossRecognisedAsResultOfRemeasuringToFairValueEquityInterestInAcquireeHeldByAcquirerBeforeBusinessCombination": {
        "label":       "Gain (loss) recognised as result of remeasuring to fair value equity interest in acquiree held by acquirer before business combination",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossRecognisedOnFinancialInstrumentsWhoseFairValuePreviouslyCouldNotBeReliablyMeasured": {
        "label":       "Gain (loss) recognised on derecognition of financial instruments whose fair value previously could not be reliably measured",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossRecognisedOnMeasurementToFairValueLessCostsToSellOrOnDisposalOfAssetsOrDisposalGroupsConstitutingDiscontinuedOperation": {
        "label":       "Gain loss recognised on measurement to fair value less costs to sell or on disposal of assets or disposal groups constituting discontinued operation",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainLossThatRelatesToIdentifiableAssetsAcquiredOrLiabilitiesAssumedInBusinessCombination": {
        "label":       "Gain loss that relates to identifiable assets acquired or liabilities assumed in business combination",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainOnRecoveryOfLoansAndAdvancesPreviouslyWrittenOff": {
        "label":       "Gain on recovery of loans and advances previously written off",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainRecognisedInBargainPurchaseTransaction": {
        "label":       "Gain recognised in bargain purchase transaction",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsArisingFromDerecognitionOfFinancialAssetsMeasuredAtAmortisedCost": {
        "label":       "Gains arising from derecognition of financial assets measured at amortised cost",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesArisingFromDifferenceBetweenPreviousCarryingAmountAndFairValueOfFinancialAssetsReclassifiedAsMeasuredAtFairValue": {
        "label":       "Gains (losses) arising from difference between previous amortised cost and fair value of financial assets reclassified out of amortised cost into fair value through profit or loss measurement category",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesArisingFromDifferenceBetweenPreviousCarryingAmountAndFairValueOfFinancialAssetsReclassifiedAsMeasuredAtFairValueInvesting": {
        "label":       "Gains losses arising from difference between previous carrying amount and fair value of financial assets reclassified as measured at fair value investing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesArisingFromDifferenceBetweenPreviousCarryingAmountAndFairValueOfFinancialAssetsReclassifiedAsMeasuredAtFairValueOperating": {
        "label":       "Gains losses arising from difference between previous carrying amount and fair value of financial assets reclassified as measured at fair value operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesArisingFromSaleAndLeasebackTransactions": {
        "label":       "Gains losses arising from sale and leaseback transactions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesArisingFromSettlementsDefinedBenefitPlans": {
        "label":       "Gains losses arising from settlements defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesArisingFromSettlementsNetDefinedBenefitLiabilityAsset": {
        "label":       "Decrease (increase) in net defined benefit liability (asset) resulting from gains (losses) arising from settlements",
        "balance":     "debit",
        "period_type": "duration",
    },
    "GainsLossesOnAvailableforsaleFinancialAssets": {
        "label":       "Gains (losses) on available-for-sale financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnCashFlowHedgesBeforeTax": {
        "label":       "Gains (losses) on cash flow hedges, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnCashFlowHedgesNetOfTax": {
        "label":       "Gains (losses) on cash flow hedges, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnChangeInFairValueEstimatesOfBiologicalAssetsForCurrentPeriod": {
        "label":       "Gains losses on change in fair value estimates of biological assets for current period",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnChangeInFairValueOfDerivatives": {
        "label":       "Gains (losses) on change in fair value of derivatives",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnChangeInValueOfForeignCurrencyBasisSpreadsBeforeTax": {
        "label":       "Gains (losses) on change in value of foreign currency basis spreads, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnChangeInValueOfForeignCurrencyBasisSpreadsNetOfTax": {
        "label":       "Gains (losses) on change in value of foreign currency basis spreads, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnChangeInValueOfForwardElementsOfForwardContractsBeforeTax": {
        "label":       "Gains (losses) on change in value of forward elements of forward contracts, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnChangeInValueOfForwardElementsOfForwardContractsNetOfTax": {
        "label":       "Gains (losses) on change in value of forward elements of forward contracts, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnChangeInValueOfTimeValueOfOptionsBeforeTax": {
        "label":       "Gains (losses) on change in value of time value of options, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnChangeInValueOfTimeValueOfOptionsNetOfTax": {
        "label":       "Gains (losses) on change in value of time value of options, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnChangesInEffectOfLimitingNetDefinedBenefitAssetToAssetCeilingExcludingInterestIncomeOrExpenseBeforeTaxDefinedBenefitPlans": {
        "label":       "Gains (losses) on changes in effect of limiting net defined benefit asset to asset ceiling excluding interest income or expense, before tax, defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnChangesInEffectOfLimitingNetDefinedBenefitAssetToAssetCeilingExcludingInterestIncomeOrExpenseNetOfTaxDefinedBenefitPlans": {
        "label":       "Gains (losses) on changes in effect of limiting net defined benefit asset to asset ceiling excluding interest income or expense, net of tax, defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnDisposalsOfAssociatesAndJointVenturesInvesting": {
        "label":       "Gains losses on disposals of associates and joint ventures investing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnDisposalsOfInvestmentProperties": {
        "label":       "Gains losses on disposals of investment properties",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnDisposalsOfInvestmentPropertyCarriedAtCostOrInAccordanceWithIFRS16WithinFairValueModel": {
        "label":       "Gains (losses) on disposals of investment property carried at cost or in accordance with IFRS 16 within fair value model",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnDisposalsOfInvestments": {
        "label":       "Gains losses on disposals of investments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnDisposalsOfInvestmentsInvesting": {
        "label":       "Gains losses on disposals of investments investing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnDisposalsOfInvestmentsOperating": {
        "label":       "Gains losses on disposals of investments operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnDisposalsOfNoncurrentAssets": {
        "label":       "Gains (losses) on disposals of non-current assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnDisposalsOfOtherNoncurrentAssets": {
        "label":       "Gains losses on disposals of other noncurrent assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnDisposalsOfPropertyPlantAndEquipment": {
        "label":       "Gains losses on disposals of property plant and equipment",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnExchangeDifferencesOnTranslationBeforeTax": {
        "label":       "Gains (losses) on exchange differences on translation of foreign operations, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnExchangeDifferencesOnTranslationNetOfTax": {
        "label":       "Gains (losses) on exchange differences on translation of foreign operations, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnExchangeDifferencesOnTranslationRecognisedInProfitOrLoss": {
        "label":       "Foreign exchange gain (loss)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnExchangeDifferencesOnTranslationRecognisedInProfitOrLossFinancing": {
        "label":       "Gains losses on exchange differences on translation recognised in profit or loss financing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnExchangeDifferencesOnTranslationRecognisedInProfitOrLossIncomeTaxes": {
        "label":       "Gains losses on exchange differences on translation recognised in profit or loss income taxes",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnExchangeDifferencesOnTranslationRecognisedInProfitOrLossInvesting": {
        "label":       "Gains losses on exchange differences on translation recognised in profit or loss investing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnExchangeDifferencesOnTranslationRecognisedInProfitOrLossOperating": {
        "label":       "Gains losses on exchange differences on translation recognised in profit or loss operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFairValueAdjustmentAttributableToPhysicalChangesBiologicalAssets": {
        "label":       "Gains losses on fair value adjustment attributable to physical changes biological assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesOnFairValueAdjustmentAttributableToPriceChangesBiologicalAssets": {
        "label":       "Gains losses on fair value adjustment attributable to price changes biological assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesOnFairValueAdjustmentBiologicalAssets": {
        "label":       "Gains losses on fair value adjustment biological assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesOnFairValueAdjustmentInvestmentProperty": {
        "label":       "Gains (losses) on fair value adjustment, investment property",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesOnFairValueAdjustmentInvestmentPropertyInvesting": {
        "label":       "Gains losses on fair value adjustment investment property investing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFairValueAdjustmentInvestmentPropertyOperating": {
        "label":       "Gains losses on fair value adjustment investment property operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialAssetsAtAmortisedCost": {
        "label":       "Gains (losses) on financial assets at amortised cost",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialAssetsAtFairValueThroughProfitOrLoss": {
        "label":       "Gains (losses) on financial assets at fair value through profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialAssetsAtFairValueThroughProfitOrLossClassifiedAsHeldForTrading": {
        "label":       "Gains (losses) on financial assets at fair value through profit or loss, classified as held for trading",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialAssetsAtFairValueThroughProfitOrLossDesignatedAsUponInitialRecognition": {
        "label":       "Gains (losses) on financial assets at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialAssetsAtFairValueThroughProfitOrLossInvesting": {
        "label":       "Gains losses on financial assets at fair value through profit or loss investing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialAssetsAtFairValueThroughProfitOrLossMandatorilyMeasuredAtFairValue": {
        "label":       "Gains (losses) on financial assets at fair value through profit or loss, mandatorily measured at fair value",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialAssetsAtFairValueThroughProfitOrLossOperating": {
        "label":       "Gains losses on financial assets at fair value through profit or loss operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeBeforeTax": {
        "label":       "Gains (losses) on financial assets measured at fair value through other comprehensive income, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeNetOfTax": {
        "label":       "Gains (losses) on financial assets measured at fair value through other comprehensive income, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialAssetsReclassifiedOutOfAvailableforsaleFinancialAssetsRecognisedInOtherComprehensiveIncome": {
        "label":       "Gains (losses) on financial assets reclassified out of available-for-sale financial assets recognised in profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialAssetsReclassifiedOutOfFinancialAssetsAtFairValueThroughProfitOrLossRecognisedInProfitOrLoss": {
        "label":       "Gains (losses) on financial assets reclassified out of financial assets at fair value through profit or loss recognised in profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialLiabilitiesAtAmortisedCost": {
        "label":       "Gains (losses) on financial liabilities at amortised cost",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialLiabilitiesAtFairValueThroughProfitOrLoss": {
        "label":       "Gains (losses) on financial liabilities at fair value through profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialLiabilitiesAtFairValueThroughProfitOrLossClassifiedAsHeldForTrading": {
        "label":       "Gains (losses) on financial liabilities at fair value through profit or loss, classified as held for trading",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialLiabilitiesAtFairValueThroughProfitOrLossDesignatedAsUponInitialRecognition": {
        "label":       "Gains (losses) on financial liabilities at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnFinancialLiabilitiesAtFairValueThroughProfitOrLossFinancing": {
        "label":       "Gains losses on financial liabilities at fair value through profit or loss financing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnHedgedItemAttributableToHedgedRisk": {
        "label":       "Gains (losses) on hedged item attributable to hedged risk, fair value hedges",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnHedgesOfNetInvestmentsInForeignOperationsBeforeTax": {
        "label":       "Gains (losses) on hedges of net investments in foreign operations, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnHedgesOfNetInvestmentsInForeignOperationsNetOfTax": {
        "label":       "Gains (losses) on hedges of net investments in foreign operations, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnHedgingInstrument": {
        "label":       "Gains (losses) on hedging instrument, fair value hedges",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnHeldtomaturityInvestments": {
        "label":       "Gains (losses) on held-to-maturity investments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnIneffectivenessOfCashFlowHedgesRecognisedInProfitOrLoss": {
        "label":       "Gains (losses) on ineffectiveness of cash flow hedges recognised in profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnIneffectivenessOfHedgesOfNetInvestmentsInForeignOperations": {
        "label":       "Gains (losses) on ineffectiveness of hedges of net investments in foreign operations recognised in profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnInitialRecognitionOfBiologicalAssetsForCurrentPeriod": {
        "label":       "Gains losses on initial recognition of biological assets for current period",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnLitigationSettlements": {
        "label":       "Gains losses on litigation settlements",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnLoansAndReceivables": {
        "label":       "Gains (losses) on loans and receivables",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnNetMonetaryPosition": {
        "label":       "Gains losses on net monetary position",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnNetMonetaryPositionOperating": {
        "label":       "Gains losses on net monetary position operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnNetMovementInRegulatoryDeferralAccountBalancesRelatedToItemsThatWillBeReclassifiedToProfitOrLossBeforeTax": {
        "label":       "Gains (losses) on net movement in regulatory deferral account balances related to items that will be reclassified to profit or loss, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnNetMovementInRegulatoryDeferralAccountBalancesRelatedToItemsThatWillBeReclassifiedToProfitOrLossNetOfTax": {
        "label":       "Gains (losses) on net movement in regulatory deferral account balances related to items that will be reclassified to profit or loss, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnRemeasuringAvailableforsaleFinancialAssetsBeforeTax": {
        "label":       "Gains (losses) on remeasuring available-for-sale financial assets, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnRemeasuringAvailableforsaleFinancialAssetsNetOfTax": {
        "label":       "Gains (losses) on remeasuring available-for-sale financial assets, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesOnSubsequentIncreaseInFairValueLessCostsToSellNotInExcessOfRecognisedCumulativeImpairmentLoss": {
        "label":       "Gains (losses) on subsequent increase in fair value less costs to sell not in excess of recognised cumulative impairment loss or write-down to fair value less costs to sell",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInOtherComprehensiveIncomeExcludingExchangeDifferencesFairValueMeasurementAssets": {
        "label":       "Gains (losses) recognised in other comprehensive income excluding exchange differences, fair value measurement, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInOtherComprehensiveIncomeExcludingExchangeDifferencesFairValueMeasurementEntitysOwnEquityInstruments": {
        "label":       "Gains (losses) recognised in other comprehensive income excluding exchange differences, fair value measurement, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInOtherComprehensiveIncomeExcludingExchangeDifferencesFairValueMeasurementLiabilities": {
        "label":       "Gains (losses) recognised in other comprehensive income excluding exchange differences, fair value measurement, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInOtherComprehensiveIncomeFairValueMeasurementAssets": {
        "label":       "Gains (losses) recognised in other comprehensive income including exchange differences, fair value measurement, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInOtherComprehensiveIncomeFairValueMeasurementEntitysOwnEquityInstruments": {
        "label":       "Gains (losses) recognised in other comprehensive income including exchange differences, fair value measurement, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInOtherComprehensiveIncomeFairValueMeasurementLiabilities": {
        "label":       "Gains (losses) recognised in other comprehensive income including exchange differences, fair value measurement, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInOtherComprehensiveIncomeOnExchangeDifferencesFairValueMeasurementAssets": {
        "label":       "Gains (losses) recognised in other comprehensive income on exchange differences, fair value measurement, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInOtherComprehensiveIncomeOnExchangeDifferencesFairValueMeasurementEntitysOwnEquityInstruments": {
        "label":       "Gains (losses) recognised in other comprehensive income on exchange differences, fair value measurement, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInOtherComprehensiveIncomeOnExchangeDifferencesFairValueMeasurementLiabilities": {
        "label":       "Gains (losses) recognised in other comprehensive income on exchange differences, fair value measurement, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInOtherComprehensiveIncomeOnFinancialLiabilitiesAtFairValueThroughProfitOrLossDesignatedUponInitialRecognitionOrSubsequently": {
        "label":       "Gains (losses) recognised in other comprehensive income on financial liabilities at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInProfitOrLossAttributableToChangeInUnrealisedGainsOrLossesForAssetsHeldAtEndOfPeriodFairValueMeasurement": {
        "label":       "Gains (losses) recognised in profit or loss attributable to change in unrealised gains or losses for assets held at end of period, fair value measurement",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInProfitOrLossAttributableToChangeInUnrealisedGainsOrLossesForEntitysOwnEquityInstrumentsHeldAtEndOfPeriodFairValueMeasurement": {
        "label":       "Gains losses recognised in profit or loss attributable to change in unrealised gains or losses for entitys own equity instruments held at end of period fair value measurement",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInProfitOrLossAttributableToChangeInUnrealisedGainsOrLossesForLiabilitiesHeldAtEndOfPeriodFairValueMeasurement": {
        "label":       "Gains (losses) recognised in profit or loss attributable to change in unrealised gains or losses for liabilities held at end of period, fair value measurement",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInProfitOrLossExcludingExchangeDifferencesFairValueMeasurementAssets": {
        "label":       "Gains (losses) recognised in profit or loss excluding exchange differences, fair value measurement, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInProfitOrLossExcludingExchangeDifferencesFairValueMeasurementEntitysOwnEquityInstruments": {
        "label":       "Gains losses recognised in profit or loss excluding exchange differences fair value measurement entitys own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInProfitOrLossExcludingExchangeDifferencesFairValueMeasurementLiabilities": {
        "label":       "Gains (losses) recognised in profit or loss excluding exchange differences, fair value measurement, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInProfitOrLossFairValueMeasurementAssets": {
        "label":       "Gains (losses) recognised in profit or loss including exchange differences, fair value measurement, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInProfitOrLossFairValueMeasurementEntitysOwnEquityInstruments": {
        "label":       "Gains losses recognised in profit or loss fair value measurement entitys own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInProfitOrLossFairValueMeasurementLiabilities": {
        "label":       "Gains (losses) recognised in profit or loss including exchange differences, fair value measurement, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInProfitOrLossOnExchangeDifferencesFairValueMeasurementAssets": {
        "label":       "Gains (losses) recognised in profit or loss on exchange differences, fair value measurement, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInProfitOrLossOnExchangeDifferencesFairValueMeasurementEntitysOwnEquityInstruments": {
        "label":       "Gains losses recognised in profit or loss on exchange differences fair value measurement entitys own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInProfitOrLossOnExchangeDifferencesFairValueMeasurementLiabilities": {
        "label":       "Gains (losses) recognised in profit or loss on exchange differences, fair value measurement, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "GainsLossesRecognisedInProfitOrLossOnFinancialLiabilitiesAtFairValueThroughProfitOrLossDesignatedUponInitialRecognitionOrSubsequently": {
        "label":       "Gains (losses) recognised in profit or loss on financial liabilities at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsLossesRecognisedWhenControlInSubsidiaryIsLost": {
        "label":       "Gains (losses) recognised when control of subsidiary is lost",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsOnChangeInFairValueOfDerivatives": {
        "label":       "Gains on change in fair value of derivatives",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsOnDisposalsOfInvestmentProperties": {
        "label":       "Gains on disposals of investment properties",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsOnDisposalsOfInvestments": {
        "label":       "Gains on disposals of investments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsOnDisposalsOfInvestmentsOperating": {
        "label":       "Gains on disposals of investments operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsOnDisposalsOfNoncurrentAssets": {
        "label":       "Gains on disposals of non-current assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsOnDisposalsOfPropertyPlantAndEquipment": {
        "label":       "Gains on disposals of property plant and equipment",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GainsOnLitigationSettlements": {
        "label":       "Gains on litigation settlements",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GeneralAndAdministrativeExpense": {
        "label":       "General and administrative expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "Goodwill": {
        "label":       "Goodwill",
        "balance":     "debit",
        "period_type": "instant",
    },
    "GoodwillDerecognisedWithoutHavingPreviouslyBeenIncludedInDisposalGroupClassifiedAsHeldForSale": {
        "label":       "Goodwill derecognised without having previously been included in disposal group classified as held for sale",
        "balance":     "credit",
        "period_type": "duration",
    },
    "GoodwillExpectedDeductibleForTaxPurposes": {
        "label":       "Goodwill expected to be deductible for tax purposes",
        "balance":     "debit",
        "period_type": "instant",
    },
    "GoodwillRecognisedAsOfAcquisitionDate": {
        "label":       "Goodwill recognised as of acquisition date",
        "balance":     "debit",
        "period_type": "instant",
    },
    "GovernmentDebtInstrumentsHeld": {
        "label":       "Government debt instruments held",
        "balance":     "debit",
        "period_type": "instant",
    },
    "GovernmentGrants": {
        "label":       "Government grants",
        "balance":     "credit",
        "period_type": "instant",
    },
    "GrossContractualAmountsReceivableForAcquiredReceivables": {
        "label":       "Gross contractual amounts receivable for acquired receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "GrossFinancialAssetsSetOffAgainstFinancialLiabilitiesSubjectToOffsettingEnforceableMasterNettingArrangementsOrSimilarAgreements": {
        "label":       "Gross financial assets set off against financial liabilities subject to offsetting, enforceable master netting arrangements or similar agreements",
        "balance":     "debit",
        "period_type": "instant",
    },
    "GrossFinancialAssetsSubjectToOffsettingEnforceableMasterNettingArrangementsOrSimilarAgreements": {
        "label":       "Gross financial assets subject to offsetting, enforceable master netting arrangements or similar agreements",
        "balance":     "debit",
        "period_type": "instant",
    },
    "GrossFinancialLiabilitiesSetOffAgainstFinancialAssetsSubjectToOffsettingEnforceableMasterNettingArrangementsOrSimilarAgreements": {
        "label":       "Gross financial liabilities set off against financial assets subject to offsetting, enforceable master netting arrangements or similar agreements",
        "balance":     "credit",
        "period_type": "instant",
    },
    "GrossFinancialLiabilitiesSubjectToOffsettingEnforceableMasterNettingArrangementsOrSimilarAgreements": {
        "label":       "Gross financial liabilities subject to offsetting, enforceable master netting arrangements or similar agreements",
        "balance":     "credit",
        "period_type": "instant",
    },
    "GrossLeaseLiabilities": {
        "label":       "Gross lease liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "GrossLoanCommitments": {
        "label":       "Gross loan commitments",
        "balance":     "credit",
        "period_type": "instant",
    },
    "GrossProfit": {
        "label":       "Gross profit",
        "balance":     "credit",
        "period_type": "duration",
    },
    "HedgedItemAssets": {
        "label":       "Hedged item, assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "HedgedItemLiabilities": {
        "label":       "Hedged item, liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "HedgingGainsLossesForHedgeOfGroupOfItemsWithOffsettingRiskPositions": {
        "label":       "Hedging gains losses for hedge of group of items with offsetting risk positions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "HedgingInstrumentAssets": {
        "label":       "Hedging instrument, assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "HedgingInstrumentLiabilities": {
        "label":       "Hedging instrument, liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "HeldtomaturityInvestments": {
        "label":       "Held-to-maturity investments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IdentifiableAssetsAcquiredLiabilitiesAssumed": {
        "label":       "Identifiable assets acquired (liabilities assumed)",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IdentifiableIntangibleAssetsRecognisedAsOfAcquisitionDate": {
        "label":       "Identifiable intangible assets recognised as of acquisition date",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ImpairmentLoss": {
        "label":       "Impairment loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ImpairmentLossAssetsRecognisedFromCostsIncurredToObtainOrFulfilContractsWithCustomers": {
        "label":       "Impairment loss assets recognised from costs incurred to obtain or fulfil contracts with customers",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ImpairmentLossImpairmentGainAndReversalOfImpairmentLossDeterminedInAccordanceWithIFRS9": {
        "label":       "Impairment loss impairment gain and reversal of impairment loss determined in accordance withifrs9",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ImpairmentLossImpairmentGainAndReversalOfImpairmentLossDeterminedInAccordanceWithIFRS9Investing": {
        "label":       "Impairment loss impairment gain and reversal of impairment loss determined in accordance withifrs9 investing",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ImpairmentLossImpairmentGainAndReversalOfImpairmentLossDeterminedInAccordanceWithIFRS9Operating": {
        "label":       "Impairment loss impairment gain and reversal of impairment loss determined in accordance withifrs9 operating",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ImpairmentLossOnFinancialAssets": {
        "label":       "Impairment loss on financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ImpairmentLossOnReceivablesOrContractAssetsArisingFromContractsWithCustomers": {
        "label":       "Impairment loss on receivables or contract assets arising from contracts with customers",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInOtherComprehensiveIncome": {
        "label":       "Impairment loss recognised in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInOtherComprehensiveIncomeIntangibleAssetsOtherThanGoodwill": {
        "label":       "Impairment loss recognised in other comprehensive income, intangible assets other than goodwill",
        "balance":     "None",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInOtherComprehensiveIncomePropertyPlantAndEquipment": {
        "label":       "Impairment loss recognised in other comprehensive income, property, plant and equipment",
        "balance":     "None",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInOtherComprehensiveIncomePropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Impairment loss recognised in other comprehensive income, property, plant and equipment including right-of-use assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInOtherComprehensiveIncomeRightofuseAssets": {
        "label":       "Impairment loss recognised in other comprehensive income, right-of-use assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInProfitOrLoss": {
        "label":       "Impairment loss recognised in profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInProfitOrLossBiologicalAssets": {
        "label":       "Impairment loss recognised in profit or loss biological assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInProfitOrLossGoodwill": {
        "label":       "Impairment loss recognised in profit or loss goodwill",
        "balance":     "None",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInProfitOrLossIntangibleAssetsAndGoodwill": {
        "label":       "Impairment loss recognised in profit or loss, intangible assets and goodwill",
        "balance":     "None",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInProfitOrLossIntangibleAssetsOtherThanGoodwill": {
        "label":       "Impairment loss recognised in profit or loss, intangible assets other than goodwill",
        "balance":     "None",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInProfitOrLossInvestmentProperty": {
        "label":       "Impairment loss recognised in profit or loss, investment property",
        "balance":     "None",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInProfitOrLossLoansAndAdvances": {
        "label":       "Impairment loss recognised in profit or loss loans and advances",
        "balance":     "None",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInProfitOrLossPropertyPlantAndEquipment": {
        "label":       "Impairment loss recognised in profit or loss property plant and equipment",
        "balance":     "None",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInProfitOrLossPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Impairment loss recognised in profit or loss, property, plant and equipment including right-of-use assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInProfitOrLossRightofuseAssets": {
        "label":       "Impairment loss recognised in profit or loss, right-of-use assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "ImpairmentLossRecognisedInProfitOrLossTradeReceivables": {
        "label":       "Impairment loss recognised in profit or loss trade receivables",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLoss": {
        "label":       "Impairment loss (reversal of impairment loss) recognised in profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLossLoansAndAdvances": {
        "label":       "Impairment loss reversal of impairment loss recognised in profit or loss loans and advances",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLossOperating": {
        "label":       "Impairment loss reversal of impairment loss recognised in profit or loss operating",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLossTradeReceivables": {
        "label":       "Impairment loss reversal of impairment loss recognised in profit or loss trade receivables",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeArisingFromExplorationForAndEvaluationOfMineralResources": {
        "label":       "Income arising from exploration for and evaluation of mineral resources",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeExpensesFromReinsuranceContractsHeldOtherThanFinanceIncomeExpenses": {
        "label":       "Income expenses from reinsurance contracts held other than finance income expenses",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeFromAmountsRecoveredFromReinsurer": {
        "label":       "Income from amounts recovered from reinsurer",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeFromContinuingInvolvementInDerecognisedFinancialAssets": {
        "label":       "Income from continuing involvement in derecognised financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeFromContinuingInvolvementInDerecognisedFinancialAssetsCumulativelyRecognised": {
        "label":       "Income from continuing involvement in derecognised financial assets cumulatively recognised",
        "balance":     "credit",
        "period_type": "instant",
    },
    "IncomeFromContinuingOperationsAttributableToOwnersOfParent": {
        "label":       "Income from continuing operations attributable to owners of parent",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeFromDiscontinuedOperationsAttributableToOwnersOfParent": {
        "label":       "Income from discontinued operations attributable to owners of parent",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeFromFinesAndPenalties": {
        "label":       "Income from fines and penalties",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeFromGovernmentGrantsRelatedToAgriculturalActivity": {
        "label":       "Income from government grants related to agricultural activity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeFromReimbursementsUnderInsurancePolicies": {
        "label":       "Income from reimbursements under insurance policies",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeFromStructuredEntities": {
        "label":       "Income from structured entities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeFromSubleasingRightofuseAssets": {
        "label":       "Income from subleasing right-of-use assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeOnFinancialAssetsReclassifiedOutOfAvailableforsaleFinancialAssetsRecognisedInOtherComprehensiveIncome": {
        "label":       "Income on financial assets reclassified out of available-for-sale financial assets recognised in profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeOnFinancialAssetsReclassifiedOutOfFinancialAssetsAtFairValueThroughProfitOrLossRecognisedInProfitOrLoss": {
        "label":       "Income on financial assets reclassified out of financial assets at fair value through profit or loss recognised in profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeRelatingToVariableLeasePaymentsForOperatingLeasesThatDoNotDependOnIndexOrRate": {
        "label":       "Income relating to variable lease payments for operating leases that do not depend on index or rate",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeRelatingToVariableLeasePaymentsNotIncludedInMeasurementOfNetInvestmentInFinanceLease": {
        "label":       "Income relating to variable lease payments not included in measurement of net investment in finance lease",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeTaxConsequencesOfDividendsProposedOrDeclaredBeforeFinancialStatementsAuthorisedForIssueNotRecognisedAsLiability": {
        "label":       "Income tax consequences of dividends proposed or declared before financial statements authorised for issue not recognised as liability",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncomeTaxExpenseContinuingOperations": {
        "label":       "Income tax expense continuing operations",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToAvailableforsaleFinancialAssetsOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to available-for-sale financial assets included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToCashFlowHedgesOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to cash flow hedges included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToChangeInValueOfForeignCurrencyBasisSpreadsOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to change in value of foreign currency basis spreads included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToChangeInValueOfForwardElementsOfForwardContractsOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to change in value of forward elements of forward contracts included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToChangeInValueOfTimeValueOfOptionsOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to change in value of time value of options included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToChangesInFairValueOfFinancialLiabilityAttributableToChangeInCreditRiskOfLiabilityOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to changes in fair value of financial liability attributable to change in credit risk of liability included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToChangesInRevaluationSurplusOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to changes in revaluation surplus of property, plant and equipment, right-of-use assets and intangible assets included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToComponentsOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to components of other comprehensive income",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss": {
        "label":       "Income tax relating to components of other comprehensive income that will be reclassified to profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToComponentsOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLoss": {
        "label":       "Income tax relating to components of other comprehensive income that will not be reclassified to profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToExchangeDifferencesOnTranslationOfForeignOperationsAndHedgesOfNetInvestmentsInForeignOperationsIncludedInOtherComprehensiveIncome": {
        "label":       "Income tax relating to exchange differences on translation of foreign operations and hedges of net investments in foreign operations included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToExchangeDifferencesOnTranslationOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to exchange differences on translation of foreign operations included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToExchangeDifferencesOnTranslationOtherThanTranslationOfForeignOperationsIncludedInOtherComprehensiveIncome": {
        "label":       "Income tax relating to exchange differences on translation other than translation of foreign operations included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToFinanceIncomeExpensesFromReinsuranceContractsHeldOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to finance income (expenses) from reinsurance contracts held included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Income tax relating to financial assets measured at fair value through other comprehensive income included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToHedgesOfInvestmentsInEquityInstrumentsOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to hedges of investments in equity instruments included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToHedgesOfNetInvestmentsInForeignOperationsOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to hedges of net investments in foreign operations included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss": {
        "label":       "Income tax relating to insurance finance income (expenses) from insurance contracts issued included in other comprehensive income that will be reclassified to profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLoss": {
        "label":       "Income tax relating to insurance finance income (expenses) from insurance contracts issued included in other comprehensive income that will not be reclassified to profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToInvestmentsInEquityInstrumentsOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to investments in equity instruments included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToNetMovementInRegulatoryDeferralAccountBalancesRelatedToItemsThatWillBeReclassifiedToProfitOrLoss": {
        "label":       "Income tax relating to net movement in regulatory deferral account balances related to items that will be reclassified to profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToNetMovementInRegulatoryDeferralAccountBalancesRelatedToItemsThatWillNotBeReclassifiedToProfitOrLoss": {
        "label":       "Income tax relating to net movement in regulatory deferral account balances related to items that will not be reclassified to profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToOtherComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLoss": {
        "label":       "Income tax relating to other components of other comprehensive income that will be reclassified to profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToOtherComponentsOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLoss": {
        "label":       "Income tax relating to other components of other comprehensive income that will not be reclassified to profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToRemeasurementsOfDefinedBenefitPlansOfOtherComprehensiveIncome": {
        "label":       "Income tax relating to remeasurements of defined benefit plans included in other comprehensive income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethod": {
        "label":       "Income tax relating to share of other comprehensive income of associates and joint ventures accounted for using equity method",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodThatWillBeReclassifiedToProfitOrLoss": {
        "label":       "Income tax relating to share of other comprehensive income of associates and joint ventures accounted for using equity method that will be reclassified to profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxRelatingToShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodThatWillNotBeReclassifiedToProfitOrLoss": {
        "label":       "Income tax relating to share of other comprehensive income of associates and joint ventures accounted for using equity method that will not be reclassified to profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncomeTaxesPaidClassifiedAsOperatingActivities": {
        "label":       "Income taxes paid, classified as operating activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeTaxesPaidRefund": {
        "label":       "Income taxes paid (refund)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeTaxesPaidRefundClassifiedAsFinancingActivities": {
        "label":       "Income taxes paid (refund), classified as financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeTaxesPaidRefundClassifiedAsInvestingActivities": {
        "label":       "Income taxes paid (refund), classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeTaxesPaidRefundClassifiedAsOperatingActivities": {
        "label":       "Income taxes paid (refund), classified as operating activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncomeTaxesRefundClassifiedAsOperatingActivities": {
        "label":       "Income taxes refund, classified as operating activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInAccountingEstimate": {
        "label":       "Increase (decrease) in accounting estimate",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInAccumulatedDeferredTaxRecognisedInOtherComprehensiveIncomeDueToChangeInTaxRate": {
        "label":       "Increase (decrease) in accumulated deferred tax recognised in other comprehensive income due to change in tax rate",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInAggregateDifferenceBetweenFairValueAtInitialRecognitionAndAmountDeterminedUsingValuationTechniqueYetToBeRecognised": {
        "label":       "Increase (decrease) in aggregate difference between fair value at initial recognition and transaction price yet to be recognised in profit or loss",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInAllowanceAccountForCreditLossesOfFinancialAssets": {
        "label":       "Increase (decrease) in allowance account for credit losses of financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInAssetsForInsuranceAcquisitionCashFlows": {
        "label":       "Increase (decrease) in assets for insurance acquisition cash flows",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInCashAndCashEquivalents": {
        "label":       "Increase (decrease) in cash and cash equivalents after effect of exchange rate changes",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges": {
        "label":       "Increase (decrease) in cash and cash equivalents before effect of exchange rate changes",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInCashAndCashEquivalentsDiscontinuedOperations": {
        "label":       "Increase (decrease) in cash and cash equivalents, discontinued operations",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInContingentConsiderationAssetLiability": {
        "label":       "Increase (decrease) in contingent consideration asset (liability)",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInContingentLiabilitiesRecognisedInBusinessCombination": {
        "label":       "Increase (decrease) in contingent liabilities recognised in business combination",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInCreditDerivativeFairValue": {
        "label":       "Increase (decrease) in credit derivative, fair value",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInCreditDerivativeNominalAmount": {
        "label":       "Increase (decrease) in credit derivative, nominal amount",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInCurrentTaxExpenseIncomeDueToRateRegulation": {
        "label":       "Increase (decrease) in current tax expense (income) due to rate regulation",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInDeferredTaxExpenseIncomeDueToRateRegulation": {
        "label":       "Increase (decrease) in deferred tax expense (income) due to rate regulation",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInDeferredTaxLiabilityAsset": {
        "label":       "Increase (decrease) in deferred tax liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInDefinedBenefitObligationDueToReasonablyPossibleDecreaseInActuarialAssumption": {
        "label":       "Increase (decrease) in defined benefit obligation due to reasonably possible decrease in actuarial assumption",
        "balance":     "credit",
        "period_type": "instant",
    },
    "IncreaseDecreaseInDefinedBenefitObligationDueToReasonablyPossibleIncreaseInActuarialAssumption": {
        "label":       "Increase (decrease) in defined benefit obligation due to reasonably possible increase in actuarial assumption",
        "balance":     "credit",
        "period_type": "instant",
    },
    "IncreaseDecreaseInDividendsPayableThroughChangeInFairValueOfNoncashAssetsHeldForDistributionToOwners": {
        "label":       "Increase (decrease) in dividends payable through change in fair value of non-cash assets held for distribution to owners",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInEquityDueToReasonablyPossibleDecreaseInRiskExposureThatArisesFromContractsWithinScopeOfIFRS17": {
        "label":       "Increase (decrease) in equity due to reasonably possible decrease in risk variable that arises from contracts within scope of IFRS 17",
        "balance":     "credit",
        "period_type": "instant",
    },
    "IncreaseDecreaseInEquityDueToReasonablyPossibleDecreaseInRiskExposureThatArisesFromContractsWithinScopeOfIFRS17InsuranceContractsIssuedBeforeMitigationByReinsuranceContractsHeld": {
        "label":       "Increase (decrease) in equity due to reasonably possible decrease in risk variable that arises from contracts within scope of IFRS 17, insurance contracts issued before mitigation by reinsurance contracts held",
        "balance":     "credit",
        "period_type": "instant",
    },
    "IncreaseDecreaseInEquityDueToReasonablyPossibleIncreaseInRiskExposureThatArisesFromContractsWithinScopeOfIFRS17": {
        "label":       "Increase (decrease) in equity due to reasonably possible increase in risk variable that arises from contracts within scope of IFRS 17",
        "balance":     "credit",
        "period_type": "instant",
    },
    "IncreaseDecreaseInEquityDueToReasonablyPossibleIncreaseInRiskExposureThatArisesFromContractsWithinScopeOfIFRS17InsuranceContractsIssuedBeforeMitigationByReinsuranceContractsHeld": {
        "label":       "Increase (decrease) in equity due to reasonably possible increase in risk variable that arises from contracts within scope of IFRS 17, insurance contracts issued before mitigation by reinsurance contracts held",
        "balance":     "credit",
        "period_type": "instant",
    },
    "IncreaseDecreaseInExistingLiabilitiesContingentLiabilitiesRecognisedInBusinessCombination": {
        "label":       "Increase in existing liabilities, contingent liabilities recognised in business combination",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInExistingProvisionsOtherProvisions": {
        "label":       "Increase in existing provisions, other provisions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInExposureToCreditRiskOnLoanCommitmentsAndFinancialGuaranteeContracts": {
        "label":       "Increase (decrease) in exposure to credit risk on loan commitments and financial guarantee contracts",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementAssets": {
        "label":       "Increase (decrease) in fair value measurement, assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputAssets": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputEntitysOwnEquityInstruments": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, entity's own equity instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputLiabilities": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputRecognisedInOtherComprehensiveIncomeAfterTaxAssets": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, recognised in other comprehensive income, after tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputRecognisedInOtherComprehensiveIncomeAfterTaxEntitysOwnEquityInstruments": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, recognised in other comprehensive income, after tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputRecognisedInOtherComprehensiveIncomeAfterTaxLiabilities": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, recognised in other comprehensive income, after tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputRecognisedInOtherComprehensiveIncomeBeforeTaxAssets": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, recognised in other comprehensive income, before tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputRecognisedInOtherComprehensiveIncomeBeforeTaxEntitysOwnEquityInstruments": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, recognised in other comprehensive income, before tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputRecognisedInOtherComprehensiveIncomeBeforeTaxLiabilities": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, recognised in other comprehensive income, before tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputRecognisedInProfitOrLossAfterTaxAssets": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, recognised in profit or loss, after tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputRecognisedInProfitOrLossAfterTaxEntitysOwnEquityInstruments": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, recognised in profit or loss, after tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputRecognisedInProfitOrLossAfterTaxLiabilities": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, recognised in profit or loss, after tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputRecognisedInProfitOrLossBeforeTaxAssets": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, recognised in profit or loss, before tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputRecognisedInProfitOrLossBeforeTaxEntitysOwnEquityInstruments": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, recognised in profit or loss, before tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleDecreaseInUnobservableInputRecognisedInProfitOrLossBeforeTaxLiabilities": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible decrease in unobservable input, recognised in profit or loss, before tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputAssets": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputEntitysOwnEquityInstruments": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, entity's own equity instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputLiabilities": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputRecognisedInOtherComprehensiveIncomeAfterTaxAssets": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, recognised in other comprehensive income, after tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputRecognisedInOtherComprehensiveIncomeAfterTaxEntitysOwnEquityInstruments": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, recognised in other comprehensive income, after tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputRecognisedInOtherComprehensiveIncomeAfterTaxLiabilities": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, recognised in other comprehensive income, after tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputRecognisedInOtherComprehensiveIncomeBeforeTaxAssets": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, recognised in other comprehensive income, before tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputRecognisedInOtherComprehensiveIncomeBeforeTaxEntitysOwnEquityInstruments": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, recognised in other comprehensive income, before tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputRecognisedInOtherComprehensiveIncomeBeforeTaxLiabilities": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, recognised in other comprehensive income, before tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputRecognisedInProfitOrLossAfterTaxAssets": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, recognised in profit or loss, after tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputRecognisedInProfitOrLossAfterTaxEntitysOwnEquityInstruments": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, recognised in profit or loss, after tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputRecognisedInProfitOrLossAfterTaxLiabilities": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, recognised in profit or loss, after tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputRecognisedInProfitOrLossBeforeTaxAssets": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, recognised in profit or loss, before tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputRecognisedInProfitOrLossBeforeTaxEntitysOwnEquityInstruments": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, recognised in profit or loss, before tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementDueToReasonablyPossibleIncreaseInUnobservableInputRecognisedInProfitOrLossBeforeTaxLiabilities": {
        "label":       "Increase (decrease) in fair value measurement due to reasonably possible increase in unobservable input, recognised in profit or loss, before tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementEntitysOwnEquityInstruments": {
        "label":       "Increase (decrease) in fair value measurement, entity's own equity instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFairValueMeasurementLiabilities": {
        "label":       "Increase (decrease) in fair value measurement, liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFinancialAssets": {
        "label":       "Increase (decrease) in financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInFinancialAssetsArisingFromChangeInMeasurementAttributeFirstApplicationOfIFRS9": {
        "label":       "Increase (decrease) in financial assets arising from change in measurement attribute, initial application of IFRS 9",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IncreaseDecreaseInFinancialAssetsOnBasisOfMeasurementCategoryFirstApplicationOfIFRS9": {
        "label":       "Increase (decrease) in financial assets on basis of measurement category, initial application of IFRS 9",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IncreaseDecreaseInFinancialLiabilitiesArisingFromChangeInMeasurementAttributeFirstApplicationOfIFRS9": {
        "label":       "Increase (decrease) in financial liabilities arising from change in measurement attribute, initial application of IFRS 9",
        "balance":     "credit",
        "period_type": "instant",
    },
    "IncreaseDecreaseInFinancialLiabilitiesOnBasisOfMeasurementCategoryFirstApplicationOfIFRS9": {
        "label":       "Increase (decrease) in financial liabilities on basis of measurement category, initial application of IFRS 9",
        "balance":     "credit",
        "period_type": "instant",
    },
    "IncreaseDecreaseInInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) in insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInIntangibleAssetsAndGoodwill": {
        "label":       "Increase (decrease) in intangible assets and goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInLiabilitiesArisingFromFinancingActivities": {
        "label":       "Increase (decrease) in liabilities arising from financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInNetAssetsAvailableForBenefits": {
        "label":       "Increase (decrease) in net assets available for benefits",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInNetDefinedBenefitLiabilityAsset": {
        "label":       "Increase (decrease) in net defined benefit liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInNetDefinedBenefitLiabilityAssetResultingFromAdministrationCostsNotReflectedInReturnOnPlanAssets": {
        "label":       "Increase (decrease) in net defined benefit liability (asset) resulting from administration costs not reflected in return on plan assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInNetDefinedBenefitLiabilityAssetResultingFromExpenseIncomeInProfitOrLoss": {
        "label":       "Increase (decrease) in net defined benefit liability (asset) resulting from expense (income) in profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInNetDefinedBenefitLiabilityAssetResultingFromMiscellaneousOtherChanges": {
        "label":       "Increase (decrease) in net defined benefit liability (asset) resulting from miscellaneous other changes",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInNetInvestmentInFinanceLease": {
        "label":       "Increase (decrease) in net investment in finance lease",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInProfitLossDueToReasonablyPossibleDecreaseInRiskExposureThatArisesFromContractsWithinScopeOfIFRS17": {
        "label":       "Increase (decrease) in profit (loss) due to reasonably possible decrease in risk variable that arises from contracts within scope of IFRS 17",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInProfitLossDueToReasonablyPossibleDecreaseInRiskExposureThatArisesFromContractsWithinScopeOfIFRS17InsuranceContractsIssuedBeforeMitigationByReinsuranceContractsHeld": {
        "label":       "Increase (decrease) in profit (loss) due to reasonably possible decrease in risk variable that arises from contracts within scope of IFRS 17, insurance contracts issued before mitigation by reinsurance contracts held",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInProfitLossDueToReasonablyPossibleIncreaseInRiskExposureThatArisesFromContractsWithinScopeOfIFRS17": {
        "label":       "Increase (decrease) in profit (loss) due to reasonably possible increase in risk variable that arises from contracts within scope of IFRS 17",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInProfitLossDueToReasonablyPossibleIncreaseInRiskExposureThatArisesFromContractsWithinScopeOfIFRS17InsuranceContractsIssuedBeforeMitigationByReinsuranceContractsHeld": {
        "label":       "Increase (decrease) in profit (loss) due to reasonably possible increase in risk variable that arises from contracts within scope of IFRS 17, insurance contracts issued before mitigation by reinsurance contracts held",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Increase (decrease) in property, plant and equipment including right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInRegulatoryDeferralAccountCreditBalances": {
        "label":       "Increase (decrease) in regulatory deferral account credit balances",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInRegulatoryDeferralAccountDebitBalances": {
        "label":       "Increase (decrease) in regulatory deferral account debit balances",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInReserveOfGainsAndLossesOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeRelatedToInsuranceContractsToWhichParagraphsC18bC19bC24bAndC24cOfIFRS17HaveBeenApplied": {
        "label":       "Increase (decrease) in reserve of gains and losses on financial assets measured at fair value through other comprehensive income related to insurance contracts to which paragraphs C18(b), C19(b), C24(b) and C24(c) of IFRS 17 have been applied",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInRightofuseAssets": {
        "label":       "Increase (decrease) in right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseInWorkingCapital": {
        "label":       "Increase (decrease) in working capital",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughAcquisitionOfSubsidiary": {
        "label":       "Increase (decrease) through acquisition of subsidiary, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughAdditionalItemsNecessaryToUnderstandChangeInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through additional items necessary to understand change, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughAdjustmentsArisingFromPassageOfTimeAllowanceAccountForCreditLossesOfFinancialAssets": {
        "label":       "Increase (decrease) through adjustments arising from passage of time, allowance account for credit losses of financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughAmortisationOfInsuranceAcquisitionCashFlowsInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through amortisation of insurance acquisition cash flows, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughAmountsRecognisedInProfitOrLossAggregateDifferenceBetweenFairValueAtInitialRecognitionAndAmountDeterminedUsingValuationTechniqueYetToBeRecognised": {
        "label":       "Increase (decrease) through amounts recognised in profit or loss, aggregate difference between fair value at initial recognition and transaction price yet to be recognised in profit or loss",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughAppropriationOfRetainedEarnings": {
        "label":       "Increase (decrease) through appropriation of retained earnings, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughBalancesRecognisedInCurrentPeriodInStatementOfFinancialPositionRegulatoryDeferralAccountCreditBalances": {
        "label":       "Increase (decrease) through balances recognised in current period in statement of financial position, regulatory deferral account credit balances",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughBalancesRecognisedInCurrentPeriodInStatementOfFinancialPositionRegulatoryDeferralAccountDebitBalances": {
        "label":       "Increase (decrease) through balances recognised in current period in statement of financial position, regulatory deferral account debit balances",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughBusinessCombinationsAndDisposalsNetDefinedBenefitLiabilityAsset": {
        "label":       "Increase (decrease) in net defined benefit liability (asset) resulting from business combinations and disposals",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughBusinessCombinationsAndDisposalsReimbursementRights": {
        "label":       "Increase (decrease) in reimbursement rights related to defined benefit obligation, resulting from resulting from business combinations and disposals",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughBusinessCombinationsDeferredTaxLiabilityAsset": {
        "label":       "Increase (decrease) through business combinations, deferred tax liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughCashFlowsInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through cash flows, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangeInDiscountRateContingentLiabilitiesRecognisedInBusinessCombination": {
        "label":       "Increase (decrease) through change in discount rate, contingent liabilities recognised in business combination",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangeInDiscountRateOtherProvisions": {
        "label":       "Increase (decrease) through change in discount rate, other provisions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangeInEquityOfSubsidiaries": {
        "label":       "Increase (decrease) through change in equity of subsidiaries, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangeInRiskAdjustmentForNonfinancialRiskThatDoesNotRelateToFutureOrPastServiceInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through change in risk adjustment for non-financial risk that does not relate to future or past service, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesInDiscountRatesRegulatoryDeferralAccountCreditBalances": {
        "label":       "Increase (decrease) through changes in discount rates, regulatory deferral account credit balances",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesInDiscountRatesRegulatoryDeferralAccountDebitBalances": {
        "label":       "Increase (decrease) through changes in discount rates, regulatory deferral account debit balances",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesInEstimatesThatAdjustContractualServiceMarginInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through changes in estimates that adjust contractual service margin, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesInEstimatesThatDoNotAdjustContractualServiceMarginInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through changes in estimates that do not adjust contractual service margin, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesInFairValuesLiabilitiesArisingFromFinancingActivities": {
        "label":       "Increase (decrease) through changes in fair values, liabilities arising from financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesInForeignExchangeRatesNetDefinedBenefitLiabilityAsset": {
        "label":       "Increase (decrease) in net defined benefit liability (asset) resulting from changes in foreign exchange rates, net defined benefit liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesInForeignExchangeRatesRegulatoryDeferralAccountCreditBalances": {
        "label":       "Increase (decrease) through changes in foreign exchange rates, regulatory deferral account credit balances",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesInForeignExchangeRatesRegulatoryDeferralAccountDebitBalances": {
        "label":       "Increase (decrease) through changes in foreign exchange rates, regulatory deferral account debit balances",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesInModelsOrRiskParametersExposureToCreditRiskOnLoanCommitmentsAndFinancialGuaranteeContracts": {
        "label":       "Increase (decrease) through changes in models or risk parameters, exposure to credit risk on loan commitments and financial guarantee contracts",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesInModelsOrRiskParametersFinancialAssets": {
        "label":       "Increase (decrease) through changes in models or risk parameters, financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesInOwnershipInterestsInSubsidiariesThatDoNotResultInLossOfControl": {
        "label":       "Increase (decrease) through changes in ownership interests in subsidiaries that do not result in loss of control, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesInOwnershipInterestsInSubsidiariesThatDoNotResultInLossOfControlEquityAttributableToOwnersOfParent": {
        "label":       "Increase (decrease) through changes in ownership interests in subsidiaries that do not result in loss of control, equity attributable to owners of parent",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesThatRelateToCurrentServiceInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through changes that relate to current service, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesThatRelateToFutureServiceInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through changes that relate to future service, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughChangesThatRelateToPastServiceInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through changes that relate to past service, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughConversionOfConvertibleInstruments": {
        "label":       "Increase (decrease) through conversion of convertible instruments, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughCumulativeCatchupAdjustmentsToRevenueArisingFromChangeInEstimateOfTransactionPriceContractAssets": {
        "label":       "Increase (decrease) through cumulative catch-up adjustments to revenue arising from change in estimate of transaction price, contract assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughCumulativeCatchupAdjustmentsToRevenueArisingFromChangeInEstimateOfTransactionPriceContractLiabilities": {
        "label":       "Increase (decrease) through cumulative catch-up adjustments to revenue arising from change in estimate of transaction price, contract liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughCumulativeCatchupAdjustmentsToRevenueArisingFromChangeInMeasureOfProgressContractAssets": {
        "label":       "Increase (decrease) through cumulative catch-up adjustments to revenue arising from change in measure of progress, contract assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughCumulativeCatchupAdjustmentsToRevenueArisingFromChangeInMeasureOfProgressContractLiabilities": {
        "label":       "Increase (decrease) through cumulative catch-up adjustments to revenue arising from change in measure of progress, contract liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughCumulativeCatchupAdjustmentsToRevenueArisingFromContractModificationContractAssets": {
        "label":       "Increase (decrease) through cumulative catch-up adjustments to revenue arising from contract modification, contract assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughCumulativeCatchupAdjustmentsToRevenueArisingFromContractModificationContractLiabilities": {
        "label":       "Increase (decrease) through cumulative catch-up adjustments to revenue arising from contract modification, contract liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughCumulativeCatchupAdjustmentsToRevenueContractAssets": {
        "label":       "Increase (decrease) through cumulative catch-up adjustments to revenue, contract assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughCumulativeCatchupAdjustmentsToRevenueContractLiabilities": {
        "label":       "Increase (decrease) through cumulative catch-up adjustments to revenue, contract liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughDisposalOfSubsidiary": {
        "label":       "Increase (decrease) through disposal of subsidiary, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughEffectOfChangesInForeignExchangeRatesLiabilitiesArisingFromFinancingActivities": {
        "label":       "Increase (decrease) through effect of changes in foreign exchange rates, liabilities arising from financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughEffectOfChangesInRiskOfNonperformanceByIssuerOfReinsuranceContractsHeldInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through effect of changes in risk of non-performance by issuer of reinsurance contracts held, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughEffectsOfContractsAcquiredInPeriodInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through effects of contracts acquired in period, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughEffectsOfContractsInitiallyRecognisedInPeriodInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through effects of contracts initially recognised in period, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughEffectsOfGroupsOfOnerousContractsInitiallyRecognisedInPeriodInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through effects of groups of onerous contracts initially recognised in period, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughExerciseOfOptions": {
        "label":       "Increase (decrease) through exercise of options, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughExerciseOfWarrantsEquity": {
        "label":       "Increase (decrease) through exercise of warrants, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughExperienceAdjustmentsInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through experience adjustments, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughFinancingCashFlowsLiabilitiesArisingFromFinancingActivities": {
        "label":       "Increase (decrease) through financing cash flows, liabilities arising from financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughForeignExchangeAndOtherMovementsExposureToCreditRiskOnLoanCommitmentsAndFinancialGuaranteeContracts": {
        "label":       "Increase (decrease) through foreign exchange and other movements, exposure to credit risk on loan commitments and financial guarantee contracts",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughForeignExchangeAndOtherMovementsFinancialAssets": {
        "label":       "Increase (decrease) through foreign exchange and other movements, financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughForeignExchangeExposureToCreditRiskOnLoanCommitmentsAndFinancialGuaranteeContracts": {
        "label":       "Increase (decrease) through foreign exchange, exposure to credit risk on loan commitments and financial guarantee contracts",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughForeignExchangeFinancialAssets": {
        "label":       "Increase (decrease) through foreign exchange, financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughGainsLossesInPeriodReserveOfGainsAndLossesOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeRelatedToInsuranceContractsToWhichParagraphsC18bC19bC24bAndC24cOfIFRS17HaveBeenApplied": {
        "label":       "Increase (decrease) through gains (losses) in period, reserve of gains and losses on financial assets measured at fair value through other comprehensive income related to insurance contracts to which paragraphs C18(b), C19(b), C24(b) and C24(c) of IFRS 17 have been applied",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughIncurredClaimsAndOtherIncurredInsuranceServiceExpensesInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through incurred claims and other incurred insurance service expenses, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughIncurredClaimsPaidAndOtherInsuranceServiceExpensesPaidForInsuranceContractsIssuedExcludingInsuranceAcquisitionCashFlowsInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through incurred claims paid and other insurance service expenses paid for insurance contracts issued excluding insurance acquisition cash flows, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughIncurredClaimsRecoveredAndOtherInsuranceServiceExpensesRecoveredUnderReinsuranceContractsHeldInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through incurred claims recovered and other insurance service expenses recovered under reinsurance contracts held, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughInsuranceAcquisitionCashFlowsInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through insurance acquisition cash flows, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughInsuranceFinanceIncomeOrExpensesInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through insurance finance income or expenses, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughInsuranceRevenueInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through insurance revenue, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughInsuranceRevenueNotRelatedToContractsThatExistedAtTransitionDateToWhichModifiedRetrospectiveApproachOrFairValueApproachHasBeenAppliedInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through insurance revenue not related to contracts that existed at transition date to which modified retrospective approach or fair value approach has been applied, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughInsuranceRevenueRelatedToContractsThatExistedAtTransitionDateToWhichFairValueApproachHasBeenAppliedInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through insurance revenue related to contracts that existed at transition date to which fair value approach has been applied, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughInsuranceRevenueRelatedToContractsThatExistedAtTransitionDateToWhichModifiedRetrospectiveApproachHasBeenAppliedInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through insurance revenue related to contracts that existed at transition date to which modified retrospective approach has been applied, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughInsuranceServiceExpensesInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through insurance service expenses, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughInsuranceServiceResultInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through insurance service result, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughInvestmentComponentsExcludedFromInsuranceRevenueAndInsuranceServiceExpensesInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through investment components excluded from insurance revenue and insurance service expenses, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughLossOfControlOfSubsidiaryDeferredTaxLiabilityAsset": {
        "label":       "Increase (decrease) through loss of control of subsidiary, deferred tax liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughModificationOfContractualCashFlowsExposureToCreditRiskOnLoanCommitmentsAndFinancialGuaranteeContracts": {
        "label":       "Increase (decrease) through modification of contractual cash flows, exposure to credit risk on loan commitments and financial guarantee contracts",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughModificationOfContractualCashFlowsFinancialAssets": {
        "label":       "Increase (decrease) through modification of contractual cash flows, financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughNetExchangeDifferencesAllowanceAccountForCreditLossesOfFinancialAssets": {
        "label":       "Increase (decrease) through net exchange differences, allowance account for credit losses of financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughNetExchangeDifferencesBiologicalAssets": {
        "label":       "Increase (decrease) through net exchange differences, biological assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughNetExchangeDifferencesDeferredTaxLiabilityAsset": {
        "label":       "Increase (decrease) through net exchange differences, deferred tax liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughNetExchangeDifferencesGoodwill": {
        "label":       "Increase (decrease) through net exchange differences, goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughNetExchangeDifferencesIntangibleAssetsAndGoodwill": {
        "label":       "Increase (decrease) through net exchange differences, intangible assets and goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughNetExchangeDifferencesIntangibleAssetsOtherThanGoodwill": {
        "label":       "Increase (decrease) through net exchange differences, intangible assets other than goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughNetExchangeDifferencesInvestmentProperty": {
        "label":       "Increase (decrease) through net exchange differences, investment property",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughNetExchangeDifferencesOtherProvisions": {
        "label":       "Increase (decrease) through net exchange differences, other provisions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughNetExchangeDifferencesPropertyPlantAndEquipment": {
        "label":       "Increase (decrease) through net exchange differences, property, plant and equipment",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughNetExchangeDifferencesPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Increase (decrease) through net exchange differences, property, plant and equipment including right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughNetExchangeDifferencesReimbursementRightsAtFairValue": {
        "label":       "Increase (decrease) in reimbursement rights related to defined benefit obligation, resulting from net exchange differences",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughNetExchangeDifferencesRightofuseAssets": {
        "label":       "Increase (decrease) through net exchange differences, right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughNewTransactionsAggregateDifferenceBetweenFairValueAtInitialRecognitionAndAmountDeterminedUsingValuationTechniqueYetToBeRecognised": {
        "label":       "Increase (decrease) through new transactions, aggregate difference between fair value at initial recognition and transaction price yet to be recognised in profit or loss",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughObtainingOrLosingControlOfSubsidiariesOrOtherBusinessesLiabilitiesArisingFromFinancingActivities": {
        "label":       "Increase (decrease) through obtaining or losing control of subsidiaries or other businesses, liabilities arising from financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherChangesAllowanceAccountForCreditLossesOfFinancialAssets": {
        "label":       "Increase (decrease) through other changes, allowance account for credit losses of financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherChangesIntangibleAssetsAndGoodwill": {
        "label":       "Increase (decrease) through other changes, intangible assets and goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherChangesIntangibleAssetsOtherThanGoodwill": {
        "label":       "Increase (decrease) through other changes, intangible assets other than goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherChangesInvestmentProperty": {
        "label":       "Increase (decrease) through other changes, investment property",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherChangesLiabilitiesArisingFromFinancingActivities": {
        "label":       "Increase (decrease) through other changes, liabilities arising from financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherChangesNetDefinedBenefitLiabilityAsset": {
        "label":       "Increase (decrease) in net defined benefit liability (asset) resulting from other changes",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherChangesPropertyPlantAndEquipment": {
        "label":       "Increase (decrease) through other changes, property, plant and equipment",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherChangesPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Increase (decrease) through other changes, property, plant and equipment including right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherChangesRegulatoryDeferralAccountCreditBalances": {
        "label":       "Increase (decrease) through other changes, regulatory deferral account credit balances",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherChangesRegulatoryDeferralAccountDebitBalances": {
        "label":       "Increase (decrease) through other changes, regulatory deferral account debit balances",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherChangesRightofuseAssets": {
        "label":       "Increase (decrease) through other changes, right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherContributionsByOwners": {
        "label":       "Increase through other contributions by owners, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherDistributionsToOwners": {
        "label":       "Decrease through other distributions to owners, equity",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherMovementsExposureToCreditRiskOnLoanCommitmentsAndFinancialGuaranteeContracts": {
        "label":       "Increase (decrease) through other movements, exposure to credit risk on loan commitments and financial guarantee contracts",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughOtherMovementsFinancialAssets": {
        "label":       "Increase (decrease) through other movements, financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughPremiumsPaidForReinsuranceContractsHeldInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through premiums paid for reinsurance contracts held, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughPremiumsReceivedForInsuranceContractsIssuedInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through premiums received for insurance contracts issued, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughReclassificationAdjustmentsInPeriodReserveOfGainsAndLossesOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeRelatedToInsuranceContractsToWhichParagraphsC18bC19bC24bAndC24cOfIFRS17HaveBeenApplied": {
        "label":       "Increase (decrease) through reclassification adjustments in period, reserve of gains and losses on financial assets measured at fair value through other comprehensive income related to insurance contracts to which paragraphs C18(b), C19(b), C24(b) and C24(c) of IFRS 17 have been applied",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughRecognitionOfContractualServiceMarginInProfitOrLossToReflectTransferOfServicesInsuranceContractsLiabilityAsset": {
        "label":       "Increase (decrease) through recognition of contractual service margin in profit or loss to reflect transfer of services, insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughSharebasedPaymentTransactions": {
        "label":       "Increase (decrease) through share-based payment transactions, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTimeValueOfMoneyAdjustmentOtherProvisions": {
        "label":       "Increase through adjustments arising from passage of time, other provisions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransactionsWithOwners": {
        "label":       "Increase (decrease) through transactions with owners, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransferBetweenRevaluationReserveAndRetainedEarnings": {
        "label":       "Increase (decrease) through transfer between revaluation surplus and retained earnings, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransferToStatutoryReserve": {
        "label":       "Increase (decrease) through transfer to statutory reserve, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersAndOtherChangesBiologicalAssets": {
        "label":       "Increase (decrease) through other changes, biological assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersAndOtherChangesEquity": {
        "label":       "Increase (decrease) through other changes, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersAndOtherChangesGoodwill": {
        "label":       "Increase (decrease) through other changes, goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersAndOtherChangesIntangibleAssetsAndGoodwill": {
        "label":       "Increase (decrease) through transfers and other changes, intangible assets and goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersAndOtherChangesIntangibleAssetsOtherThanGoodwill": {
        "label":       "Increase (decrease) through transfers and other changes, intangible assets other than goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersAndOtherChangesOtherProvisions": {
        "label":       "Increase (decrease) through transfers and other changes, other provisions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersAndOtherChangesPropertyPlantAndEquipment": {
        "label":       "Increase (decrease) through transfers and other changes, property, plant and equipment",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersAndOtherChangesPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Increase (decrease) through transfers and other changes, property, plant and equipment including right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersAndOtherChangesRightofuseAssets": {
        "label":       "Increase (decrease) through transfers and other changes, right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersExposureToCreditRiskOnLoanCommitmentsAndFinancialGuaranteeContracts": {
        "label":       "Increase (decrease) through transfers, exposure to credit risk on loan commitments and financial guarantee contracts",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersFinancialAssets": {
        "label":       "Increase (decrease) through transfers, financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersFromConstructionInProgressPropertyPlantAndEquipment": {
        "label":       "Increase (decrease) through transfers from construction in progress, property, plant and equipment",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersFromConstructionInProgressPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Increase (decrease) through transfers from construction in progress, property, plant and equipment including right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersFromToInvestmentPropertyPropertyPlantAndEquipment": {
        "label":       "Increase (decrease) through transfers from (to) investment property, property, plant and equipment",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersFromToInvestmentPropertyPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Increase (decrease) through transfers from (to) investment property, property, plant and equipment including right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersIntangibleAssetsAndGoodwill": {
        "label":       "Increase (decrease) through transfers, intangible assets and goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersIntangibleAssetsOtherThanGoodwill": {
        "label":       "Increase (decrease) through transfers, intangible assets other than goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersPropertyPlantAndEquipment": {
        "label":       "Increase (decrease) through transfers, property, plant and equipment",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Increase (decrease) through transfers, property, plant and equipment including right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersRightofuseAssets": {
        "label":       "Increase (decrease) through transfers, right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersToDisposalGroupsRegulatoryDeferralAccountCreditBalances": {
        "label":       "Increase (decrease) through transfers to disposal groups, regulatory deferral account credit balances",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTransfersToDisposalGroupsRegulatoryDeferralAccountDebitBalances": {
        "label":       "Increase (decrease) through transfers to disposal groups, regulatory deferral account debit balances",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseDecreaseThroughTreasuryShareTransactions": {
        "label":       "Increase (decrease) through treasury share transactions, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseDecreaseToProfitLossToReflectDilutiveEffectResultingFromAssumedConversionOfPotentialOrdinaryShares": {
        "label":       "Increase (decrease) to profit (loss) to reflect dilutive effect resulting from assumed conversion of potential ordinary shares",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsAssets": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsEntitysOwnEquityInstruments": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, entity's own equity instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsLiabilities": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInOtherComprehensiveIncomeAfterTaxAssets": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in other comprehensive income, after tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInOtherComprehensiveIncomeAfterTaxEntitysOwnEquityInstruments": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in other comprehensive income, after tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInOtherComprehensiveIncomeAfterTaxLiabilities": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in other comprehensive income, after tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInOtherComprehensiveIncomeBeforeTaxAssets": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in other comprehensive income, before tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInOtherComprehensiveIncomeBeforeTaxEntitysOwnEquityInstruments": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in other comprehensive income, before tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInOtherComprehensiveIncomeBeforeTaxLiabilities": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in other comprehensive income, before tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInProfitOrLossAfterTaxAssets": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in profit or loss, after tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInProfitOrLossAfterTaxEntitysOwnEquityInstruments": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in profit or loss, after tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInProfitOrLossAfterTaxLiabilities": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in profit or loss, after tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInProfitOrLossBeforeTaxAssets": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in profit or loss, before tax, assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInProfitOrLossBeforeTaxEntitysOwnEquityInstruments": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in profit or loss, before tax, entity's own equity instruments",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseInFairValueMeasurementDueToChangeInMultipleUnobservableInputsToReflectReasonablyPossibleAlternativeAssumptionsRecognisedInProfitOrLossBeforeTaxLiabilities": {
        "label":       "Increase in fair value measurement due to change in multiple unobservable inputs to reflect reasonably possible alternative assumptions, recognised in profit or loss, before tax, liabilities",
        "balance":     "None",
        "period_type": "duration",
    },
    "IncreaseThroughAdjustmentsArisingFromPassageOfTimeContingentLiabilitiesRecognisedInBusinessCombination": {
        "label":       "Increase through adjustments arising from passage of time, contingent liabilities recognised in business combination",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseThroughBusinessCombinationsContractAssets": {
        "label":       "Increase through business combinations, contract assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseThroughBusinessCombinationsContractLiabilities": {
        "label":       "Increase through business combinations, contract liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseThroughItemsAcquiredInBusinessCombinationRegulatoryDeferralAccountDebitBalances": {
        "label":       "Increase through items acquired in business combination, regulatory deferral account debit balances",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseThroughItemsAssumedInBusinessCombinationRegulatoryDeferralAccountCreditBalances": {
        "label":       "Increase through items assumed in business combination, regulatory deferral account credit balances",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseThroughNewLeasesLiabilitiesArisingFromFinancingActivities": {
        "label":       "Increase through new leases, liabilities arising from financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseThroughOriginationOrPurchaseExposureToCreditRiskOnLoanCommitmentsAndFinancialGuaranteeContracts": {
        "label":       "Increase through origination or purchase, exposure to credit risk on loan commitments and financial guarantee contracts",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IncreaseThroughOriginationOrPurchaseFinancialAssets": {
        "label":       "Increase through origination or purchase, financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncreaseThroughReversalsOfImpairmentLossesAssetsForInsuranceAcquisitionCashFlows": {
        "label":       "Increase through reversals of impairment losses, assets for insurance acquisition cash flows",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IncrementalFairValueGrantedModifiedSharebasedPaymentArrangements": {
        "label":       "Incremental fair value granted, modified share-based payment arrangements",
        "balance":     "None",
        "period_type": "duration",
    },
    "IndemnificationAssetsRecognisedAsOfAcquisitionDate": {
        "label":       "Indemnification assets recognised as of acquisition date",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InflowsOfCashFromInvestingActivities": {
        "label":       "Inflows of cash from investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InsuranceContractsIssuedThatAreAssets": {
        "label":       "Insurance contracts issued that are assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InsuranceContractsIssuedThatAreLiabilities": {
        "label":       "Insurance contracts issued that are liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "InsuranceContractsLiabilityAsset": {
        "label":       "Insurance contracts liability (asset)",
        "balance":     "credit",
        "period_type": "instant",
    },
    "InsuranceContractsLiabilityAssetAtDateOfChangeContractsWithDirectParticipationFeaturesForWhichEntityChangedBasisOfDisaggregationOfInsuranceFinanceIncomeExpensesBetweenProfitOrLossAndOtherComprehensiveIncome": {
        "label":       "Insurance contracts liability (asset) at date of change, contracts with direct participation features for which entity changed basis of disaggregation of insurance finance income (expenses) between profit or loss and other comprehensive income",
        "balance":     "credit",
        "period_type": "instant",
    },
    "InsuranceContractsThatAreAssets": {
        "label":       "Insurance contracts that are assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InsuranceContractsThatAreLiabilities": {
        "label":       "Insurance contracts that are liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "InsuranceExpense": {
        "label":       "Insurance expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InsuranceFinanceIncomeExpenses": {
        "label":       "Insurance finance income expenses",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLossBeforeTax": {
        "label":       "Insurance finance income (expenses) from insurance contracts issued excluded from profit or loss that will be reclassified to profit or loss, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLossNetOfTax": {
        "label":       "Insurance finance income (expenses) from insurance contracts issued excluded from profit or loss that will be reclassified to profit or loss, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedRecognisedInProfitOrLoss": {
        "label":       "Insurance finance income expenses from insurance contracts issued recognised in profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InsuranceRevenue": {
        "label":       "Insurance revenue",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InsuranceRevenueAllocationOfPortionOfPremiumsThatRelateToRecoveryOfInsuranceAcquisitionCashFlows": {
        "label":       "Insurance revenue allocation of portion of premiums that relate to recovery of insurance acquisition cash flows",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InsuranceRevenueAmountsRelatingToChangesInLiabilityForRemainingCoverage": {
        "label":       "Insurance revenue amounts relating to changes in liability for remaining coverage",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InsuranceRevenueChangeInRiskAdjustmentForNonfinancialRisk": {
        "label":       "Insurance revenue change in risk adjustment for nonfinancial risk",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InsuranceRevenueContractualServiceMarginRecognisedInProfitOrLossBecauseOfTransferOfServices": {
        "label":       "Insurance revenue contractual service margin recognised in profit or loss because of transfer of services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InsuranceRevenueInsuranceServiceExpensesIncurredDuringPeriodMeasuredAtAmountsExpectedAtBeginningOfPeriod": {
        "label":       "Insurance revenue insurance service expenses incurred during period measured at amounts expected at beginning of period",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InsuranceRevenueOtherAmounts": {
        "label":       "Insurance revenue other amounts",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InsuranceServiceExpensesFromInsuranceContractsIssued": {
        "label":       "Insurance service expenses from insurance contracts issued",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InsuranceServiceResult": {
        "label":       "Insurance service result",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IntangibleAssetFairValueUsedAsDeemedCost": {
        "label":       "Intangible asset fair value used as deemed cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IntangibleAssetsAcquiredByWayOfGovernmentGrant": {
        "label":       "Intangible assets acquired by way of government grant",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IntangibleAssetsAcquiredByWayOfGovernmentGrantAtFairValue": {
        "label":       "Intangible assets acquired by way of government grant, fair value initially recognised",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IntangibleAssetsAndGoodwill": {
        "label":       "Intangible assets and goodwill",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IntangibleAssetsMaterialToEntity": {
        "label":       "Intangible assets material to entity",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IntangibleAssetsOtherThanGoodwill": {
        "label":       "Intangible assets other than goodwill",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IntangibleAssetsOtherThanGoodwillCarryingAmountAtCostOfRevaluedAssets": {
        "label":       "Intangible assets other than goodwill, revalued assets, at cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IntangibleAssetsOtherThanGoodwillCarryingAmountOfRevaluedAssets": {
        "label":       "Intangible assets other than goodwill, revalued assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IntangibleAssetsOtherThanGoodwillRevaluationSurplus": {
        "label":       "Intangible assets other than goodwill, revaluation surplus",
        "balance":     "credit",
        "period_type": "instant",
    },
    "IntangibleAssetsPledgedAsSecurityForLiabilities": {
        "label":       "Intangible assets pledged as security for liabilities",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IntangibleAssetsUnderDevelopment": {
        "label":       "Intangible assets under development",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IntangibleAssetsWhoseTitleIsRestricted": {
        "label":       "Intangible assets whose title is restricted",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IntangibleAssetsWithIndefiniteUsefulLife": {
        "label":       "Intangible assets with indefinite useful life",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IntangibleExplorationAndEvaluationAssets": {
        "label":       "Intangible exploration and evaluation assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InterestCostsCapitalised": {
        "label":       "Interest costs capitalised",
        "balance":     "None",
        "period_type": "duration",
    },
    "InterestCostsIncurred": {
        "label":       "Interest costs incurred",
        "balance":     "None",
        "period_type": "duration",
    },
    "InterestExpense": {
        "label":       "Interest expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseDefinedBenefitPlans": {
        "label":       "Interest expense defined benefit plans",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseFinancing": {
        "label":       "Interest expense financing",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseForFinancialLiabilitiesNotAtFairValueThroughProfitOrLoss": {
        "label":       "Interest expense for financial liabilities not at fair value through profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseIncomeDefinedBenefitPlans": {
        "label":       "Interest expense income defined benefit plans",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseIncomeNetDefinedBenefitLiabilityAsset": {
        "label":       "Increase (decrease) in net defined benefit liability (asset) resulting from interest expense (income)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestExpenseOnBankLoansAndOverdrafts": {
        "label":       "Interest expense on bank loans and overdrafts",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseOnBonds": {
        "label":       "Interest expense on bonds",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseOnBorrowings": {
        "label":       "Interest expense on borrowings",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseOnDebtInstrumentsIssued": {
        "label":       "Interest expense on debt instruments issued",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseOnDepositsFromBanks": {
        "label":       "Interest expense on deposits from banks",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseOnDepositsFromCustomers": {
        "label":       "Interest expense on deposits from customers",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseOnFinancialLiabilitiesDesignatedAtFairValueThroughProfitOrLoss": {
        "label":       "Interest expense on financial liabilities designated at fair value through profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseOnFinancialLiabilitiesHeldForTrading": {
        "label":       "Interest expense on financial liabilities held for trading",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseOnLeaseLiabilities": {
        "label":       "Interest expense on lease liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseOnLiabilitiesDueToCentralBanks": {
        "label":       "Interest expense on liabilities due to central banks",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseOnOtherFinancialLiabilities": {
        "label":       "Interest expense on other financial liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseOnRepurchaseAgreementsAndCashCollateralOnSecuritiesLent": {
        "label":       "Interest expense on repurchase agreements and cash collateral on securities lent",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpenseOperating": {
        "label":       "Interest expense operating",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestExpensesOnPensionLiabilitiesFinancing": {
        "label":       "Interest expenses on pension liabilities financing",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestIncomeDefinedBenefitPlans": {
        "label":       "Interest income defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeExpenseRecognisedForAssetsReclassifiedIntoMeasuredAtAmortisedCost": {
        "label":       "Interest revenue recognised for assets reclassified out of fair value through profit or loss category into amortised cost or fair value through other comprehensive income category",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeExpenseRecognisedForFinancialAssetsReclassifiedIntoMeasuredAtAmortisedCostFirstApplicationOfIFRS9": {
        "label":       "Interest revenue (expense) recognised for financial assets reclassified out of fair value through profit or loss category, initial application of IFRS 9",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeExpenseRecognisedForFinancialLiabilitiesReclassifiedIntoMeasuredAtAmortisedCostFirstApplicationOfIFRS9": {
        "label":       "Interest revenue (expense) recognised for financial liabilities reclassified out of fair value through profit or loss category, initial application of IFRS 9",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeForFinancialAssetsMeasuredAtAmortisedCost": {
        "label":       "Interest revenue for financial assets measured at amortised cost",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeForFinancialAssetsNotAtFairValueThroughProfitOrLoss": {
        "label":       "Interest income for financial assets not at fair value through profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnAvailableforsaleFinancialAssets": {
        "label":       "Interest income on available-for-sale financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnCashAndBankBalancesAtCentralBanks": {
        "label":       "Interest income on cash and bank balances at central banks",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnCashAndCashEquivalents": {
        "label":       "Interest income on cash and cash equivalents",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnDebtInstrumentsHeld": {
        "label":       "Interest income on debt instruments held",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnDeposits": {
        "label":       "Interest income on deposits",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnFinancialAssetsDesignatedAtFairValueThroughProfitOrLoss": {
        "label":       "Interest income on financial assets designated at fair value through profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnFinancialAssetsHeldForTrading": {
        "label":       "Interest income on financial assets held for trading",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnHeldtomaturityInvestments": {
        "label":       "Interest income on held-to-maturity investments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnImpairedFinancialAssetsAccrued": {
        "label":       "Interest income on impaired financial assets accrued",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnLoansAndAdvancesToBanks": {
        "label":       "Interest income on loans and advances to banks",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnLoansAndAdvancesToCustomers": {
        "label":       "Interest income on loans and advances to customers",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnLoansAndReceivables": {
        "label":       "Interest income on loans and receivables",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnOtherFinancialAssets": {
        "label":       "Interest income on other financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeOnReverseRepurchaseAgreementsAndCashCollateralOnSecuritiesBorrowed": {
        "label":       "Interest income on reverse repurchase agreements and cash collateral on securities borrowed",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestIncomeReimbursementRights": {
        "label":       "Increase in reimbursement rights related to defined benefit obligation, resulting from interest income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestPaidClassifiedAsFinancingActivities": {
        "label":       "Interest paid, classified as financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestPaidClassifiedAsInvestingActivities": {
        "label":       "Interest paid classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestPaidClassifiedAsOperatingActivities": {
        "label":       "Interest paid, classified as operating activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestPaidOnDepositLiabilitiesClassifiedAsOperatingActivities": {
        "label":       "Interest paid on deposit liabilities, classified as operating activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestPayable": {
        "label":       "Interest payable",
        "balance":     "credit",
        "period_type": "instant",
    },
    "InterestReceivable": {
        "label":       "Interest receivable",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InterestReceivedClassifiedAsInvestingActivities": {
        "label":       "Interest received, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestReceivedClassifiedAsOperatingActivities": {
        "label":       "Interest received, classified as operating activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestReceivedFromDebtInstrumentsHeldClassifiedAsOperatingActivities": {
        "label":       "Interest received from debt instruments held, classified as operating activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestReceivedFromLoansAndAdvancesClassifiedAsOperatingActivities": {
        "label":       "Interest received from loans and advances, classified as operating activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "InterestRevenueCalculatedUsingEffectiveInterestMethod": {
        "label":       "Interest revenue calculated using effective interest method",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestRevenueCalculatedUsingEffectiveInterestMethodInvesting": {
        "label":       "Interest revenue calculated using effective interest method investing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestRevenueCalculatedUsingEffectiveInterestMethodOperating": {
        "label":       "Interest revenue calculated using effective interest method operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestRevenueExpense": {
        "label":       "Interest revenue expense",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InterestRevenueForFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Interest revenue for financial assets measured at fair value through other comprehensive income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IntrinsicValueOfLiabilitiesFromSharebasedPaymentTransactionsForWhichCounterpartysRightToCashOrOtherAssetsVested2011": {
        "label":       "Intrinsic value of liabilities from share-based payment transactions for which counterparty's right to cash or other assets vested",
        "balance":     "credit",
        "period_type": "instant",
    },
    "Inventories": {
        "label":       "Current inventories",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InventoriesAtFairValueLessCostsToSell": {
        "label":       "Inventories, at fair value less costs to sell",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InventoriesAtNetRealisableValue": {
        "label":       "Inventories, at net realisable value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InventoriesPledgedAsSecurityForLiabilities": {
        "label":       "Inventories pledged as security for liabilities",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InventoriesTotal": {
        "label":       "Inventories",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InventoryRecognisedAsOfAcquisitionDate": {
        "label":       "Inventory recognised as of acquisition date",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InventoryWritedown2011": {
        "label":       "Inventory writedown2011",
        "balance":     "None",
        "period_type": "duration",
    },
    "InvestmentAccountedForUsingEquityMethod": {
        "label":       "Investments accounted for using equity method",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentContractsLiabilities": {
        "label":       "Investment contracts liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "InvestmentFundsAmountContributedToFairValueOfPlanAssets": {
        "label":       "Investment funds, amount contributed to fair value of plan assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentIncome": {
        "label":       "Investment income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InvestmentIncomeInvesting": {
        "label":       "Investment income investing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InvestmentIncomeOperating": {
        "label":       "Investment income operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "InvestmentProperty": {
        "label":       "Investment property",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentPropertyCarriedAtCostOrInAccordanceWithIFRS16WithinFairValueModelAtTimeOfSale": {
        "label":       "Investment property carried at cost or in accordance with IFRS 16 within fair value model, at time of sale",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentPropertyCompleted": {
        "label":       "Investment property completed",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentPropertyFairValueUsedAsDeemedCost": {
        "label":       "Investment property fair value used as deemed cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentPropertyUnderConstructionOrDevelopment": {
        "label":       "Investment property under construction or development",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentsForRiskOfPolicyholders": {
        "label":       "Investments for risk of policyholders",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentsAccountedForUsingEquityMethod": {
        "label":       "Investments accounted for using equity method",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentsInAssociates": {
        "label":       "Investments in associates reported in separate financial statements",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentsInAssociatesAccountedForUsingEquityMethod": {
        "label":       "Investments in associates accounted for using equity method",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentsInJointVentures": {
        "label":       "Investments in joint ventures reported in separate financial statements",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentsInJointVenturesAccountedForUsingEquityMethod": {
        "label":       "Investments in joint ventures accounted for using equity method",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentsInSubsidiaries": {
        "label":       "Investments in subsidiaries reported in separate financial statements",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentsInSubsidiariesJointVenturesAndAssociates": {
        "label":       "Investments in subsidiaries, joint ventures and associates reported in separate financial statements",
        "balance":     "debit",
        "period_type": "instant",
    },
    "InvestmentsOtherThanInvestmentsAccountedForUsingEquityMethod": {
        "label":       "Investments other than investments accounted for using equity method",
        "balance":     "debit",
        "period_type": "instant",
    },
    "IssueCostsNotRecognisedAsExpenseForTransactionRecognisedSeparatelyFromAcquisitionOfAssetsAndAssumptionOfLiabilitiesInBusinessCombination": {
        "label":       "Issue costs not recognised as expense for transaction recognised separately from acquisition of assets and assumption of liabilities in business combination",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IssueOfConvertibleInstruments": {
        "label":       "Issue of convertible instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IssueOfEquity": {
        "label":       "Issue of equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IssuedCapital": {
        "label":       "Issued capital",
        "balance":     "credit",
        "period_type": "instant",
    },
    "IssuedCapitalOrdinaryShares": {
        "label":       "Issued capital, ordinary shares",
        "balance":     "credit",
        "period_type": "instant",
    },
    "IssuedCapitalPreferenceShares": {
        "label":       "Issued capital, preference shares",
        "balance":     "credit",
        "period_type": "instant",
    },
    "IssuesFairValueMeasurementAssets": {
        "label":       "Issues, fair value measurement, assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "IssuesFairValueMeasurementEntitysOwnEquityInstruments": {
        "label":       "Issues, fair value measurement, entity's own equity instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "IssuesFairValueMeasurementLiabilities": {
        "label":       "Issues, fair value measurement, liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ItemsInCourseOfCollectionFromOtherBanks": {
        "label":       "Items in course of collection from other banks",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ItemsInCourseOfTransmissionToOtherBanks": {
        "label":       "Items in course of transmission to other banks",
        "balance":     "credit",
        "period_type": "instant",
    },
    "KeyManagementPersonnelCompensation": {
        "label":       "Key management personnel compensation",
        "balance":     "debit",
        "period_type": "duration",
    },
    "KeyManagementPersonnelCompensationOtherLongtermBenefits": {
        "label":       "Key management personnel compensation other longterm benefits",
        "balance":     "debit",
        "period_type": "duration",
    },
    "KeyManagementPersonnelCompensationPostemploymentBenefits": {
        "label":       "Key management personnel compensation postemployment benefits",
        "balance":     "debit",
        "period_type": "duration",
    },
    "KeyManagementPersonnelCompensationSharebasedPayment": {
        "label":       "Key management personnel compensation sharebased payment",
        "balance":     "debit",
        "period_type": "duration",
    },
    "KeyManagementPersonnelCompensationShorttermEmployeeBenefits": {
        "label":       "Key management personnel compensation shortterm employee benefits",
        "balance":     "debit",
        "period_type": "duration",
    },
    "KeyManagementPersonnelCompensationTerminationBenefits": {
        "label":       "Key management personnel compensation termination benefits",
        "balance":     "debit",
        "period_type": "duration",
    },
    "Land": {
        "label":       "Land",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LandAndBuildings": {
        "label":       "Land and buildings",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LeaseCommitmentsForShorttermLeasesForWhichRecognitionExemptionHasBeenUsed": {
        "label":       "Lease commitments for short-term leases for which recognition exemption has been used",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LeaseLiabilities": {
        "label":       "Lease liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LeasesAsLesseeRelatedPartyTransactions": {
        "label":       "Leases as lessee, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "LeasesAsLessorRelatedPartyTransactions": {
        "label":       "Leases as lessor, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "LegalProceedingsProvision": {
        "label":       "Legal proceedings provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "Liabilities": {
        "label":       "Liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LiabilitiesArisingFromExplorationForAndEvaluationOfMineralResources": {
        "label":       "Liabilities arising from exploration for and evaluation of mineral resources",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LiabilitiesArisingFromFinancingActivities": {
        "label":       "Liabilities arising from financing activities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LiabilitiesDueToCentralBanks": {
        "label":       "Liabilities due to central banks",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LiabilitiesForIncurredClaimsThatAriseFromContractsWithinScopeOfIFRS17": {
        "label":       "Liabilities for incurred claims that arise from contracts within scope of IFRS 17",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LiabilitiesFromSharebasedPaymentTransactions2011": {
        "label":       "Liabilities from share-based payment transactions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LiabilitiesInSubsidiaryOrBusinessesAcquiredOrDisposed2013": {
        "label":       "Liabilities in subsidiary or businesses acquired or disposed",
        "balance":     "credit",
        "period_type": "duration",
    },
    "LiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale": {
        "label":       "Liabilities included in disposal groups classified as held for sale",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LiabilitiesIncurred": {
        "label":       "Liabilities incurred",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LiabilitiesOtherThanActuarialPresentValueOfPromisedRetirementBenefits": {
        "label":       "Liabilities other than actuarial present value of promised retirement benefits",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LiabilitiesRecognisedInEntitysFinancialStatementsInRelationToStructuredEntities": {
        "label":       "Liabilities recognised in entity's financial statements in relation to structured entities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LiabilitiesToWhichSignificantRestrictionsApply": {
        "label":       "Liabilities to which significant restrictions apply",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LiabilitiesWithSignificantRiskOfMaterialAdjustmentsWithinNextFinancialYear": {
        "label":       "Liabilities with significant risk of material adjustments within next financial year",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LiabilityAssetOfDefinedBenefitPlans": {
        "label":       "Net defined benefit liability (asset)",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LicenceFeeIncome": {
        "label":       "Licence fee income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "LicencesAndFranchises": {
        "label":       "Licences and franchises",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvances": {
        "label":       "Loans and advances",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesAtAmortisedCost": {
        "label":       "Loans and advances at amortised cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesAtAmortisedCostAllowanceForExpectedCreditLosses": {
        "label":       "Loans and advances at amortised cost, allowance for expected credit losses",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LoansAndAdvancesAtAmortisedCostGrossCarryingAmount": {
        "label":       "Loans and advances at amortised cost, gross carrying amount",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesAtFairValueThroughProfitOrLossClassifiedAsHeldForTrading": {
        "label":       "Loans and advances at fair value through profit or loss, classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesAtFairValueThroughProfitOrLossMandatorilyMeasuredAtFairValueOtherThanThoseClassifiedAsHeldForTrading": {
        "label":       "Loans and advances at fair value through profit or loss, mandatorily measured at fair value, other than those classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Loans and advances measured at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesToBanks": {
        "label":       "Loans and advances to banks",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesToBanksAtAmortisedCost": {
        "label":       "Loans and advances to banks at amortised cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesToBanksAtFairValueThroughProfitOrLossClassifiedAsHeldForTrading": {
        "label":       "Loans and advances to banks at fair value through profit or loss, classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesToBanksAtFairValueThroughProfitOrLossMandatorilyMeasuredAtFairValueOtherThanThoseClassifiedAsHeldForTrading": {
        "label":       "Loans and advances to banks at fair value through profit or loss, mandatorily measured at fair value, other than those classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesToBanksMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Loans and advances to banks measured at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesToCentralBanks": {
        "label":       "Loans and advances to central banks",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesToCustomers": {
        "label":       "Loans and advances to customers",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesToCustomersAtAmortisedCost": {
        "label":       "Loans and advances to customers at amortised cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesToCustomersAtFairValueThroughProfitOrLossClassifiedAsHeldForTrading": {
        "label":       "Loans and advances to customers at fair value through profit or loss, classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesToCustomersAtFairValueThroughProfitOrLossMandatorilyMeasuredAtFairValueOtherThanThoseClassifiedAsHeldForTrading": {
        "label":       "Loans and advances to customers at fair value through profit or loss, mandatorily measured at fair value, other than those classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesToCustomersMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Loans and advances to customers measured at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndAdvancesToOtherCreditInstitutions": {
        "label":       "Loans and advances to other credit institutions",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansAndReceivables": {
        "label":       "Loans and receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LoansPayableInBreachWhichPermittedLenderToDemandAcceleratedRepayment": {
        "label":       "Loans payable in breach which permitted lender to demand accelerated repayment",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LoansPayableInDefault": {
        "label":       "Loans payable in default",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LoansReceived": {
        "label":       "Loans received",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LoansToGovernment": {
        "label":       "Loans to government",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LongtermBorrowings": {
        "label":       "Non-current portion of non-current borrowings",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LongtermDeposits": {
        "label":       "Long-term deposits",
        "balance":     "debit",
        "period_type": "instant",
    },
    "LongtermLegalProceedingsProvision": {
        "label":       "Non-current legal proceedings provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LongtermMiscellaneousOtherProvisions": {
        "label":       "Non-current miscellaneous other provisions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LongtermOnerousContractsProvision": {
        "label":       "Non-current onerous contracts provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LongtermProvisionForDecommissioningRestorationAndRehabilitationCosts": {
        "label":       "Non-current provision for decommissioning, restoration and rehabilitation costs",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LongtermRestructuringProvision": {
        "label":       "Non-current restructuring provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LongtermWarrantyProvision": {
        "label":       "Non-current warranty provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "LossesArisingFromDerecognitionOfFinancialAssetsMeasuredAtAmortisedCost": {
        "label":       "Losses arising from derecognition of financial assets measured at amortised cost",
        "balance":     "debit",
        "period_type": "duration",
    },
    "LossesIncurredInRelationToInterestsInStructuredEntities": {
        "label":       "Losses incurred in relation to interests in structured entities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "LossesOnChangeInFairValueOfDerivatives": {
        "label":       "Losses on change in fair value of derivatives",
        "balance":     "debit",
        "period_type": "duration",
    },
    "LossesOnDisposalsOfInvestmentProperties": {
        "label":       "Losses on disposals of investment properties",
        "balance":     "debit",
        "period_type": "duration",
    },
    "LossesOnDisposalsOfInvestments": {
        "label":       "Losses on disposals of investments",
        "balance":     "debit",
        "period_type": "duration",
    },
    "LossesOnDisposalsOfInvestmentsOperating": {
        "label":       "Losses on disposals of investments operating",
        "balance":     "debit",
        "period_type": "duration",
    },
    "LossesOnDisposalsOfNoncurrentAssets": {
        "label":       "Losses on disposals of non-current assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "LossesOnDisposalsOfPropertyPlantAndEquipment": {
        "label":       "Losses on disposals of property plant and equipment",
        "balance":     "debit",
        "period_type": "duration",
    },
    "LossesOnLitigationSettlements": {
        "label":       "Losses on litigation settlements",
        "balance":     "debit",
        "period_type": "duration",
    },
    "Machinery": {
        "label":       "Machinery",
        "balance":     "debit",
        "period_type": "instant",
    },
    "MandatoryReserveDepositsAtCentralBanks": {
        "label":       "Mandatory reserve deposits at central banks",
        "balance":     "debit",
        "period_type": "instant",
    },
    "MastheadsAndPublishingTitles": {
        "label":       "Mastheads and publishing titles",
        "balance":     "debit",
        "period_type": "instant",
    },
    "MaximumExposureToCreditRisk": {
        "label":       "Maximum exposure to credit risk",
        "balance":     "None",
        "period_type": "instant",
    },
    "MaximumExposureToCreditRiskFinancialInstrumentsToWhichImpairmentRequirementsInIFRS9AreNotApplied": {
        "label":       "Maximum exposure to credit risk, financial instruments to which impairment requirements in IFRS 9 are not applied",
        "balance":     "None",
        "period_type": "instant",
    },
    "MaximumExposureToCreditRiskOfFinancialAssets": {
        "label":       "Maximum exposure to credit risk of financial assets designated as measured at fair value through profit or loss",
        "balance":     "None",
        "period_type": "instant",
    },
    "MaximumExposureToCreditRiskOfLoansOrReceivables": {
        "label":       "Maximum exposure to credit risk of loans or receivables",
        "balance":     "None",
        "period_type": "instant",
    },
    "MaximumExposureToCreditRiskThatArisesFromContractsWithinScopeOfIFRS17": {
        "label":       "Maximum exposure to credit risk that arises from contracts within scope of IFRS 17",
        "balance":     "None",
        "period_type": "instant",
    },
    "MaximumExposureToLossFromContinuingInvolvement": {
        "label":       "Maximum exposure to loss from continuing involvement",
        "balance":     "None",
        "period_type": "instant",
    },
    "MaximumExposureToLossFromInterestsInStructuredEntities": {
        "label":       "Maximum exposure to loss from interests in structured entities",
        "balance":     "None",
        "period_type": "instant",
    },
    "MaximumLimitOfLossesOfStructuredEntitiesWhichEntityIsRequiredToAbsorbBeforeOtherParties": {
        "label":       "Maximum limit of losses of structured entities which entity is required to absorb before other parties",
        "balance":     "credit",
        "period_type": "instant",
    },
    "MeasurementPeriodAdjustmentsRecognisedForParticularAssetsLiabilitiesNoncontrollingInterestsOrItemsOfConsideration": {
        "label":       "Measurement period adjustments recognised for particular assets, liabilities, non-controlling interests or items of consideration",
        "balance":     "None",
        "period_type": "duration",
    },
    "MediaProductionExpense": {
        "label":       "Media production expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "Merchandise": {
        "label":       "Current merchandise",
        "balance":     "debit",
        "period_type": "instant",
    },
    "MergerReserve": {
        "label":       "Merger reserve",
        "balance":     "credit",
        "period_type": "instant",
    },
    "MiningAssets": {
        "label":       "Mining assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "MiscellaneousOtherOperatingExpense": {
        "label":       "Miscellaneous other operating expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "MiscellaneousOtherOperatingIncome": {
        "label":       "Miscellaneous other operating income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "MiscellaneousOtherProvisions": {
        "label":       "Miscellaneous other provisions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "MortgageLoans": {
        "label":       "Mortgage loans",
        "balance":     "debit",
        "period_type": "instant",
    },
    "MotorVehicles": {
        "label":       "Motor vehicles",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NetAmountsForPayfloatingReceivefixedInterestRateSwapsForWhichNetCashFlowsAreExchanged": {
        "label":       "Net amounts for pay-floating (receive-fixed) interest rate swaps for which net cash flows are exchanged",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NetAssetsLiabilities": {
        "label":       "Assets (liabilities)",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NetDebt": {
        "label":       "Net debt",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NetDeferredTaxAssets": {
        "label":       "Net deferred tax assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NetDeferredTaxLiabilities": {
        "label":       "Net deferred tax liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NetFinancialAssetsSubjectToOffsettingEnforceableMasterNettingArrangementsOrSimilarAgreements": {
        "label":       "Net financial assets subject to offsetting, enforceable master netting arrangements or similar agreements",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NetFinancialAssetsSubjectToOffsettingEnforceableMasterNettingArrangementsOrSimilarAgreementsInStatementOfFinancialPosition": {
        "label":       "Net financial assets subject to offsetting, enforceable master netting arrangements or similar agreements in statement of financial position",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NetFinancialLiabilitiesSubjectToOffsettingEnforceableMasterNettingArrangementsOrSimilarAgreements": {
        "label":       "Net financial liabilities subject to offsetting, enforceable master netting arrangements or similar agreements",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NetFinancialLiabilitiesSubjectToOffsettingEnforceableMasterNettingArrangementsOrSimilarAgreementsInStatementOfFinancialPosition": {
        "label":       "Net financial liabilities subject to offsetting, enforceable master netting arrangements or similar agreements in statement of financial position",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NetForeignExchangeGain": {
        "label":       "Net foreign exchange gain",
        "balance":     "credit",
        "period_type": "duration",
    },
    "NetForeignExchangeLoss": {
        "label":       "Net foreign exchange loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "NetInvestmentInFinanceLease": {
        "label":       "Net investment in finance lease",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NetMovementInDeferredTaxArisingFromRegulatoryDeferralAccountBalancesRelatedToProfitOrLoss": {
        "label":       "Net movement in deferred tax arising from regulatory deferral account balances related to profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "NetMovementInOtherRegulatoryDeferralAccountBalancesRelatedToProfitOrLoss": {
        "label":       "Net movement in other regulatory deferral account balances related to profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "NetMovementInRegulatoryDeferralAccountBalancesRelatedToProfitOrLoss": {
        "label":       "Net movement in regulatory deferral account balances related to profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "NetMovementInRegulatoryDeferralAccountBalancesRelatedToProfitOrLossAndNetMovementInRelatedDeferredTax": {
        "label":       "Net movement in regulatory deferral account balances related to profit or loss and net movement in related deferred tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "NetMovementInRegulatoryDeferralAccountBalancesRelatedToProfitOrLossAttributableToNoncontrollingInterests": {
        "label":       "Net movement in regulatory deferral account balances related to profit or loss, attributable to non-controlling interests",
        "balance":     "credit",
        "period_type": "duration",
    },
    "NetMovementInRegulatoryDeferralAccountBalancesRelatedToProfitOrLossDirectlyAssociatedWithDiscontinuedOperation": {
        "label":       "Net movement in regulatory deferral account balances related to profit or loss directly associated with discontinued operation",
        "balance":     "credit",
        "period_type": "duration",
    },
    "NewLiabilitiesContingentLiabilitiesRecognisedInBusinessCombination": {
        "label":       "New liabilities, contingent liabilities recognised in business combination",
        "balance":     "credit",
        "period_type": "duration",
    },
    "NewProvisionsOtherProvisions": {
        "label":       "New provisions, other provisions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "NominalAmountOfHedgingInstrumentsInHedgingRelationshipsToWhichAmendmentsForInterestRateBenchmarkReformAreApplied": {
        "label":       "Nominal amount of hedging instruments in hedging relationships to which amendments for interest rate benchmark reform are applied",
        "balance":     "None",
        "period_type": "instant",
    },
    "NominalOrPrincipalAmountOfFinancialInstrumentOnDiscontinuationOfMeasurementAtFairValueThroughProfitOrLossBecauseCreditDerivativeIsUsedToManageCreditRisk": {
        "label":       "Nominal or principal amount of financial instrument on discontinuation of measurement at fair value through profit or loss because credit derivative is used to manage credit risk",
        "balance":     "None",
        "period_type": "instant",
    },
    "NoncashAssetsDeclaredForDistributionToOwnersBeforeFinancialStatementsAuthorisedForIssue": {
        "label":       "Non-cash assets declared for distribution to owners before financial statements authorised for issue",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncashAssetsDeclaredForDistributionToOwnersBeforeFinancialStatementsAuthorisedForIssueAtFairValue": {
        "label":       "Non-cash assets declared for distribution to owners before financial statements authorised for issue, at fair value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncashAssetsPledgedAsCollateralForWhichTransfereeHasRightByContractOrCustomToSellOrRepledgeCollateral": {
        "label":       "Non-cash assets pledged as collateral for which transferee has right by contract or custom to sell or repledge collateral",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncashEffectOfBusinessCombinationsSupplierFinanceArrangements": {
        "label":       "Non-cash effect of business combinations, supplier finance arrangements",
        "balance":     "credit",
        "period_type": "duration",
    },
    "NoncashEffectOfExchangeDifferencesSupplierFinanceArrangements": {
        "label":       "Non-cash effect of exchange differences, supplier finance arrangements",
        "balance":     "credit",
        "period_type": "duration",
    },
    "NoncontrollingInterestInAcquireeRecognisedAtAcquisitionDate": {
        "label":       "Non-controlling interest in acquiree recognised at acquisition date",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncontrollingInterests": {
        "label":       "Non-controlling interests",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentAccrualsAndNoncurrentDeferredIncomeIncludingNoncurrentContractLiabilities": {
        "label":       "Non-current accruals and non-current deferred income including non-current contract liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentAccruedIncomeIncludingNoncurrentContractAssets": {
        "label":       "Non-current accrued income including non-current contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentAccruedIncomeOtherThanNoncurrentContractAssets": {
        "label":       "Non-current accrued income other than non-current contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentAdvances": {
        "label":       "Non-current advances received, representing non-current contract liabilities for performance obligations satisfied at point in time",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentAssets": {
        "label":       "Non-current assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentAssetsOrDisposalGroupsClassifiedAsHeldForDistributionToOwners": {
        "label":       "Non-current assets or disposal groups classified as held for distribution to owners",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentAssetsOrDisposalGroupsClassifiedAsHeldForSale": {
        "label":       "Non-current assets or disposal groups classified as held for sale",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners": {
        "label":       "Non-current assets or disposal groups classified as held for sale or as held for distribution to owners",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentAssetsOtherThanFinancialInstrumentsDeferredTaxAssetsPostemploymentBenefitAssetsAndRightsArisingUnderInsuranceContracts": {
        "label":       "Non-current assets other than financial instruments, deferred tax assets, post-employment benefit assets, and rights arising under insurance contracts",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentAssetsRecognisedAsOfAcquisitionDate": {
        "label":       "Non-current assets recognised as of acquisition date",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentBiologicalAssets": {
        "label":       "Non-current biological assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentContractAssets": {
        "label":       "Non-current contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentContractLiabilities": {
        "label":       "Non-current contract liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentContractLiabilitiesForPerformanceObligationsSatisfiedOverTime": {
        "label":       "Non-current contract liabilities for performance obligations satisfied over time",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentDebtInstrumentsIssued": {
        "label":       "Non-current debt instruments issued",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentDeferredIncomeIncludingNoncurrentContractLiabilities": {
        "label":       "Non-current deferred income including non-current contract liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentDeferredIncomeOtherThanNoncurrentContractLiabilities": {
        "label":       "Non-current deferred income other than non-current contract liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentDepositsFromCustomers": {
        "label":       "Non-current deposits from customers",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentDerivativeFinancialAssets": {
        "label":       "Non-current derivative financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentDerivativeFinancialLiabilities": {
        "label":       "Non-current derivative financial liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentDividendPayables": {
        "label":       "Non-current dividend payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentExciseTaxPayables": {
        "label":       "Non-current excise tax payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentFinanceLeaseReceivables": {
        "label":       "Non-current finance lease receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentFinancialAssets": {
        "label":       "Non-current financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentFinancialAssetsAtAmortisedCost": {
        "label":       "Non-current financial assets at amortised cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentFinancialAssetsAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Non-current financial assets at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentFinancialAssetsAtFairValueThroughProfitOrLoss": {
        "label":       "Non-current financial assets at fair value through profit or loss",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentFinancialAssetsAtFairValueThroughProfitOrLossClassifiedAsHeldForTrading": {
        "label":       "Non-current financial assets at fair value through profit or loss, classified as held for trading",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentFinancialAssetsAtFairValueThroughProfitOrLossDesignatedUponInitialRecognition": {
        "label":       "Non-current financial assets at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentFinancialAssetsAtFairValueThroughProfitOrLossMandatorilyMeasuredAtFairValue": {
        "label":       "Non-current financial assets at fair value through profit or loss, mandatorily measured at fair value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentFinancialAssetsAtFairValueThroughProfitOrLossMeasuredAsSuchInAccordanceWithExemptionForReacquisitionOfOwnEquityInstruments": {
        "label":       "Non-current financial assets at fair value through profit or loss, measured as such in accordance with exemption for reacquisition of own equity instruments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentFinancialAssetsAtFairValueThroughProfitOrLossMeasuredAsSuchInAccordanceWithExemptionForRepurchaseOfOwnFinancialLiabilities": {
        "label":       "Non-current financial assets at fair value through profit or loss, measured as such in accordance with exemption for repurchase of own financial liabilities",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentFinancialAssetsAvailableforsale": {
        "label":       "Non-current financial assets available-for-sale",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Non-current financial assets measured at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentFinancialLiabilities": {
        "label":       "Non-current financial liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentFinancialLiabilitiesAtAmortisedCost": {
        "label":       "Non-current financial liabilities at amortised cost",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentFinancialLiabilitiesAtFairValueThroughProfitOrLoss": {
        "label":       "Non-current financial liabilities at fair value through profit or loss",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentFinancialLiabilitiesAtFairValueThroughProfitOrLossClassifiedAsHeldForTrading": {
        "label":       "Non-current financial liabilities at fair value through profit or loss, classified as held for trading",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentFinancialLiabilitiesAtFairValueThroughProfitOrLossDesignatedUponInitialRecognition": {
        "label":       "Non-current financial liabilities at fair value through profit or loss, designated upon initial recognition or subsequently",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentGovernmentGrants": {
        "label":       "Non-current government grants",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentHeldtomaturityInvestments": {
        "label":       "Non-current held-to-maturity investments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentInterestPayable": {
        "label":       "Non-current interest payable",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentInterestReceivable": {
        "label":       "Non-current interest receivable",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentInventories": {
        "label":       "Non-current inventories",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentInvestmentsInEquityInstrumentsDesignatedAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Non-current investments in equity instruments designated at fair value through other comprehensive income",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentInvestmentsOtherThanInvestmentsAccountedForUsingEquityMethod": {
        "label":       "Non-current investments other than investments accounted for using equity method",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentLeaseLiabilities": {
        "label":       "Non-current lease liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentLeasePrepayments": {
        "label":       "Non-current lease prepayments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentLiabilities": {
        "label":       "Non-current liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentLiabilitiesRecognisedAsOfAcquisitionDate": {
        "label":       "Non-current liabilities recognised as of acquisition date",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentLoansAndReceivables": {
        "label":       "Non-current loans and receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentNoncashAssetsPledgedAsCollateralForWhichTransfereeHasRightByContractOrCustomToSellOrRepledgeCollateral": {
        "label":       "Non-current non-cash assets pledged as collateral for which transferee has right by contract or custom to sell or repledge collateral",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentOreStockpiles": {
        "label":       "Non-current ore stockpiles",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentPayables": {
        "label":       "Trade and other non-current payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentPayablesForPurchaseOfEnergy": {
        "label":       "Non-current payables for purchase of energy",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentPayablesForPurchaseOfNoncurrentAssets": {
        "label":       "Non-current payables for purchase of non-current assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentPayablesOnSocialSecurityAndTaxesOtherThanIncomeTax": {
        "label":       "Non-current payables on social security and taxes other than income tax",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentPayablesToRelatedParties": {
        "label":       "Non-current payables to related parties",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentPayablesToTradeSuppliers": {
        "label":       "Non-current trade payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentPortionOfNoncurrentBondsIssued": {
        "label":       "Non-current portion of non-current bonds issued",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentPortionOfNoncurrentCommercialPapersIssued": {
        "label":       "Non-current portion of non-current commercial papers issued",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentPortionOfNoncurrentLoansReceived": {
        "label":       "Non-current portion of non-current loans received",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentPortionOfNoncurrentNotesAndDebenturesIssued": {
        "label":       "Non-current portion of non-current notes and debentures issued",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentPortionOfNoncurrentSecuredBankLoansReceived": {
        "label":       "Non-current portion of non-current secured bank loans received",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentPortionOfNoncurrentUnsecuredBankLoansReceived": {
        "label":       "Non-current portion of non-current unsecured bank loans received",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentPortionOfOtherNoncurrentBorrowings": {
        "label":       "Non-current portion of other non-current borrowings",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentPrepayments": {
        "label":       "Non-current prepayments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentPrepaymentsAndNoncurrentAccruedIncomeIncludingNoncurrentContractAssets": {
        "label":       "Non-current prepayments and non-current accrued income including non-current contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentPrepaymentsAndNoncurrentAccruedIncomeOtherThanNoncurrentContractAssets": {
        "label":       "Non-current prepayments and non-current accrued income other than non-current contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentProgrammingAssets": {
        "label":       "Non-current programming assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentProvisions": {
        "label":       "Non-current provisions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentProvisionsForEmployeeBenefits": {
        "label":       "Non-current provisions for employee benefits",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentReceivables": {
        "label":       "Trade and other non-current receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentReceivablesDueFromAssociates": {
        "label":       "Non-current receivables due from associates",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentReceivablesDueFromJointVentures": {
        "label":       "Non-current receivables due from joint ventures",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentReceivablesDueFromRelatedParties": {
        "label":       "Non-current receivables due from related parties",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentReceivablesFromContractsWithCustomers": {
        "label":       "Non-current receivables from contracts with customers",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentReceivablesFromRentalOfProperties": {
        "label":       "Non-current receivables from rental of properties",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentReceivablesFromSaleOfProperties": {
        "label":       "Non-current receivables from sale of properties",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentReceivablesFromTaxesOtherThanIncomeTax": {
        "label":       "Non-current receivables from taxes other than income tax",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentRecognisedAssetsDefinedBenefitPlan": {
        "label":       "Non-current net defined benefit asset",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentRecognisedLiabilitiesDefinedBenefitPlan": {
        "label":       "Non-current net defined benefit liability",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentRefundsProvision": {
        "label":       "Non-current refunds provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentRestrictedCashAndCashEquivalents": {
        "label":       "Non-current restricted cash and cash equivalents",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentRetentionPayables": {
        "label":       "Non-current retention payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentTradeReceivables": {
        "label":       "Non-current trade receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentValueAddedTaxPayables": {
        "label":       "Non-current value added tax payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NoncurrentValueAddedTaxReceivables": {
        "label":       "Non-current value added tax receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "NoncurrentWarrantLiability": {
        "label":       "Non-current warrant liability",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NonderivativeFinancialLiabilitiesUndiscountedCashFlows": {
        "label":       "Non-derivative financial liabilities, undiscounted cash flows",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NonsubscriptionCirculationRevenue": {
        "label":       "Nonsubscription circulation revenue",
        "balance":     "credit",
        "period_type": "duration",
    },
    "NotesAndDebenturesIssued": {
        "label":       "Notes and debentures issued",
        "balance":     "credit",
        "period_type": "instant",
    },
    "NotionalAmount": {
        "label":       "Notional amount",
        "balance":     "None",
        "period_type": "instant",
    },
    "OccupancyExpense": {
        "label":       "Occupancy expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OfficeEquipment": {
        "label":       "Office equipment",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OilAndGasAssets": {
        "label":       "Oil and gas assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OnerousContractsProvision": {
        "label":       "Onerous contracts provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OperatingExpense": {
        "label":       "Operating expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OperatingExpenseExcludingCostOfSales": {
        "label":       "Operating expense excluding cost of sales",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OperatingLeaseIncome": {
        "label":       "Operating lease income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OperatingProfitLossAndAllIncomeExpensesClassifiedInInvestingCategory": {
        "label":       "Operating profit loss and all income expenses classified in investing category",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OperatingProfitLossAndIncomeExpensesFromAllInvestmentsAccountedForUsingEquityMethod": {
        "label":       "Operating profit loss and income expenses from all investments accounted for using equity method",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OperatingProfitLossBeforeDepreciationAmortisationAndImpairmentsOperating": {
        "label":       "Operating profit loss before depreciation amortisation and impairments operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OperatingProfitLossOperating": {
        "label":       "Operating profit loss operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OriginalAssetsBeforeTransfer": {
        "label":       "Original assets before transfer",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherAdjustmentsForNoncashItems": {
        "label":       "Other adjustments for non-cash items",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherAdjustmentsForWhichCashEffectsAreInvestingOrFinancingCashFlow": {
        "label":       "Other adjustments for which cash effects are investing or financing cash flow",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherAdjustmentsToReconcileProfitLoss": {
        "label":       "Other adjustments to reconcile profit loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherAssets": {
        "label":       "Other assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherAssetsAmountContributedToFairValueOfPlanAssets": {
        "label":       "Other assets, amount contributed to fair value of plan assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherBorrowings": {
        "label":       "Other borrowings",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherCashAndCashEquivalents": {
        "label":       "Other cash and cash equivalents",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherCashPaymentsFromOperatingActivities": {
        "label":       "Other cash payments from operating activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherCashPaymentsToAcquireEquityOrDebtInstrumentsOfOtherEntitiesClassifiedAsInvestingActivities": {
        "label":       "Other cash payments to acquire equity or debt instruments of other entities, classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherCashPaymentsToAcquireInterestsInAssociatesAndJointVenturesClassifiedAsInvestingActivities": {
        "label":       "Other cash payments to acquire interests in associates and joint ventures classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherCashPaymentsToAcquireInterestsInJointVenturesClassifiedAsInvestingActivities": {
        "label":       "Other cash payments to acquire interests in joint ventures, classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherCashReceiptsFromOperatingActivities": {
        "label":       "Other cash receipts from operating activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherCashReceiptsFromSalesOfEquityOrDebtInstrumentsOfOtherEntitiesClassifiedAsInvestingActivities": {
        "label":       "Other cash receipts from sales of equity or debt instruments of other entities, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherCashReceiptsFromSalesOfInterestsInAssociatesAndJointVenturesClassifiedAsInvestingActivities": {
        "label":       "Other cash receipts from sales of interests in associates and joint ventures classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherCashReceiptsFromSalesOfInterestsInJointVenturesClassifiedAsInvestingActivities": {
        "label":       "Other cash receipts from sales of interests in joint ventures, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherComponentsOfDeferredTaxExpenseIncome": {
        "label":       "Other components of deferred tax expense income",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax": {
        "label":       "Other components of other comprehensive income that will be reclassified to profit or loss, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComponentsOfOtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax": {
        "label":       "Other components of other comprehensive income that will be reclassified to profit or loss, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComponentsOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax": {
        "label":       "Other components of other comprehensive income that will not be reclassified to profit or loss, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComponentsOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossNetOfTax": {
        "label":       "Other components of other comprehensive income that will not be reclassified to profit or loss, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncome": {
        "label":       "Other comprehensive income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeAttributableToNoncontrollingInterests": {
        "label":       "Other comprehensive income, attributable to non-controlling interests",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeAttributableToOwnersOfParent": {
        "label":       "Other comprehensive income, attributable to owners of parent",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTax": {
        "label":       "Other comprehensive income, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxAvailableforsaleFinancialAssets": {
        "label":       "Other comprehensive income before tax availableforsale financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxCashFlowHedges": {
        "label":       "Other comprehensive income, before tax, cash flow hedges",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxChangeInFairValueOfFinancialLiabilityAttributableToChangeInCreditRiskOfLiability": {
        "label":       "Other comprehensive income, before tax, change in fair value of financial liability attributable to change in credit risk of liability",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxChangeInValueOfForeignCurrencyBasisSpreads": {
        "label":       "Other comprehensive income, before tax, change in value of foreign currency basis spreads",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxChangeInValueOfForwardElementsOfForwardContracts": {
        "label":       "Other comprehensive income, before tax, change in value of forward elements of forward contracts",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxChangeInValueOfTimeValueOfOptions": {
        "label":       "Other comprehensive income, before tax, change in value of time value of options",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxExchangeDifferencesOnTranslation": {
        "label":       "Other comprehensive income, before tax, exchange differences on translation of foreign operations",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxExchangeDifferencesOnTranslationOfForeignOperationsAndHedgesOfNetInvestmentsInForeignOperations": {
        "label":       "Other comprehensive income, before tax, exchange differences on translation of foreign operations and hedges of net investments in foreign operations",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxExchangeDifferencesOnTranslationOtherThanTranslationOfForeignOperations": {
        "label":       "Other comprehensive income, before tax, exchange differences on translation, other than translation of foreign operations",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLoss": {
        "label":       "Other comprehensive income, before tax, finance income (expenses) from reinsurance contracts held excluded from profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Other comprehensive income, before tax, financial assets measured at fair value through other comprehensive income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxGainsLossesFromInvestmentsInEquityInstruments": {
        "label":       "Other comprehensive income, before tax, gains (losses) from investments in equity instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxGainsLossesFromInvestmentsInEquityInstrumentsDerecognisedDuringPeriod": {
        "label":       "Other comprehensive income, before tax, gains (losses) from investments in equity instruments derecognised during period",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxGainsLossesFromInvestmentsInEquityInstrumentsHeldAtEndOfReportingPeriod": {
        "label":       "Other comprehensive income, before tax, gains (losses) from investments in equity instruments held at end of reporting period",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxGainsLossesOnHedgingInstrumentsThatHedgeInvestmentsInEquityInstruments": {
        "label":       "Other comprehensive income, before tax, gains (losses) on hedging instruments that hedge investments in equity instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxGainsLossesOnRemeasurementsOfDefinedBenefitPlans": {
        "label":       "Other comprehensive income, before tax, gains (losses) on remeasurements of defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxGainsLossesOnRevaluation": {
        "label":       "Other comprehensive income, before tax, gains (losses) on revaluation of property, plant and equipment, right-of-use assets and intangible assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxHedgesOfNetInvestmentsInForeignOperations": {
        "label":       "Other comprehensive income, before tax, hedges of net investments in foreign operations",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLoss": {
        "label":       "Other comprehensive income, before tax, insurance finance income (expenses) from insurance contracts issued excluded from profit or loss that will be reclassified to profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillNotBeReclassifiedToProfitOrLoss": {
        "label":       "Other comprehensive income, before tax, insurance finance income (expenses) from insurance contracts issued excluded from profit or loss that will not be reclassified to profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxNetMovementInRegulatoryDeferralAccountBalancesRelatedToItemsThatWillBeReclassifiedToProfitOrLoss": {
        "label":       "Other comprehensive income, before tax, net movement in regulatory deferral account balances related to items that will be reclassified to profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeBeforeTaxNetMovementInRegulatoryDeferralAccountBalancesRelatedToItemsThatWillNotBeReclassifiedToProfitOrLoss": {
        "label":       "Other comprehensive income, before tax, net movement in regulatory deferral account balances related to items that will not be reclassified to profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxAvailableforsaleFinancialAssets": {
        "label":       "Other comprehensive income net of tax availableforsale financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxCashFlowHedges": {
        "label":       "Other comprehensive income, net of tax, cash flow hedges",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxChangeInFairValueOfFinancialLiabilityAttributableToChangeInCreditRiskOfLiability": {
        "label":       "Other comprehensive income, net of tax, change in fair value of financial liability attributable to change in credit risk of liability",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxChangeInValueOfForeignCurrencyBasisSpreads": {
        "label":       "Other comprehensive income, net of tax, change in value of foreign currency basis spreads",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxChangeInValueOfForeignCurrencyBasisSpreadsThatHedgeTimeperiodRelatedHedgedItems": {
        "label":       "Other comprehensive income, net of tax, change in value of foreign currency basis spreads that hedge time-period related hedged items",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxChangeInValueOfForeignCurrencyBasisSpreadsThatHedgeTransactionRelatedHedgedItems": {
        "label":       "Other comprehensive income, net of tax, change in value of foreign currency basis spreads that hedge transaction related hedged items",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxChangeInValueOfForwardElementsOfForwardContracts": {
        "label":       "Other comprehensive income, net of tax, change in value of forward elements of forward contracts",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxChangeInValueOfForwardElementsOfForwardContractsThatHedgeTimeperiodRelatedHedgedItems": {
        "label":       "Other comprehensive income, net of tax, change in value of forward elements of forward contracts that hedge time-period related hedged items",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxChangeInValueOfForwardElementsOfForwardContractsThatHedgeTransactionRelatedHedgedItems": {
        "label":       "Other comprehensive income, net of tax, change in value of forward elements of forward contracts that hedge transaction related hedged items",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxChangeInValueOfTimeValueOfOptions": {
        "label":       "Other comprehensive income, net of tax, change in value of time value of options",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxChangeInValueOfTimeValueOfOptionsThatHedgeTimeperiodRelatedHedgedItems": {
        "label":       "Other comprehensive income, net of tax, change in value of time value of options that hedge time-period related hedged items",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxChangeInValueOfTimeValueOfOptionsThatHedgeTransactionRelatedHedgedItems": {
        "label":       "Other comprehensive income, net of tax, change in value of time value of options that hedge transaction related hedged items",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxExchangeDifferencesOnTranslation": {
        "label":       "Other comprehensive income, net of tax, exchange differences on translation of foreign operations",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxExchangeDifferencesOnTranslationOfForeignOperationsAndHedgesOfNetInvestmentsInForeignOperations": {
        "label":       "Other comprehensive income, net of tax, exchange differences on translation of foreign operations and hedges of net investments in foreign operations",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxExchangeDifferencesOnTranslationOtherThanTranslationOfForeignOperations": {
        "label":       "Other comprehensive income, net of tax, exchange differences on translation, other than translation of foreign operations",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLoss": {
        "label":       "Other comprehensive income, net of tax, finance income (expenses) from reinsurance contracts held excluded from profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Other comprehensive income, net of tax, financial assets measured at fair value through other comprehensive income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxGainsLossesFromInvestmentsInEquityInstruments": {
        "label":       "Other comprehensive income, net of tax, gains (losses) from investments in equity instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxGainsLossesOnHedgingInstrumentsThatHedgeInvestmentsInEquityInstruments": {
        "label":       "Other comprehensive income, net of tax, gains (losses) on hedging instruments that hedge investments in equity instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxGainsLossesOnRemeasurementsOfDefinedBenefitPlans": {
        "label":       "Other comprehensive income, net of tax, gains (losses) on remeasurements of defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxGainsLossesOnRevaluation": {
        "label":       "Other comprehensive income, net of tax, gains (losses) on revaluation of property, plant and equipment, right-of-use assets and intangible assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxHedgesOfNetInvestmentsInForeignOperations": {
        "label":       "Other comprehensive income, net of tax, hedges of net investments in foreign operations",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLoss": {
        "label":       "Other comprehensive income, net of tax, insurance finance income (expenses) from insurance contracts issued excluded from profit or loss that will be reclassified to profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillNotBeReclassifiedToProfitOrLoss": {
        "label":       "Other comprehensive income, net of tax, insurance finance income (expenses) from insurance contracts issued excluded from profit or loss that will not be reclassified to profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxNetMovementInRegulatoryDeferralAccountBalancesRelatedToItemsThatWillBeReclassifiedToProfitOrLoss": {
        "label":       "Other comprehensive income, net of tax, net movement in regulatory deferral account balances related to items that will be reclassified to profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeNetOfTaxNetMovementInRegulatoryDeferralAccountBalancesRelatedToItemsThatWillNotBeReclassifiedToProfitOrLoss": {
        "label":       "Other comprehensive income, net of tax, net movement in regulatory deferral account balances related to items that will not be reclassified to profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossBeforeTax": {
        "label":       "Other comprehensive income that will be reclassified to profit or loss, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax": {
        "label":       "Other comprehensive income that will be reclassified to profit or loss, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax": {
        "label":       "Other comprehensive income that will not be reclassified to profit or loss, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossNetOfTax": {
        "label":       "Other comprehensive income that will not be reclassified to profit or loss, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherCurrentAssets": {
        "label":       "Other current assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherCurrentBorrowingsAndCurrentPortionOfOtherNoncurrentBorrowings": {
        "label":       "Other current borrowings and current portion of other non-current borrowings",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherCurrentFinancialAssets": {
        "label":       "Other current financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherCurrentFinancialLiabilities": {
        "label":       "Other current financial liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherCurrentLiabilities": {
        "label":       "Other current liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherCurrentNonfinancialAssets": {
        "label":       "Other current non-financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherCurrentNonfinancialLiabilities": {
        "label":       "Other current non-financial liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherCurrentPayables": {
        "label":       "Other current payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherCurrentReceivables": {
        "label":       "Other current receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherDebtInstrumentsHeld": {
        "label":       "Other debt instruments held",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherDecreasesAggregateDifferenceBetweenFairValueAtInitialRecognitionAndAmountDeterminedUsingValuationTechniqueYetToBeRecognised": {
        "label":       "Other decreases, aggregate difference between fair value at initial recognition and transaction price yet to be recognised in profit or loss",
        "balance":     "None",
        "period_type": "duration",
    },
    "OtherDifferencesToCashAndCashEquivalentsInStatementOfCashFlows": {
        "label":       "Other differences to cash and cash equivalents in statement of cash flows",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherEmployeeExpense": {
        "label":       "Other employee expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherEquityInterest": {
        "label":       "Other equity interest",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherExpenseByFunction": {
        "label":       "Other expense by function",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherExpenseByNature": {
        "label":       "Other expense by nature",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherFeeAndCommissionExpense": {
        "label":       "Other fee and commission expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherFeeAndCommissionIncome": {
        "label":       "Other fee and commission income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherFinanceCost": {
        "label":       "Other finance cost",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherFinanceIncome": {
        "label":       "Other finance income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherFinanceIncomeCost": {
        "label":       "Other finance income cost",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherFinancialAssets": {
        "label":       "Other financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherFinancialLiabilities": {
        "label":       "Other financial liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherGainsLosses": {
        "label":       "Other gains losses",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherIncome": {
        "label":       "Other income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherIncomeExpenseFromSubsidiariesJointlyControlledEntitiesAndAssociates": {
        "label":       "Other income expense from subsidiaries jointly controlled entities and associates",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherIncreasesAggregateDifferenceBetweenFairValueAtInitialRecognitionAndAmountDeterminedUsingValuationTechniqueYetToBeRecognised": {
        "label":       "Other increases, aggregate difference between fair value at initial recognition and transaction price yet to be recognised in profit or loss",
        "balance":     "None",
        "period_type": "duration",
    },
    "OtherInflowsOutflowsOfCashClassifiedAsFinancingActivities": {
        "label":       "Other inflows (outflows) of cash, classified as financing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherInflowsOutflowsOfCashClassifiedAsInvestingActivities": {
        "label":       "Other inflows (outflows) of cash, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherInflowsOutflowsOfCashClassifiedAsOperatingActivities": {
        "label":       "Other inflows (outflows) of cash, classified as operating activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherIntangibleAssets": {
        "label":       "Other intangible assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherInventories": {
        "label":       "Other current inventories",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherLiabilities": {
        "label":       "Other liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherLongtermBenefits": {
        "label":       "Other longterm benefits",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherLongtermProvisions": {
        "label":       "Other non-current provisions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherMaterialNoncashItems": {
        "label":       "Other material non-cash items",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherNoncashEffectsSupplierFinanceArrangements": {
        "label":       "Other non-cash effects, supplier finance arrangements",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherNoncurrentAssets": {
        "label":       "Other non-current assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherNoncurrentFinancialAssets": {
        "label":       "Other non-current financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherNoncurrentFinancialLiabilities": {
        "label":       "Other non-current financial liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherNoncurrentLiabilities": {
        "label":       "Other non-current liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherNoncurrentNonfinancialAssets": {
        "label":       "Other non-current non-financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherNoncurrentNonfinancialLiabilities": {
        "label":       "Other non-current non-financial liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherNoncurrentPayables": {
        "label":       "Other non-current payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherNoncurrentReceivables": {
        "label":       "Other non-current receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherNonfinancialAssets": {
        "label":       "Other non-financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherNonfinancialLiabilities": {
        "label":       "Other non-financial liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherOperatingExpensesOperating": {
        "label":       "Other operating expenses operating",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherOperatingIncomeExpense": {
        "label":       "Other operating income expense",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherOperatingIncomeOperating": {
        "label":       "Other operating income operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherPayables": {
        "label":       "Other payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherPropertyPlantAndEquipment": {
        "label":       "Other property, plant and equipment",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherProvisions": {
        "label":       "Other provisions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherReceivables": {
        "label":       "Other receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherRegulatoryDeferralAccountCreditBalances": {
        "label":       "Other regulatory deferral account credit balances",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherRegulatoryDeferralAccountDebitBalances": {
        "label":       "Other regulatory deferral account debit balances",
        "balance":     "debit",
        "period_type": "instant",
    },
    "OtherReserves": {
        "label":       "Other reserves",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherRevenue": {
        "label":       "Other revenue",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherReversalsOfProvisions": {
        "label":       "Other reversals of provisions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherShorttermEmployeeBenefits": {
        "label":       "Other shortterm employee benefits",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherShorttermProvisions": {
        "label":       "Other current provisions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherTangibleOrIntangibleAssetsTransferred": {
        "label":       "Other tangible or intangible assets transferred",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OtherTaxEffectsForReconciliationBetweenAccountingProfitAndTaxExpenseIncome": {
        "label":       "Other tax effects for reconciliation between accounting profit and tax expense (income)",
        "balance":     "debit",
        "period_type": "duration",
    },
    "OtherTradingIncomeExpense": {
        "label":       "Other trading income expense",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OtherWorkPerformedByEntityAndCapitalised": {
        "label":       "Other work performed by entity and capitalised",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OutflowsOfCashFromInvestingActivities": {
        "label":       "Outflows of cash from investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "OutstandingCommitmentsMadeByEntityRelatedPartyTransactions": {
        "label":       "Outstanding commitments made by entity, related party transactions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OutstandingCommitmentsMadeOnBehalfOfEntityRelatedPartyTransactions": {
        "label":       "Outstanding commitments made on behalf of entity, related party transactions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "OwneroccupiedPropertyMeasuredUsingInvestmentPropertyFairValueModel": {
        "label":       "Owner-occupied property measured using investment property fair value model",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ParticipationInDefinedBenefitPlanThatSharesRisksBetweenGroupEntitiesRelatedPartyTransactions": {
        "label":       "Participation in defined benefit plan that shares risks between group entities, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "PastServiceCostAndGainsLossesArisingFromSettlementsNetDefinedBenefitLiabilityAsset": {
        "label":       "Increase (decrease) in net defined benefit liability (asset) resulting from past service cost and losses (gains) arising from settlements",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PastServiceCostAndLossesGainsArisingFromSettlementsDefinedBenefitPlans": {
        "label":       "Past service cost and losses gains arising from settlements defined benefit plans",
        "balance":     "debit",
        "period_type": "duration",
    },
    "PastServiceCostDefinedBenefitPlans": {
        "label":       "Past service cost defined benefit plans",
        "balance":     "debit",
        "period_type": "duration",
    },
    "PastServiceCostNetDefinedBenefitLiabilityAsset": {
        "label":       "Increase (decrease) in net defined benefit liability (asset) resulting from past service cost",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PayablesForPurchaseOfEnergy": {
        "label":       "Payables for purchase of energy",
        "balance":     "credit",
        "period_type": "instant",
    },
    "PayablesForPurchaseOfNoncurrentAssets": {
        "label":       "Payables for purchase of non-current assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "PayablesOnSocialSecurityAndTaxesOtherThanIncomeTax": {
        "label":       "Payables on social security and taxes other than income tax",
        "balance":     "credit",
        "period_type": "instant",
    },
    "PaymentsForDebtIssueCosts": {
        "label":       "Payments for debt issue costs",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsForDevelopmentProjectExpenditure": {
        "label":       "Payments for development project expenditure",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsForExplorationAndEvaluationExpenses": {
        "label":       "Payments for exploration and evaluation expenses",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsForShareIssueCosts": {
        "label":       "Payments for share issue costs",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsFromChangesInOwnershipInterestsInSubsidiaries": {
        "label":       "Payments from changes in ownership interests in subsidiaries that do not result in loss of control",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsFromContractsHeldForDealingOrTradingPurpose": {
        "label":       "Payments from contracts held for dealing or trading purpose",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsFromPlanNetDefinedBenefitLiabilityAsset": {
        "label":       "Decrease (increase) in net defined benefit liability (asset) resulting from payments from plan",
        "balance":     "debit",
        "period_type": "duration",
    },
    "PaymentsInRespectOfSettlementsNetDefinedBenefitLiabilityAsset": {
        "label":       "Decrease (increase) in net defined benefit liability (asset) resulting from payments in respect of settlements",
        "balance":     "debit",
        "period_type": "duration",
    },
    "PaymentsInRespectOfSettlementsReimbursementRights": {
        "label":       "Decrease in reimbursement rights related to defined benefit obligation, resulting from payments in respect of settlements",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsOfLeaseLiabilitiesClassifiedAsFinancingActivities": {
        "label":       "Payments of lease liabilities, classified as financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsOfOtherEquityInstruments": {
        "label":       "Payments of other equity instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsRelatingToRoyaltiesFeesAndCommissions": {
        "label":       "Payments relating to royalties, fees and commissions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsToAcquireOrRedeemEntitysShares": {
        "label":       "Payments to acquire or redeem entity's shares",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsToAndOnBehalfOfEmployees": {
        "label":       "Payments to and on behalf of employees",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsToManufactureOrAcquireAssetsHeldForRentalToOthersAndSubsequentlyHeldForSale": {
        "label":       "Payments to manufacture or acquire assets held for rental to others and subsequently held for sale",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsToSuppliersForGoodsAndServices": {
        "label":       "Payments to suppliers for goods and services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PaymentsToSuppliersForGoodsAndServicesAndToAndOnBehalfOfEmployees": {
        "label":       "Payments to suppliers for goods and services and to and on behalf of employees",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PlanAssetsAtFairValue": {
        "label":       "Plan assets, at fair value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PortfolioAndOtherManagementFeeIncome": {
        "label":       "Portfolio and other management fee income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PortionOfConsiderationPaidReceivedConsistingOfCashAndCashEquivalents": {
        "label":       "Portion of consideration paid (received) consisting of cash and cash equivalents",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PortionOfGainsLossesRecognisedWhenControlOfSubsidiaryIsLostAttributableToDerecognisingRegulatoryDeferralAccountBalancesInFormerSubsidiary": {
        "label":       "Portion of gains losses recognised when control of subsidiary is lost attributable to derecognising regulatory deferral account balances in former subsidiary",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PortionOfGainsLossesRecognisedWhenControlOfSubsidiaryIsLostAttributableToRecognisingInvestmentRetainedInFormerSubsidiary": {
        "label":       "Portion of gains (losses) recognised when control of subsidiary is lost, attributable to recognising investment retained in former subsidiary",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PostemploymentBenefitExpenseDefinedBenefitPlans": {
        "label":       "Postemployment benefit expense defined benefit plans",
        "balance":     "debit",
        "period_type": "duration",
    },
    "PostemploymentBenefitExpenseDefinedContributionPlans": {
        "label":       "Postemployment benefit expense defined contribution plans",
        "balance":     "debit",
        "period_type": "duration",
    },
    "PostemploymentBenefitExpenseInProfitOrLoss": {
        "label":       "Postemployment benefit expense in profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "Prepayments": {
        "label":       "Prepayments",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PrepaymentsAndAccruedIncomeIncludingContractAssets": {
        "label":       "Prepayments and accrued income including contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PrepaymentsAndAccruedIncomeOtherThanContractAssets": {
        "label":       "Prepayments and accrued income other than contract assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PricesSpecifiedInForwardAgreementsToPurchaseFinancialAssetsForCash": {
        "label":       "Prices specified in forward agreements to purchase financial assets for cash",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ProceedsFromBorrowingsClassifiedAsFinancingActivities": {
        "label":       "Proceeds from borrowings, classified as financing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromChangesInOwnershipInterestsInSubsidiaries": {
        "label":       "Proceeds from changes in ownership interests in subsidiaries that do not result in loss of control",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromContributionsOfNoncontrollingInterests": {
        "label":       "Proceeds from contributions of non-controlling interests",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromCurrentBorrowings": {
        "label":       "Proceeds from current borrowings",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromDisposalOfExplorationAndEvaluationAssets": {
        "label":       "Proceeds from disposal of exploration and evaluation assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromDisposalOfMiningAssets": {
        "label":       "Proceeds from disposal of mining assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromDisposalOfNoncurrentAssetsOrDisposalGroupsClassifiedAsHeldForSaleAndDiscontinuedOperations": {
        "label":       "Proceeds from disposal of non-current assets or disposal groups classified as held for sale and discontinued operations",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromDisposalOfOilAndGasAssets": {
        "label":       "Proceeds from disposal of oil and gas assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromDisposalOrMaturityOfAvailableforsaleFinancialAssets": {
        "label":       "Proceeds from disposal or maturity of available-for-sale financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromDisposalsOfPropertyPlantAndEquipmentIntangibleAssetsOtherThanGoodwillInvestmentPropertyAndOtherNoncurrentAssets": {
        "label":       "Proceeds from disposals of property, plant and equipment, intangible assets other than goodwill, investment property and other non-current assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromExerciseOfOptions": {
        "label":       "Proceeds from exercise of options",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromExerciseOfWarrants": {
        "label":       "Proceeds from exercise of warrants",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromGovernmentGrantsClassifiedAsFinancingActivities": {
        "label":       "Proceeds from government grants, classified as financing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromGovernmentGrantsClassifiedAsInvestingActivities": {
        "label":       "Proceeds from government grants, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromIssueOfBondsNotesAndDebentures": {
        "label":       "Proceeds from issue of bonds, notes and debentures",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromIssueOfOrdinaryShares": {
        "label":       "Proceeds from issue of ordinary shares",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromIssueOfPreferenceShares": {
        "label":       "Proceeds from issue of preference shares",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromIssueOfRegulatoryCapitalEquity": {
        "label":       "Proceeds from issue of regulatory capital, equity",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromIssueOfRegulatoryCapitalFinancialLiabilities": {
        "label":       "Proceeds from issue of regulatory capital, financial liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromIssueOfSubordinatedLiabilities": {
        "label":       "Proceeds from issue of subordinated liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromIssuingOtherEquityInstruments": {
        "label":       "Proceeds from issuing other equity instruments",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromIssuingShares": {
        "label":       "Proceeds from issuing shares",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromNoncurrentBorrowings": {
        "label":       "Proceeds from non-current borrowings",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromOtherLongtermAssetsClassifiedAsInvestingActivities": {
        "label":       "Proceeds from sales of other long-term assets, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromSaleOrIssueOfTreasuryShares": {
        "label":       "Proceeds from sale or issue of treasury shares",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromSalesOfBiologicalAssets": {
        "label":       "Proceeds from sales of biological assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromSalesOfIntangibleAssetsClassifiedAsInvestingActivities": {
        "label":       "Proceeds from sales of intangible assets, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromSalesOfInterestsInAssociates": {
        "label":       "Proceeds from sales of interests in associates",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromSalesOfInvestmentProperty": {
        "label":       "Proceeds from sales of investment property",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromSalesOfInvestmentsAccountedForUsingEquityMethod": {
        "label":       "Proceeds from sales of investments accounted for using equity method",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromSalesOfInvestmentsOtherThanInvestmentsAccountedForUsingEquityMethod": {
        "label":       "Proceeds from sales of investments other than investments accounted for using equity method",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromSalesOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities": {
        "label":       "Proceeds from sales of property, plant and equipment, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromSalesOfUnusedNaturedependentElectricity": {
        "label":       "Proceeds from sales of unused nature-dependent electricity",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromSalesOrMaturityOfFinancialAssetsMeasuredAtAmortisedCostClassifiedAsInvestingActivities": {
        "label":       "Proceeds from sales or maturity of financial assets measured at amortised cost, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromSalesOrMaturityOfFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeClassifiedAsInvestingActivities": {
        "label":       "Proceeds from sales or maturity of financial assets measured at fair value through other comprehensive income, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromSalesOrMaturityOfFinancialAssetsMeasuredAtFairValueThroughProfitOrLossClassifiedAsInvestingActivities": {
        "label":       "Proceeds from sales or maturity of financial assets measured at fair value through profit or loss, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromSalesOrMaturityOfFinancialInstrumentsClassifiedAsInvestingActivities": {
        "label":       "Proceeds from sales or maturity of financial instruments, classified as investing activities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsFromTransferActivity": {
        "label":       "Proceeds from transfer activity during period representing greatest transfer activity",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProceedsIncludedInProfitOrLossInAccordanceWithParagraph20AOfIAS16ThatRelateToItemsProducedThatAreNotOutputOfEntitysOrdinaryActivities": {
        "label":       "Proceeds included in profit or loss in accordance with paragraph20 a ofias16 that relate to items produced that are not output of entitys ordinary activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProductionSupplies": {
        "label":       "Current production supplies",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ProfessionalFeesExpense": {
        "label":       "Professional fees expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProfitLoss": {
        "label":       "Profit (loss)",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossAttributableToNoncontrollingInterests": {
        "label":       "Profit (loss), attributable to non-controlling interests",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossAttributableToOrdinaryEquityHoldersOfParentEntity": {
        "label":       "Profit (loss), attributable to ordinary equity holders of parent entity, used in calculating basic earnings per share",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossAttributableToOrdinaryEquityHoldersOfParentEntityIncludingDilutiveEffects": {
        "label":       "Profit (loss), attributable to ordinary equity holders of parent entity, used in calculating diluted earnings per share",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossAttributableToOwnersOfParent": {
        "label":       "Profit (loss), attributable to owners of parent",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossAttributableToParticipatingEquityInstrumentsOtherThanOrdinarySharesUsedInCalculatingBasicEarningsLossPerInstrument": {
        "label":       "Profit (loss) attributable to participating equity instruments other than ordinary shares, used in calculating basic earnings (loss) per instrument",
        "balance":     "None",
        "period_type": "duration",
    },
    "ProfitLossAttributableToParticipatingEquityInstrumentsOtherThanOrdinarySharesUsedInCalculatingDilutedEarningsLossPerInstrument": {
        "label":       "Profit (loss) attributable to participating equity instruments other than ordinary shares, used in calculating diluted earnings (loss) per instrument",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossBeforeFinancingAndIncomeTaxes": {
        "label":       "Profit loss before financing and income taxes",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossBeforeTax": {
        "label":       "Profit loss before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossFromContinuingOperations": {
        "label":       "Profit (loss) from continuing operations",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossFromContinuingOperationsAttributableToNoncontrollingInterests": {
        "label":       "Profit (loss) from continuing operations attributable to non-controlling interests",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossFromContinuingOperationsAttributableToOrdinaryEquityHoldersOfParentEntity": {
        "label":       "Profit (loss) from continuing operations attributable to ordinary equity holders of parent entity, used in calculating basic earnings per share",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossFromContinuingOperationsAttributableToOrdinaryEquityHoldersOfParentEntityIncludingDilutiveEffects": {
        "label":       "Profit (loss) from continuing operations attributable to ordinary equity holders of parent entity, used in calculating diluted earnings per share",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossFromContinuingOperationsAttributableToParticipatingEquityInstrumentsOtherThanOrdinarySharesUsedInCalculatingBasicEarningsLossPerInstrument": {
        "label":       "Profit (loss) from continuing operations attributable to participating equity instruments other than ordinary shares, used in calculating basic earnings (loss) per instrument",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossFromContinuingOperationsAttributableToParticipatingEquityInstrumentsOtherThanOrdinarySharesUsedInCalculatingDilutedEarningsLossPerInstrument": {
        "label":       "Profit (loss) from continuing operations attributable to participating equity instruments other than ordinary shares, used in calculating diluted earnings (loss) per instrument",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossFromDiscontinuedOperations": {
        "label":       "Profit loss from discontinued operations",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossFromDiscontinuedOperationsAttributableToNoncontrollingInterests": {
        "label":       "Profit (loss) from discontinued operations attributable to non-controlling interests",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossFromDiscontinuedOperationsAttributableToOrdinaryEquityHoldersOfParentEntity": {
        "label":       "Profit (loss) from discontinued operations attributable to ordinary equity holders of parent entity, used in calculating basic earnings per share",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossFromDiscontinuedOperationsAttributableToOrdinaryEquityHoldersOfParentEntityIncludingDilutiveEffects": {
        "label":       "Profit (loss) from discontinued operations attributable to ordinary equity holders of parent entity, used in calculating diluted earnings per share",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossFromDiscontinuedOperationsAttributableToParticipatingEquityInstrumentsOtherThanOrdinarySharesUsedInCalculatingBasicEarningsLossPerInstrument": {
        "label":       "Profit (loss) from discontinued operations attributable to participating equity instruments other than ordinary shares, used in calculating basic earnings (loss) per instrument",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossFromDiscontinuedOperationsAttributableToParticipatingEquityInstrumentsOtherThanOrdinarySharesUsedInCalculatingDilutedEarningsLossPerInstrument": {
        "label":       "Profit (loss) from discontinued operations attributable to participating equity instruments other than ordinary shares, used in calculating diluted earnings (loss) per instrument",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossFromOperatingActivities": {
        "label":       "Profit loss from operating activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossIncludingNetMovementInRegulatoryDeferralAccountBalancesRelatedToProfitOrLossAndNetMovementInRelatedDeferredTax": {
        "label":       "Profit (loss), including net movement in regulatory deferral account balances related to profit or loss and net movement in related deferred tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossIncludingNetMovementInRegulatoryDeferralAccountBalancesRelatedToProfitOrLossAndNetMovementInRelatedDeferredTaxAttributableToNoncontrollingInterests": {
        "label":       "Profit (loss), including net movement in regulatory deferral account balances related to profit or loss and net movement in related deferred tax, attributable to non-controlling interests",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossIncludingNetMovementInRegulatoryDeferralAccountBalancesRelatedToProfitOrLossAndNetMovementInRelatedDeferredTaxAttributableToOwnersOfParent": {
        "label":       "Profit (loss), including net movement in regulatory deferral account balances related to profit or loss and net movement in related deferred tax, attributable to owners of parent",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossOfAcquiree": {
        "label":       "Profit (loss) of acquiree since acquisition date",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossOfCombinedEntity": {
        "label":       "Profit (loss) of combined entity as if combination occurred at beginning of period",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossRecognisedOnExchangingConstructionServicesForFinancialAsset2011": {
        "label":       "Profit (loss) recognised on exchanging construction services for financial asset",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitLossRecognisedOnExchangingConstructionServicesForIntangibleAsset2011": {
        "label":       "Profit (loss) recognised on exchanging construction services for intangible asset",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProfitsLossesOnDisposalOfInvestmentsAndChangesInValueOfInvestments": {
        "label":       "Profit (loss) on disposal of investments and changes in value of investments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ProgrammingAssets": {
        "label":       "Programming assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyAmountContributedToFairValueOfPlanAssets": {
        "label":       "Real estate, amount contributed to fair value of plan assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyDevelopmentAndProjectManagementExpense": {
        "label":       "Property development and project management expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "PropertyDevelopmentAndProjectManagementIncome": {
        "label":       "Property development and project management income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PropertyIntendedForSaleInOrdinaryCourseOfBusiness": {
        "label":       "Property intended for sale in ordinary course of business",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyManagementExpense": {
        "label":       "Property management expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "PropertyPlantAndEquipment": {
        "label":       "Property, plant and equipment",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyPlantAndEquipmentCarryingAmountAtCostOfRevaluedAssets": {
        "label":       "Property, plant and equipment, revalued assets, at cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyPlantAndEquipmentCarryingAmountOfAssetsRetiredFromActiveUse": {
        "label":       "Property, plant and equipment, assets retired from active use and not classified as held for sale",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyPlantAndEquipmentCarryingAmountOfRevaluedAssets": {
        "label":       "Property, plant and equipment, revalued assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyPlantAndEquipmentExpendituresRecognisedForConstructions": {
        "label":       "Property, plant and equipment, expenditures recognised in course of its construction",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyPlantAndEquipmentFairValueUsedAsDeemedCost": {
        "label":       "Property, plant and equipment fair value used as deemed cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyPlantAndEquipmentGrossCarryingAmountFullyDepreciated": {
        "label":       "Property, plant and equipment, gross carrying amount of fully depreciated assets still in use",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Property, plant and equipment including right-of-use assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyPlantAndEquipmentPledgedAsSecurity": {
        "label":       "Property, plant and equipment, pledged as security",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyPlantAndEquipmentRecognisedAsOfAcquisitionDate": {
        "label":       "Property, plant and equipment recognised as of acquisition date",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyPlantAndEquipmentRestrictionsOnTitle": {
        "label":       "Property, plant and equipment, restrictions on title",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyPlantAndEquipmentRevaluationSurplus": {
        "label":       "Property, plant and equipment, revaluation surplus",
        "balance":     "credit",
        "period_type": "instant",
    },
    "PropertyPlantAndEquipmentTemporarilyIdle": {
        "label":       "Property, plant and equipment, temporarily idle",
        "balance":     "debit",
        "period_type": "instant",
    },
    "PropertyServiceChargeExpense": {
        "label":       "Property service charge expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "PropertyServiceChargeIncome": {
        "label":       "Property service charge income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PropertyServiceChargeIncomeExpense": {
        "label":       "Property service charge income expense",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PropertyTaxExpense": {
        "label":       "Property tax expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ProvisionForDecommissioningRestorationAndRehabilitationCosts": {
        "label":       "Provision for decommissioning, restoration and rehabilitation costs",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ProvisionOfGuaranteesOrCollateralByEntityRelatedPartyTransactions": {
        "label":       "Provision of guarantees or collateral by entity, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "ProvisionOfGuaranteesOrCollateralToEntityRelatedPartyTransactions": {
        "label":       "Provision of guarantees or collateral to entity, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "ProvisionUsedOtherProvisions": {
        "label":       "Provision used, other provisions",
        "balance":     "debit",
        "period_type": "duration",
    },
    "Provisions": {
        "label":       "Provisions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ProvisionsForDoubtfulDebtsRelatedToOutstandingBalancesOfRelatedPartyTransaction": {
        "label":       "Provisions for doubtful debts related to outstanding balances of related party transaction",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ProvisionsForEmployeeBenefits": {
        "label":       "Provisions for employee benefits",
        "balance":     "credit",
        "period_type": "instant",
    },
    "PurchaseOfAvailableforsaleFinancialAssets": {
        "label":       "Purchase of available-for-sale financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfBiologicalAssets": {
        "label":       "Purchase of biological assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfExplorationAndEvaluationAssets": {
        "label":       "Purchase of exploration and evaluation assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfFinancialAssetsMeasuredAtAmortisedCostClassifiedAsInvestingActivities": {
        "label":       "Purchase of financial assets measured at amortised cost, classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeClassifiedAsInvestingActivities": {
        "label":       "Purchase of financial assets measured at fair value through other comprehensive income, classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfFinancialAssetsMeasuredAtFairValueThroughProfitOrLossClassifiedAsInvestingActivities": {
        "label":       "Purchase of financial assets measured at fair value through profit or loss, classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfFinancialInstrumentsClassifiedAsInvestingActivities": {
        "label":       "Purchase of financial instruments, classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities": {
        "label":       "Purchase of intangible assets, classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfInterestsInAssociates": {
        "label":       "Purchase of interests in associates",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfInterestsInInvestmentsAccountedForUsingEquityMethod": {
        "label":       "Purchase of interests in investments accounted for using equity method",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfInvestmentProperty": {
        "label":       "Purchase of investment property",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfInvestmentsOtherThanInvestmentsAccountedForUsingEquityMethod": {
        "label":       "Purchase of investments other than investments accounted for using equity method",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfMiningAssets": {
        "label":       "Purchase of mining assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfOilAndGasAssets": {
        "label":       "Purchase of oil and gas assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfOtherLongtermAssetsClassifiedAsInvestingActivities": {
        "label":       "Purchase of other long-term assets, classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities": {
        "label":       "Purchase of property, plant and equipment, classified as investing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfPropertyPlantAndEquipmentIntangibleAssetsOtherThanGoodwillInvestmentPropertyAndOtherNoncurrentAssets": {
        "label":       "Purchase of property, plant and equipment, intangible assets other than goodwill, investment property and other non-current assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchaseOfTreasuryShares": {
        "label":       "Purchase of treasury shares",
        "balance":     "debit",
        "period_type": "duration",
    },
    "PurchasesFairValueMeasurementAssets": {
        "label":       "Purchases, fair value measurement, assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "PurchasesFairValueMeasurementEntitysOwnEquityInstruments": {
        "label":       "Purchases, fair value measurement, entity's own equity instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchasesFairValueMeasurementLiabilities": {
        "label":       "Purchases, fair value measurement, liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchasesOfElectricityMadeToOffsetSalesOfUnusedNaturedependentElectricity": {
        "label":       "Purchases of electricity made to offset sales of unused nature-dependent electricity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchasesOfGoodsRelatedPartyTransactions": {
        "label":       "Purchases of goods, related party transactions",
        "balance":     "debit",
        "period_type": "duration",
    },
    "PurchasesOfNaturedependentElectricity": {
        "label":       "Purchases of nature-dependent electricity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "PurchasesOfPropertyAndOtherAssetsRelatedPartyTransactions": {
        "label":       "Purchases of property and other assets, related party transactions",
        "balance":     "debit",
        "period_type": "duration",
    },
    "PurchasesOfUnusedNaturedependentElectricity": {
        "label":       "Purchases of unused nature-dependent electricity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "QualifyingInsurancePoliciesAmountContributedToFairValueOfPlanAssets": {
        "label":       "Qualifying insurance policies, amount contributed to fair value of plan assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "RatedCreditExposures": {
        "label":       "Rated credit exposures",
        "balance":     "None",
        "period_type": "instant",
    },
    "RawMaterials": {
        "label":       "Current raw materials",
        "balance":     "debit",
        "period_type": "instant",
    },
    "RawMaterialsAndConsumablesUsed": {
        "label":       "Raw materials and consumables used",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReceiptsFromContractsHeldForDealingOrTradingPurpose": {
        "label":       "Receipts from contracts held for dealing or trading purposes",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReceiptsFromRentsAndSubsequentSalesOfSuchAssets": {
        "label":       "Receipts from rents and subsequent sales of assets held for rental to others and subsequently held for sale",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReceiptsFromRoyaltiesFeesCommissionsAndOtherRevenue": {
        "label":       "Receipts from royalties, fees, commissions and other revenue",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReceiptsFromSalesOfGoodsAndRenderingOfServices": {
        "label":       "Receipts from sales of goods and rendering of services",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReceivablesDueFromAssociates": {
        "label":       "Receivables due from associates",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ReceivablesDueFromJointVentures": {
        "label":       "Receivables due from joint ventures",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ReceivablesFromContractsWithCustomers": {
        "label":       "Receivables from contracts with customers",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ReceivablesFromRentalOfProperties": {
        "label":       "Receivables from rental of properties",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ReceivablesFromSaleOfProperties": {
        "label":       "Receivables from sale of properties",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ReceivablesFromTaxesOtherThanIncomeTax": {
        "label":       "Receivables from taxes other than income tax",
        "balance":     "debit",
        "period_type": "instant",
    },
    "RecipesFormulaeModelsDesignsAndPrototypes": {
        "label":       "Recipes, formulae, models, designs and prototypes",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ReclassificationAdjustmentsOnAvailableforsaleFinancialAssetsBeforeTax": {
        "label":       "Reclassification adjustments on available-for-sale financial assets, before tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnAvailableforsaleFinancialAssetsNetOfTax": {
        "label":       "Reclassification adjustments on available-for-sale financial assets, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnCashFlowHedgesBeforeTax": {
        "label":       "Reclassification adjustments on cash flow hedges, before tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnCashFlowHedgesForWhichHedgedFutureCashFlowsAreNoLongerExpectedToOccurNetOfTax": {
        "label":       "Reclassification adjustments on cash flow hedges for which hedged future cash flows are no longer expected to occur, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnCashFlowHedgesForWhichHedgedItemAffectedProfitOrLossNetOfTax": {
        "label":       "Reclassification adjustments on cash flow hedges for which hedged item affected profit or loss, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnCashFlowHedgesForWhichReserveOfCashFlowHedgesWillNotBeRecoveredInOneOrMoreFuturePeriodsNetOfTax": {
        "label":       "Reclassification adjustments on cash flow hedges for which reserve of cash flow hedges will not be recovered in one or more future periods, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnCashFlowHedgesNetOfTax": {
        "label":       "Reclassification adjustments on cash flow hedges, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnChangeInValueOfForeignCurrencyBasisSpreadsBeforeTax": {
        "label":       "Reclassification adjustments on change in value of foreign currency basis spreads, before tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnChangeInValueOfForeignCurrencyBasisSpreadsNetOfTax": {
        "label":       "Reclassification adjustments on change in value of foreign currency basis spreads, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnChangeInValueOfForwardElementsOfForwardContractsBeforeTax": {
        "label":       "Reclassification adjustments on change in value of forward elements of forward contracts, before tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnChangeInValueOfForwardElementsOfForwardContractsNetOfTax": {
        "label":       "Reclassification adjustments on change in value of forward elements of forward contracts, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnChangeInValueOfTimeValueOfOptionsBeforeTax": {
        "label":       "Reclassification adjustments on change in value of time value of options, before tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnChangeInValueOfTimeValueOfOptionsNetOfTax": {
        "label":       "Reclassification adjustments on change in value of time value of options, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnExchangeDifferencesOnTranslationBeforeTax": {
        "label":       "Reclassification adjustments on exchange differences on translation of foreign operations, before tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnExchangeDifferencesOnTranslationNetOfTax": {
        "label":       "Reclassification adjustments on exchange differences on translation of foreign operations, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLossBeforeTax": {
        "label":       "Reclassification adjustments on finance income (expenses) from reinsurance contracts held excluded from profit or loss, before tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLossNetOfTax": {
        "label":       "Reclassification adjustments on finance income (expenses) from reinsurance contracts held excluded from profit or loss, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeBeforeTax": {
        "label":       "Reclassification adjustments on financial assets measured at fair value through other comprehensive income, before tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeNetOfTax": {
        "label":       "Reclassification adjustments on financial assets measured at fair value through other comprehensive income, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnHedgesOfNetInvestmentsInForeignOperationsBeforeTax": {
        "label":       "Reclassification adjustments on hedges of net investments in foreign operations, before tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnHedgesOfNetInvestmentsInForeignOperationsNetOfTax": {
        "label":       "Reclassification adjustments on hedges of net investments in foreign operations, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossBeforeTax": {
        "label":       "Reclassification adjustments on insurance finance income (expenses) from insurance contracts issued excluded from profit or loss, before tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossNetOfTax": {
        "label":       "Reclassification adjustments on insurance finance income (expenses) from insurance contracts issued excluded from profit or loss, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnNetMovementInRegulatoryDeferralAccountBalancesBeforeTax": {
        "label":       "Reclassification adjustments on net movement in regulatory deferral account balances, before tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationAdjustmentsOnNetMovementInRegulatoryDeferralAccountBalancesNetOfTax": {
        "label":       "Reclassification adjustments on net movement in regulatory deferral account balances, net of tax",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationIntoAvailableforsaleFinancialAssets": {
        "label":       "Reclassification into available-for-sale financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationIntoFinancialAssetsAtFairValueThroughProfitOrLoss": {
        "label":       "Reclassification into financial assets at fair value through profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationIntoHeldtomaturityInvestments": {
        "label":       "Reclassification into held-to-maturity investments",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationIntoLoansAndReceivables": {
        "label":       "Reclassification into loans and receivables",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReclassificationOfFinancialAssetsOutOfMeasuredAtAmortisedCostIntoMeasuredAtFairValue": {
        "label":       "Reclassification of financial assets out of measured at amortised cost into measured at fair value through profit or loss",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReclassificationOfFinancialAssetsOutOfMeasuredAtAmortisedCostIntoMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Reclassification of financial assets out of measured at amortised cost into measured at fair value through other comprehensive income",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReclassificationOfFinancialAssetsOutOfMeasuredAtFairValueIntoMeasuredAtAmortisedCost": {
        "label":       "Reclassification of financial assets out of measured at fair value through profit or loss into measured at amortised cost",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReclassificationOfFinancialAssetsOutOfMeasuredAtFairValueThroughOtherComprehensiveIncomeIntoMeasuredAtAmortisedCost": {
        "label":       "Reclassification of financial assets out of measured at fair value through other comprehensive income into measured at amortised cost",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReclassificationOfFinancialAssetsOutOfMeasuredAtFairValueThroughOtherComprehensiveIncomeIntoMeasuredAtFairValueThroughProfitOrLoss": {
        "label":       "Reclassification of financial assets out of measured at fair value through other comprehensive income into measured at fair value through profit or loss",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReclassificationOfFinancialAssetsOutOfMeasuredAtFairValueThroughProfitOrLossIntoMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Reclassification of financial assets out of measured at fair value through profit or loss into measured at fair value through other comprehensive income",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReclassificationOutOfAvailableforsaleFinancialAssets": {
        "label":       "Reclassification out of available-for-sale financial assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ReclassificationOutOfFinancialAssetsAtFairValueThroughProfitOrLoss": {
        "label":       "Reclassification out of financial assets at fair value through profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ReclassificationOutOfHeldtomaturityInvestments": {
        "label":       "Reclassification out of held-to-maturity investments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ReclassificationOutOfLoansAndReceivables": {
        "label":       "Reclassification out of loans and receivables",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RecognisedAssetsDefinedBenefitPlan": {
        "label":       "Net defined benefit asset",
        "balance":     "debit",
        "period_type": "instant",
    },
    "RecognisedAssetsRepresentingContinuingInvolvementInDerecognisedFinancialAssets": {
        "label":       "Recognised assets representing continuing involvement in derecognised financial assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "RecognisedLiabilitiesDefinedBenefitPlan": {
        "label":       "Net defined benefit liability",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RecognisedLiabilitiesRepresentingContinuingInvolvementInDerecognisedFinancialAssets": {
        "label":       "Recognised liabilities representing continuing involvement in derecognised financial assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RecoverableAmountOfAssetOrCashgeneratingUnit": {
        "label":       "Recoverable amount of asset or cash-generating unit",
        "balance":     "debit",
        "period_type": "instant",
    },
    "RecoveriesOnLoansPreviouslyWrittenOff": {
        "label":       "Recoveries on loans previously written off",
        "balance":     "debit",
        "period_type": "duration",
    },
    "RedesignatedFinancialAssetAtFairValueThroughProfitOrLoss": {
        "label":       "Redesignated financial asset as at fair value through profit or loss",
        "balance":     "debit",
        "period_type": "instant",
    },
    "RedesignatedFinancialLiabilityAtFairValueThroughProfitOrLoss": {
        "label":       "Redesignated financial liability as at fair value through profit or loss",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReductionOfIssuedCapital": {
        "label":       "Reduction of issued capital",
        "balance":     "debit",
        "period_type": "duration",
    },
    "RefundsProvision": {
        "label":       "Refunds provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RegulatoryDeferralAccountCreditBalances": {
        "label":       "Regulatory deferral account credit balances",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RegulatoryDeferralAccountCreditBalancesAndRelatedDeferredTaxLiability": {
        "label":       "Regulatory deferral account credit balances and related deferred tax liability",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RegulatoryDeferralAccountCreditBalancesDirectlyRelatedToDisposalGroup": {
        "label":       "Regulatory deferral account credit balances directly related to disposal group",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RegulatoryDeferralAccountDebitBalances": {
        "label":       "Regulatory deferral account debit balances",
        "balance":     "debit",
        "period_type": "instant",
    },
    "RegulatoryDeferralAccountDebitBalancesAndRelatedDeferredTaxAsset": {
        "label":       "Regulatory deferral account debit balances and related deferred tax asset",
        "balance":     "debit",
        "period_type": "instant",
    },
    "RegulatoryDeferralAccountDebitBalancesDirectlyRelatedToDisposalGroup": {
        "label":       "Regulatory deferral account debit balances directly related to disposal group",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ReimbursementRightsAtFairValue": {
        "label":       "Reimbursement rights related to defined benefit obligation, at fair value",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ReinsuranceContractsHeldThatAreAssets": {
        "label":       "Reinsurance contracts held that are assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ReinsuranceContractsHeldThatAreLiabilities": {
        "label":       "Reinsurance contracts held that are liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RemainingContractualUndiscountedCashOutflowsInflowsThatAriseFromContractsWithinScopeOfIFRS17ThatAreLiabilities": {
        "label":       "Remaining contractual undiscounted cash outflows (inflows) that arise from contracts within scope of IFRS 17 that are liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RentDeferredIncome": {
        "label":       "Rent deferred income",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RentDeferredIncomeClassifiedAsCurrent": {
        "label":       "Rent deferred income classified as current",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RentDeferredIncomeClassifiedAsNoncurrent": {
        "label":       "Rent deferred income classified as non-current",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RentalExpense": {
        "label":       "Rental expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "RentalIncome": {
        "label":       "Rental income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RentalIncomeExpenseOperating": {
        "label":       "Rental income expense operating",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RentalIncomeFromInvestmentProperty": {
        "label":       "Rental income from investment property",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RentalIncomeFromInvestmentPropertyNetOfDirectOperatingExpense": {
        "label":       "Rental income from investment property net of direct operating expense",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RentalIncomeInvesting": {
        "label":       "Rental income investing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RepairsAndMaintenanceExpense": {
        "label":       "Repairs and maintenance expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "RepaymentsOfBondsNotesAndDebentures": {
        "label":       "Repayments of bonds, notes and debentures",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RepaymentsOfBorrowingsClassifiedAsFinancingActivities": {
        "label":       "Repayments of borrowings, classified as financing activities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RepaymentsOfCurrentBorrowings": {
        "label":       "Repayments of current borrowings",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RepaymentsOfNoncurrentBorrowings": {
        "label":       "Repayments of non-current borrowings",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RepaymentsOfRegulatoryCapitalEquity": {
        "label":       "Repayments of regulatory capital, equity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RepaymentsOfRegulatoryCapitalFinancialLiabilities": {
        "label":       "Repayments of regulatory capital, financial liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RepaymentsOfSubordinatedLiabilities": {
        "label":       "Repayments of subordinated liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RepurchaseAgreementsAndCashCollateralOnSecuritiesLent": {
        "label":       "Repurchase agreements and cash collateral on securities lent",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ResearchAndDevelopmentExpense": {
        "label":       "Research and development expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReserveOfCashFlowHedges": {
        "label":       "Reserve of cash flow hedges",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfCashFlowHedgesContinuingHedges": {
        "label":       "Reserve of cash flow hedges, continuing hedges",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfCashFlowHedgesHedgingRelationshipsForWhichHedgeAccountingIsNoLongerApplied": {
        "label":       "Reserve of cash flow hedges, hedging relationships for which hedge accounting is no longer applied",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfChangeInFairValueOfFinancialLiabilityAttributableToChangeInCreditRiskOfLiability": {
        "label":       "Reserve of change in fair value of financial liability attributable to change in credit risk of liability",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfChangeInValueOfForeignCurrencyBasisSpreads": {
        "label":       "Reserve of change in value of foreign currency basis spreads",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfChangeInValueOfForwardElementsOfForwardContracts": {
        "label":       "Reserve of change in value of forward elements of forward contracts",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfChangeInValueOfTimeValueOfOptions": {
        "label":       "Reserve of change in value of time value of options",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfEquityComponentOfConvertibleInstruments": {
        "label":       "Reserve of equity component of convertible instruments",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfExchangeDifferencesOnTranslation": {
        "label":       "Reserve of exchange differences on translation",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfExchangeDifferencesOnTranslationContinuingHedges": {
        "label":       "Reserve of exchange differences on translation, continuing hedges",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfExchangeDifferencesOnTranslationHedgingRelationshipsForWhichHedgeAccountingIsNoLongerApplied": {
        "label":       "Reserve of exchange differences on translation, hedging relationships for which hedge accounting is no longer applied",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfFinanceIncomeExpensesFromReinsuranceContractsHeldExcludedFromProfitOrLoss": {
        "label":       "Reserve of finance income (expenses) from reinsurance contracts held excluded from profit or loss",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfGainsAndLossesFromInvestmentsInEquityInstruments": {
        "label":       "Reserve of gains and losses from investments in equity instruments",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfGainsAndLossesOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome": {
        "label":       "Reserve of gains and losses on financial assets measured at fair value through other comprehensive income",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfGainsAndLossesOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeRelatedToInsuranceContractsToWhichParagraphsC18bC19bC24bAndC24cOfIFRS17HaveBeenApplied": {
        "label":       "Reserve of gains and losses on financial assets measured at fair value through other comprehensive income related to insurance contracts to which paragraphs C18(b), C19(b), C24(b) and C24(c) of IFRS 17 have been applied",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfGainsAndLossesOnHedgingInstrumentsThatHedgeInvestmentsInEquityInstruments": {
        "label":       "Reserve of gains and losses on hedging instruments that hedge investments in equity instruments",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfGainsAndLossesOnRemeasuringAvailableforsaleFinancialAssets": {
        "label":       "Reserve of gains and losses on remeasuring available-for-sale financial assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillBeReclassifiedToProfitOrLoss": {
        "label":       "Reserve of insurance finance income (expenses) from insurance contracts issued excluded from profit or loss that will be reclassified to profit or loss",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfInsuranceFinanceIncomeExpensesFromInsuranceContractsIssuedExcludedFromProfitOrLossThatWillNotBeReclassifiedToProfitOrLoss": {
        "label":       "Reserve of insurance finance income (expenses) from insurance contracts issued excluded from profit or loss that will not be reclassified to profit or loss",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfRemeasurementsOfDefinedBenefitPlans": {
        "label":       "Reserve of remeasurements of defined benefit plans",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ReserveOfSharebasedPayments": {
        "label":       "Reserve of share-based payments",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RestrictedCashAndCashEquivalents": {
        "label":       "Restricted cash and cash equivalents",
        "balance":     "debit",
        "period_type": "instant",
    },
    "RestrictionsOnRealisabilityOfInvestmentPropertyOrRemittanceOfIncomeAndProceedsOfDisposalOfInvestmentProperty": {
        "label":       "Restrictions on realisability of investment property or remittance of income and proceeds of disposal of investment property",
        "balance":     "None",
        "period_type": "instant",
    },
    "RestructuringProvision": {
        "label":       "Restructuring provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RetainedEarnings": {
        "label":       "Retained earnings",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RetainedEarningsExcludingProfitLossForReportingPeriod": {
        "label":       "Retained earnings, excluding profit (loss) for reporting period",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RetainedEarningsProfitLossForReportingPeriod": {
        "label":       "Retained earnings, profit (loss) for reporting period",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RetentionPayables": {
        "label":       "Retention payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RetirementsIntangibleAssetsAndGoodwill": {
        "label":       "Retirements, intangible assets and goodwill",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RetirementsIntangibleAssetsOtherThanGoodwill": {
        "label":       "Retirements, intangible assets other than goodwill",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RetirementsPropertyPlantAndEquipment": {
        "label":       "Retirements, property, plant and equipment",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RetirementsPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Retirements, property, plant and equipment including right-of-use assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RetirementsRightofuseAssets": {
        "label":       "Retirements, right-of-use assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ReturnOnPlanAssetsExcludingInterestIncomeOrExpenseBeforeTaxDefinedBenefitPlans": {
        "label":       "Return on plan assets excluding interest income or expense, before tax, defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ReturnOnPlanAssetsExcludingInterestIncomeOrExpenseNetOfTaxDefinedBenefitPlans": {
        "label":       "Return on plan assets excluding interest income or expense, net of tax, defined benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ReturnOnPlanAssetsNetDefinedBenefitLiabilityAsset": {
        "label":       "Decrease (increase) in net defined benefit liability (asset) resulting from return on plan assets excluding interest income or expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ReturnOnReimbursementRights": {
        "label":       "Increase (decrease) in reimbursement rights related to defined benefit obligation, resulting from return on reimbursement rights, excluding interest income or expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "RevaluationIncreaseDecreaseIntangibleAssetsOtherThanGoodwill": {
        "label":       "Revaluation increase (decrease), intangible assets other than goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "RevaluationIncreaseDecreasePropertyPlantAndEquipment": {
        "label":       "Revaluation increase (decrease), property, plant and equipment",
        "balance":     "debit",
        "period_type": "duration",
    },
    "RevaluationIncreaseDecreasePropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Revaluation increase (decrease), property, plant and equipment including right-of-use assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "RevaluationSurplus": {
        "label":       "Revaluation surplus",
        "balance":     "credit",
        "period_type": "instant",
    },
    "Revenue": {
        "label":       "Revenue",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueAndOperatingIncome": {
        "label":       "Revenue and operating income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromConstructionContracts": {
        "label":       "Revenue from construction contracts",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromContractsWithCustomers": {
        "label":       "Revenue from contracts with customers",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromDividends": {
        "label":       "Revenue from dividends",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromDividendsInvesting": {
        "label":       "Revenue from dividends investing",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromGovernmentGrants": {
        "label":       "Revenue from government grants",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromHotelOperations": {
        "label":       "Revenue from hotel operations",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromInterest": {
        "label":       "Interest income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromPerformanceObligationsSatisfiedOrPartiallySatisfiedInPreviousPeriods": {
        "label":       "Revenue from performance obligations satisfied or partially satisfied in previous periods",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfAdvertisingServices": {
        "label":       "Revenue from rendering of advertising services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfCargoAndMailTransportServices": {
        "label":       "Revenue from rendering of cargo and mail transport services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfDataServices": {
        "label":       "Revenue from rendering of data services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfGamingServices": {
        "label":       "Revenue from rendering of gaming services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfInformationTechnologyConsultingServices": {
        "label":       "Revenue from rendering of information technology consulting services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfInformationTechnologyMaintenanceAndSupportServices": {
        "label":       "Revenue from rendering of information technology maintenance and support services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfInformationTechnologyServices": {
        "label":       "Revenue from rendering of information technology services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfInterconnectionServices": {
        "label":       "Revenue from rendering of interconnection services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfInternetAndDataServices": {
        "label":       "Revenue from rendering of internet and data services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfInternetServices": {
        "label":       "Revenue from rendering of internet services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfLandLineTelephoneServices": {
        "label":       "Revenue from rendering of land line telephone services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfMobileTelephoneServices": {
        "label":       "Revenue from rendering of mobile telephone services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfOtherTelecommunicationServices": {
        "label":       "Revenue from rendering of other telecommunication services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfPassengerTransportServices": {
        "label":       "Revenue from rendering of passenger transport services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfPrintingServices": {
        "label":       "Revenue from rendering of printing services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfServices": {
        "label":       "Revenue from rendering of services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfServicesRelatedPartyTransactions": {
        "label":       "Revenue from rendering of services related party transactions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfTelecommunicationServices": {
        "label":       "Revenue from rendering of telecommunication services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfTelephoneServices": {
        "label":       "Revenue from rendering of telephone services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRenderingOfTransportServices": {
        "label":       "Revenue from rendering of transport services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRoomOccupancyServices": {
        "label":       "Revenue from room occupancy services",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromRoyalties": {
        "label":       "Revenue from royalties",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfAgriculturalProduce": {
        "label":       "Revenue from sale of agricultural produce",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfAlcoholAndAlcoholicDrinks": {
        "label":       "Revenue from sale of alcohol and alcoholic drinks",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfBooks": {
        "label":       "Revenue from sale of books",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfCopper": {
        "label":       "Revenue from sale of copper",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfCrudeOil": {
        "label":       "Revenue from sale of crude oil",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfElectricity": {
        "label":       "Revenue from sale of electricity",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfFoodAndBeverage": {
        "label":       "Revenue from sale of food and beverage",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfGold": {
        "label":       "Revenue from sale of gold",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfGoods": {
        "label":       "Revenue from sale of goods",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfGoodsRelatedPartyTransactions": {
        "label":       "Revenue from sale of goods related party transactions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfNaturalGas": {
        "label":       "Revenue from sale of natural gas",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfOilAndGasProducts": {
        "label":       "Revenue from sale of oil and gas products",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfPetroleumAndPetrochemicalProducts": {
        "label":       "Revenue from sale of petroleum and petrochemical products",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfPublications": {
        "label":       "Revenue from sale of publications",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfSilver": {
        "label":       "Revenue from sale of silver",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfSugar": {
        "label":       "Revenue from sale of sugar",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueFromSaleOfTelecommunicationEquipment": {
        "label":       "Revenue from sale of telecommunication equipment",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueOfAcquiree": {
        "label":       "Revenue of acquiree",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueOfCombinedEntity": {
        "label":       "Revenue of combined entity as if combination occurred at beginning of period",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueRecognisedOnExchangingConstructionServicesForFinancialAsset": {
        "label":       "Revenue recognised on exchanging construction services for financial asset",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueRecognisedOnExchangingConstructionServicesForIntangibleAsset": {
        "label":       "Revenue recognised on exchanging construction services for intangible asset",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RevenueThatWasIncludedInContractLiabilityBalanceAtBeginningOfPeriod": {
        "label":       "Revenue that was included in contract liability balance at beginning of period",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ReversalAllowanceAccountForCreditLossesOfFinancialAssets": {
        "label":       "Reversal, allowance account for credit losses of financial assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLoss": {
        "label":       "Reversal of impairment loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInOtherComprehensiveIncome": {
        "label":       "Reversal of impairment loss recognised in other comprehensive income",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInOtherComprehensiveIncomeIntangibleAssetsOtherThanGoodwill": {
        "label":       "Reversal of impairment loss recognised in other comprehensive income, intangible assets other than goodwill",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInOtherComprehensiveIncomePropertyPlantAndEquipment": {
        "label":       "Reversal of impairment loss recognised in other comprehensive income, property, plant and equipment",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInOtherComprehensiveIncomePropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Reversal of impairment loss recognised in other comprehensive income, property, plant and equipment including right-of-use assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInOtherComprehensiveIncomeRightofuseAssets": {
        "label":       "Reversal of impairment loss recognised in other comprehensive income, right-of-use assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInProfitOrLoss": {
        "label":       "Reversal of impairment loss recognised in profit or loss",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInProfitOrLossBiologicalAssets": {
        "label":       "Reversal of impairment loss recognised in profit or loss biological assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInProfitOrLossIntangibleAssetsOtherThanGoodwill": {
        "label":       "Reversal of impairment loss recognised in profit or loss, intangible assets other than goodwill",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInProfitOrLossInvestmentProperty": {
        "label":       "Reversal of impairment loss recognised in profit or loss, investment property",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInProfitOrLossLoansAndAdvances": {
        "label":       "Reversal of impairment loss recognised in profit or loss loans and advances",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInProfitOrLossPropertyPlantAndEquipment": {
        "label":       "Reversal of impairment loss recognised in profit or loss property plant and equipment",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInProfitOrLossPropertyPlantAndEquipmentIncludingRightofuseAssets": {
        "label":       "Reversal of impairment loss recognised in profit or loss, property, plant and equipment including right-of-use assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInProfitOrLossRightofuseAssets": {
        "label":       "Reversal of impairment loss recognised in profit or loss, right-of-use assets",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReversalOfImpairmentLossRecognisedInProfitOrLossTradeReceivables": {
        "label":       "Reversal of impairment loss recognised in profit or loss trade receivables",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ReversalOfInventoryWritedown": {
        "label":       "Reversal of inventory writedown",
        "balance":     "None",
        "period_type": "duration",
    },
    "ReversalOfProvisionsForCostOfRestructuring": {
        "label":       "Reversal of provisions for cost of restructuring",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ReverseRepurchaseAgreementsAndCashCollateralOnSecuritiesBorrowed": {
        "label":       "Reverse repurchase agreements and cash collateral on securities borrowed",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ReversedUnsettledLiabilitiesContingentLiabilitiesRecognisedInBusinessCombination": {
        "label":       "Reversed unsettled liabilities, contingent liabilities recognised in business combination",
        "balance":     "debit",
        "period_type": "duration",
    },
    "RightofuseAssetFairValueUsedAsDeemedCost": {
        "label":       "Right-of-use asset fair value used as deemed cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "RightofuseAssets": {
        "label":       "Right-of-use assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "RightofuseAssetsIncreaseDecreaseInRevaluationSurplus": {
        "label":       "Right-of-use assets, increase (decrease) in revaluation surplus",
        "balance":     "credit",
        "period_type": "duration",
    },
    "RightofuseAssetsRevaluationSurplus": {
        "label":       "Right-of-use assets, revaluation surplus",
        "balance":     "credit",
        "period_type": "instant",
    },
    "RightofuseAssetsRevaluedAssetsAtCost": {
        "label":       "Right-of-use assets, revalued assets, at cost",
        "balance":     "debit",
        "period_type": "instant",
    },
    "RiskExposureAssociatedWithInstrumentsSharingCharacteristic": {
        "label":       "Risk exposure associated with instruments sharing characteristic",
        "balance":     "None",
        "period_type": "instant",
    },
    "RoyaltyExpense": {
        "label":       "Royalty expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "SaleOrIssueOfTreasuryShares": {
        "label":       "Sale or issue of treasury shares",
        "balance":     "credit",
        "period_type": "duration",
    },
    "SalesAndMarketingExpense": {
        "label":       "Sales and marketing expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "SalesFairValueMeasurementAssets": {
        "label":       "Sales, fair value measurement, assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "SalesFairValueMeasurementEntitysOwnEquityInstruments": {
        "label":       "Sales fair value measurement entitys own equity instruments",
        "balance":     "debit",
        "period_type": "duration",
    },
    "SalesFairValueMeasurementLiabilities": {
        "label":       "Sales, fair value measurement, liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "SalesOfPropertyAndOtherAssetsRelatedPartyTransactions": {
        "label":       "Sales of property and other assets, related party transactions",
        "balance":     "credit",
        "period_type": "duration",
    },
    "SecuredBankLoansReceived": {
        "label":       "Secured bank loans received",
        "balance":     "credit",
        "period_type": "instant",
    },
    "SellingExpense": {
        "label":       "Selling expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "SellingGeneralAndAdministrativeExpense": {
        "label":       "Selling general and administrative expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "SellingProfitLossOnFinanceLeases": {
        "label":       "Selling profit (loss) on finance leases",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ServicesExpense": {
        "label":       "Services expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ServicesReceivedRelatedPartyTransactions": {
        "label":       "Services received, related party transactions",
        "balance":     "debit",
        "period_type": "duration",
    },
    "SettledLiabilitiesContingentLiabilitiesRecognisedInBusinessCombination": {
        "label":       "Settled liabilities, contingent liabilities recognised in business combination",
        "balance":     "debit",
        "period_type": "duration",
    },
    "SettlementOfLiabilitiesByEntityOnBehalfOfRelatedPartyRelatedPartyTransactions": {
        "label":       "Settlement of liabilities by entity on behalf of related party, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "SettlementOfLiabilitiesOnBehalfOfEntityByRelatedPartyRelatedPartyTransactions": {
        "label":       "Settlement of liabilities on behalf of entity by related party, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "SettlementsFairValueMeasurementAssets": {
        "label":       "Settlements, fair value measurement, assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "SettlementsFairValueMeasurementEntitysOwnEquityInstruments": {
        "label":       "Settlements, fair value measurement, entity's own equity instruments",
        "balance":     "debit",
        "period_type": "duration",
    },
    "SettlementsFairValueMeasurementLiabilities": {
        "label":       "Settlements, fair value measurement, liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ShareIssueRelatedCost": {
        "label":       "Share issue related cost",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ShareOfContingentLiabilitiesIncurredJointlyWithOtherVenturers": {
        "label":       "Share of contingent liabilities of joint ventures incurred jointly with other investors",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ShareOfContingentLiabilitiesOfAssociatesIncurredJointlyWithOtherInvestors": {
        "label":       "Share of contingent liabilities of associates incurred jointly with other investors",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethod": {
        "label":       "Share of other comprehensive income of associates and joint ventures accounted for using equity method, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodBeforeTax": {
        "label":       "Share of other comprehensive income of associates and joint ventures accounted for using equity method, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodThatWillBeReclassifiedToProfitOrLossBeforeTax": {
        "label":       "Share of other comprehensive income of associates and joint ventures accounted for using equity method that will be reclassified to profit or loss, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodThatWillBeReclassifiedToProfitOrLossNetOfTax": {
        "label":       "Share of other comprehensive income of associates and joint ventures accounted for using equity method that will be reclassified to profit or loss, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodThatWillNotBeReclassifiedToProfitOrLossBeforeTax": {
        "label":       "Share of other comprehensive income of associates and joint ventures accounted for using equity method that will not be reclassified to profit or loss, before tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodThatWillNotBeReclassifiedToProfitOrLossNetOfTax": {
        "label":       "Share of other comprehensive income of associates and joint ventures accounted for using equity method that will not be reclassified to profit or loss, net of tax",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ShareOfProfitLossOfAssociatesAccountedForUsingEquityMethod": {
        "label":       "Share of profit loss of associates accounted for using equity method",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ShareOfProfitLossOfAssociatesAndJointVenturesAccountedForUsingEquityMethod": {
        "label":       "Share of profit loss of associates and joint ventures accounted for using equity method",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ShareOfProfitLossOfContinuingOperationsOfAssociatesAndJointVenturesAccountedForUsingEquityMethod": {
        "label":       "Share of profit loss of continuing operations of associates and joint ventures accounted for using equity method",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ShareOfProfitLossOfDiscontinuedOperationsOfAssociatesAndJointVenturesAccountedForUsingEquityMethod": {
        "label":       "Share of profit loss of discontinued operations of associates and joint ventures accounted for using equity method",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ShareOfProfitLossOfJointVenturesAccountedForUsingEquityMethod": {
        "label":       "Share of profit loss of joint ventures accounted for using equity method",
        "balance":     "credit",
        "period_type": "duration",
    },
    "ShareOfTotalComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethod": {
        "label":       "Share of total comprehensive income of associates and joint ventures accounted for using equity method",
        "balance":     "credit",
        "period_type": "duration",
    },
    "SharePremium": {
        "label":       "Share premium",
        "balance":     "credit",
        "period_type": "instant",
    },
    "Ships": {
        "label":       "Ships",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ShorttermBorrowings": {
        "label":       "Current borrowings",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ShorttermDepositsClassifiedAsCashEquivalents": {
        "label":       "Short-term deposits, classified as cash equivalents",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ShorttermDepositsNotClassifiedAsCashEquivalents": {
        "label":       "Short-term deposits, not classified as cash equivalents",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ShorttermEmployeeBenefitsAccruals": {
        "label":       "Short-term employee benefits accruals",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ShorttermEmployeeBenefitsExpense": {
        "label":       "Shortterm employee benefits expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ShorttermInvestmentsClassifiedAsCashEquivalents": {
        "label":       "Short-term investments, classified as cash equivalents",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ShorttermLegalProceedingsProvision": {
        "label":       "Current legal proceedings provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ShorttermMiscellaneousOtherProvisions": {
        "label":       "Current miscellaneous other provisions",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ShorttermOnerousContractsProvision": {
        "label":       "Current onerous contracts provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ShorttermProvisionForDecommissioningRestorationAndRehabilitationCosts": {
        "label":       "Current provision for decommissioning, restoration and rehabilitation costs",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ShorttermRestructuringProvision": {
        "label":       "Current restructuring provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ShorttermWarrantyProvision": {
        "label":       "Current warranty provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "SocialSecurityContributions": {
        "label":       "Social security contributions",
        "balance":     "debit",
        "period_type": "duration",
    },
    "SpareParts": {
        "label":       "Current spare parts",
        "balance":     "debit",
        "period_type": "instant",
    },
    "StatutoryReserve": {
        "label":       "Statutory reserve",
        "balance":     "credit",
        "period_type": "instant",
    },
    "StructuredDebtAmountContributedToFairValueOfPlanAssets": {
        "label":       "Structured debt, amount contributed to fair value of plan assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "SubordinatedLiabilities": {
        "label":       "Subordinated liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "SubordinatedLiabilitiesAtAmortisedCost": {
        "label":       "Subordinated liabilities at amortised cost",
        "balance":     "credit",
        "period_type": "instant",
    },
    "SubscriptionCirculationRevenue": {
        "label":       "Subscription circulation revenue",
        "balance":     "credit",
        "period_type": "duration",
    },
    "SubsequentRecognitionOfDeferredTaxAssetsGoodwill": {
        "label":       "Subsequent recognition of deferred tax assets, goodwill",
        "balance":     "credit",
        "period_type": "duration",
    },
    "SupportProvidedToStructuredEntityWithoutHavingContractualObligationToDoSo": {
        "label":       "Support provided to structured entity without having contractual obligation to do so",
        "balance":     "None",
        "period_type": "duration",
    },
    "SupportProvidedToSubsidiaryWithoutHavingContractualObligationToDoSo": {
        "label":       "Support provided to subsidiary by investment entity or its subsidiaries without having contractual obligation to do so",
        "balance":     "None",
        "period_type": "duration",
    },
    "SurplusDeficitInPlan": {
        "label":       "Surplus (deficit) in plan",
        "balance":     "debit",
        "period_type": "instant",
    },
    "TangibleExplorationAndEvaluationAssets": {
        "label":       "Tangible exploration and evaluation assets",
        "balance":     "debit",
        "period_type": "instant",
    },
    "TaxBenefitArisingFromPreviouslyUnrecognisedTaxLossTaxCreditOrTemporaryDifferenceOfPriorPeriodUsedToReduceCurrentTaxExpense": {
        "label":       "Tax benefit arising from previously unrecognised tax loss tax credit or temporary difference of prior period used to reduce current tax expense",
        "balance":     "credit",
        "period_type": "duration",
    },
    "TaxBenefitArisingFromPreviouslyUnrecognisedTaxLossTaxCreditOrTemporaryDifferenceOfPriorPeriodUsedToReduceDeferredTaxExpense": {
        "label":       "Tax benefit arising from previously unrecognised tax loss tax credit or temporary difference of prior period used to reduce deferred tax expense",
        "balance":     "credit",
        "period_type": "duration",
    },
    "TaxEffectFromChangeInTaxRate": {
        "label":       "Tax effect from change in tax rate",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TaxEffectOfExpenseNotDeductibleInDeterminingTaxableProfitTaxLoss": {
        "label":       "Tax effect of expense not deductible in determining taxable profit (tax loss)",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TaxEffectOfForeignTaxRates": {
        "label":       "Tax effect of foreign tax rates",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TaxEffectOfImpairmentOfGoodwill": {
        "label":       "Tax effect of impairment of goodwill",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TaxEffectOfRevenuesExemptFromTaxation2011": {
        "label":       "Tax effect of revenues exempt from taxation",
        "balance":     "credit",
        "period_type": "duration",
    },
    "TaxEffectOfTaxLosses": {
        "label":       "Tax effect of tax losses",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TaxExpenseIncomeAtApplicableTaxRate": {
        "label":       "Tax expense (income) at applicable tax rate",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TaxExpenseIncomeRelatingToChangesInAccountingPoliciesAndErrorsIncludedInProfitOrLoss": {
        "label":       "Tax expense income relating to changes in accounting policies and errors included in profit or loss",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TaxExpenseOtherThanIncomeTaxExpense": {
        "label":       "Tax expense other than income tax expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TaxExpenseRelatingToGainLossOnDiscontinuance": {
        "label":       "Tax expense relating to gain loss on discontinuance",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TaxExpenseRelatingToProfitLossFromOrdinaryActivitiesOfDiscontinuedOperations": {
        "label":       "Tax expense relating to profit loss from ordinary activities of discontinued operations",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TechnologybasedIntangibleAssetsRecognisedAsOfAcquisitionDate": {
        "label":       "Technology-based intangible assets recognised as of acquisition date",
        "balance":     "debit",
        "period_type": "instant",
    },
    "TemporaryDifferencesAssociatedWithInvestmentsInSubsidiariesBranchesAndAssociatesAndInterestsInJointVentures": {
        "label":       "Temporary differences associated with investments in subsidiaries, branches and associates and interests in joint arrangements for which deferred tax liabilities have not been recognised",
        "balance":     "None",
        "period_type": "instant",
    },
    "TerminationBenefitsExpense": {
        "label":       "Termination benefits expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TradeAndOtherCurrentPayables": {
        "label":       "Trade and other current payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "TradeAndOtherCurrentPayablesToRelatedParties": {
        "label":       "Current payables to related parties",
        "balance":     "credit",
        "period_type": "instant",
    },
    "TradeAndOtherCurrentPayablesToTradeSuppliers": {
        "label":       "Current trade payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "TradeAndOtherCurrentReceivables": {
        "label":       "Trade and other current receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "TradeAndOtherCurrentReceivablesDueFromRelatedParties": {
        "label":       "Current receivables due from related parties",
        "balance":     "debit",
        "period_type": "instant",
    },
    "TradeAndOtherPayables": {
        "label":       "Trade and other payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "TradeAndOtherPayablesRecognisedAsOfAcquisitionDate": {
        "label":       "Trade and other payables recognised as of acquisition date",
        "balance":     "credit",
        "period_type": "instant",
    },
    "TradeAndOtherPayablesToRelatedParties": {
        "label":       "Payables to related parties",
        "balance":     "credit",
        "period_type": "instant",
    },
    "TradeAndOtherPayablesToTradeSuppliers": {
        "label":       "Trade payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "TradeAndOtherPayablesUndiscountedCashFlows": {
        "label":       "Trade and other payables, undiscounted cash flows",
        "balance":     "credit",
        "period_type": "instant",
    },
    "TradeAndOtherReceivables": {
        "label":       "Trade and other receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "TradeAndOtherReceivablesDueFromRelatedParties": {
        "label":       "Receivables due from related parties",
        "balance":     "debit",
        "period_type": "instant",
    },
    "TradeReceivables": {
        "label":       "Trade receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "TradingIncomeExpense": {
        "label":       "Trading income expense",
        "balance":     "credit",
        "period_type": "duration",
    },
    "TradingIncomeExpenseOnDebtInstruments": {
        "label":       "Trading income expense on debt instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "TradingIncomeExpenseOnDerivativeFinancialInstruments": {
        "label":       "Trading income expense on derivative financial instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "TradingIncomeExpenseOnEquityInstruments": {
        "label":       "Trading income expense on equity instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "TradingIncomeExpenseOnForeignExchangeContracts": {
        "label":       "Trading income expense on foreign exchange contracts",
        "balance":     "credit",
        "period_type": "duration",
    },
    "TransactionPriceAllocatedToRemainingPerformanceObligations": {
        "label":       "Transaction price allocated to remaining performance obligations",
        "balance":     "credit",
        "period_type": "instant",
    },
    "TransferBetweenFinancialLiabilitiesAndEquityAttributableToChangeInRedemptionProhibition": {
        "label":       "Transfer between financial liabilities and equity attributable to change in redemption prohibition",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransferFromInvestmentPropertyUnderConstructionOrDevelopmentInvestmentProperty": {
        "label":       "Transfer from investment property under construction or development, investment property",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TransferFromToInventoriesAndOwnerOccupiedPropertyInvestmentProperty": {
        "label":       "Transfer from (to) inventories and owner-occupied property, investment property",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TransfersFromToOtherRetirementBenefitPlans": {
        "label":       "Transfers from (to) other retirement benefit plans",
        "balance":     "credit",
        "period_type": "duration",
    },
    "TransfersIntoLevel3OfFairValueHierarchyAssets": {
        "label":       "Transfers into Level 3 of fair value hierarchy, assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TransfersIntoLevel3OfFairValueHierarchyEntitysOwnEquityInstruments": {
        "label":       "Transfers into Level 3 of fair value hierarchy, entity's own equity instruments",
        "balance":     "credit",
        "period_type": "duration",
    },
    "TransfersIntoLevel3OfFairValueHierarchyLiabilities": {
        "label":       "Transfers into Level 3 of fair value hierarchy, liabilities",
        "balance":     "credit",
        "period_type": "duration",
    },
    "TransfersOfCumulativeGainLossWithinEquity": {
        "label":       "Transfers of cumulative gain (loss) within equity when changes in liability's credit risk are presented in other comprehensive income",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransfersOfCumulativeGainLossWithinEquityWhenInvestmentsInEquityInstrumentsDesignatedAtFairValueThroughOtherComprehensiveIncomeAreDerecognisedDuringPeriod": {
        "label":       "Transfers of cumulative gain (loss) within equity when investments in equity instruments designated at fair value through other comprehensive income are derecognised during period",
        "balance":     "credit",
        "period_type": "duration",
    },
    "TransfersOfResearchAndDevelopmentFromEntityRelatedPartyTransactions": {
        "label":       "Transfers of research and development from entity, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransfersOfResearchAndDevelopmentToEntityRelatedPartyTransactions": {
        "label":       "Transfers of research and development to entity, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransfersOutOfLevel1IntoLevel2OfFairValueHierarchyAssets": {
        "label":       "Transfers out of Level 1 into Level 2 of fair value hierarchy, assets held at end of reporting period",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransfersOutOfLevel1IntoLevel2OfFairValueHierarchyEntitysOwnEquityInstruments": {
        "label":       "Transfers out of Level 1 into Level 2 of fair value hierarchy, entity's own equity instruments held at end of reporting period",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransfersOutOfLevel1IntoLevel2OfFairValueHierarchyLiabilities": {
        "label":       "Transfers out of Level 1 into Level 2 of fair value hierarchy, liabilities held at end of reporting period",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransfersOutOfLevel2IntoLevel1OfFairValueHierarchyAssets": {
        "label":       "Transfers out of Level 2 into Level 1 of fair value hierarchy, assets held at end of reporting period",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransfersOutOfLevel2IntoLevel1OfFairValueHierarchyEntitysOwnEquityInstruments": {
        "label":       "Transfers out of Level 2 into Level 1 of fair value hierarchy, entity's own equity instruments held at end of reporting period",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransfersOutOfLevel2IntoLevel1OfFairValueHierarchyLiabilities": {
        "label":       "Transfers out of Level 2 into Level 1 of fair value hierarchy, liabilities held at end of reporting period",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransfersOutOfLevel3OfFairValueHierarchyAssets": {
        "label":       "Transfers out of Level 3 of fair value hierarchy, assets",
        "balance":     "credit",
        "period_type": "duration",
    },
    "TransfersOutOfLevel3OfFairValueHierarchyEntitysOwnEquityInstruments": {
        "label":       "Transfers out of Level 3 of fair value hierarchy, entity's own equity instruments",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TransfersOutOfLevel3OfFairValueHierarchyLiabilities": {
        "label":       "Transfers out of Level 3 of fair value hierarchy, liabilities",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TransfersUnderFinanceAgreementsFromEntityRelatedPartyTransactions": {
        "label":       "Transfers under finance agreements from entity, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransfersUnderFinanceAgreementsToEntityRelatedPartyTransactions": {
        "label":       "Transfers under finance agreements to entity, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransfersUnderLicenseAgreementsFromEntityRelatedPartyTransactions": {
        "label":       "Transfers under licence agreements from entity, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransfersUnderLicenseAgreementsToEntityRelatedPartyTransactions": {
        "label":       "Transfers under licence agreements to entity, related party transactions",
        "balance":     "None",
        "period_type": "duration",
    },
    "TransportationExpense": {
        "label":       "Transportation expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TravelExpense": {
        "label":       "Travel expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "TreasuryShares": {
        "label":       "Treasury shares",
        "balance":     "debit",
        "period_type": "instant",
    },
    "UnallocatedGoodwill": {
        "label":       "Unallocated goodwill",
        "balance":     "debit",
        "period_type": "instant",
    },
    "UndatedSubordinatedLiabilities": {
        "label":       "Undated subordinated liabilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "UndiscountedCashOutflowRequiredToRepurchaseDerecognisedFinancialAssets": {
        "label":       "Undiscounted cash outflow required to repurchase derecognised financial assets",
        "balance":     "credit",
        "period_type": "instant",
    },
    "UndiscountedExpectedCreditLossesAtInitialRecognitionOnPurchasedOrOriginatedCreditimpairedFinancialAssetsInitiallyRecognised": {
        "label":       "Undiscounted expected credit losses at initial recognition on purchased or originated credit-impaired financial assets initially recognised",
        "balance":     "credit",
        "period_type": "duration",
    },
    "UndiscountedFinanceLeasePaymentsToBeReceived": {
        "label":       "Undiscounted finance lease payments to be received",
        "balance":     "debit",
        "period_type": "instant",
    },
    "UndiscountedOperatingLeasePaymentsToBeReceived": {
        "label":       "Undiscounted operating lease payments to be received",
        "balance":     "debit",
        "period_type": "instant",
    },
    "UndrawnBorrowingFacilities": {
        "label":       "Undrawn borrowing facilities",
        "balance":     "credit",
        "period_type": "instant",
    },
    "UnearnedFinanceIncomeRelatingToFinanceLeasePaymentsReceivable": {
        "label":       "Unearned finance income relating to finance lease payments receivable",
        "balance":     "credit",
        "period_type": "instant",
    },
    "UnratedCreditExposures": {
        "label":       "Unrated credit exposures",
        "balance":     "None",
        "period_type": "instant",
    },
    "UnrecognisedShareOfLossesOfAssociates": {
        "label":       "Unrecognised share of losses of associates",
        "balance":     "debit",
        "period_type": "duration",
    },
    "UnrecognisedShareOfLossesOfJointVentures": {
        "label":       "Unrecognised share of losses of joint ventures",
        "balance":     "debit",
        "period_type": "duration",
    },
    "UnsecuredBankLoansReceived": {
        "label":       "Unsecured bank loans received",
        "balance":     "credit",
        "period_type": "instant",
    },
    "UnusedProvisionReversedOtherProvisions": {
        "label":       "Unused provision reversed, other provisions",
        "balance":     "debit",
        "period_type": "duration",
    },
    "UnusedTaxCreditsForWhichNoDeferredTaxAssetRecognised": {
        "label":       "Unused tax credits for which no deferred tax asset recognised",
        "balance":     "None",
        "period_type": "instant",
    },
    "UnusedTaxLossesForWhichNoDeferredTaxAssetRecognised": {
        "label":       "Unused tax losses for which no deferred tax asset recognised",
        "balance":     "None",
        "period_type": "instant",
    },
    "UtilisationAllowanceAccountForCreditLossesOfFinancialAssets": {
        "label":       "Utilisation, allowance account for credit losses of financial assets",
        "balance":     "debit",
        "period_type": "duration",
    },
    "UtilitiesExpense": {
        "label":       "Utilities expense",
        "balance":     "debit",
        "period_type": "duration",
    },
    "ValueAddedTaxPayables": {
        "label":       "Value added tax payables",
        "balance":     "credit",
        "period_type": "instant",
    },
    "ValueAddedTaxReceivables": {
        "label":       "Value added tax receivables",
        "balance":     "debit",
        "period_type": "instant",
    },
    "ValueAtRisk": {
        "label":       "Value at risk",
        "balance":     "None",
        "period_type": "instant",
    },
    "Vehicles": {
        "label":       "Vehicles",
        "balance":     "debit",
        "period_type": "instant",
    },
    "WagesAndSalaries": {
        "label":       "Wages and salaries",
        "balance":     "debit",
        "period_type": "duration",
    },
    "WarrantLiability": {
        "label":       "Warrant liability",
        "balance":     "credit",
        "period_type": "instant",
    },
    "WarrantReserve": {
        "label":       "Warrant reserve",
        "balance":     "credit",
        "period_type": "instant",
    },
    "WarrantyProvision": {
        "label":       "Warranty provision",
        "balance":     "credit",
        "period_type": "instant",
    },
    "WeightedAverageFairValueAtMeasurementDateOtherEquityInstrumentsGranted": {
        "label":       "Weighted average fair value at measurement date, other equity instruments granted",
        "balance":     "credit",
        "period_type": "instant",
    },
    "WeightedAverageFairValueAtMeasurementDateShareOptionsGranted": {
        "label":       "Weighted average fair value at measurement date, share options granted",
        "balance":     "credit",
        "period_type": "instant",
    },
    "WorkInProgress": {
        "label":       "Current work in progress",
        "balance":     "debit",
        "period_type": "instant",
    },
    "WritedownsReversalsOfInventories": {
        "label":       "Writedowns reversals of inventories",
        "balance":     "debit",
        "period_type": "duration",
    },
    "WritedownsReversalsOfPropertyPlantAndEquipment": {
        "label":       "Writedowns reversals of property plant and equipment",
        "balance":     "None",
        "period_type": "duration",
    },
}