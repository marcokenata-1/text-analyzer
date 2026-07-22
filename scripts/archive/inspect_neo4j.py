"""
Inspect current Neo4j graph structure.
Run this to see what's actually in the graph.
"""

from neo4j import GraphDatabase

URI      = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "12345678"
DB       = "ifrs-gics"


def inspect():
    driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

    with driver.session(database=DB) as session:

        # ── Node labels ───────────────────────────────────────────────────────
        print("=" * 60)
        print("NODE LABELS AND COUNTS")
        print("=" * 60)
        result = session.run("CALL db.labels() YIELD label RETURN label")
        labels = [r["label"] for r in result]
        for label in labels:
            count = session.run(
                f"MATCH (n:{label}) RETURN count(n) AS c"
            ).single()["c"]
            print(f"  {label:25s}: {count}")

        # ── Relationship types ────────────────────────────────────────────────
        print("\n" + "=" * 60)
        print("RELATIONSHIP TYPES AND COUNTS")
        print("=" * 60)
        result = session.run(
            "CALL db.relationshipTypes() YIELD relationshipType RETURN relationshipType"
        )
        rel_types = [r["relationshipType"] for r in result]
        for rel in rel_types:
            count = session.run(
                f"MATCH ()-[r:{rel}]->() RETURN count(r) AS c"
            ).single()["c"]
            print(f"  {rel:25s}: {count}")

        # ── Sample SUMS_TO rules ──────────────────────────────────────────────
        print("\n" + "=" * 60)
        print("CURRENT SUMS_TO RULES")
        print("=" * 60)
        result = session.run("""
            MATCH (child:IFRSTag)-[:SUMS_TO]->(parent:IFRSTag)
            RETURN child.name  AS child,
                   child.label AS child_label,
                   parent.name  AS parent,
                   parent.label AS parent_label
            ORDER BY parent.name
        """)
        rows = list(result)
        if not rows:
            print("  ⚠️  No SUMS_TO rules found!")
        for row in rows:
            print(f"  {row['child_label']:50s}")
            print(f"    → {row['parent_label']}")
            print()

        # ── Sample MAPS_TO ────────────────────────────────────────────────────
        print("\n" + "=" * 60)
        print("SAMPLE MAPS_TO (Financials sector, first 10)")
        print("=" * 60)
        result = session.run("""
            MATCH (s:Sector {code: '40'})-[r:MAPS_TO]->(t:IFRSTag)
            RETURN t.name AS name, t.label AS label, r.source AS source
            ORDER BY t.name
            LIMIT 10
        """)
        for row in result:
            print(f"  [{row['source']:15s}] {row['name']}")
            print(f"                    → {row['label']}")

        # ── GICS hierarchy sample ─────────────────────────────────────────────
        print("\n" + "=" * 60)
        print("GICS HIERARCHY SAMPLE (Financials)")
        print("=" * 60)
        result = session.run("""
            MATCH (s:Sector {code: '40'})
                  -[:PARENT_OF]->(ig:IndustryGroup)
                  -[:PARENT_OF]->(i:Industry)
                  -[:PARENT_OF]->(si:SubIndustry)
            RETURN ig.name AS ig, i.name AS i, si.name AS si
            ORDER BY ig.name, i.name
            LIMIT 10
        """)
        for row in result:
            print(f"  {row['ig']:30s} > {row['i']:30s} > {row['si']}")

        # ── IFRSTag sample with properties ────────────────────────────────────
        print("\n" + "=" * 60)
        print("IFRSTAG SAMPLE — checking properties")
        print("=" * 60)
        result = session.run("""
            MATCH (t:IFRSTag)
            RETURN t.name AS name, t.label AS label,
                   t.balance AS balance, t.period_type AS period_type
            LIMIT 10
        """)
        for row in result:
            print(f"  {row['name']}")
            print(f"    label:       {row['label']}")
            print(f"    balance:     {row['balance']}")
            print(f"    period_type: {row['period_type']}")
            print()

    driver.close()


if __name__ == "__main__":
    inspect()