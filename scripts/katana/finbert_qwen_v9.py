"""
FinBERT + Qwen3-14B IFRS Tag Mapper v9 (Katana HPC)

SELECT mode (not v5's REMOVE mode): ask Qwen3 to pick only the tags that
are specifically relevant, default is EXCLUDE. v5 switched to "remove only
clearly wrong tags, default KEEP". As expected of an LLM asked to
justify removal rather than inclusion, it ended up keeping ~1800 of ~2000
candidate tags for nearly every SubIndustry, defeating the entire point of
Contextual Pruning (see subindustry_ifrs_mapping_v5.json). SELECT mode is
what actually produced the precise, industry-specific mappings this
pipeline currently uses (subindustry_ifrs_mapping_v3_katana.json).

Fixes over the archived finbert_qwen_mapper.py run (subindustry_ifrs_mapping_v4_qwen.json,
see logs/ifrs_finbert_qwen14b.o8244800): that run completed with exit 0 in
under 40 minutes but came back 82% empty (133/163 SubIndustries with zero
tags). Root cause: Qwen3 is a reasoning model that emits a <think>...</think>
block before its answer, the old script fed it a raw prompt string (no chat
template) with MAX_NEW_TOKENS=150, and most batches ran out of budget mid-
thought, so parse_numbers correctly found no complete "[...]" array after
stripping the (truncated, unclosed) think block, so it silently returned [].
Fix: use the proper chat template with enable_thinking=False, which skips
the reasoning trace entirely instead of just hoping it finishes in time.

Also widens FinBERT top-K from 100 -> 150: v3_katana/v4_qwen's 100-candidate
shortlist is why only 21.3% of the full IFRS taxonomy is reachable by any
SubIndustry at all (measured directly against the live GraphDB, see
project notes). 150 gives Qwen3 meaningfully more to select from without
approaching v5's "send it everything" over-inclusion.

Setup on Katana:
    module load python/3.11.3
    source ~/thesis_env/bin/activate
    pip install sentence-transformers transformers accelerate --user

Usage on Katana:
    qsub run_v9.pbs
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

# `ollama` and `build_graphdb` (rdflib/SPARQLWrapper) are NOT installed in
# the Katana HPC environment (see module docstring's pip list) and aren't
# needed there; only generate_disclosure_tags()/generate_sector_specific_
# tags() below use them, and those are meant to be run locally/once to
# produce the small cached JSON files the Katana mapper actually loads.
# Imported lazily inside those two functions instead of at module level so
# a normal Katana run of this script never touches either dependency.


# Config
BIENCODER_MODEL = "ProsusAI/finbert"
LLM_MODEL       = "/srv/scratch/z5603945/hf_cache/Qwen3-14B"

OUTPUT_FILE     = "subindustry_ifrs_mapping_v9.json"
CHECKPOINT_FILE = "subindustry_ifrs_mapping_v9_checkpoint.json"

# Stage 1: FinBERT candidates. 150 (up from the 100 that produced
# v3_katana/v4_qwen), meaningfully broader without approaching v5's
# effectively-unfiltered ~1800.
BIENCODER_TOPK  = 150

# Stage 2: Qwen3 batch size. enable_thinking=False means no reasoning
# trace to budget for, so this covers a batch of up to 50 selected numbers
# comfortably.
QWEN_BATCH_SIZE = 50
MAX_NEW_TOKENS  = 300

# Disclosure-only tags (notes/breakdowns, never a standalone reported line
# item) are NOT a hand-maintained list here; see generate_disclosure_tags()
# below, which produces this file once (LLM-classified, then validated
# against the calculation linkbase) and caches it; the mapper just loads it.
DISCLOSURE_TAGS_FILE = "data/taxonomy/disclosure_tags.json"

# Sector-specific tags (Oil & Gas/Mining tags leaking into unrelated
# SubIndustries, banking/insurance tags leaking in via generic financial-
# vocabulary overlap like "loans", "fair value", "credit"). An LLM-generate
# + embedding-validate attempt at making this dynamic (generate_sector_
# specific_tags() below) was tried and rejected: sampling its output found
# real false positives (e.g. CurrentPortionOfLongtermBorrowings,
# OtherFinanceIncomeCost, ProceedsFromIssuingOtherEquityInstruments;
# generic tags any company could report, not bank-exclusive), and checking
# the actual similarity margins confirmed embedding closeness to a sector's
# GICS description measures "does this tag's wording resemble that sector's
# vocabulary," not "would only that sector report this". False and true
# positives had overlapping margins (e.g. a false positive at 0.076 vs a
# true positive at 0.079), so no threshold fixes it. Kept hand-maintained
# until a better validation signal exists (e.g. cross-referencing empirical
# tag usage across many companies' actual filings, once enough are on hand,
# rather than embedding vocabulary resemblance alone).
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

FINANCIAL_INSTITUTION_KEYWORDS = [
    "LoansAndAdvances", "Brokerage", "CreditDerivative", "InsuranceFinance",
    "InsuranceContract", "Reinsurance", "DepositsFrom", "CentralBank",
    "LoanCommitment", "CreditInstitution", "Policyholder",
]
FINANCIAL_SECTOR_EXEMPT = {"40"}


def is_financial_institution_tag(tag: str) -> bool:
    return any(kw in tag for kw in FINANCIAL_INSTITUTION_KEYWORDS)


def load_disclosure_tags() -> set:
    with open(DISCLOSURE_TAGS_FILE) as f:
        return set(json.load(f))


# Helpers

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


def parse_numbers(raw: str, max_n: int) -> list:
    raw = re.sub(r'<think>.*?</think>', '', raw, flags=re.DOTALL).strip()
    start = raw.find("[")
    end   = raw.rfind("]")
    if start == -1 or end == -1:
        return None  # distinguish "couldn't parse" from "parsed to []"
    try:
        nums = json.loads(raw[start:end+1].strip())
        return [n for n in nums if isinstance(n, int) and 1 <= n <= max_n]
    except Exception:
        return None


def apply_hard_blocklist(mapping: dict) -> dict:
    cleaned = {}
    removed = 0
    fi_removed = 0
    for si_code, tags in mapping.items():
        sector = si_code[:2]
        filtered = tags if sector in BLOCKLIST_EXEMPT else [t for t in tags if t not in HARD_BLOCKLIST]
        removed += len(tags) - len(filtered)
        if sector not in FINANCIAL_SECTOR_EXEMPT:
            before = len(filtered)
            filtered = [t for t in filtered if not is_financial_institution_tag(t)]
            fi_removed += before - len(filtered)
        cleaned[si_code] = filtered
    log(f"Hard blocklist removed {removed} domain-impossible tags")
    log(f"Financial-institution blocklist removed {fi_removed} bank/insurer-specific tags")
    return cleaned


# Dynamic tag classification (generate once, cache to disk)
#
# generate_disclosure_tags() is NOT part of a normal Katana mapping run;
# it's a separate, one-time (or "re-run when the taxonomy changes")
# preprocessing step meant to be run locally, producing the small
# DISCLOSURE_TAGS_FILE the actual mapper loads via load_disclosure_tags().
# Requires `ollama` and this repo's data/taxonomy/ (for build_graphdb's
# calculation linkbase parser); neither is expected to be present on
# Katana, hence the lazy imports.
#
# generate_sector_specific_tags() is kept below for its embedding-validation
# approach and docstring explaining why it's NOT currently wired in (see the
# HARD_BLOCKLIST/FINANCIAL_INSTITUTION_KEYWORDS comment above): a starting
# point if a better validation signal shows up later, not dead code to
# resurrect blindly.

def _ollama_classify_batch(prompt: str, ollama_model: str = "llama3.1") -> dict:
    """Ask Ollama for a JSON object response, tolerating trailing prose."""
    import ollama
    try:
        resp = ollama.chat(
            model=ollama_model,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0.0},
        )
        raw = re.sub(r"^```(?:json)?|```$", "", resp["message"]["content"].strip(), flags=re.M).strip()
        parsed, _ = json.JSONDecoder().raw_decode(raw)
        return parsed
    except Exception as e:
        log(f"  [classify] batch failed, continuing: {e}")
        return {}


def generate_disclosure_tags(tags: list) -> set:
    """
    LLM-classifies each tag as a PRIMARY financial-statement line item or a
    DISCLOSURE-only figure (notes: breakdowns, roll-forwards, related-party
    detail, fair-value hierarchy levels, etc, never a top-level reported
    total), batched.

    Validated against the calculation linkbase (build_graphdb.load_
    calculation_rules): any tag that participates in an official IFRS
    summation rule is definitionally PRIMARY regardless of what the LLM
    says. This overrides the LLM's classification instead of trusting its
    judgment blindly, the same principle as build_chromadb.py's
    validate_synonym_map. Concretely caught a real case during design: the
    old hand-maintained list excluded every "ShareOfOtherComprehensiveIncome*"
    tag as disclosure-only, but those tags are genuine calculation-linkbase
    children of OtherComprehensiveIncome, a real bug this validation fixes.
    """
    from build_graphdb import load_calculation_rules
    rules = load_calculation_rules()
    calculation_tags = {p for p, _, _ in rules} | {c for _, c, _ in rules}

    BATCH = 50
    disclosure = set()
    total_batches = (len(tags) - 1) // BATCH + 1
    for i in range(0, len(tags), BATCH):
        batch = tags[i:i + BATCH]
        items = "\n".join(f"{n}. {camel_to_sentence(t)}" for n, t in enumerate(batch, 1))
        prompt = f"""You are an IFRS financial reporting expert.

