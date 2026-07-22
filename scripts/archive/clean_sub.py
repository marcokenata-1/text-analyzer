"""
Smart IFRS tag filter — removes clearly wrong tags from FinBERT results.

The problem: FinBERT picks up tags that sound financial but belong to
completely different sectors. This script:

1. Defines sector-specific BLOCKLISTS — tags that should NEVER appear
   in a given sector regardless of FinBERT score
2. Defines sector-specific ALLOWLISTS — tags that MUST appear in a
   given sector regardless of FinBERT score
3. Applies these rules to the subindustry mapping JSON

Run after rebuild_neo4j.py to clean up the mapping.
"""

import json

# ── Sector blocklists ──────────────────────────────────────────────────────────
# Tags that should NEVER appear in these sectors

SECTOR_BLOCKLISTS = {
    # Banks should never have oil/gas/mining/agricultural tags
    "40": [
        "OilAndGasAssets", "RevenueFromSaleOfCrudeOil",
        "RevenueFromSaleOfNaturalGas", "RevenueFromSaleOfOilAndGasProducts",
        "PurchaseOfOilAndGasAssets", "ProceedsFromDisposalOfOilAndGasAssets",
        "CashFlowsUsedInExplorationAndDevelopmentActivities",
        "PurchaseOfExplorationAndEvaluationAssets",
        "IncomeArisingFromExplorationForAndEvaluationOfMineralResources",
        "AssetsArisingFromExplorationForAndEvaluationOfMineralResources",
        "CommitmentsForDevelopmentOrAcquisitionOfBiologicalAssets",
        "AcquisitionsThroughBusinessCombinationsBiologicalAssets",
        "RevenueFromSaleOfAlcoholAndAlcoholicDrinks",
        "RevenueFromSaleOfFoodAndBeverage",
        "RevenueFromSaleOfGold",
        "CurrentPetroleumAndPetrochemicalProducts",
        "FuelAndEnergyExpense",
        "MiningAssets",
        "BiologicalAssets",
    ],

    # Energy should never have banking/insurance tags
    "10": [
        "LoansAndAdvancesToCustomers", "DepositsFromCustomers",
        "InterestIncome", "FeeAndCommissionIncome",
        "InsuranceRevenue", "InsuranceClaims",
        "BankingArrangementsClassifiedAsCashEquivalents",
        "CashAndBalancesWithCentralBank",
    ],

    # Utilities should never have banking tags
    "55": [
        "LoansAndAdvancesToCustomers", "DepositsFromCustomers",
        "FeeAndCommissionIncome", "InsuranceRevenue",
        "CashAndBalancesWithCentralBank",
    ],
}

# ── Sub-industry allowlists ────────────────────────────────────────────────────
# Tags that MUST appear in specific sub-industries

SUBINDUSTRY_ALLOWLISTS = {
    # Diversified Banks
    "40101010": [
        "LoansAndAdvancesToCustomers",
        "LoansAndAdvancesToBanksAtAmortisedCost",
        "DepositsFromCustomers",
        "DepositsFromBanks",
        "BankingArrangementsClassifiedAsCashEquivalents",
        "CashAndBalancesWithCentralBank",
        "InterestReceivedFromLoansAndAdvancesClassifiedAsOperatingActivities",
        "InterestPaidClassifiedAsFinancingActivities",
        "AllowanceAccountForCreditLossesOfFinancialAssets",
        "LoansAndReceivables",
        "ShorttermDepositsNotClassifiedAsCashEquivalents",
    ],
    # Regional Banks — same core + more specific
    "40101015": [
        "LoansAndAdvancesToCustomers",
        "LoansAndAdvancesToBanksAtAmortisedCost",
        "DepositsFromCustomers",
        "DepositsFromBanks",
        "BankingArrangementsClassifiedAsCashEquivalents",
        "CashAndBalancesWithCentralBank",
        "InterestReceivedFromLoansAndAdvancesClassifiedAsOperatingActivities",
        "InterestPaidClassifiedAsFinancingActivities",
        "AllowanceAccountForCreditLossesOfFinancialAssets",
        "LoansAndReceivables",
        "ShorttermDepositsNotClassifiedAsCashEquivalents",
        "CorporateLoans",
        "CommercialPapersIssued",
        "UnsecuredBankLoansReceived",
        "SecuredBankLoansReceived",
    ],
    # Thrifts & Mortgage Finance
    "40101040": [
        "LoansAndAdvancesToCustomers",
        "DepositsFromCustomers",
        "AllowanceAccountForCreditLossesOfFinancialAssets",
    ],
    # Integrated Oil & Gas
    "10102010": [
        "OilAndGasAssets",
        "RevenueFromSaleOfCrudeOil",
        "RevenueFromSaleOfNaturalGas",
        "FuelAndEnergyExpense",
    ],
}

