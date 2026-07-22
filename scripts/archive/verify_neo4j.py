"""
Verify the Neo4j graph loaded correctly.
Run this after load_neo4j.py to check all nodes and relationships.
"""

from neo4j import GraphDatabase

URI      = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "12345678"


def verify():
    driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

    with driver.session(database="ifrs-gics") as session:

        # ── Node counts ────────────────────────────────────────────────────
        print("=" * 55)
        print("NODE COUNTS")
        print("=" * 55)

        labels = ["Sector", "IndustryGroup", "Industry", "SubIndustry", "IFRSTag"]
        for label in labels:
            result = session.run(f"MATCH (n:{label}) RETURN count(n) AS count")
            count  = result.single()["count"]
            print(f"  {label:20s}: {count}")

        # ── Relationship counts ────────────────────────────────────────────
        print("\n" + "=" * 55)
        print("RELATIONSHIP COUNTS")
        print("=" * 55)

        rels = ["PARENT_OF", "MAPS_TO", "SUMS_TO"]
        for rel in rels:
            result = session.run(f"MATCH ()-[r:{rel}]->() RETURN count(r) AS count")
            count  = result.single()["count"]
            print(f"  {rel:20s}: {count}")

        # ── Sectors with tag counts ────────────────────────────────────────
        print("\n" + "=" * 55)
        print("SECTORS → IFRS TAG COUNTS")
        print("=" * 55)

        result = session.run("""
            MATCH (s:Sector)-[:MAPS_TO]->(t:IFRSTag)
            RETURN s.code AS code, s.name AS name, count(t) AS tags
            ORDER BY s.code
        """)
        for row in result:
            print(f"  [{row['code']}] {row['name']:35s} → {row['tags']} tags")

        # ── Financials unique tags sample ──────────────────────────────────
        print("\n" + "=" * 55)
        print("SAMPLE — FINANCIALS (40) IFRS TAGS")
        print("=" * 55)

        result = session.run("""
            MATCH (s:Sector {code: '40'})-[r:MAPS_TO]->(t:IFRSTag)
            RETURN t.name AS name, t.label AS label, r.source AS source
            ORDER BY t.name
            LIMIT 20
        """)
        for row in result:
            print(f"  [{row['source']:20s}] {row['name']}")
            print(f"                         → {row['label']}")

        # ── SUMS_TO validation rules ───────────────────────────────────────
        print("\n" + "=" * 55)
        print("SUMS_TO VALIDATION RULES")
        print("=" * 55)

        result = session.run("""
            MATCH (child:IFRSTag)-[:SUMS_TO]->(parent:IFRSTag)
            RETURN child.name AS child, parent.name AS parent
            ORDER BY parent.name
        """)
        for row in result:
            print(f"  {row['child']:55s} → {row['parent']}")

        # ── Financials hierarchy ───────────────────────────────────────────
        print("\n" + "=" * 55)
        print("FINANCIALS HIERARCHY (40)")
        print("=" * 55)

        result = session.run("""
            MATCH (s:Sector {code: '40'})-[:PARENT_OF]->(ig:IndustryGroup)
                  -[:PARENT_OF]->(i:Industry)
                  -[:PARENT_OF]->(si:SubIndustry)
            RETURN ig.name AS industry_group, i.name AS industry, si.name AS subindustry
            ORDER BY ig.name, i.name, si.name
        """)
        for row in result:
            print(f"  {row['industry_group']:30s} > {row['industry']:30s} > {row['subindustry']}")

    driver.close()
    print("\n✅ Verification complete!")


if __name__ == "__main__":
    verify()
