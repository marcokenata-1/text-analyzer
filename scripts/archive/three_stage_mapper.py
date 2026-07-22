"""
Three-Stage IFRS Tag Mapper

Stage 1: FinBERT bi-encoder    → top 150 candidates (fast, broad)
Stage 2: Cross-encoder         → filters to top 30-50 (precise, no blocklists)
Stage 3: Ollama/Qwen grey zone → resolves ambiguous cases (smart)

No manual blocklists needed — cross-encoder handles wrong sector tags
automatically by scoring (SubIndustry description, IFRS tag label) pairs.

Setup:
    pip install sentence-transformers
    ollama pull llama3.1  (optional, for Stage 3)
"""

import json
import re
import ollama
import torch
from sentence_transformers import SentenceTransformer, CrossEncoder, util

from d_20230318          import definition as gics_definition
from ifrs_tags           import definition as ifrs_definition
from universal_ifrs_tags import UNIVERSAL_TAGS


# ── Config ─────────────────────────────────────────────────────────────────────
BIENCODER_MODEL    = "ProsusAI/finbert"
CROSSENCODER_MODEL = "cross-encoder/stsb-roberta-base"  # semantic similarity, not search
OLLAMA_MODEL       = "llama3.1"

OUTPUT_FILE = "data/mappings/subindustry_ifrs_mapping_v3.json"

# Stage 1 — FinBERT
BIENCODER_TOPK     = 150    # keep top 150 candidates

# Stage 2 — Cross-encoder thresholds
# Calibrated from test scores:
#   0.494 = Oil & Gas → Oil and gas assets       (relevant)
#   0.567 = Banks → Deposits from customers          HIGH ✅
#   0.398 = Banks → Loans and advances               HIGH ✅
#   0.158 = Banks → Allowance credit losses          GREY ⚠️
#   0.147 = Oil  → Revenue from sale of crude oil    GREY ⚠️
#   0.059 = Oil  → Fuel and energy expense           GREY ⚠️
#   0.040 = CE   → Raw materials                     GREY ⚠️
#   0.009 = CE   → Warranty provision                GREY ⚠️
#   0.003 = CE   → Petroleum products                REJECT ❌
#   0.002 = CE   → R&D expense                       REJECT ❌
CE_HIGH        = 0.40   # auto-accept — only very obvious pairs
CE_GREY_LOW    = 0.005  # grey zone — everything above noise goes to Ollama
# Below 0.005 → reject (clearly wrong sector tags)

# Stage 3 — Ollama
USE_OLLAMA         = True
MAX_GREY_TO_OLLAMA = 30


# ── Helpers ────────────────────────────────────────────────────────────────────

def camel_to_sentence(name: str) -> str:
    s = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', s)
    return s.strip()


def build_subindustry_description(si_code: str) -> str:
    """Rich description including parent hierarchy context."""
    data          = gics_definition.get(si_code, {})
    name          = data.get("name", "")
    desc          = data.get("description", "")
    industry_name = gics_definition.get(si_code[:6], {}).get("name", "")
    ig_name       = gics_definition.get(si_code[:4], {}).get("name", "")
    sector_name   = gics_definition.get(si_code[:2], {}).get("name", "")
    return (f"Sector: {sector_name}. "
            f"Industry Group: {ig_name}. "
            f"Industry: {industry_name}. "
            f"Sub-industry: {name}. "
            f"Description: {desc}")


