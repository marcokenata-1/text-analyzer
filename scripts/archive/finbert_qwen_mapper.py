"""
Two-Stage IFRS Tag Mapper — FinBERT + Qwen3 (Katana HPC Version)

Stage 1: FinBERT bi-encoder  → top 100 candidates (fast, ~5 mins total)
Stage 2: Qwen3 4B            → reasons about candidates, picks relevant ones

Why this is better than cross-encoder:
- Qwen3 understands IFRS domain context
- Qwen3 reasons about WHY a tag is relevant, not just similarity
- No manual blocklists needed
- More accurate than cosine similarity alone

Setup on Katana:
    module load python/3.11.3
    source ~/thesis_env/bin/activate
    pip install sentence-transformers transformers accelerate --user
"""

import json
import os
import re
import sys
import time
import torch
from pathlib import Path
from sentence_transformers import SentenceTransformer, util
from transformers import AutoModelForCausalLM, AutoTokenizer

from d_20230318          import definition as gics_definition
from ifrs_tags           import definition as ifrs_definition
from universal_ifrs_tags import UNIVERSAL_TAGS


# ── Config ─────────────────────────────────────────────────────────────────────
BIENCODER_MODEL = "ProsusAI/finbert"
LLM_MODEL       = "/srv/scratch/z5603945/hf_cache/Qwen3-14B"

OUTPUT_FILE     = "data/mappings/subindustry_ifrs_mapping_v4_qwen.json"
CHECKPOINT_FILE = "data/mappings/subindustry_ifrs_mapping_v4_checkpoint.json"

# Stage 1 — FinBERT candidates
BIENCODER_TOPK  = 100   # top 100 for Qwen3 to reason about

# Stage 2 — Qwen3 batch size
QWEN_BATCH_SIZE = 50    # tags per Qwen3 call
MAX_NEW_TOKENS  = 150

# Hard blocklist — final safety net
HARD_BLOCKLIST = [
    "CurrentPetroleumAndPetrochemicalProducts",
    "RevenueFromSaleOfPetroleumAndPetrochemicalProducts",
    "RevenueFromSaleOfOilAndGasProducts",
    "PurchaseOfOilAndGasAssets",
    "ProceedsFromDisposalOfOilAndGasAssets",
    "OilAndGasAssets", "PurchaseOfMiningAssets",
    "RevenueFromSaleOfAlcoholAndAlcoholicDrinks",
    "AssetsArisingFromExplorationForAndEvaluationOfMineralResources",
    "IncomeArisingFromExplorationForAndEvaluationOfMineralResources",
    "CashFlowsFromUsedInExplorationForAndEvaluationOfMineralResourcesClassifiedAsInvestingActivities",
    "CashFlowsFromUsedInExplorationForAndEvaluationOfMineralResourcesClassifiedAsOperatingActivities",
]
BLOCKLIST_EXEMPT = {"10", "15"}


# ── Helpers ────────────────────────────────────────────────────────────────────

def log(msg: str):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def camel_to_sentence(name: str) -> str:
    s = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', s)
    return s.strip()


def build_subindustry_description(si_code: str) -> str:
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


def apply_hard_blocklist(mapping: dict) -> dict:
    cleaned = {}
    removed = 0
    for si_code, tags in mapping.items():
        if si_code[:2] in BLOCKLIST_EXEMPT:
            cleaned[si_code] = tags
        else:
            filtered = [t for t in tags if t not in HARD_BLOCKLIST]
            removed += len(tags) - len(filtered)
            cleaned[si_code] = filtered
    log(f"Hard blocklist removed {removed} domain-impossible tags")
    return cleaned


# ── Qwen3 resolver ─────────────────────────────────────────────────────────────

