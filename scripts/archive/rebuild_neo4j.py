"""
Full Neo4j Knowledge Graph Rebuild

Correct graph structure:
    Sector -[HAS_CHILD]-> IndustryGroup -[HAS_CHILD]-> Industry
        -[HAS_CHILD]-> SubIndustry -[HAS_RELEVANT_TAG]-> IFRSTag
    IFRSTag -[HAS_PARENT]-> IFRSTag  (summation rules)
    Sector  -[HAS_RELEVANT_TAG]-> IFRSTag  (universal tags only)

Mapping strategy:
    1. Universal tags  → hardcoded, added to ALL sectors via Sector node
    2. Sector-specific → FinBERT at SubIndustry level (fast, ~10 mins)
    3. Grey zone       → Ollama disambiguation (0.65-0.75 score range only)

Setup:
    pip install sentence-transformers neo4j ollama
    ollama pull llama3.1
"""

import json
import re
import ollama
from sentence_transformers import SentenceTransformer, util
from neo4j import GraphDatabase
import xml.etree.ElementTree as ET

from d_20230318          import definition as gics_definition
from ifrs_tags           import definition as ifrs_definition
from universal_ifrs_tags import UNIVERSAL_TAGS


# ── Config ─────────────────────────────────────────────────────────────────────
URI      = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "12345678"
DB       = "ifrs-gics"

MODEL_NAME    = "ProsusAI/finbert"
OLLAMA_MODEL  = "llama3.1"
OUTPUT_FILE   = "data/mappings/subindustry_ifrs_mapping.json"

THRESHOLD_HIGH = 0.80   # auto-accept
THRESHOLD_GREY = 0.79   # send to Ollama for disambiguation
# Below 0.65 → reject


# ── SUMS_TO / HAS_PARENT rules ─────────────────────────────────────────────────
HAS_PARENT_RULES = [
    # Assets
    ("NoncurrentAssets",                   "Assets"),
    ("CurrentAssets",                      "Assets"),
    # Liabilities
    ("NoncurrentLiabilities",              "Liabilities"),
    ("CurrentLiabilities",                 "Liabilities"),
    # Equity
    ("IssuedCapital",                      "Equity"),
    ("SharePremium",                       "Equity"),
    ("RetainedEarnings",                   "Equity"),
    ("NoncontrollingInterests",            "Equity"),
    ("EquityAttributableToOwnersOfParent", "Equity"),
    # Fundamental equation
    ("Liabilities",                        "Assets"),
    ("Equity",                             "Assets"),
    # Profit
    ("ProfitLossFromContinuingOperations", "ProfitLoss"),
    ("ProfitLossAttributableToOwnersOfParent",          "ProfitLoss"),
    ("ProfitLossAttributableToNoncontrollingInterests", "ProfitLoss"),
    # Cash flows
    ("CashFlowsFromUsedInOperatingActivities",
     "IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges"),
    ("CashFlowsFromUsedInInvestingActivities",
     "IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges"),
    ("CashFlowsFromUsedInFinancingActivities",
     "IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges"),
    # Comprehensive income
    ("ProfitLoss",              "ComprehensiveIncome"),
    ("OtherComprehensiveIncome","ComprehensiveIncome"),
]


# ── IFRS label parser ──────────────────────────────────────────────────────────

def camel_to_sentence(name: str) -> str:
    s = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', s)
    return s.strip()


def load_ifrs_labels() -> dict:
    """Parse human-readable labels from IFRS label XML."""
    label_map = {}
    tree = ET.parse("data/taxonomy/lab_full_ifrs-en_2025-03-27.xml")
    root = tree.getroot()
    ns   = {"link": "http://www.xbrl.org/2003/linkbase"}

    for label in root.findall(".//link:label", ns):
        id_attr = label.get("id", "")
        text    = label.text or ""
        if (id_attr.startswith("ifrs-full_")
                and id_attr.endswith("_label")
                and text and "[" not in text):
            tag = id_attr[len("ifrs-full_"):-len("_label")]
            if tag not in label_map:
                label_map[tag] = text

    # Fallback: camelCase split for tags without XML label
    for tag in ifrs_definition:
        if tag not in label_map:
            label_map[tag] = camel_to_sentence(tag)

    return label_map


# ── FinBERT mapper ─────────────────────────────────────────────────────────────

def build_sector_description(sector_code: str) -> str:
    """Build rich description from all sub-industry descriptions in sector."""
    lines = [gics_definition[sector_code]["name"]]
    for code, data in gics_definition.items():
        if len(code) == 8 and code.startswith(sector_code):
            name = data.get("name", "")
            desc = data.get("description", "")
            lines.append(f"{name}: {desc}" if desc else name)
    return " | ".join(lines)