def is_disclosure_tag(tag: str) -> bool:
    """Filter out note disclosure / movement table tags."""
    PREFIXES = [
        "Retirements", "Disposals", "Additions", "Transfers",
        "Settlements", "Reclassification", "PurchasesFairValue",
        "FairValueOf", "FairValueGainsLosses", "MaximumExposureTo",
        "DescriptionOf", "OtherCashPaymentsToAcquire",
        "OtherCashReceiptsFromSales", "ProceedsFromGovernmentGrants",
        "ProceedsFromOther", "ProceedsIncludedInProfitOrLoss",
        "ProceedsFromDisposals", "ProceedsFromSalesOf",
        "ProceedsFromSalesOr", "PurchaseOfOther",
        "PurchaseOfExploration", "PurchaseOfInterests",
        "PurchaseOfProperty", "PurchaseOfIntangible",
        "MeasurementPeriod", "IncomeTaxRelatingToShare",
        "IncomeTaxRelatingToInvestments",
        "ShareOfOtherComprehensiveIncome", "ShareOfTotalComprehensive",
        "OtherWorkPerformed", "IssueCostsNot",
        "AcquisitionrelatedCosts", "AcquisitionsThroughBusinessCombinations",
        "CustomerrelatedIntangible", "TechnologybasedIntangible",
        "IntangibleAssetsAcquiredByWayOfGovernment",
        "ContractualCommitmentsFor", "DecreaseThroughTransfer",
        "PropertyPlantAndEquipmentCarrying",
        "CashFlowsUsedInObtainingControl",
        "CashPaymentsForFutureContracts", "CashReceiptsFromFutureContracts",
        "CashReceiptsFromRepaymentOf", "CashAdvancesAndLoans",
        "ParticipationIn", "CommitmentsFor", "RecognisedAssets",
        "ReserveOfGains", "ProfitLossAttributableToParticipating",
        "ProfitLossFromDiscontinuedOperations",
        "DividendsRecognisedAsDistributions", "DividendsPaidToEquity",
        "DividendsReceivedFrom", "FinancialAssetsReclassified",
        "FinancialAssetsThatWere", "FinancialAssetsWhose",
        "FinancialLiabilitiesThatWere", "SalesOfProperty",
        "PurchasesOfProperty", "TransferFromTo",
    ]
    SUFFIXES = [
        "FairValueHierarchy", "RelatedPartyTransaction",
        "WherePriceQuotationsPublished",
        "ThatAreNotDerecognisedInTheirEntirety",
        "HedgingRelationshipsForWhichHedgeAccountingIsNoLongerApplied",
        "InRelationToStructuredEntities",
        "BeforeApplicationOfIFRS17",
        "BeforeApplicationOfAmendmentsToIFRS9MadeByIFRS17",
        "IncludingRightofuseAssets",
    ]
    for p in PREFIXES:
        if tag.startswith(p):
            return True
    for s in SUFFIXES:
        if tag.endswith(s):
            return True
    return False


def parse_numbers(raw: str, max_n: int) -> list:
    """Parse JSON array of numbers from LLM response."""
    raw = re.sub(r'<think>.*?</think>', '', raw, flags=re.DOTALL).strip()
    start = raw.find("[")
    end   = raw.rfind("]")
    if start == -1 or end == -1:
        return []
    try:
        numbers = json.loads(raw[start:end+1].strip())
        return [n for n in numbers if isinstance(n, int) and 1 <= n <= max_n]
    except Exception:
        return []


def ollama_resolve(si_name: str, si_desc: str, grey_tags: list) -> list:
    """
    Stage 3: Ask Ollama to resolve genuinely ambiguous grey zone tags.
    Only called for 10-30 tags — small, fast, focused.
    """
    if not grey_tags:
        return []

    tag_list = "\n".join(
        f"{i+1}. {label} (cross-encoder score={score:.3f})"
        for i, (_, label, score) in enumerate(grey_tags)
    )

    prompt = f"""You are an IFRS financial reporting expert.

Sub-industry: {si_name}
Description: {si_desc[:300]}

These IFRS tags scored in the borderline range (0.3-0.5) from a cross-encoder.
They may or may not be relevant to this specific sub-industry.

Universal tags like Assets, Revenue, ProfitLoss are already included separately.
Select ONLY tags that are clearly and specifically relevant to this sub-industry.

Tags to evaluate:
{tag_list}

Return ONLY a JSON array of numbers e.g. [1, 3] or []
/no_think"""

    try:
        response = ollama.chat(
            model   = OLLAMA_MODEL,
            messages= [{"role": "user", "content": prompt}],
            options = {"temperature": 0.0, "think": False},
        )
        raw     = response["message"]["content"].strip()
        numbers = parse_numbers(raw, len(grey_tags))
        return [grey_tags[n-1][0] for n in numbers]
    except Exception as e:
        print(f"          Ollama error: {e}")
        return []


