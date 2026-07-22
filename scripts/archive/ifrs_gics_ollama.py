"""
GICS → IFRS Mapping using Ollama — improved with universal tags.

Key improvement:
- Universal tags (IAS 1 required) are hardcoded and EXCLUDED from LLM search
- LLM only asked to find SECTOR-SPECIFIC tags from remaining ~2,264 tags
- Prompt explicitly says "universals already covered — find only tags unique
  to THIS sector that would NOT appear in other sectors"
- Much easier task for 8B model = better differentiation

Setup:
    ollama pull llama3.1
    pip install ollama
"""

import json
import ollama

from d_20230318          import definition as gics_definition
from ifrs_tags           import definition as ifrs_definition
from universal_ifrs_tags import UNIVERSAL_TAGS


# ── Config ─────────────────────────────────────────────────────────────────────
MODEL         = "llama3.1"
OUTPUT_FILE   = "data/mappings/gics_ifrs_mapping_ollama.json"
CHUNK_SIZE    = 200   # smaller chunks = more focused LLM attention
MAX_PER_CHUNK = 15    # forces selectivity per chunk

# Sectors to map (High level structure)
TARGET_SECTORS = [k for k in gics_definition.keys() if len(k) == 2]


# ── Helpers ────────────────────────────────────────────────────────────────────

def get_subindustry_descriptions(sector_code: str, gics: dict) -> list:
    lines = []
    for code, data in gics.items():
        if len(code) == 8 and code.startswith(sector_code):
            name = data.get("name", "")
            desc = data.get("description", "")
            lines.append(f"{name}: {desc}" if desc else name)
    return lines


def chunk_ifrs_excluding_universal(ifrs: dict, chunk_size: int) -> list:
    """Chunk only sector-specific tags — universals excluded."""
    sector_specific = {k: v for k, v in ifrs.items() if k not in UNIVERSAL_TAGS}
    items = list(sector_specific.items())
    return [dict(items[i:i + chunk_size]) for i in range(0, len(items), chunk_size)]


def build_ifrs_list(ifrs_chunk: dict) -> str:
    return "\n".join(
        f"{i}. {meta['label']}"
        for i, (tag, meta) in enumerate(ifrs_chunk.items(), 1)
    )


def parse_numbers(raw: str, max_n: int) -> list:
    raw = raw.strip()
    if "```" in raw:
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    start = raw.find("[")
    end   = raw.rfind("]")
    if start == -1 or end == -1:
        return []
    try:
        numbers = json.loads(raw[start:end + 1].strip())
        return [n for n in numbers if isinstance(n, int) and 1 <= n <= max_n]
    except json.JSONDecodeError:
        return []


def map_chunk(sector_code, sector_name, subindustry_descs,
              ifrs_chunk, chunk_index, total_chunks):

    context      = "\n".join(f"  - {s}" for s in subindustry_descs[:12])
    tag_keys     = list(ifrs_chunk.keys())
    n_tags       = len(tag_keys)
    tag_list_str = build_ifrs_list(ifrs_chunk)

    prompt = f"""You are an IFRS financial reporting expert.

TASK: From the IFRS tags below, select ONLY those SPECIFIC to {sector_name} companies.

IMPORTANT: Universal tags like Assets, Revenue, ProfitLoss, CashAndCashEquivalents,
PropertyPlantAndEquipment, RetainedEarnings, IncomeTaxExpense, EarningsPerShare and
all standard IAS 1 / IAS 7 line items are ALREADY INCLUDED — do NOT select them.

You are only looking for tags that a {sector_name} company would report that OTHER
sectors (Banking, Technology, Consumer Goods) would NOT typically report.

{sector_name.upper()} sub-industries:
{context}

IFRS TAGS (batch {chunk_index}/{total_chunks}):
{tag_list_str}

RULES:
- Return ONLY a JSON array of integers e.g. [3, 7, 12]
- Maximum {MAX_PER_CHUNK} numbers per batch
- If nothing is sector-specific in this batch, return []
- Do NOT select generic accounting tags
- Only select tags clearly unique to {sector_name}
- Start with [ and end with ]"""

    try:
        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0.0},
        )
        raw     = response["message"]["content"].strip()
        numbers = parse_numbers(raw, n_tags)

        if len(numbers) > MAX_PER_CHUNK:
            numbers = numbers[:MAX_PER_CHUNK]

        return [tag_keys[n - 1] for n in numbers]

    except Exception as e:
        print(f"        ✗ Error: {e}")
        return []


