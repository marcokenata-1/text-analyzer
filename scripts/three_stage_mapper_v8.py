"""
Three-Stage IFRS Tag Mapper v8 — Katana HPC
============================================
Key changes from v3 katana (best so far):
- BIENCODER_TOPK = 400  (was 150) — wider FinBERT net
- CE_HIGH        = 0.50 (was 0.40) — stricter cross-encoder
- CE_GREY_LOW    = 0.30 (was 0.02) — tighter grey zone
- LLM_MODEL      = Qwen3-14B (was Qwen3-4B) — better reasoning

Rationale:
  v3 katana top-150 misses valid tags ranked 151-400 by FinBERT
  Stricter cross-encoder compensates for wider FinBERT net
  Expected: 60-120 tags/SI (vs 34.5 in v3)

Stage 1: FinBERT bi-encoder  → top 400 candidates
Stage 2: Cross-encoder       → CE >= 0.50 auto-accept, 0.30-0.50 grey zone
Stage 3: Qwen3-14B           → resolves grey zone (max 15 tags)
"""

import json
import re
import sys
import time
import torch
from pathlib import Path
from sentence_transformers import SentenceTransformer, CrossEncoder, util
from transformers import AutoModelForCausalLM, AutoTokenizer

from d_20230318          import definition as gics_definition
from ifrs_tags           import definition as ifrs_definition
from universal_ifrs_tags import UNIVERSAL_TAGS


# ── Config ─────────────────────────────────────────────────────────────────────
BIENCODER_MODEL    = "ProsusAI/finbert"
CROSSENCODER_MODEL = "cross-encoder/stsb-roberta-base"
LLM_MODEL          = "/srv/scratch/z5603945/hf_cache/Qwen3-14B"

OUTPUT_FILE     = "subindustry_ifrs_mapping_v8.json"
CHECKPOINT_FILE = "subindustry_ifrs_mapping_v8_checkpoint.json"

# Stage 1 — FinBERT wider net
BIENCODER_TOPK  = 400   # was 150 in v3

# Stage 2 — Stricter cross-encoder to compensate
CE_HIGH         = 0.50  # was 0.40 in v3
CE_GREY_LOW     = 0.30  # was 0.02 in v3 — tighter grey zone
# Below 0.30 → reject automatically

# Stage 3 — Qwen3-14B grey zone
USE_LLM         = True
MAX_GREY_TO_LLM = 15


# ── Helpers ────────────────────────────────────────────────────────────────────

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def camel_to_sentence(name):
    s = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', s)
    return s.strip()


def build_subindustry_description(si_code):
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


def is_disclosure_tag(tag):
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
        "IncreaseDecrease", "IncreaseThroughOriginationOrPurchase",
        "DecreaseThroughDerecognition", "DecreaseThroughLossOfControl",
        "DecreaseThroughClassifiedAsHeldForSale",
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
        "RecognisedAsOfAcquisitionDate",
        "ClassifiedAsOfAcquisitionDate",
    ]
    for p in PREFIXES:
        if tag.startswith(p):
            return True
    for s in SUFFIXES:
        if tag.endswith(s):
            return True
    return False


def parse_numbers(raw, max_n):
    raw = re.sub(r'<think>.*?</think>', '', raw, flags=re.DOTALL).strip()
    start = raw.find("[")
    end   = raw.rfind("]")
    if start == -1 or end == -1:
        return []
    try:
        nums = json.loads(raw[start:end+1].strip())
        return [n for n in nums if isinstance(n, int) and 1 <= n <= max_n]
    except Exception:
        return []


# ── Stage 3: Qwen3-14B ────────────────────────────────────────────────────────

