"""
Load the full GICS → IFRS knowledge graph into Neo4j.

Graph schema:
  Nodes:
    (:Sector      {code, name})                        — GICS top level
    (:IndustryGroup {code, name})                      — GICS 4-digit
    (:Industry    {code, name})                        — GICS 6-digit
    (:SubIndustry {code, name, description})           — GICS 8-digit
    (:IFRSTag     {name, label, balance, period_type}) — IFRS XBRL tag

  Relationships:
    (:Sector)-[:PARENT_OF]->(:IndustryGroup)
    (:IndustryGroup)-[:PARENT_OF]->(:Industry)
    (:Industry)-[:PARENT_OF]->(:SubIndustry)
    (:Sector)-[:MAPS_TO {source}]->(:IFRSTag)         — from merged mapping
    (:IFRSTag)-[:SUMS_TO]->(:IFRSTag)                 — validation rules

Usage:
    python load_neo4j.py
"""

import json
import xml.etree.ElementTree as ET
from neo4j import GraphDatabase

from d_20230318 import definition as gics_definition


# ── Config ─────────────────────────────────────────────────────────────────────
URI      = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "12345678"

MAPPING_FILE = "data/mappings/gics_ifrs_mapping_merged.json"


# ── IFRS tag parser ────────────────────────────────────────────────────────────

def load_ifrs_tags():
    """Parse IFRS tags from XSD + labels XML."""
    # Parse labels
    label_map = {}
    tree = ET.parse("data/taxonomy/lab_full_ifrs-en_2025-03-27.xml")
    root = tree.getroot()
    ns   = {
        "link":  "http://www.xbrl.org/2003/linkbase",
        "xlink": "http://www.w3.org/1999/xlink"
    }
    for label in root.findall(".//link:label", ns):
        role = label.get("{http://www.w3.org/1999/xlink}label", "")
        text = label.text or ""
        if role and text:
            tag = role.replace("label_", "").replace("_label_en", "").split("_label")[0]
            tag = tag.replace("ifrs-full_", "")
            if tag not in label_map:
                label_map[tag] = text

    # Parse monetary tags from XSD
    xsd_tree = ET.parse("data/taxonomy/full_ifrs-cor_2025-03-27.xsd")
    xsd_root = xsd_tree.getroot()
    xsd_ns   = {"xs": "http://www.w3.org/2001/XMLSchema"}

    ifrs_tags = {}
    for elem in xsd_root.findall(".//xs:element", xsd_ns):
        name    = elem.get("name", "")
        typ     = elem.get("type", "")
        balance = elem.get("{http://www.xbrl.org/2003/instance}balance", "")
        period  = elem.get("{http://www.xbrl.org/2003/instance}periodType", "")
        if "monetaryItemType" in typ and name:
            ifrs_tags[name] = {
                "label":       label_map.get(name, name),
                "balance":     balance,
                "period_type": period,
            }

    return ifrs_tags


# ── SUMS_TO validation rules ───────────────────────────────────────────────────

SUMS_TO_RULES = [
    # Assets = NonCurrentAssets + CurrentAssets
    ("NoncurrentAssets",  "Assets"),
    ("CurrentAssets",     "Assets"),

    # Equity + Liabilities = Assets
    ("Equity",            "Assets"),
    ("Liabilities",       "Assets"),

    # Liabilities breakdown
    ("NoncurrentLiabilities", "Liabilities"),
    ("CurrentLiabilities",    "Liabilities"),

    # Equity breakdown
    ("IssuedCapital",          "Equity"),
    ("SharePremium",           "Equity"),
    ("RetainedEarnings",       "Equity"),
    ("NoncontrollingInterests","Equity"),

    # Profit
    ("ProfitLossFromContinuingOperations", "ProfitLoss"),
    ("ProfitLossAttributableToOwnersOfParent", "ProfitLoss"),
    ("ProfitLossAttributableToNoncontrollingInterests", "ProfitLoss"),

    # Cash flows
    ("CashFlowsFromUsedInOperatingActivities",  "IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges"),
    ("CashFlowsFromUsedInInvestingActivities",  "IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges"),
    ("CashFlowsFromUsedInFinancingActivities",  "IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges"),
]


# ── Neo4j loader ───────────────────────────────────────────────────────────────