For each numbered IFRS XBRL tag label below, classify it as either:
  PRIMARY    — a figure that appears as a standalone line item on a
               company's primary financial statements (balance sheet,
               income statement, cash flow statement, equity statement)
  DISCLOSURE — a figure that only appears in the notes to the financial
               statements: breakdowns, roll-forwards, related-party
               detail, fair-value hierarchy levels, maximum-exposure
               disclosures, retirements/disposals/additions detail, etc.
               Never a top-level reported total.

{items}

Reply with ONLY a JSON object mapping each number (as a string) to
"PRIMARY" or "DISCLOSURE". No other text."""
        result = _ollama_classify_batch(prompt)
        for n, label in result.items():
            try:
                idx = int(n) - 1
            except ValueError:
                continue
            if 0 <= idx < len(batch) and label == "DISCLOSURE":
                disclosure.add(batch[idx])
        log(f"  [disclosure classify] batch {i // BATCH + 1}/{total_batches}")

    overridden = disclosure & calculation_tags
    if overridden:
        log(f"  [disclosure classify] overriding {len(overridden)} tags the LLM called "
            f"DISCLOSURE but which participate in the calculation linkbase (definitionally PRIMARY)")
    return disclosure - calculation_tags


def generate_sector_specific_tags(tags: list, model) -> dict:
    """
    NOT CURRENTLY USED. See the HARD_BLOCKLIST/FINANCIAL_INSTITUTION_KEYWORDS
    comment above for why. Kept as a documented, tested-and-rejected attempt
    rather than deleted, since the approach (LLM classify + embedding
    validate) is sound in principle, just not with this validation signal.

    LLM-classifies which GICS Sector (if any) each tag is exclusive to,
    batched. "Validated" by embedding: the tag's own label must sit closer
    to its claimed sector's GICS description than to every other sector's;
    the same principle as build_chromadb.py's validate_synonym_map, but it
    doesn't hold up here: sampling the output found real false positives
    (generic tags like CurrentPortionOfLongtermBorrowings and
    OtherFinanceIncomeCost classified as Financials-exclusive), and their
    similarity margins overlap with genuine true positives' margins (e.g. a
    false positive at 0.076 vs a true positive at 0.079); no threshold
    separates them. This embedding check measures "does this tag's wording
    resemble the claimed sector's vocabulary," which isn't the same
    question as "would only that sector realistically report this," and
    apparently can't be made to answer it just by tightening the cutoff.
    """
    import chromadb
    sector_names = {code: d["name"] for code, d in gics_definition.items() if len(code) == 2}
    client = chromadb.HttpClient(host="localhost", port=8001)
    gics_docs = client.get_collection("gics_definitions").get(ids=list(sector_names), include=["documents"])
    sector_codes = gics_docs["ids"]
    sector_embs  = model.encode(gics_docs["documents"], normalize_embeddings=True)

    options = "\n".join(f"  {c} = {n}" for c, n in sorted(sector_names.items()))

    BATCH = 50
    claims: dict = {}
    total_batches = (len(tags) - 1) // BATCH + 1
    for i in range(0, len(tags), BATCH):
        batch = tags[i:i + BATCH]
        items = "\n".join(f"{n}. {camel_to_sentence(t)}" for n, t in enumerate(batch, 1))
        prompt = f"""You are an IFRS financial reporting expert.