class Qwen3Resolver:

    def __init__(self, device):
        log(f"Loading Qwen3-14B from {LLM_MODEL}...")
        self.tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
        self.model     = AutoModelForCausalLM.from_pretrained(
            LLM_MODEL,
            torch_dtype = torch.float16 if device == "cuda" else torch.float32,
            device_map  = "auto",
        )
        self.model.eval()
        log("Qwen3-14B loaded.")

    def resolve(self, si_name, si_desc, grey_tags):
        """Resolve grey zone tags — SELECT mode on small set (max 15)."""
        if not grey_tags:
            return []

        tag_list = "\n".join(
            f"{i+1}. {label} (score={score:.3f})"
            for i, (_, label, score) in enumerate(grey_tags)
        )

        prompt = f"""You are an IFRS financial reporting expert.

Sub-industry: {si_name}
Description: {si_desc[:350]}

These IFRS tags scored 0.30-0.50 on a semantic similarity cross-encoder
— borderline relevant. Universal tags like Assets, Revenue, ProfitLoss
are already included separately.

Select ONLY tags that would specifically appear as line items in a
financial statement for this sub-industry.

Tags:
{tag_list}

Return ONLY a JSON array of numbers e.g. [1, 3] or []
Do not explain. Just the array."""

        inputs = self.tokenizer(
            prompt,
            return_tensors = "pt",
            truncation     = True,
            max_length     = 2048,
        ).to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens = 100,
                do_sample      = False,
                temperature    = 1.0,
                pad_token_id   = self.tokenizer.eos_token_id,
            )

        new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        raw        = self.tokenizer.decode(new_tokens, skip_special_tokens=True)
        numbers    = parse_numbers(raw, len(grey_tags))
        return [grey_tags[n-1][0] for n in numbers]


# ── Main mapper ────────────────────────────────────────────────────────────────

