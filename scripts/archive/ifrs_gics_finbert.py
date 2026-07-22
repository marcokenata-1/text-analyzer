"""
GICS → IFRS Mapping using FinBERT semantic similarity.

Instead of asking an LLM to reason about which tags belong to which sector,
we use FinBERT to measure semantic similarity between:
  - GICS sector descriptions (from sub-industry descriptions)
  - IFRS tag labels

Setup:
    pip install sentence-transformers torch
"""

import json
from sentence_transformers import SentenceTransformer, util

from d_20230318 import definition as gics_definition
from ifrs_tags  import definition as ifrs_definition

# Universal tags — hardcoded for all sectors, excluded from FinBERT search
# so FinBERT only hunts for sector-specific tags
from universal_ifrs_tags import UNIVERSAL_TAGS


# ── Config ─────────────────────────────────────────────────────────────────────
MODEL_NAME  = "ProsusAI/finbert"
OUTPUT_FILE = "data/mappings/gics_ifrs_mapping_finbert.json"
THRESHOLD   = 0.75   # cosine similarity cutoff for sector-specific tags
TOP_K       = None   # set to e.g. 100 to cap sector-specific tags, or None

# Sectors to map (High level structure)
TARGET_SECTORS = [k for k in gics_definition.keys() if len(k) == 2]


# ── Helpers ────────────────────────────────────────────────────────────────────

def get_sector_description(sector_code: str, gics: dict) -> str:
    """
    Build a rich semantic description of a sector by concatenating:
    - Sector name
    - All industry group names under it
    - All sub-industry descriptions under it (most informative)
    """
    lines = []

    # Sector name
    if sector_code in gics:
        lines.append(f"Sector: {gics[sector_code]['name']}")

    # Industry groups (4-digit codes)
    for code, data in gics.items():
        if len(code) == 4 and code.startswith(sector_code):
            lines.append(f"Industry group: {data['name']}")

    # Industries (6-digit codes)
    for code, data in gics.items():
        if len(code) == 6 and code.startswith(sector_code):
            lines.append(f"Industry: {data['name']}")

    # Sub-industries with descriptions (8-digit codes) — most informative
    for code, data in gics.items():
        if len(code) == 8 and code.startswith(sector_code):
            name = data.get("name", "")
            desc = data.get("description", "")
            if desc:
                lines.append(f"{name}: {desc}")
            else:
                lines.append(name)

    return " | ".join(lines)


def map_sector_finbert(
    sector_code: str,
    sector_name: str,
    sector_description: str,
    tag_keys: list[str],
    tag_labels: list[str],
    tag_embeddings,
    model: SentenceTransformer,
) -> list[str]:
    """Compute cosine similarity between sector description and all IFRS tags."""

    sector_emb = model.encode(sector_description, convert_to_tensor=True)
    scores     = util.cos_sim(sector_emb, tag_embeddings)[0]

    if TOP_K:
        # Take top K tags regardless of threshold
        top_indices = scores.argsort(descending=True)[:TOP_K]
        selected = [tag_keys[i] for i in top_indices]
    else:
        # Take all tags above threshold
        selected = [
            tag_keys[i]
            for i, score in enumerate(scores)
            if score.item() > THRESHOLD
        ]

    return selected, scores


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print(f"Loading FinBERT model ({MODEL_NAME})...")
    model = SentenceTransformer(MODEL_NAME)
    print("Model loaded.\n")

    # Exclude universal tags from FinBERT search — they're hardcoded for all sectors
    sector_specific = {
        k: v for k, v in ifrs_definition.items()
        if k not in UNIVERSAL_TAGS
    }
    tag_keys   = list(sector_specific.keys())
    tag_labels = [meta["label"] for meta in sector_specific.values()]

    print(f"Universal tags (hardcoded for all sectors): {len(UNIVERSAL_TAGS)}")
    print(f"Sector-specific tags (FinBERT will search): {len(tag_keys)}")
    print(f"Embedding {len(tag_labels)} sector-specific IFRS tag labels...")
    tag_embeddings = model.encode(tag_labels, convert_to_tensor=True, show_progress_bar=True)
    print("Done.\n")

    mapping = {}

    for sector_code in TARGET_SECTORS:
        if sector_code not in gics_definition:
            print(f"Sector {sector_code} not found in GICS definition, skipping.")
            continue

        sector_name = gics_definition[sector_code]["name"]
        sector_desc = get_sector_description(sector_code, gics_definition)

        print(f"[{sector_code}] {sector_name}")
        print(f"  Description length: {len(sector_desc)} chars")

        finbert_tags, scores = map_sector_finbert(
            sector_code, sector_name, sector_desc,
            tag_keys, tag_labels, tag_embeddings, model
        )

        # Merge: universal tags + FinBERT sector-specific tags
        final_tags = sorted(UNIVERSAL_TAGS | set(finbert_tags))

        mapping[sector_code] = {
            "name":             sector_name,
            "universal_tags":   sorted(UNIVERSAL_TAGS),
            "sector_tags":      sorted(finbert_tags),
            "ifrs_tags":        final_tags,
        }

        print(f"  ✓ Universal: {len(UNIVERSAL_TAGS)}  +  Sector-specific: {len(finbert_tags)}  =  Total: {len(final_tags)}")

        # Show top 10 FinBERT matches for inspection
        top10 = sorted(
            zip(tag_keys, scores.tolist()),
            key=lambda x: x[1], reverse=True
        )[:10]
        print("  Top 10 FinBERT matches:")
        for tag, score in top10:
            label = sector_specific[tag]["label"]
            print(f"    {score:.3f}  {tag} — {label}")
        print()

    # Save
    with open(OUTPUT_FILE, "w") as f:
        json.dump(mapping, f, indent=2)
    print(f"Saved to {OUTPUT_FILE}")

    # Compare sectors — only sector-specific tags (universals are same for both)
    if len(TARGET_SECTORS) == 2:
        s1, s2     = TARGET_SECTORS
        set1 = set(mapping[s1]["sector_tags"])
        set2 = set(mapping[s2]["sector_tags"])
        overlap    = set1 & set2
        only1      = set1 - set2
        only2      = set2 - set1

        print(f"\n{'='*50}")
        print(f"Sector-specific tag comparison (excluding {len(UNIVERSAL_TAGS)} universal tags):")
        print(f"  {mapping[s1]['name']:15s} sector-specific: {len(set1)}")
        print(f"  {mapping[s2]['name']:15s} sector-specific: {len(set2)}")
        print(f"  Overlap:                         {len(overlap)}")
        print(f"  Unique to {mapping[s1]['name']:12s}: {len(only1)}")
        print(f"  Unique to {mapping[s2]['name']:12s}: {len(only2)}")

        print(f"\n  Unique to {mapping[s1]['name']} (all):")
        for t in sorted(only1):
            print(f"    {t}")

        print(f"\n  Unique to {mapping[s2]['name']} (all):")
        for t in sorted(only2):
            print(f"    {t}")

        print(f"\n  Overlap (in both sectors, above threshold):")
        for t in sorted(overlap)[:20]:
            print(f"    {t}")


if __name__ == "__main__":
    main()