class Qwen3Resolver:

    def __init__(self, device: str):
        log(f"Loading Qwen3 ({LLM_MODEL})...")
        self.tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
        self.model     = AutoModelForCausalLM.from_pretrained(
            LLM_MODEL,
            torch_dtype = torch.float16 if device == "cuda" else torch.float32,
            device_map  = "auto",
        )
        self.model.eval()
        log("Qwen3 loaded.")

    def resolve_batch(
        self,
        si_name: str,
        si_desc: str,
        batch: list,          # list of (tag_name, tag_label)
        batch_num: int,
        total_batches: int,
    ) -> list:
        """Ask Qwen3 which tags in this batch are relevant."""

        tag_list = "\n".join(
            f"{i+1}. {label}"
            for i, (_, label) in enumerate(batch)
        )

        prompt = f"""You are an IFRS financial reporting expert.

TASK: Select ONLY the IFRS tags below that are specifically relevant to this sub-industry.

Sub-industry: {si_name}
Description: {si_desc[:400]}

IMPORTANT RULES:
- Universal tags like Assets, Revenue, ProfitLoss, CashAndCashEquivalents are 
  already included separately — do NOT select them
- Only select tags a company in THIS specific sub-industry would report
- Reject tags that belong to other sectors (e.g. oil/gas tags for banks)
- Be inclusive — if a tag could plausibly appear in a financial statement 
 for this sub-industry, select it. It is better to include too many than too few.

IFRS tags (batch {batch_num}/{total_batches}):
{tag_list}

Return ONLY a JSON array of numbers e.g. [1, 4, 7] or []
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
                max_new_tokens = MAX_NEW_TOKENS,
                do_sample      = False,
                temperature    = 1.0,
                pad_token_id   = self.tokenizer.eos_token_id,
            )

        new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        raw        = self.tokenizer.decode(new_tokens, skip_special_tokens=True)
        numbers    = parse_numbers(raw, len(batch))
        return [batch[n-1][0] for n in numbers]

    def resolve_all_batches(
        self,
        si_name: str,
        si_desc: str,
        candidates: list,   # list of (tag_name, tag_label)
    ) -> list:
        """Split candidates into batches and resolve each."""
        accepted = []
        batches  = [
            candidates[i:i+QWEN_BATCH_SIZE]
            for i in range(0, len(candidates), QWEN_BATCH_SIZE)
        ]

        for idx, batch in enumerate(batches, 1):
            tags = self.resolve_batch(si_name, si_desc, batch, idx, len(batches))
            accepted.extend(tags)

        return list(set(accepted))


# ── Main mapper ────────────────────────────────────────────────────────────────

class FinBERTQwenMapper:

    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        log(f"Device: {device}")
        if device == "cuda":
            log(f"GPU: {torch.cuda.get_device_name(0)}")
            log(f"VRAM: {torch.cuda.get_device_properties(0).total_memory/1e9:.1f}GB")

        # Stage 1 — FinBERT
        log(f"Loading FinBERT ({BIENCODER_MODEL})...")
        self.biencoder = SentenceTransformer(BIENCODER_MODEL, device=device)

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

        log("Embedding tag pool with FinBERT...")
        self.tag_embs = self.biencoder.encode(
            self.tag_labels,
            convert_to_tensor = True,
            batch_size        = 256,
            show_progress_bar = False,
        )
        log("FinBERT ready.")

        # Stage 2 — Qwen3
        self.qwen = Qwen3Resolver(device)

    def get_finbert_candidates(self, si_desc: str) -> list:
        """Stage 1: FinBERT top-K candidates."""
        si_emb = self.biencoder.encode(si_desc, convert_to_tensor=True)
        scores = util.cos_sim(si_emb, self.tag_embs)[0].tolist()
        top_k  = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:BIENCODER_TOPK]
        return [(self.tag_keys[i], self.tag_labels[i]) for i, _ in top_k]

    def map_subindustry(self, si_code: str) -> list:
        si_data    = gics_definition.get(si_code, {})
        si_name    = si_data.get("name", si_code)
        si_desc    = build_subindustry_description(si_code)

        # Stage 1: FinBERT candidates
        candidates = self.get_finbert_candidates(si_desc)

        # Stage 2: Qwen3 reasoning
        accepted   = self.qwen.resolve_all_batches(si_name, si_desc, candidates)

        return sorted(accepted)

    def map_all(self, checkpoint: dict = None) -> dict:
        subindustries = {k: v for k, v in gics_definition.items() if len(k) == 8}
        total_si      = len(subindustries)
        mapping       = checkpoint or {}

        log(f"Mapping {total_si} SubIndustries — FinBERT + Qwen3")
        log(f"Stage 1: FinBERT top-{BIENCODER_TOPK} candidates")
        log(f"Stage 2: Qwen3 batches of {QWEN_BATCH_SIZE}\n")

        for idx, (si_code, si_data) in enumerate(subindustries.items(), 1):
            if si_code in mapping:
                continue

            si_name = si_data.get("name", si_code)
            t_start = time.time()

            tags = self.map_subindustry(si_code)
            mapping[si_code] = tags

            elapsed  = time.time() - t_start
            n_batches = (BIENCODER_TOPK + QWEN_BATCH_SIZE - 1) // QWEN_BATCH_SIZE
            log(f"[{idx:3d}/{total_si}] {si_name[:40]:40s} "
                f"candidates={BIENCODER_TOPK} batches={n_batches} "
                f"→ {len(tags)} tags ({elapsed:.1f}s)")

            # Save checkpoint
            with open(CHECKPOINT_FILE, "w") as f:
                json.dump(mapping, f)

        return mapping


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    log("=" * 60)
    log("FinBERT + Qwen3 IFRS Tag Mapper — Katana HPC")
    log("=" * 60)
    log(f"Python:  {sys.version.split()[0]}")
    log(f"PyTorch: {torch.__version__}")

    # Resume from checkpoint
    checkpoint = {}
    if Path(CHECKPOINT_FILE).exists():
        with open(CHECKPOINT_FILE) as f:
            checkpoint = json.load(f)
        log(f"Resuming from checkpoint — {len(checkpoint)} done")

    # Run
    mapper  = FinBERTQwenMapper()
    mapping = mapper.map_all(checkpoint=checkpoint)

    # Apply hard blocklist
    mapping = apply_hard_blocklist(mapping)

    # Save
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


if __name__ == "__main__":
    main()