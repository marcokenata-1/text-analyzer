"""
GraphDB/SPARQL access for api.py: pruned candidate tags and summation
rules, both read from the knowledge graph build_graphdb.py loads.
"""

import os

import requests
from fastapi import HTTPException

GRAPHDB_URL = os.environ.get("GRAPHDB_URL", "http://localhost:7200")
REPOSITORY  = os.environ.get("GRAPHDB_REPOSITORY", "ifrs-gics")
SPARQL_URL  = f"{GRAPHDB_URL}/repositories/{REPOSITORY}"

PREFIXES = """
    PREFIX kg:   <http://ifrs-gics.ontotext.com/ontology/>
    PREFIX gics: <http://gics.msci.com/ontology/>
    PREFIX ifrs: <http://xbrl.ifrs.org/taxonomy/2025/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""


def _sparql_select(query: str) -> list[dict]:
    """Run a SPARQL SELECT against GraphDB, return its result bindings."""
    resp = requests.get(
        SPARQL_URL,
        params={"query": PREFIXES + query},
        headers={"Accept": "application/sparql-results+json"},
    )
    if resp.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail=f"GraphDB query failed: {resp.status_code} {resp.text[:200]}",
        )
    return resp.json()["results"]["bindings"]


def fetch_relevant_tags(si_code: str) -> list[str]:
    """Pruned candidate XBRL tags for a sub-industry, via GraphDB HAS_RELEVANT_TAG."""
    bindings = _sparql_select(f"""
        SELECT ?tagName WHERE {{
            gics:{si_code} kg:HAS_RELEVANT_TAG ?t .
            ?t ifrs:tagName ?tagName .
        }}
    """)
    return [b["tagName"]["value"] for b in bindings]


def fetch_summation_rules() -> dict[str, list[tuple[str, float]]]:
    """
    Every HAS_CHILD_TAG (+1.0) / HAS_CHILD_TAG_NEGATIVE (-1.0) parent->child
    pair in GraphDB, grouped by parent tag as (child, weight). Sourced from
    the IFRS taxonomy's calculation linkbases, e.g. GrossProfit = Revenue
    (+1.0) - CostOfSales (-1.0).
    """
    bindings = _sparql_select("""
        SELECT ?parentName ?childName ?sign WHERE {
            { ?parent kg:HAS_CHILD_TAG ?child . BIND("+" AS ?sign) }
            UNION
            { ?parent kg:HAS_CHILD_TAG_NEGATIVE ?child . BIND("-" AS ?sign) }
            ?parent ifrs:tagName ?parentName .
            ?child  ifrs:tagName ?childName .
        }
    """)
    rules: dict[str, list[tuple[str, float]]] = {}
    for b in bindings:
        weight = 1.0 if b["sign"]["value"] == "+" else -1.0
        rules.setdefault(b["parentName"]["value"], []).append((b["childName"]["value"], weight))
    return rules
