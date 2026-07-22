"""
Step 1: GICS → IFRS Mapping using Groq (llama-3.3-70b-versatile)

Setup:
    pip install groq python-dotenv
    Create a .env file in the same folder with:
        GROQ_API_KEY=your_key_here
"""

import json
import time
import os
from groq import Groq
from dotenv import load_dotenv

# ── Load environment variables ─────────────────────────────────────────────────
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

# ── Import your existing files ─────────────────────────────────────────────────
from d_20230318 import definition as gics_definition
from ifrs_tags import definition as ifrs_definition


# ── Config ─────────────────────────────────────────────────────────────────────
MODEL       = "llama-3.3-70b-versatile"
OUTPUT_FILE = "data/mappings/gics_ifrs_mapping.json"
CHUNK_SIZE  = 200    # safe under 12k TPM limit
DELAY       = 6      # seconds between requests (stays under 30 RPM)

# Only mapping Financials (40) for SNB use case
TARGET_SECTORS = [
    "40",  # Financials
]


# ── Init Groq client ───────────────────────────────────────────────────────────
client = Groq(api_key=GROQ_API_KEY)


# ── Helpers ────────────────────────────────────────────────────────────────────

def get_subindustry_names(sector_code: str, gics: dict) -> list[str]:
    return [
        data["name"]
        for code, data in gics.items()
        if len(code) == 8 and code.startswith(sector_code)
    ]


def chunk_ifrs(ifrs: dict, chunk_size: int) -> list[dict]:
    items = list(ifrs.items())
    return [
        dict(items[i:i + chunk_size])
        for i in range(0, len(items), chunk_size)
    ]


def build_ifrs_list(ifrs_chunk: dict) -> str:
    return "\n".join(
        f"{i}. {meta['label']} ({meta['period_type']})"
        for i, (tag, meta) in enumerate(ifrs_chunk.items(), 1)
    )


def parse_numbers(raw: str, max_n: int) -> list[int]:
    raw = raw.strip()
    if "```" in raw:
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    start = raw.find("[")
    end   = raw.rfind("]")
    if start != -1 and end != -1:
        raw = raw[start:end + 1]
    numbers = json.loads(raw.strip())
    return [n for n in numbers if isinstance(n, int) and 1 <= n <= max_n]


def call_groq_with_retry(prompt: str, retries: int = 5) -> str:
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1024,
                temperature=0.1,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            err = str(e).lower()
            if "rate_limit" in err or "429" in err:
                wait = 60 * (attempt + 1)
                print(f"        Rate limited, waiting {wait}s (attempt {attempt+1}/{retries})...")
                time.sleep(wait)
            elif "daily" in err or "tpd" in err:
                print(f"        ✗ Daily token limit reached. Please try again tomorrow.")
                raise SystemExit(1)
            else:
                print(f"        ✗ Error: {e}")
                return "[]"
    return "[]"


def map_chunk(
    sector_code: str,
    sector_name: str,
    subindustries: list[str],
    ifrs_chunk: dict,
    chunk_index: int,
    total_chunks: int,
) -> list[str]:

    subindustry_context = "\n".join(f"  - {s}" for s in subindustries[:15])
    tag_keys            = list(ifrs_chunk.keys())
    n_tags              = len(tag_keys)

    prompt = f"""You are an expert in IFRS financial reporting and industry analysis.

TASK: From the numbered IFRS tags below (batch {chunk_index}/{total_chunks}),
select ONLY those commonly reported by companies in this specific GICS sector.

GICS SECTOR:
  Code: {sector_code}
  Name: {sector_name}
  Sub-industries include:
{subindustry_context}

IFRS TAGS (format: Number. Label (period_type)):
{build_ifrs_list(ifrs_chunk)}

CRITICAL INSTRUCTIONS:
- Return the NUMBERS of relevant tags, not their names
- Be SELECTIVE — think carefully about what THIS specific sector reports
- Include universal tags (Assets, Revenue) AND tags unique to this sector
- Do NOT select tags irrelevant to this sector
- Maximum 30 tags per batch
- If NO tags are relevant return: []
- Return ONLY a JSON array of integers, no explanation, no markdown
- Start with [ and end with ]
- Example: [1, 4, 7, 23, 45]
"""

    raw = call_groq_with_retry(prompt)

    try:
        numbers = parse_numbers(raw, n_tags)

        # Skip suspiciously high selections
        if len(numbers) > 50:
            print(f"        ⚠ Suspiciously high ({len(numbers)}) — skipping chunk")
            return []

        tags = [tag_keys[n - 1] for n in numbers]
        return tags
    except json.JSONDecodeError as e:
        print(f"        ✗ JSON parse error: {e} | raw: {raw[:100]}")
        return []


def map_sector(sector_code: str, sector_name: str) -> list[str]:
    subindustries = get_subindustry_names(sector_code, gics_definition)
    chunks        = chunk_ifrs(ifrs_definition, CHUNK_SIZE)
    n_chunks      = len(chunks)
    all_tags      = []

    print(f"    {n_chunks} chunks × {CHUNK_SIZE} tags")

    for i, chunk in enumerate(chunks, 1):
        print(f"      Chunk {i}/{n_chunks}...", end=" ", flush=True)
        tags = map_chunk(sector_code, sector_name, subindustries, chunk, i, n_chunks)
        all_tags.extend(tags)
        print(f"{len(tags)} matched")
        time.sleep(DELAY)

    return list(set(all_tags))


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    mapping = {}
    total   = len(TARGET_SECTORS)

    print(f"Mapping {total} GICS sectors → IFRS tags using Groq ({MODEL})\n")

    for i, code in enumerate(TARGET_SECTORS, 1):
        data = gics_definition[code]
        name = data["name"]
        print(f"[{i}/{total}] {name} (code: {code})")

        tags = map_sector(code, name)
        mapping[code] = {"name": name, "ifrs_tags": tags}

        print(f"    ✓ Total: {len(tags)} IFRS tags mapped\n")

        # Save after each sector in case of interruption
        with open(OUTPUT_FILE, "w") as f:
            json.dump(mapping, f, indent=2)
        print(f"    💾 Progress saved to {OUTPUT_FILE}\n")

    print("Done! Summary:")
    for code, data in mapping.items():
        print(f"  {data['name']:35s} → {len(data['ifrs_tags'])} tags")


if __name__ == "__main__":
    main()