def map_sector(sector_code: str, sector_name: str) -> dict:
    subindustry_descs = get_subindustry_descriptions(sector_code, gics_definition)
    chunks            = chunk_ifrs_excluding_universal(ifrs_definition, CHUNK_SIZE)
    n_chunks          = len(chunks)
    sector_tags       = []

    print(f"    {n_chunks} chunks × {CHUNK_SIZE} sector-specific tags")

    for i, chunk in enumerate(chunks, 1):
        print(f"      Chunk {i}/{n_chunks}...", end=" ", flush=True)
        tags = map_chunk(sector_code, sector_name, subindustry_descs, chunk, i, n_chunks)
        sector_tags.extend(tags)
        print(f"{len(tags)} matched")

    sector_tags = list(set(sector_tags))
    final_tags  = sorted(UNIVERSAL_TAGS | set(sector_tags))

    return {
        "name":           sector_name,
        "universal_tags": sorted(UNIVERSAL_TAGS),
        "sector_tags":    sorted(sector_tags),
        "ifrs_tags":      final_tags,
    }


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    all_sectors = {k: v for k, v in gics_definition.items() if len(k) == 2}
    sectors     = {k: v for k, v in all_sectors.items() if k in TARGET_SECTORS}
    mapping     = {}

    print(f"Mapping {len(sectors)} GICS sectors → IFRS tags using Ollama ({MODEL})")
    print(f"Universal tags hardcoded: {len(UNIVERSAL_TAGS)}")
    print(f"LLM searches sector-specific pool: {len(ifrs_definition) - len(UNIVERSAL_TAGS)} tags\n")

    for code, data in sectors.items():
        name = data["name"]
        print(f"\n[{code}] {name}")
        result = map_sector(code, name)
        mapping[code] = result
        print(f"    ✓ Universal: {len(result['universal_tags'])}  +  "
              f"Sector-specific: {len(result['sector_tags'])}  =  "
              f"Total: {len(result['ifrs_tags'])}")

    with open(OUTPUT_FILE, "w") as f:
        json.dump(mapping, f, indent=2)
    print(f"\nSaved to {OUTPUT_FILE}")

    # Compare sector-specific only
    if len(TARGET_SECTORS) == 2:
        s1, s2  = TARGET_SECTORS
        set1    = set(mapping[s1]["sector_tags"])
        set2    = set(mapping[s2]["sector_tags"])
        overlap = set1 & set2
        only1   = set1 - set2
        only2   = set2 - set1

        print(f"\n{'='*55}")
        print(f"Sector-specific comparison (universals excluded):")
        print(f"  {mapping[s1]['name']:15s} specific: {len(set1)}")
        print(f"  {mapping[s2]['name']:15s} specific: {len(set2)}")
        print(f"  Overlap:                  {len(overlap)}")
        print(f"  Unique to {mapping[s1]['name']:10s}:  {len(only1)}")
        print(f"  Unique to {mapping[s2]['name']:10s}:  {len(only2)}")

        print(f"\n  Unique to {mapping[s1]['name']}:")
        for t in sorted(only1):
            print(f"    {t}")

        print(f"\n  Unique to {mapping[s2]['name']}:")
        for t in sorted(only2):
            print(f"    {t}")

        print(f"\n  Overlap (in both):")
        for t in sorted(overlap):
            print(f"    {t}")


if __name__ == "__main__":
    main()