class GraphLoader:

    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    def clear_database(self):
        """Wipe everything — start fresh."""
        with self.driver.session(database="ifrs-gics") as session:
            session.run("MATCH (n) DETACH DELETE n")
            print("  ✓ Database cleared")

    def create_constraints(self):
        """Create uniqueness constraints for fast lookup."""
        with self.driver.session(database="ifrs-gics") as session:
            constraints = [
                "CREATE CONSTRAINT sector_code IF NOT EXISTS FOR (n:Sector) REQUIRE n.code IS UNIQUE",
                "CREATE CONSTRAINT industry_group_code IF NOT EXISTS FOR (n:IndustryGroup) REQUIRE n.code IS UNIQUE",
                "CREATE CONSTRAINT industry_code IF NOT EXISTS FOR (n:Industry) REQUIRE n.code IS UNIQUE",
                "CREATE CONSTRAINT subindustry_code IF NOT EXISTS FOR (n:SubIndustry) REQUIRE n.code IS UNIQUE",
                "CREATE CONSTRAINT ifrstag_name IF NOT EXISTS FOR (n:IFRSTag) REQUIRE n.name IS UNIQUE",
            ]
            for c in constraints:
                session.run(c)
            print("  ✓ Constraints created")

    def load_gics_hierarchy(self, gics: dict):
        """Load all GICS nodes and PARENT_OF relationships."""
        with self.driver.session(database="ifrs-gics") as session:
            sectors        = 0
            industry_groups = 0
            industries     = 0
            subindustries  = 0

            for code, data in gics.items():
                name = data.get("name", "")
                desc = data.get("description", "")

                if len(code) == 2:
                    session.run(
                        "MERGE (n:Sector {code: $code}) SET n.name = $name",
                        code=code, name=name
                    )
                    sectors += 1

                elif len(code) == 4:
                    session.run(
                        "MERGE (n:IndustryGroup {code: $code}) SET n.name = $name",
                        code=code, name=name
                    )
                    # PARENT_OF: Sector → IndustryGroup
                    session.run("""
                        MATCH (s:Sector {code: $sector_code})
                        MATCH (ig:IndustryGroup {code: $ig_code})
                        MERGE (s)-[:PARENT_OF]->(ig)
                    """, sector_code=code[:2], ig_code=code)
                    industry_groups += 1

                elif len(code) == 6:
                    session.run(
                        "MERGE (n:Industry {code: $code}) SET n.name = $name",
                        code=code, name=name
                    )
                    # PARENT_OF: IndustryGroup → Industry
                    session.run("""
                        MATCH (ig:IndustryGroup {code: $ig_code})
                        MATCH (i:Industry {code: $i_code})
                        MERGE (ig)-[:PARENT_OF]->(i)
                    """, ig_code=code[:4], i_code=code)
                    industries += 1

                elif len(code) == 8:
                    session.run(
                        "MERGE (n:SubIndustry {code: $code}) SET n.name = $name, n.description = $desc",
                        code=code, name=name, desc=desc
                    )
                    # PARENT_OF: Industry → SubIndustry
                    session.run("""
                        MATCH (i:Industry {code: $i_code})
                        MATCH (si:SubIndustry {code: $si_code})
                        MERGE (i)-[:PARENT_OF]->(si)
                    """, i_code=code[:6], si_code=code)
                    subindustries += 1

            print(f"  ✓ GICS nodes: {sectors} sectors, {industry_groups} industry groups, "
                  f"{industries} industries, {subindustries} sub-industries")

    def load_ifrs_tags(self, ifrs_tags: dict):
        """Load all IFRS tag nodes."""
        with self.driver.session(database="ifrs-gics") as session:
            count = 0
            for name, meta in ifrs_tags.items():
                session.run("""
                    MERGE (t:IFRSTag {name: $name})
                    SET t.label       = $label,
                        t.balance     = $balance,
                        t.period_type = $period_type
                """,
                    name=name,
                    label=meta["label"],
                    balance=meta.get("balance", ""),
                    period_type=meta.get("period_type", ""),
                )
                count += 1
            print(f"  ✓ IFRS tag nodes: {count}")

    def load_maps_to(self, mapping: dict):
        """Load MAPS_TO edges from sector to IFRS tags."""
        with self.driver.session(database="ifrs-gics") as session:
            total = 0
            for sector_code, data in mapping.items():
                universal_set = set(data.get("universal_tags", []))

                for tag in data.get("ifrs_tags", []):
                    source = "universal" if tag in universal_set else "finbert_ollama"
                    session.run("""
                        MATCH (s:Sector {code: $sector_code})
                        MATCH (t:IFRSTag {name: $tag_name})
                        MERGE (s)-[r:MAPS_TO]->(t)
                        SET r.source = $source
                    """,
                        sector_code=sector_code,
                        tag_name=tag,
                        source=source,
                    )
                    total += 1

            print(f"  ✓ MAPS_TO relationships: {total}")

    def load_sums_to(self, rules: list):
        """Load SUMS_TO validation edges between IFRS tags."""
        with self.driver.session(database="ifrs-gics") as session:
            count = 0
            for child_tag, parent_tag in rules:
                result = session.run("""
                    MATCH (child:IFRSTag {name: $child})
                    MATCH (parent:IFRSTag {name: $parent})
                    MERGE (child)-[:SUMS_TO]->(parent)
                    RETURN count(*) AS created
                """, child=child_tag, parent=parent_tag)
                count += 1
            print(f"  ✓ SUMS_TO relationships: {count}")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("Loading IFRS tags from XSD...")
    ifrs_tags = load_ifrs_tags()
    print(f"  {len(ifrs_tags)} monetary tags loaded")

    print("\nLoading GICS → IFRS mapping...")
    with open(MAPPING_FILE) as f:
        mapping = json.load(f)
    print(f"  {len(mapping)} sectors loaded")

    print("\nConnecting to Neo4j...")
    loader = GraphLoader(URI, USERNAME, PASSWORD)

    print("\n[1/5] Clearing database...")
    loader.clear_database()

    print("\n[2/5] Creating constraints...")
    loader.create_constraints()

    print("\n[3/5] Loading GICS hierarchy...")
    loader.load_gics_hierarchy(gics_definition)

    print("\n[4/5] Loading IFRS tag nodes...")
    loader.load_ifrs_tags(ifrs_tags)

    print("\n[5/5] Loading MAPS_TO relationships...")
    loader.load_maps_to(mapping)

    print("\n[6/6] Loading SUMS_TO validation rules...")
    loader.load_sums_to(SUMS_TO_RULES)

    loader.close()

    print("\n✅ Graph loaded successfully!")
    print("\nOpen Neo4j Browser at http://localhost:7474 and run:")
    print("  MATCH (s:Sector)-[:MAPS_TO]->(t:IFRSTag)")
    print("  WHERE s.code = '40'")
    print("  RETURN s, t LIMIT 50")


if __name__ == "__main__":
    main()