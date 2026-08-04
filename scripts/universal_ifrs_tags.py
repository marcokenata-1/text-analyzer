"""
Universal IFRS tags, verified against IFRS taxonomy 2025-03-27.

These are the core line items required by IAS 1 (Presentation of Financial
Statements) and IAS 7 (Cash Flow Statements) that every company regardless
of sector must report. They are added to ALL sector mappings automatically,
so FinBERT only needs to find the sector-specific tags.

Source: full_ifrs-cor_2025-03-27.xsd + lab_full_ifrs-en_2025-03-27.xml
"""

UNIVERSAL_TAGS = {

    # ── STATEMENT OF FINANCIAL POSITION (IAS 1) ────────────────────────────

    # Assets
    "Assets",
    "CashAndCashEquivalents",
    "Inventories",
    "TradeAndOtherReceivables",
    "OtherCurrentFinancialAssets",
    "CurrentAssets",
    "PropertyPlantAndEquipment",
    "RightofuseAssets",
    "Goodwill",
    "IntangibleAssetsOtherThanGoodwill",
    "InvestmentsAccountedForUsingEquityMethod",
    "DeferredTaxAssets",
    "NoncurrentAssets",
    "CurrentTaxAssets",

    # Liabilities
    "Liabilities",
    "TradeAndOtherPayables",
    "CurrentTaxLiabilities",
    "OtherCurrentFinancialLiabilities",
    "CurrentLiabilities",
    "DeferredTaxLiabilities",
    "NoncurrentLiabilities",
    "Provisions",
    "CurrentProvisions",
    "NoncurrentProvisions",
    "LeaseLiabilities",
    "CurrentLeaseLiabilities",
    "NoncurrentLeaseLiabilities",
    "Borrowings",
    "NoncurrentAssetsOrDisposalGroupsClassifiedAsHeldForSale",
    "LiabilitiesIncludedInDisposalGroupsClassifiedAsHeldForSale",
    "ContractAssets",
    "ContractLiabilities",

    # Equity
    "Equity",
    "IssuedCapital",
    "SharePremium",
    "TreasuryShares",
    "RetainedEarnings",
    "NoncontrollingInterests",
    "EquityAttributableToOwnersOfParent",
    "OtherReserves",
    "OtherEquityInterest",

    # ── STATEMENT OF PROFIT OR LOSS (IAS 1) ────────────────────────────────

    "Revenue",
    "CostOfSales",
    "GrossProfit",
    "DepreciationAndAmortisationExpense",
    "EmployeeBenefitsExpense",
    "GeneralAndAdministrativeExpense",
    "DistributionCosts",
    "OtherIncome",
    "OtherOperatingIncomeExpense",
    "ProfitLossFromOperatingActivities",
    "FinanceIncome",
    "FinanceCosts",
    "ShareOfProfitLossOfAssociatesAndJointVenturesAccountedForUsingEquityMethod",
    "ProfitLossBeforeTax",
    "IncomeTaxExpenseContinuingOperations",
    "ProfitLossFromContinuingOperations",
    "ProfitLoss",
    "ProfitLossAttributableToOwnersOfParent",
    "ProfitLossAttributableToNoncontrollingInterests",

    # ── STATEMENT OF COMPREHENSIVE INCOME (IAS 1) ──────────────────────────

    "OtherComprehensiveIncome",
    "ComprehensiveIncome",
    "ComprehensiveIncomeAttributableToOwnersOfParent",
    "ComprehensiveIncomeAttributableToNoncontrollingInterests",
    "OtherComponentsOfOtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossBeforeTax",

    # ── EARNINGS PER SHARE (IAS 33) ─────────────────────────────────────────

    "BasicEarningsLossPerShare",
    "DilutedEarningsLossPerShare",

    # ── STATEMENT OF CASH FLOWS (IAS 7) ────────────────────────────────────

    "CashFlowsFromUsedInOperatingActivities",
    "CashFlowsFromUsedInInvestingActivities",
    "CashFlowsFromUsedInFinancingActivities",
    "IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges",
    "AdjustmentsForDepreciationAndAmortisationExpense",
    "AdjustmentsForIncomeTaxExpense",
    "AdjustmentsForFinanceCosts",
    "ProceedsFromBorrowingsClassifiedAsFinancingActivities",
    "RepaymentsOfBorrowingsClassifiedAsFinancingActivities",

    # ── DIVIDENDS ───────────────────────────────────────────────────────────

    "DividendsPaidClassifiedAsFinancingActivities",
    "DividendsPaidToNoncontrollingInterestsClassifiedAsFinancingActivities",
}


if __name__ == "__main__":
    print(f"Total universal tags: {len(UNIVERSAL_TAGS)}")
    print("\nBy category:")
    print(f"  Balance Sheet (Assets):      {sum(1 for t in UNIVERSAL_TAGS if any(k in t for k in ['Assets','Receivables','Inventories','Cash','Goodwill','Intangible','Property','RightofuseAssets','DeferredTax','Investments']))}")
    print(f"  Balance Sheet (L&E):         {sum(1 for t in UNIVERSAL_TAGS if any(k in t for k in ['Payables','Liabilities','Capital','Premium','Treasury','Retained','Equity','Noncontrolling']))}")
    print(f"  Income Statement:            {sum(1 for t in UNIVERSAL_TAGS if any(k in t for k in ['Revenue','Gross','Depreciation','Employee','Admin','Operating','Finance','Profit','Tax','Share']))}")
    print(f"  Cash Flows:                  {sum(1 for t in UNIVERSAL_TAGS if 'CashFlows' in t or 'IncreaseDec' in t)}")
    print(f"  EPS:                         {sum(1 for t in UNIVERSAL_TAGS if 'EarningsLoss' in t)}")
    print(f"  Dividends:                   {sum(1 for t in UNIVERSAL_TAGS if 'Dividend' in t)}")