# ── Three-stage mapper ─────────────────────────────────────────────────────────

class ThreeStageMapper:

    def __init__(self):
        print(f"[Setup] Loading FinBERT bi-encoder ({BIENCODER_MODEL})...")
        self.biencoder    = SentenceTransformer(BIENCODER_MODEL)

        print(f"[Setup] Loading cross-encoder ({CROSSENCODER_MODEL})...")
        self.crossencoder = CrossEncoder(CROSSENCODER_MODEL)

        # Pre-filter tag pool — exclude universals and disclosure tags
        self.tag_keys   = []
        self.tag_labels = []
        for name, meta in ifrs_definition.items():
            if name in UNIVERSAL_TAGS:
                continue
            if is_disclosure_tag(name):
                continue
            label = camel_to_sentence(name)
            self.tag_keys.append(name)
            self.tag_labels.append(label)

        print(f"[Setup] Tag pool: {len(self.tag_keys)} "
              f"(from {len(ifrs_definition)} total, "
              f"excluded {len(UNIVERSAL_TAGS)} universal + disclosure tags)")

        print(f"[Setup] Embedding tag pool with FinBERT...")
        self.tag_embs = self.biencoder.encode(
            self.tag_labels,
            convert_to_tensor  = True,
            show_progress_bar  = True,
            batch_size         = 64,
        )
        print("[Setup] Done.\n")

    def map_subindustry(self, si_code: str) -> dict:
        """
        Run three-stage mapping for one SubIndustry.
        Returns dict with stage breakdown and final tags.
        """
        si_data = gics_definition.get(si_code, {})
        si_name = si_data.get("name", si_code)
        si_desc = build_subindustry_description(si_code)

        # ── Stage 1: FinBERT bi-encoder ───────────────────────────────
        si_emb  = self.biencoder.encode(si_desc, convert_to_tensor=True)
        scores  = util.cos_sim(si_emb, self.tag_embs)[0].tolist()

        # Get top-K candidates
        top_k = sorted(
            enumerate(scores), key=lambda x: x[1], reverse=True
        )[:BIENCODER_TOPK]

        stage1_candidates = [(self.tag_keys[i], self.tag_labels[i], s)
                             for i, s in top_k]

        # ── Stage 2: Cross-encoder reranking ──────────────────────────
        pairs = [(si_desc, label) for _, label, _ in stage1_candidates]
        ce_scores = self.crossencoder.predict(pairs).tolist()

        high_tags = []
        grey_tags = []
        rejected  = 0

        for (tag, label, bi_score), ce_score in zip(stage1_candidates, ce_scores):
            if ce_score >= CE_HIGH:
                high_tags.append(tag)
            elif ce_score >= CE_GREY_LOW:
                grey_tags.append((tag, label, ce_score))
            else:
                rejected += 1

        # ── Stage 3: Ollama grey zone resolution ──────────────────────
        ollama_accepted = []
        if USE_OLLAMA and grey_tags:
            # Sort grey zone by CE score descending — best first
            grey_tags.sort(key=lambda x: x[2], reverse=True)
            # Cap to avoid sending too many to Ollama
            grey_subset = grey_tags[:MAX_GREY_TO_OLLAMA]
            ollama_accepted = ollama_resolve(si_name, si_desc, grey_subset)

        final_tags = sorted(set(high_tags + ollama_accepted))

        return {
            "tags":             final_tags,
            "stage1_candidates": len(stage1_candidates),
            "stage2_high":      len(high_tags),
            "stage2_grey":      len(grey_tags),
            "stage2_rejected":  rejected,
            "stage3_accepted":  len(ollama_accepted),
        }

    def map_all(self) -> dict:
        """Map all 163 SubIndustries."""
        subindustries = {k: v for k, v in gics_definition.items() if len(k) == 8}
        total_si      = len(subindustries)
        mapping       = {}

        print(f"Mapping {total_si} SubIndustries — three-stage pipeline\n")
        print(f"  Stage 1: FinBERT top-{BIENCODER_TOPK} candidates")
        print(f"  Stage 2: Cross-encoder (accept >{CE_HIGH}, grey {CE_GREY_LOW}-{CE_HIGH})")
        print(f"  Stage 3: Ollama grey zone (max {MAX_GREY_TO_OLLAMA} per SI)\n")

        for idx, (si_code, si_data) in enumerate(subindustries.items(), 1):
            si_name = si_data.get("name", si_code)
            print(f"  [{idx:3d}/{total_si}] {si_name[:40]:40s}", end=" ", flush=True)

            result = self.map_subindustry(si_code)
            mapping[si_code] = result["tags"]

            grey_info = (f"  grey={result['stage2_grey']}→{result['stage3_accepted']}"
                         if USE_OLLAMA and result["stage2_grey"] > 0 else "")
            print(f"S1={result['stage1_candidates']} "
                  f"S2={result['stage2_high']} "
                  f"reject={result['stage2_rejected']}"
                  f"{grey_info} "
                  f"→ {len(result['tags'])} final")

        return mapping


