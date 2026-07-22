"""
Quick fix — attach universal tags to all SubIndustries in GraphDB.
Run this without re-running the full build.
"""

import requests
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS, XSD
from universal_ifrs_tags import UNIVERSAL_TAGS
from ifrs_tags import definition as ifrs_definition
from d_20230318 import definition as gics_definition

GRAPHDB_URL = "http://localhost:7200"
REPOSITORY  = "ifrs-gics"
UPDATE_URL  = f"{GRAPHDB_URL}/repositories/{REPOSITORY}/statements"
SPARQL_URL  = f"{GRAPHDB_URL}/repositories/{REPOSITORY}"

GICS = Namespace("http://gics.msci.com/ontology/")
IFRS = Namespace("http://xbrl.ifrs.org/taxonomy/2025/")
KG   = Namespace("http://ifrs-gics.ontotext.com/ontology/")


def insert_triples(g: Graph):
    turtle_data = g.serialize(format="turtle")
    response    = requests.post(
        UPDATE_URL,
        data    = turtle_data.encode("utf-8"),
        headers = {"Content-Type": "text/turtle"},
    )
    if response.status_code not in (200, 204):
        raise Exception(f"Insert failed: {response.status_code} {response.text[:200]}")


def fix_missing_tags():
    """Add 3 missing universal tags as XBRLTag nodes."""
    import re

    def camel_to_sentence(name):
        s = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
        s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', s)
        return s.strip()

    # These 3 tags aren't in ifrs_definition but are valid IFRS concepts
    missing_tags = {
        "BasicEarningsLossPerShare": {
            "label": "Basic earnings (loss) per share",
            "balance": "", "period_type": "duration"
        },
        "DilutedEarningsLossPerShare": {
            "label": "Diluted earnings (loss) per share",
            "balance": "", "period_type": "duration"
        },
        "InvestmentsAccountedForUsingEquityMethod": {
            "label": "Investments accounted for using equity method",
            "balance": "debit", "period_type": "instant"
        },
    }

    g = Graph()
    g.bind("ifrs", IFRS)
    g.bind("kg",   KG)
    g.bind("rdfs", RDFS)

    for name, meta in missing_tags.items():
        uri = IFRS[name]
        g.add((uri, RDF.type,          KG.XBRLTag))
        g.add((uri, RDFS.label,        Literal(meta["label"])))
        g.add((uri, IFRS.tagName,      Literal(name)))
        g.add((uri, IFRS.isUniversal,  Literal(True, datatype=XSD.boolean)))
        if meta["balance"]:
            g.add((uri, IFRS.balance,  Literal(meta["balance"])))
        if meta["period_type"]:
            g.add((uri, IFRS.periodType, Literal(meta["period_type"])))

    insert_triples(g)
    print(f"  ✓ Added {len(missing_tags)} missing XBRLTag nodes")


def fix_universal_tags():
    """Attach all universal tags to every SubIndustry."""
    g        = Graph()
    g.bind("gics", GICS)
    g.bind("ifrs", IFRS)
    g.bind("kg",   KG)

    si_codes = [c for c in gics_definition if len(c) == 8]
    count    = 0

    for si_code in si_codes:
        si_uri = GICS[si_code]
        for tag in UNIVERSAL_TAGS:
            g.add((si_uri, KG.HAS_RELEVANT_TAG, IFRS[tag]))
            count += 1

    insert_triples(g)
    print(f"  ✓ Added {count} universal HAS_RELEVANT_TAG triples "
          f"({len(UNIVERSAL_TAGS)} tags × {len(si_codes)} sub-industries)")


def verify():
    """Quick verification."""
    from SPARQLWrapper import SPARQLWrapper, JSON

    sparql = SPARQLWrapper(SPARQL_URL)
    sparql.setReturnFormat(JSON)

    PREFIX = """
        PREFIX kg:   <http://ifrs-gics.ontotext.com/ontology/>
        PREFIX gics: <http://gics.msci.com/ontology/>
        PREFIX ifrs: <http://xbrl.ifrs.org/taxonomy/2025/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    """

    def q(query):
        sparql.setQuery(PREFIX + query)
        return sparql.query().convert()["results"]["bindings"]

    # Total triples
    rows = q("SELECT (COUNT(*) AS ?c) WHERE { ?s kg:HAS_RELEVANT_TAG ?o }")
    print(f"\n  Total HAS_RELEVANT_TAG: {rows[0]['c']['value']}")

    # Universal on Regional Banks
    rows = q("""
        SELECT (COUNT(?tag) AS ?c) WHERE {
            gics:40101015 kg:HAS_RELEVANT_TAG ?tag .
            ?tag ifrs:isUniversal "true"^^<http://www.w3.org/2001/XMLSchema#boolean> .
        }
    """)
    print(f"  Universal tags on Regional Banks: {rows[0]['c']['value']}/52")

    # Total on Regional Banks
    rows = q("""
        SELECT (COUNT(?tag) AS ?c) WHERE {
            gics:40101015 kg:HAS_RELEVANT_TAG ?tag .
        }
    """)
    print(f"  Total tags on Regional Banks:     {rows[0]['c']['value']}")


def main():
    print("=" * 55)
    print("GraphDB Quick Fix")
    print("=" * 55)

    print("\n[1] Adding missing XBRLTag nodes...")
    fix_missing_tags()

    print("\n[2] Attaching universal tags to all SubIndustries...")
    fix_universal_tags()

    print("\n[3] Verifying...")
    verify()

    print("\n✅ Done!")
    print("\nExpected:")
    print("  Total HAS_RELEVANT_TAG: ~14,700+ triples")
    print("  Universal tags on Regional Banks: 52/52")
    print("  Total tags on Regional Banks:     127")


if __name__ == "__main__":
    main()