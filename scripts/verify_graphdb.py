"""
Verify universal tags are loaded correctly in GraphDB.
"""

from SPARQLWrapper import SPARQLWrapper, JSON
from universal_ifrs_tags import UNIVERSAL_TAGS

SPARQL_URL = "http://localhost:7200/repositories/ifrs-gics"

PREFIX = """
    PREFIX kg:   <http://ifrs-gics.ontotext.com/ontology/>
    PREFIX gics: <http://gics.msci.com/ontology/>
    PREFIX ifrs: <http://xbrl.ifrs.org/taxonomy/2025/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""

sparql = SPARQLWrapper(SPARQL_URL)
sparql.setReturnFormat(JSON)


def query(q):
    sparql.setQuery(PREFIX + q)
    return sparql.query().convert()["results"]["bindings"]


def main():

    # ── 1. Total HAS_RELEVANT_TAG triples ─────────────────────
    print("=" * 55)
    print("UNIVERSAL TAG VERIFICATION")
    print("=" * 55)

    rows = query("SELECT (COUNT(*) AS ?c) WHERE { ?s kg:HAS_RELEVANT_TAG ?o }")
    print(f"\nTotal HAS_RELEVANT_TAG triples: {rows[0]['c']['value']}")

    # ── 2. Check each universal tag exists as XBRLTag ──────────
    print(f"\nChecking {len(UNIVERSAL_TAGS)} universal tags in GraphDB...")
    missing = []
    for tag in sorted(UNIVERSAL_TAGS):
        rows = query(f"""
            SELECT ?label WHERE {{
                ifrs:{tag} rdfs:label ?label .
            }}
        """)
        if not rows:
            missing.append(tag)

    if missing:
        print(f"  ❌ Missing from GraphDB ({len(missing)}):")
        for t in missing:
            print(f"    {t}")
    else:
        print(f"  ✅ All {len(UNIVERSAL_TAGS)} universal tags exist as XBRLTag nodes")

    # ── 3. Check universal tags on Regional Banks ──────────────
    print(f"\nChecking universal tags on Regional Banks (40101015)...")
    rows = query("""
        SELECT ?tagName WHERE {
            gics:40101015 kg:HAS_RELEVANT_TAG ?tag .
            ?tag ifrs:tagName ?tagName .
            ?tag ifrs:isUniversal "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
        }
        ORDER BY ?tagName
    """)

    found_universal = {r["tagName"]["value"] for r in rows}
    missing_on_si   = UNIVERSAL_TAGS - found_universal

    print(f"  Universal tags on Regional Banks: {len(found_universal)}/{len(UNIVERSAL_TAGS)}")

    if missing_on_si:
        print(f"  ❌ Missing on SubIndustry ({len(missing_on_si)}):")
        for t in sorted(missing_on_si):
            print(f"    {t}")
    else:
        print(f"  ✅ All {len(UNIVERSAL_TAGS)} universal tags attached to Regional Banks")

    # ── 4. Sample — show first 10 universal tags on SNB ────────
    print(f"\nSample universal tags on Regional Banks:")
    for tag in sorted(found_universal)[:10]:
        print(f"  {tag}")

    # ── 5. Count sector-specific vs universal per SubIndustry ──
    print(f"\nTag breakdown for Regional Banks (40101015):")
    rows = query("""
        SELECT 
            (COUNT(?tag) AS ?total)
        WHERE {
            gics:40101015 kg:HAS_RELEVANT_TAG ?tag .
        }
    """)
    total = int(rows[0]["total"]["value"])

    rows = query("""
        SELECT (COUNT(?tag) AS ?universal) WHERE {
            gics:40101015 kg:HAS_RELEVANT_TAG ?tag .
            ?tag ifrs:isUniversal "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
        }
    """)
    universal = int(rows[0]["universal"]["value"])
    specific  = total - universal

    print(f"  Total tags:       {total}")
    print(f"  Universal tags:   {universal}")
    print(f"  Sector-specific:  {specific}")
    print(f"  Expected total:   {len(UNIVERSAL_TAGS)} + {specific} = {len(UNIVERSAL_TAGS) + specific}")


if __name__ == "__main__":
    main()