def build_subindustry_description(si_code: str) -> str:
    """Build description for a single sub-industry."""
    data = gics_definition.get(si_code, {})
    name = data.get("name", "")
    desc = data.get("description", "")
    # Add parent industry/group context
    industry_code = si_code[:6]
    ig_code       = si_code[:4]
    industry_name = gics_definition.get(industry_code, {}).get("name", "")
    ig_name       = gics_definition.get(ig_code,       {}).get("name", "")
    return f"{ig_name} > {industry_name} > {name}: {desc}"


def ollama_disambiguate(
    si_name: str,
    si_desc: str,
    grey_tags: list,   # list of (tag_name, label, score)
) -> list:
    """
    Ask Ollama to decide from the grey zone tags.
    Only called for tags scoring 0.65-0.75 — much smaller set.
    """
    if not grey_tags:
        return []

    tag_list = "\n".join(
        f"{i+1}. {label} (score={score:.2f})"
        for i, (_, label, score) in enumerate(grey_tags)
    )

    prompt = f"""You are an IFRS expert.

Sub-industry: {si_name}
Description:  {si_desc[:300]}

These IFRS tags scored 0.65-0.75 similarity (grey zone — borderline relevant).
Select ONLY tags clearly relevant to this specific sub-industry.
Universal tags like Assets, Revenue, ProfitLoss are already included — do NOT select them.

Tags:
{tag_list}

Return ONLY a JSON array of numbers e.g. [1, 3] or []
Start with [ and end with ]"""

    try:
        response = ollama.chat(
            model   = OLLAMA_MODEL,
            messages= [{"role": "user", "content": prompt}],
            options = {"temperature": 0.0},
        )
        raw   = response["message"]["content"].strip()
        start = raw.find("[")
        end   = raw.rfind("]")
        if start == -1 or end == -1:
            return []
        numbers = json.loads(raw[start:end+1])
        return [grey_tags[n-1][0] for n in numbers
                if isinstance(n, int) and 1 <= n <= len(grey_tags)]
    except Exception as e:
        print(f"          Ollama error: {e}")
        return []


def map_subindustry_finbert(
    si_code: str,
    si_desc: str,
    sector_tags: set,       # exclude sector-specific already found
    tag_keys: list,
    tag_labels: list,
    tag_embs,
    model: SentenceTransformer,
    use_ollama: bool = True,
) -> list:
    """
    Map a single SubIndustry to IFRS tags using FinBERT.
    Grey zone tags optionally disambiguated by Ollama.
    """
    # Exclude universal + already-sector-mapped tags from search
    search_keys   = []
    search_labels = []
    search_embs   = []

    for i, key in enumerate(tag_keys):
        if key not in UNIVERSAL_TAGS and key not in sector_tags:
            search_keys.append(key)
            search_labels.append(tag_labels[i])
            search_embs.append(tag_embs[i])

    if not search_keys:
        return []

    import torch
    search_tensor = torch.stack(search_embs)
    si_emb        = model.encode(si_desc, convert_to_tensor=True)
    scores        = util.cos_sim(si_emb, search_tensor)[0].tolist()

    high_tags = []
    grey_tags = []

    for tag, label, score in zip(search_keys, search_labels, scores):
        if score >= THRESHOLD_HIGH:
            high_tags.append(tag)
        elif score >= THRESHOLD_GREY:
            grey_tags.append((tag, label, score))

    # Ollama disambiguation for grey zone
    if use_ollama and grey_tags:
        si_name = gics_definition.get(si_code, {}).get("name", si_code)
        ollama_tags = ollama_disambiguate(si_name, si_desc, grey_tags)
        high_tags.extend(ollama_tags)
        print(f"          Grey zone: {len(grey_tags)} → Ollama kept {len(ollama_tags)}")

    return list(set(high_tags))


# ── Neo4j loader ───────────────────────────────────────────────────────────────

