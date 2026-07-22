"""
FinBERT + Qwen3-14B IFRS Tag Mapper v5 — Katana HPC
====================================================
Maps all 163 GICS SubIndustries to IFRS XBRL tags.

Key improvements over v3:
- Qwen3-14B loaded from local scratch (no download)
- REMOVE mode prompt — keeps tags by default, only removes clearly wrong ones
- All 1,800 non-disclosure tags sent to Qwen3 (no FinBERT top-K cutoff)
- Hard blocklist as final safety net
- Checkpoint saves after every SubIndustry
- Output: subindustry_ifrs_mapping_v5.json

Usage on Katana:
    qsub run_v5.pbs
"""

import json
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

OUTPUT_FILE     = "data/mappings/subindustry_ifrs_mapping_v5.json"
CHECKPOINT_FILE = "data/mappings/subindustry_ifrs_mapping_v5_checkpoint.json"

# FinBERT used for ordering only — Qwen3 sees all non-disclosure tags
BIENCODER_TOPK  = 1800  # effectively all non-disclosure tags
QWEN_BATCH_SIZE = 50    # tags per Qwen3 call
MAX_NEW_TOKENS  = 200

# Hard blocklist disabled — Qwen3-14B handles domain filtering
# If wrong tags appear after results, add them here as evidence
HARD_BLOCKLIST   = []
BLOCKLIST_EXEMPT = set()


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
    """Filter out note disclosure and movement table tags."""
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


def parse_numbers(raw, max_n):
    """Parse JSON array from Qwen3 output, stripping think tags."""
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


def apply_hard_blocklist(mapping):
    """Final safety net — disabled when HARD_BLOCKLIST is empty."""
    if not HARD_BLOCKLIST:
        log("Hard blocklist disabled — Qwen3-14B handles domain filtering")
        return mapping
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