# ── Tag quality filter ─────────────────────────────────────────────────────────
# Remove tags that are clearly disclosure/movement table tags
# not primary statement line items — these are note detail tags
# that don't belong in the primary mapping

DISCLOSURE_SUFFIXES = [
    "FairValueHierarchy",
    "ReconcilingItem",
    "RelatedPartyTransaction",
    "DefinedBenefitPlan",
    "PlanAssets",
    "ContinuingInvolvement",
    "MeasurementPeriodAdjustment",
    "IssueCosts",
    "AcquisitionRelatedCosts",
]

DISCLOSURE_PREFIXES = [
    "Transfers",
    "Retirements",
    "Disposals",
    "Additions",
    "Purchases",
    "Settlements",
    "Reclassification",
    "PurchasesFairValue",
    "SettlementsFairValue",
    "IssuesFairValue",
]


def is_disclosure_tag(tag: str) -> bool:
    """Check if tag is a note disclosure tag rather than primary line item."""
    for suffix in DISCLOSURE_SUFFIXES:
        if suffix in tag:
            return True
    for prefix in DISCLOSURE_PREFIXES:
        if tag.startswith(prefix):
            return True
    return False


def clean_mapping(
    mapping: dict,
    remove_disclosure_tags: bool = True,
) -> dict:
    """Apply blocklists, allowlists and disclosure filter to mapping."""

    cleaned   = {}
    stats     = {
        "total_before":    0,
        "total_after":     0,
        "blocked":         0,
        "disclosure_removed": 0,
        "allowlisted":     0,
    }

    for si_code, tags in mapping.items():
        sector_code = si_code[:2]
        tag_set     = set(tags)

        stats["total_before"] += len(tag_set)

        # Apply sector blocklist
        blocklist = SECTOR_BLOCKLISTS.get(sector_code, [])
        blocked   = tag_set & set(blocklist)
        tag_set  -= blocked
        stats["blocked"] += len(blocked)

        # Remove disclosure/movement table tags
        if remove_disclosure_tags:
            disclosure = {t for t in tag_set if is_disclosure_tag(t)}
            tag_set   -= disclosure
            stats["disclosure_removed"] += len(disclosure)

        # Apply sub-industry allowlist (force include)
        allowlist = SUBINDUSTRY_ALLOWLISTS.get(si_code, [])
        for tag in allowlist:
            if tag not in tag_set:
                tag_set.add(tag)
                stats["allowlisted"] += 1

        cleaned[si_code] = sorted(tag_set)
        stats["total_after"] += len(tag_set)

    return cleaned, stats


def analyse_cleaned(mapping: dict):
    """Print analysis of cleaned mapping."""
    total_si   = len(mapping)
    total_tags = sum(len(v) for v in mapping.values())
    avg_tags   = total_tags / total_si if total_si else 0

    print(f"\nCleaned mapping stats:")
    print(f"  Sub-industries: {total_si}")
    print(f"  Total edges:    {total_tags}")
    print(f"  Average/SI:     {avg_tags:.1f}")
    print(f"  Min:            {min(len(v) for v in mapping.values())}")
    print(f"  Max:            {max(len(v) for v in mapping.values())}")

    # Show Financials
    print(f"\n  Financials sub-industries after cleaning:")
    for code, tags in sorted(mapping.items()):
        if code.startswith("40"):
            print(f"    [{code}] {len(tags):3d} tags")

    # Show Regional Banks specifically
    snb = "40101015"
    if snb in mapping:
        print(f"\n  Regional Banks [{snb}] — {len(mapping[snb])} tags:")
        for t in sorted(mapping[snb]):
            print(f"    {t}")


def main():
    # Load mapping
    with open("data/mappings/subindustry_ifrs_mapping.json") as f:
        mapping = json.load(f)

    print(f"Original mapping: {sum(len(v) for v in mapping.values())} total edges")

    # Clean
    cleaned, stats = clean_mapping(mapping, remove_disclosure_tags=True)

    print(f"\nCleaning stats:")
    print(f"  Blocked (wrong sector):  {stats['blocked']}")
    print(f"  Disclosure tags removed: {stats['disclosure_removed']}")
    print(f"  Allowlist additions:     {stats['allowlisted']}")
    print(f"  Before: {stats['total_before']}")
    print(f"  After:  {stats['total_after']}")
    print(f"  Reduction: {(1 - stats['total_after']/stats['total_before'])*100:.1f}%")

    analyse_cleaned(cleaned)

    # Save
    with open("data/mappings/subindustry_ifrs_mapping_cleaned.json", "w") as f:
        json.dump(cleaned, f, indent=2)
    print(f"\nSaved to subindustry_ifrs_mapping_cleaned.json")


if __name__ == "__main__":
    main()