GICS Sectors:
{options}

For each numbered IFRS XBRL tag label below, name the GICS Sector code it
is EXCLUSIVELY specific to — i.e. it would be nonsensical for a company
outside that sector to report it (e.g. an oil drilling cost, a bank's
customer deposits, an insurer's reinsurance premiums). Most tags apply
broadly across industries — for those, answer "none".

{items}

Reply with ONLY a JSON object mapping each number (as a string) to a
2-digit sector code or "none". No other text."""
        result = _ollama_classify_batch(prompt)
        for n, sector in result.items():
            try:
                idx = int(n) - 1
            except ValueError:
                continue
            if 0 <= idx < len(batch) and sector in sector_names:
                claims[batch[idx]] = sector
        log(f"  [sector classify] batch {i // BATCH + 1}/{total_batches}")

    log(f"  [sector classify] {len(claims)} tags claimed sector-specific, validating by embedding...")
    tag_labels = [camel_to_sentence(t) for t in claims]
    tag_embs   = model.encode(tag_labels, normalize_embeddings=True)
    sims       = tag_embs @ sector_embs.T   # (n_claims, n_sectors)

    validated = {}
    for (tag, claimed_sector), row in zip(claims.items(), sims):
        best_idx = int(row.argmax())
        if sector_codes[best_idx] == claimed_sector:
            validated[tag] = claimed_sector
    log(f"  [sector classify] {len(validated)}/{len(claims)} claims validated "
        f"(claimed sector was the tag's closest embedding match)")
    return validated


# Qwen3 resolver

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

    def _build_prompt(self, si_name: str, si_desc: str, batch: list, batch_num: int, total_batches: int) -> str:
        tag_list = "\n".join(f"{i+1}. {label}" for i, (_, label) in enumerate(batch))
        return f"""You are an IFRS financial reporting expert.

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

    def _generate(self, prompt: str) -> str:
        # enable_thinking=False is the actual fix over the archived mapper:
        # without it Qwen3 spends its output budget on a <think> block that
        # often doesn't finish before max_new_tokens, leaving no closed
        # "[...]" for parse_numbers to find (see module docstring).
        messages = [{"role": "user", "content": prompt}]
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,
        )
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=2048).to(self.model.device)
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens = MAX_NEW_TOKENS,
                do_sample      = False,
                temperature    = 1.0,
                pad_token_id   = self.tokenizer.eos_token_id,
            )
        new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        return self.tokenizer.decode(new_tokens, skip_special_tokens=True)

    def resolve_batch(self, si_name: str, si_desc: str, batch: list, batch_num: int, total_batches: int) -> list:
        """Ask Qwen3 which tags in this batch are relevant. One retry on an unparseable response."""
        prompt = self._build_prompt(si_name, si_desc, batch, batch_num, total_batches)

        for attempt in (1, 2):
            raw     = self._generate(prompt)
            numbers = parse_numbers(raw, len(batch))
            if numbers is not None:
                return [batch[n-1][0] for n in numbers]
            log(f"    [batch {batch_num}/{total_batches} attempt {attempt}] "
                f"unparseable response, raw={raw[:200]!r}")

        log(f"    [batch {batch_num}/{total_batches}] gave up after 2 attempts, treating as empty")
        return []

    def resolve_all_batches(self, si_name: str, si_desc: str, candidates: list) -> list:
        accepted = []
        batches  = [candidates[i:i+QWEN_BATCH_SIZE] for i in range(0, len(candidates), QWEN_BATCH_SIZE)]
        for idx, batch in enumerate(batches, 1):
            tags = self.resolve_batch(si_name, si_desc, batch, idx, len(batches))
            accepted.extend(tags)
        return list(set(accepted))