class GraphBuilder:

    def __init__(self):
        self.driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

    def close(self):
        self.driver.close()

    def wipe(self):
        with self.driver.session(database=DB) as s:
            s.run("MATCH (n) DETACH DELETE n")
        print("  ✓ Database wiped")

    def create_constraints(self):
        with self.driver.session(database=DB) as s:
            for cypher in [
                "CREATE CONSTRAINT IF NOT EXISTS FOR (n:Sector)       REQUIRE n.code IS UNIQUE",
                "CREATE CONSTRAINT IF NOT EXISTS FOR (n:IndustryGroup) REQUIRE n.code IS UNIQUE",
                "CREATE CONSTRAINT IF NOT EXISTS FOR (n:Industry)      REQUIRE n.code IS UNIQUE",
                "CREATE CONSTRAINT IF NOT EXISTS FOR (n:SubIndustry)   REQUIRE n.code IS UNIQUE",
                "CREATE CONSTRAINT IF NOT EXISTS FOR (n:IFRSTag)       REQUIRE n.name IS UNIQUE",
            ]:
                s.run(cypher)
        print("  ✓ Constraints created")

    def load_gics(self):
        """Load GICS hierarchy with HAS_CHILD relationships."""
        counts = {"sector": 0, "ig": 0, "industry": 0, "si": 0}

        with self.driver.session(database=DB) as s:
            for code, data in gics_definition.items():
                name = data.get("name", "")
                desc = data.get("description", "")

                if len(code) == 2:
                    s.run("MERGE (n:Sector {code:$c}) SET n.name=$n",
                          c=code, n=name)
                    counts["sector"] += 1

                elif len(code) == 4:
                    s.run("MERGE (n:IndustryGroup {code:$c}) SET n.name=$n",
                          c=code, n=name)
                    s.run("""MATCH (p:Sector {code:$pc})
                             MATCH (ch:IndustryGroup {code:$cc})
                             MERGE (p)-[:HAS_CHILD]->(ch)""",
                          pc=code[:2], cc=code)
                    counts["ig"] += 1

                elif len(code) == 6:
                    s.run("MERGE (n:Industry {code:$c}) SET n.name=$n",
                          c=code, n=name)
                    s.run("""MATCH (p:IndustryGroup {code:$pc})
                             MATCH (ch:Industry {code:$cc})
                             MERGE (p)-[:HAS_CHILD]->(ch)""",
                          pc=code[:4], cc=code)
                    counts["industry"] += 1

                elif len(code) == 8:
                    s.run("""MERGE (n:SubIndustry {code:$c})
                             SET n.name=$n, n.description=$d""",
                          c=code, n=name, d=desc)
                    s.run("""MATCH (p:Industry {code:$pc})
                             MATCH (ch:SubIndustry {code:$cc})
                             MERGE (p)-[:HAS_CHILD]->(ch)""",
                          pc=code[:6], cc=code)
                    counts["si"] += 1

        print(f"  ✓ GICS: {counts['sector']} sectors, {counts['ig']} groups, "
              f"{counts['industry']} industries, {counts['si']} sub-industries")

    def load_ifrs_tags(self, label_map: dict):
        """Load all IFRSTag nodes with human-readable labels."""
        with self.driver.session(database=DB) as s:
            for name, meta in ifrs_definition.items():
                label = label_map.get(name, camel_to_sentence(name))
                s.run("""MERGE (t:IFRSTag {name:$name})
                         SET t.label       = $label,
                             t.balance     = $balance,
                             t.period_type = $period_type,
                             t.is_universal = $universal""",
                      name=name,
                      label=label,
                      balance=meta.get("balance", ""),
                      period_type=meta.get("period_type", ""),
                      universal=(name in UNIVERSAL_TAGS))
        print(f"  ✓ IFRSTag nodes: {len(ifrs_definition)}")

    def load_universal_to_sectors(self):
        """
        Universal tags → attached to ALL Sector nodes.
        These propagate down to all sub-industries automatically via graph traversal.
        """
        count = 0
        with self.driver.session(database=DB) as s:
            for tag in UNIVERSAL_TAGS:
                # Check tag exists
                exists = s.run(
                    "MATCH (t:IFRSTag {name:$n}) RETURN count(t) AS c",
                    n=tag
                ).single()["c"]
                if not exists:
                    continue

                # Attach to all sectors
                s.run("""MATCH (sec:Sector)
                         MATCH (t:IFRSTag {name:$tag})
                         MERGE (sec)-[:HAS_RELEVANT_TAG {source:'universal'}]->(t)""",
                      tag=tag)
                count += 1

        print(f"  ✓ Universal tags: {count} tags → all {len([c for c in gics_definition if len(c)==2])} sectors")

    def load_subindustry_tags(self, mapping: dict):
        """
        Load HAS_RELEVANT_TAG from SubIndustry → IFRSTag.
        mapping format: {si_code: [tag_names]}
        """
        total_edges = 0
        with self.driver.session(database=DB) as s:
            for si_code, tags in mapping.items():
                for tag in tags:
                    result = s.run("""
                        MATCH (si:SubIndustry {code:$si})
                        MATCH (t:IFRSTag {name:$tag})
                        MERGE (si)-[:HAS_RELEVANT_TAG {source:'finbert_ollama'}]->(t)
                        RETURN count(*) AS c
                    """, si=si_code, tag=tag).single()
                    if result:
                        total_edges += result["c"]

        print(f"  ✓ SubIndustry HAS_RELEVANT_TAG edges: {total_edges}")

    def load_has_parent(self, rules: list):
        """Load HAS_PARENT (summation) rules between IFRSTag nodes."""
        count = 0
        with self.driver.session(database=DB) as s:
            for child_tag, parent_tag in rules:
                result = s.run("""
                    MATCH (child:IFRSTag {name:$child})
                    MATCH (parent:IFRSTag {name:$parent})
                    MERGE (child)-[:HAS_PARENT]->(parent)
                    RETURN count(*) AS c
                """, child=child_tag, parent=parent_tag).single()
                if result and result["c"]:
                    count += 1

        print(f"  ✓ HAS_PARENT edges: {count}")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("Neo4j Knowledge Graph Full Rebuild")
    print("=" * 60)

    # ── Load labels ────────────────────────────────────────────────
    print("\n[1] Loading IFRS labels...")
    label_map = load_ifrs_labels()
    print(f"  {len(label_map)} labels loaded")

    # ── FinBERT setup ──────────────────────────────────────────────
    print(f"\n[2] Loading FinBERT ({MODEL_NAME})...")
    model      = SentenceTransformer(MODEL_NAME)
    tag_keys   = list(ifrs_definition.keys())
    tag_labels = [label_map.get(k, camel_to_sentence(k)) for k in tag_keys]

    print(f"  Embedding {len(tag_labels)} IFRS tags...")
    import torch
    tag_embs_tensor = model.encode(tag_labels, convert_to_tensor=True,
                                   show_progress_bar=True)
    tag_embs_list   = [tag_embs_tensor[i] for i in range(len(tag_keys))]
    print("  Done.")

    # ── Build SubIndustry mapping ──────────────────────────────────
    print("\n[3] Mapping SubIndustries → IFRS tags via FinBERT...")

    # Get all sub-industries
    subindustries = {
        code: data for code, data in gics_definition.items()
        if len(code) == 8
    }

    # Pre-compute sector-level tags for context
    sector_finbert_tags = {}
    for sector_code in [c for c in gics_definition if len(c) == 2]:
        desc = build_sector_description(sector_code)
        emb  = model.encode(desc, convert_to_tensor=True)
        scores = util.cos_sim(emb, tag_embs_tensor)[0].tolist()
        sector_finbert_tags[sector_code] = {
            tag_keys[i] for i, s in enumerate(scores)
            if s >= THRESHOLD_HIGH and tag_keys[i] not in UNIVERSAL_TAGS
        }

    # Map each SubIndustry
    si_mapping   = {}
    total_si     = len(subindustries)

    for idx, (si_code, si_data) in enumerate(subindustries.items(), 1):
        sector_code  = si_code[:2]
        si_name      = si_data.get("name", si_code)
        si_desc      = build_subindustry_description(si_code)
        sector_known = sector_finbert_tags.get(sector_code, set())

        print(f"  [{idx:3d}/{total_si}] {si_name[:45]}", end=" ... ", flush=True)

        tags = map_subindustry_finbert(
            si_code, si_desc,
            sector_known,
            tag_keys, tag_labels, tag_embs_list,
            model,
            use_ollama=True,
        )

        si_mapping[si_code] = tags
        print(f"{len(tags)} tags")

    # Save mapping
    with open(OUTPUT_FILE, "w") as f:
        json.dump(si_mapping, f, indent=2)
    print(f"\n  Saved to {OUTPUT_FILE}")

    # ── Neo4j rebuild ──────────────────────────────────────────────
    print("\n[4] Rebuilding Neo4j graph...")
    builder = GraphBuilder()

    print("  Wiping database...")
    builder.wipe()

    print("  Creating constraints...")
    builder.create_constraints()

    print("  Loading GICS hierarchy (HAS_CHILD)...")
    builder.load_gics()

    print("  Loading IFRSTag nodes...")
    builder.load_ifrs_tags(label_map)

    print("  Loading universal tags → all sectors (HAS_RELEVANT_TAG)...")
    builder.load_universal_to_sectors()

    print("  Loading SubIndustry → IFRS tags (HAS_RELEVANT_TAG)...")
    builder.load_subindustry_tags(si_mapping)

    print("  Loading HAS_PARENT summation rules...")
    builder.load_has_parent(HAS_PARENT_RULES)

    builder.close()

    # ── Summary ────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("✅ Graph rebuild complete!")
    print("=" * 60)
    print("\nGraph structure:")
    print("  Sector -[HAS_CHILD]-> IndustryGroup")
    print("  IndustryGroup -[HAS_CHILD]-> Industry")
    print("  Industry -[HAS_CHILD]-> SubIndustry")
    print("  Sector -[HAS_RELEVANT_TAG {source:universal}]-> IFRSTag")
    print("  SubIndustry -[HAS_RELEVANT_TAG {source:finbert_ollama}]-> IFRSTag")
    print("  IFRSTag -[HAS_PARENT]-> IFRSTag")
    print("\nCypher to verify SNB:")
    print("""
  MATCH (si:SubIndustry {code: '40101015'})
        -[:HAS_RELEVANT_TAG]->(t:IFRSTag)
  RETURN si.name, t.name, t.label
  LIMIT 20
    """)


if __name__ == "__main__":
    main()