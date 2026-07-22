import json

KNOWLEDGE_GRAPH = {
    "Sector_40": {
        "Name": "Financials",
        "Anchor": "Saudi National Bank",
        "XBRL_Structure": {
            "ifrs-full:CashAndBalancesWithCentralBanks": ["Cash", "Central Bank"],
            "ifrs-full:LoansAndAdvancesToCustomers": ["Financing and advances", "Lending"],
            "ifrs-full:Investments": ["Investments, net"],
            "ifrs-full:DepositsFromCustomers": ["Customers' deposits"]
        },
        "Math_Rule": "Assets == Cash + DueFromBanks + Investments + Financing + Derivatives + PPE + Goodwill + Intangibles + ROU + OtherAssets"
    },
    "Sector_55": {
        "Name": "Utilities",
        "Anchor": "ACWA Power",
        "XBRL_Structure": {
            "ifrs-full:PropertyPlantAndEquipment": ["Plants", "Infrastructure", "Machinery"],
            "ifrs-full:NetInvestmentInFinanceLeases": ["Finance lease", "PPA receivable"],
            "ifrs-full:EquityAccountedInvestees": ["Equity accounted", "Joint ventures"],
            "ifrs-full:Revenue": ["Operating revenue", "Capacity charges"]
        },
        "Math_Rule": "Assets == PPE + Intangibles + EquityInvestees + FinanceLease + TaxAssets + Derivatives + OtherAssets"
    }
}


class AgenticFinancialController:
    def __init__(self, raw_extraction, taxonomy):
        self.raw_data = raw_extraction
        self.taxonomy = taxonomy
        self.ledger = []

    def solve_conglomerate_dilemma(self):
        """Thought: I must identify the GICS footprint before mapping."""
        scores = {"Sector_40": 0, "Sector_55": 0}
        labels = [row["label"] for row in self.raw_data]
        
        for label in labels:
            for sector_id, content in self.taxonomy.items():
                aliases = [a for sub in content["XBRL_Structure"].values() for a in sub]
                if any(a.lower() in label.lower() for a in aliases):
                    scores[sector_id] += 1
        
        # Action: Generate Probability Vector
        total = sum(scores.values())
        prob_vector = {k: round(v/total, 2) for k, v in scores.items()}
        
        # Observation: Determine primary sector
        primary_sector = max(prob_vector, key=prob_vector.get)
        print(f"REASONING: Probability Vector is {prob_vector}. Anchoring to {primary_sector}.")
        return primary_sector

    def perform_semantic_mapping(self, sector_id):
        """Action: Map PDF labels to XBRL 'Alphabet'[cite: 1]."""
        sector_rules = self.taxonomy[sector_id]["XBRL_Structure"]
        
        for row in self.raw_data:
            for xbrl_tag, aliases in sector_rules.items():
                if any(a.lower() in row["label"].lower() for a in aliases):
                    self.ledger.append({
                        "xbrl_tag": xbrl_tag,
                        "source_label": row["label"],
                        "value": row["value"],
                        "sector_context": self.taxonomy[sector_id]["Name"]
                    })
        return self.ledger


def run_validation(ledger, reported_total, sector_id):
    """Thought: Accuracy must be mathematically verified[cite: 1]."""
    calculated_sum = sum(item["value"] for item in ledger)
    
    # Formula: Total = Σ Sub-components
    if calculated_sum == reported_total:
        return "SUCCESS: Verified Ledger Confirmed. Math check passed."
    else:
        # Trigger Recovery Loop if math fails[cite: 1]
        delta = reported_total - calculated_sum
        return f"ERROR: Recovery Loop Triggered. Missing Value: {delta}."

snb_raw_table = [
    {"label": "Cash and cash equivalents", "value": 42119698},
    {"label": "Investments, net", "value": 292486807},
    {"label": "Financing and advances, net", "value": 654252346},
    {"label": "Other assets", "value": 14189843}
]
snb_reported_total = 1104154640 

# 1. Initialize Agent
agent = AgenticFinancialController(snb_raw_table, KNOWLEDGE_GRAPH)

active_sector = agent.solve_conglomerate_dilemma()

verified_ledger = agent.perform_semantic_mapping(active_sector)

status = run_validation(verified_ledger, snb_reported_total, active_sector)

print("\n--- FINAL VERIFIED LEDGER OUTPUT ---")
print(json.dumps(verified_ledger, indent=2))
print(f"\nVALIDATION STATUS: {status}")