# Main mapper

class FinBERTQwenMapper:

    def __init__(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        log(f"Device: {device}")
        if device == "cuda":
            log(f"GPU: {torch.cuda.get_device_name(0)}")
            log(f"VRAM: {torch.cuda.get_device_properties(0).total_memory/1e9:.1f}GB")

        log(f"Loading FinBERT ({BIENCODER_MODEL})...")
        self.biencoder = SentenceTransformer(BIENCODER_MODEL, device=device)

        disclosure_tags = load_disclosure_tags()
        self.tag_keys   = []
        self.tag_labels = []
        for name in ifrs_definition:
            if name in UNIVERSAL_TAGS:
                continue
            if name in disclosure_tags:
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

        self.qwen = Qwen3Resolver(device)

    def get_finbert_candidates(self, si_desc: str) -> list:
        si_emb = self.biencoder.encode(si_desc, convert_to_tensor=True)
        scores = util.cos_sim(si_emb, self.tag_embs)[0].tolist()
        top_k  = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:BIENCODER_TOPK]
        return [(self.tag_keys[i], self.tag_labels[i]) for i, _ in top_k]

    def map_subindustry(self, si_code: str) -> list:
        si_data    = gics_definition.get(si_code, {})
        si_name    = si_data.get("name", si_code)
        si_desc    = build_subindustry_description(si_code)
        candidates = self.get_finbert_candidates(si_desc)
        accepted   = self.qwen.resolve_all_batches(si_name, si_desc, candidates)
        return sorted(accepted)

    def map_all(self, checkpoint: dict = None) -> dict:
        subindustries = {k: v for k, v in gics_definition.items() if len(k) == 8}
        total_si      = len(subindustries)
        mapping       = checkpoint or {}

        log(f"Mapping {total_si} SubIndustries: FinBERT + Qwen3")
        log(f"Stage 1: FinBERT top-{BIENCODER_TOPK} candidates")
        log(f"Stage 2: Qwen3 batches of {QWEN_BATCH_SIZE}, enable_thinking=False\n")

        for idx, (si_code, si_data) in enumerate(subindustries.items(), 1):
            if si_code in mapping:
                continue

            si_name = si_data.get("name", si_code)
            t_start = time.time()

            tags = self.map_subindustry(si_code)
            mapping[si_code] = tags

            elapsed   = time.time() - t_start
            n_batches = (BIENCODER_TOPK + QWEN_BATCH_SIZE - 1) // QWEN_BATCH_SIZE
            log(f"[{idx:3d}/{total_si}] {si_name[:40]:40s} "
                f"candidates={BIENCODER_TOPK} batches={n_batches} "
                f"-> {len(tags)} tags ({elapsed:.1f}s)")

            with open(CHECKPOINT_FILE, "w") as f:
                json.dump(mapping, f)

        return mapping


# Main

def main():
    log("=" * 60)
    log("FinBERT + Qwen3 IFRS Tag Mapper v9 (Katana HPC)")
    log("=" * 60)
    log(f"Python:  {sys.version.split()[0]}")
    log(f"PyTorch: {torch.__version__}")

    checkpoint = {}
    if Path(CHECKPOINT_FILE).exists():
        with open(CHECKPOINT_FILE) as f:
            checkpoint = json.load(f)
        log(f"Resuming from checkpoint, {len(checkpoint)} done")

    mapper  = FinBERTQwenMapper()
    mapping = mapper.map_all(checkpoint=checkpoint)

    mapping = apply_hard_blocklist(mapping)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(mapping, f, indent=2)
    log(f"Saved to {OUTPUT_FILE}")

    total_tags = sum(len(v) for v in mapping.values())
    zeros      = [k for k, v in mapping.items() if len(v) == 0]
    log("\nSUMMARY")
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