# ── Qwen3-14B Resolver ─────────────────────────────────────────────────────────

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

    def resolve_batch(self, si_name, si_desc, batch, batch_num, total_batches):
        """
        REMOVE mode — ask Qwen3 to identify wrong tags to remove.
        Default is KEEP — only removes clearly wrong sector tags.
        """
        tag_list = "\n".join(
            f"{i+1}. {label}"
            for i, (_, label) in enumerate(batch)
        )

        prompt = f"""You are an IFRS financial reporting expert.

Sub-industry: {si_name}
Description: {si_desc[:400]}

The IFRS tags below were selected as potentially relevant to this sub-industry.
Your job is to REMOVE only tags that are CLEARLY WRONG for this sub-industry.

A tag is CLEARLY WRONG only if it belongs to a completely different sector:
- oil/gas/petroleum/mining tags for a bank → REMOVE
- banking/loan/deposit tags for an oil company → REMOVE  
- agricultural/biological tags for a tech company → REMOVE
- insurance-specific tags for a retail company → REMOVE

DO NOT remove tags just because they seem uncommon or niche.
DO NOT remove tags that could appear in ANY company in this sub-industry.
When in doubt → KEEP the tag.
Universal tags like Assets, Revenue, ProfitLoss are already excluded separately.

IFRS tags (batch {batch_num}/{total_batches}):
{tag_list}

Return a JSON array of NUMBER(S) to REMOVE, or [] to keep all.
Example: [2, 7] means remove tags 2 and 7 from this batch.
Do not explain. Just the array."""

        inputs = self.tokenizer(
            prompt,
            return_tensors = "pt",
            truncation     = True,
            max_length     = 3000,
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

        # REMOVE mode — keep tags NOT in remove list
        remove_set = set(numbers)
        kept = [batch[i][0] for i in range(len(batch)) if (i+1) not in remove_set]
        return kept

    def resolve_all_batches(self, si_name, si_desc, candidates):
        """Process all batches and collect kept tags."""
        kept    = []
        batches = [candidates[i:i+QWEN_BATCH_SIZE]
                   for i in range(0, len(candidates), QWEN_BATCH_SIZE)]
        for idx, batch in enumerate(batches, 1):
            tags = self.resolve_batch(si_name, si_desc, batch, idx, len(batches))
            kept.extend(tags)
        return list(set(kept))


# ── Main Mapper ────────────────────────────────────────────────────────────────

class FinBERTQwen14BMapper:

    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        log(f"Device: {device}")
        if device == "cuda":
            log(f"GPU:  {torch.cuda.get_device_name(0)}")
            log(f"VRAM: {torch.cuda.get_device_properties(0).total_memory/1e9:.1f}GB")

        # Build filtered tag pool (exclude universal + disclosure)
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
            f"(excluded {len(UNIVERSAL_TAGS)} universal + disclosure tags)")

        # FinBERT for ordering candidates by relevance
        log(f"Loading FinBERT ({BIENCODER_MODEL})...")
        self.biencoder = SentenceTransformer(BIENCODER_MODEL, device=device)
        log("Embedding tag pool with FinBERT...")
        self.tag_embs = self.biencoder.encode(
            self.tag_labels,
            convert_to_tensor = True,
            batch_size        = 256,
            show_progress_bar = False,
        )
        log("FinBERT ready.")

        # Qwen3-14B for relevance filtering
        self.qwen = Qwen3Resolver(device)

    def get_candidates(self, si_desc):
        """
        Use FinBERT to ORDER tags by relevance.
        Return all tags sorted by similarity score (most relevant first).
        Qwen3 then decides which to keep.
        """
        si_emb = self.biencoder.encode(si_desc, convert_to_tensor=True)
        scores = util.cos_sim(si_emb, self.tag_embs)[0].tolist()

        # Sort all tags by FinBERT score — most relevant first
        sorted_idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

        # Apply BIENCODER_TOPK if set (1800 = effectively all)
        topk = sorted_idx[:BIENCODER_TOPK]
        return [(self.tag_keys[i], self.tag_labels[i]) for i in topk]

    def map_subindustry(self, si_code):
        si_data    = gics_definition.get(si_code, {})
        si_name    = si_data.get("name", si_code)
        si_desc    = build_subindustry_description(si_code)
        candidates = self.get_candidates(si_desc)
        kept       = self.qwen.resolve_all_batches(si_name, si_desc, candidates)
        return sorted(kept)

    def map_all(self, checkpoint=None):
        subindustries = {k: v for k, v in gics_definition.items() if len(k) == 8}
        total_si      = len(subindustries)
        mapping       = checkpoint or {}

        n_batches = (min(BIENCODER_TOPK, len(self.tag_keys)) + QWEN_BATCH_SIZE - 1) \
                    // QWEN_BATCH_SIZE

        log(f"Mapping {total_si} SubIndustries")
        log(f"  Tag pool:    {len(self.tag_keys)} tags per SubIndustry")
        log(f"  Batches:     {n_batches} per SubIndustry")
        log(f"  Mode:        REMOVE (Qwen3 removes wrong tags, keeps the rest)")
        log(f"  Checkpoint:  {CHECKPOINT_FILE}\n")

        for idx, (si_code, si_data) in enumerate(subindustries.items(), 1):
            if si_code in mapping:
                continue

            si_name = si_data.get("name", si_code)
            t_start = time.time()

            tags    = self.map_subindustry(si_code)
            mapping[si_code] = tags

            elapsed = time.time() - t_start
            log(f"[{idx:3d}/{total_si}] {si_name[:40]:40s} "
                f"batches={n_batches} → {len(tags)} tags ({elapsed:.1f}s)")

            # Save checkpoint after every SubIndustry
            with open(CHECKPOINT_FILE, "w") as f:
                json.dump(mapping, f)

        return mapping


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    log("=" * 65)
    log("FinBERT + Qwen3-14B IFRS Tag Mapper v5")
    log("REMOVE mode — Qwen3 removes wrong tags, keeps the rest")
    log("=" * 65)
    log(f"Python:  {sys.version.split()[0]}")
    log(f"PyTorch: {torch.__version__}")

    # Resume from checkpoint if exists
    checkpoint = {}
    if Path(CHECKPOINT_FILE).exists():
        with open(CHECKPOINT_FILE) as f:
            checkpoint = json.load(f)
        log(f"Resuming from checkpoint — {len(checkpoint)}/163 done")

    # Run mapper
    mapper  = FinBERTQwen14BMapper()
    mapping = mapper.map_all(checkpoint=checkpoint)

    # Apply hard blocklist
    mapping = apply_hard_blocklist(mapping)

    # Save final output
    with open(OUTPUT_FILE, "w") as f:
        json.dump(mapping, f, indent=2)
    log(f"Saved to {OUTPUT_FILE}")

    # Summary stats
    total_tags = sum(len(v) for v in mapping.values())
    zeros      = [k for k, v in mapping.items() if len(v) == 0]
    log(f"\nSUMMARY")
    log(f"  Sub-industries:     {len(mapping)}")
    log(f"  Total tag edges:    {total_tags}")
    log(f"  Average tags/SI:    {total_tags/len(mapping):.1f}")
    log(f"  Min:                {min(len(v) for v in mapping.values())}")
    log(f"  Max:                {max(len(v) for v in mapping.values())}")
    log(f"  Zero tag SIs:       {len(zeros)}")

    # Financials breakdown
    log(f"\nFinancials sub-industries:")
    for code, tags in sorted(mapping.items()):
        if code.startswith("40"):
            name = gics_definition.get(code, {}).get("name", code)
            log(f"  [{code}] {name:35s} {len(tags):3d} tags")

    # Key SubIndustry checks
    for code, label in [("40101015", "Regional Banks"), ("25201010", "Consumer Electronics")]:
        tags = mapping.get(code, [])
        log(f"\n{label} [{code}]: {len(tags)} tags")
        for t in sorted(tags):
            log(f"  {t}")


if __name__ == "__main__":
    main()