# ── Analysis ───────────────────────────────────────────────────────────────────

def analyse(mapping: dict):
    total_si   = len(mapping)
    total_tags = sum(len(v) for v in mapping.values())
    avg        = total_tags / total_si

    print(f"\n{'='*55}")
    print(f"MAPPING SUMMARY")
    print(f"{'='*55}")
    print(f"  Sub-industries:  {total_si}")
    print(f"  Total edges:     {total_tags}")
    print(f"  Average/SI:      {avg:.1f}")
    print(f"  Min:             {min(len(v) for v in mapping.values())}")
    print(f"  Max:             {max(len(v) for v in mapping.values())}")
    zeros = [k for k, v in mapping.items() if len(v) == 0]
    print(f"  Zero tag SIs:    {len(zeros)}")

    print(f"\n  Financials sub-industries:")
    for code, tags in sorted(mapping.items()):
        if code.startswith("40"):
            si_name = gics_definition.get(code, {}).get("name", code)
            print(f"    [{code}] {si_name:35s} {len(tags):3d} tags")

    # Consumer Electronics check
    ce = mapping.get("25201010", [])
    print(f"\n  Consumer Electronics [25201010]: {len(ce)} tags")
    for t in sorted(ce):
        print(f"    {t}")

    # Regional Banks check
    rb = mapping.get("40101015", [])
    print(f"\n  Regional Banks [40101015]: {len(rb)} tags")
    for t in sorted(rb):
        print(f"    {t}")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Three-Stage IFRS Tag Mapper")
    print("=" * 60)

    mapper  = ThreeStageMapper()
    mapping = mapper.map_all()

    # Save
    with open(OUTPUT_FILE, "w") as f:
        json.dump(mapping, f, indent=2)
    print(f"\nSaved to {OUTPUT_FILE}")

    # Analyse
    analyse(mapping)

    print(f"\n{'='*60}")
    print("Next step: load into GraphDB")
    print("  Set OUTPUT_JSON = 'data/mappings/subindustry_ifrs_mapping_v3.json'")
    print("  Set SKIP_FINBERT = True")
    print("  Run: python build_graphdb.py")
    print("=" * 60)


if __name__ == "__main__":
    main()