class ThreeStageMapper:

    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        log(f"Device: {device}")
        if device == "cuda":
            log(f"GPU:  {torch.cuda.get_device_name(0)}")
            log(f"VRAM: {torch.cuda.get_device_properties(0).total_memory/1e9:.1f}GB")

        # Build filtered tag pool
        self.tag_keys   = []
        self.tag_labels = []
        for name in ifrs_definition:
            if name in UNIVERSAL_TAGS:
                continue
            if is_disclosure_tag(name):
                continue
            self.tag_keys.append(name)
            self.tag_labels.append(camel_to_sentence(name))

        log(f"Tag pool: {len(self.tag_keys)} tags "
            f"(excluded {len(UNIVERSAL_TAGS)} universal + disclosure)")

        # Stage 1 — FinBERT
        log(f"Loading FinBERT ({BIENCODER_MODEL})...")
        self.biencoder = SentenceTransformer(BIENCODER_MODEL, device=device)
        log("Embedding tag pool...")
        self.tag_embs = self.biencoder.encode(
            self.tag_labels,
            convert_to_tensor = True,
            batch_size        = 256,
            show_progress_bar = False,
        )
        log("FinBERT ready.")

        # Stage 2 — Cross-encoder
        log(f"Loading cross-encoder ({CROSSENCODER_MODEL})...")
        self.crossencoder = CrossEncoder(CROSSENCODER_MODEL, device=device)
        log("Cross-encoder ready.")

        # Stage 3 — Qwen3-14B
        self.llm = Qwen3Resolver(device) if USE_LLM else None

    def map_subindustry(self, si_code):
        si_data = gics_definition.get(si_code, {})
        si_name = si_data.get("name", si_code)
        si_desc = build_subindustry_description(si_code)

        # Stage 1: FinBERT top-400
        si_emb = self.biencoder.encode(si_desc, convert_to_tensor=True)
        scores = util.cos_sim(si_emb, self.tag_embs)[0].tolist()
        top_k  = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:BIENCODER_TOPK]
        candidates = [(self.tag_keys[i], self.tag_labels[i]) for i, _ in top_k]

        # Stage 2: Cross-encoder filter
        pairs     = [(si_desc, label) for _, label in candidates]
        ce_scores = self.crossencoder.predict(pairs, batch_size=64).tolist()

        high_tags = []
        grey_tags = []
        rejected  = 0

        for (tag, label), ce_score in zip(candidates, ce_scores):
            if ce_score >= CE_HIGH:
                high_tags.append(tag)
            elif ce_score >= CE_GREY_LOW:
                grey_tags.append((tag, label, ce_score))
            else:
                rejected += 1

        # Stage 3: Qwen3-14B grey zone
        llm_tags = []
        if self.llm and grey_tags:
            grey_tags.sort(key=lambda x: x[2], reverse=True)
            grey_subset = grey_tags[:MAX_GREY_TO_LLM]
            llm_tags    = self.llm.resolve(si_name, si_desc, grey_subset)

        return {
            "tags":      sorted(set(high_tags + llm_tags)),
            "s1_total":  len(candidates),
            "s2_high":   len(high_tags),
            "s2_grey":   len(grey_tags),
            "s2_reject": rejected,
            "s3_kept":   len(llm_tags),
        }

    def map_all(self, checkpoint=None):
        subindustries = {k: v for k, v in gics_definition.items() if len(k) == 8}
        total_si      = len(subindustries)
        mapping       = checkpoint or {}

        log(f"Mapping {total_si} SubIndustries — three-stage pipeline v8")
        log(f"  Stage 1: FinBERT top-{BIENCODER_TOPK}")
        log(f"  Stage 2: CE >= {CE_HIGH} accept, {CE_GREY_LOW}-{CE_HIGH} grey zone")
        log(f"  Stage 3: Qwen3-14B (max {MAX_GREY_TO_LLM} grey tags)\n")

        for idx, (si_code, si_data) in enumerate(subindustries.items(), 1):
            if si_code in mapping:
                continue

            si_name = si_data.get("name", si_code)
            t_start = time.time()
            result  = self.map_subindustry(si_code)
            mapping[si_code] = result["tags"]

            elapsed = time.time() - t_start
            log(f"[{idx:3d}/{total_si}] {si_name[:38]:38s} "
                f"S2={result['s2_high']:3d} grey={result['s2_grey']:3d}"
                f"→{result['s3_kept']:2d} "
                f"reject={result['s2_reject']:3d} "
                f"→ {len(result['tags']):3d} tags ({elapsed:.1f}s)")

            with open(CHECKPOINT_FILE, "w") as f:
                json.dump(mapping, f)

        return mapping


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    log("=" * 65)
    log("Three-Stage IFRS Tag Mapper v8 — Katana HPC")
    log(f"  FinBERT top-{BIENCODER_TOPK} → CE >= {CE_HIGH} → Qwen3-14B grey zone")
    log("=" * 65)
    log(f"Python: {sys.version.split()[0]}  PyTorch: {torch.__version__}")

    checkpoint = {}
    if Path(CHECKPOINT_FILE).exists():
        with open(CHECKPOINT_FILE) as f:
            checkpoint = json.load(f)
        log(f"Resuming from checkpoint — {len(checkpoint)}/163 done")

    mapper  = ThreeStageMapper()
    mapping = mapper.map_all(checkpoint=checkpoint)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(mapping, f, indent=2)
    log(f"Saved to {OUTPUT_FILE}")

    # Summary
    total_tags = sum(len(v) for v in mapping.values())
    zeros      = [k for k, v in mapping.items() if len(v) == 0]
    log(f"\nSUMMARY")
    log(f"  Sub-industries:  {len(mapping)}")
    log(f"  Total edges:     {total_tags}")
    log(f"  Average/SI:      {total_tags/len(mapping):.1f}")
    log(f"  Min:             {min(len(v) for v in mapping.values())}")
    log(f"  Max:             {max(len(v) for v in mapping.values())}")
    log(f"  Zero tag SIs:    {len(zeros)}")

    log("\nFinancials sub-industries:")
    for code, tags in sorted(mapping.items()):
        if code.startswith("40"):
            name = gics_definition.get(code, {}).get("name", code)
            log(f"  [{code}] {name:35s} {len(tags):3d} tags")

    log("\nRegional Banks [40101015]:")
    for t in sorted(mapping.get("40101015", [])):
        log(f"  {t}")

    log("\nConsumer Electronics [25201010]:")
    for t in sorted(mapping.get("25201010", [])):
        log(f"  {t}")

    # Wrong tag check
    WRONG  = ["CurrentPetroleumAndPetrochemicalProducts",
               "OilAndGasAssets", "BiologicalAssets",
               "RevenueFromSaleOfAlcoholAndAlcoholicDrinks"]
    EXEMPT = {"10", "15"}
    flagged = 0
    for code, tags in mapping.items():
        if code[:2] in EXEMPT:
            continue
        for tag in tags:
            if tag in WRONG:
                log(f"  ❌ WRONG [{code}] {tag}")
                flagged += 1
    if flagged == 0:
        log("\n✅ No wrong tags found!")


if __name__ == "__main__":
    main()
