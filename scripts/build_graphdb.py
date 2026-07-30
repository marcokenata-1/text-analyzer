"""
GraphDB Knowledge Graph Builder

Replaces Neo4j entirely — loads IFRS-GICS knowledge graph into
Ontotext GraphDB using RDF triples and SPARQL.

Graph structure (matches KG diagram):
    gics:Sector -[kg:PARENT_OF]-> gics:IndustryGroup
    gics:IndustryGroup -[kg:PARENT_OF]-> gics:Industry
    gics:Industry -[kg:PARENT_OF]-> gics:SubIndustry
    gics:SubIndustry -[kg:HAS_RELEVANT_TAG]-> ifrs:XBRLTag
    ifrs:XBRLTag -[kg:HAS_CHILD_TAG]-> ifrs:XBRLTag          (summation rules, weight +1.0)
    ifrs:XBRLTag -[kg:HAS_CHILD_TAG_NEGATIVE]-> ifrs:XBRLTag (summation rules, weight -1.0)

SubIndustry → XBRL tag mapping is read directly from
data/mappings/subindustry_ifrs_mapping_v3_katana.json (already computed
on Katana HPC via the two-stage FinBERT + Qwen3 mapper). This script does
not recompute the mapping — it only loads it, plus the universal tags,
into GraphDB.

Setup:
    pip install SPARQLWrapper rdflib requests
    GraphDB running at http://localhost:7200 (docker compose up -d graphdb)
    Repository 'ifrs-gics' is auto-created if missing
"""

import fnmatch
import glob
import io
import json
import re
import requests
import xml.etree.ElementTree as ET
import zipfile
from rdflib import Graph, Namespace, URIRef, Literal, RDF, RDFS, XSD
from SPARQLWrapper import SPARQLWrapper, JSON

from d_20230318          import definition as gics_definition
from ifrs_tags           import definition as ifrs_definition
from universal_ifrs_tags import UNIVERSAL_TAGS


# ── Config ─────────────────────────────────────────────────────────────────────
GRAPHDB_URL  = "http://localhost:7200"
REPOSITORY   = "ifrs-gics"
SPARQL_URL   = f"{GRAPHDB_URL}/repositories/{REPOSITORY}"
UPDATE_URL   = f"{GRAPHDB_URL}/repositories/{REPOSITORY}/statements"

INPUT_JSON   = "data/mappings/subindustry_ifrs_mapping_v3_katana.json"

# Official IFRS Accounting Taxonomy package (xbrl.ifrs.org), used as a
# fallback source for the two functions below when data/taxonomy/ hasn't
# been extracted/flattened by hand — reads straight out of the zip instead.
TAXONOMY_ZIP = "IFRSAT-2025.zip"


def _taxonomy_files(flat_glob: str, zip_glob: str):
    """Yield readable file objects matching flat_glob under data/taxonomy/,
    or — if none are found there — matching zip_glob inside TAXONOMY_ZIP."""
    paths = sorted(glob.glob(flat_glob))
    if paths:
        for path in paths:
            yield open(path, "rb")
        return
    with zipfile.ZipFile(TAXONOMY_ZIP) as zf:
        for name in sorted(n for n in zf.namelist() if fnmatch.fnmatch(n, zip_glob)):
            yield io.BytesIO(zf.read(name))

REPO_CONFIG_TTL = f"""
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rep: <http://www.openrdf.org/config/repository#> .
@prefix sr: <http://www.openrdf.org/config/repository/sail#> .
@prefix sail: <http://www.openrdf.org/config/sail#> .
@prefix graphdb: <http://www.ontotext.com/config/graphdb#> .

[] a rep:Repository ;
    rep:repositoryID "{REPOSITORY}" ;
    rdfs:label "IFRS-GICS Knowledge Graph" ;
    rep:repositoryImpl [
        rep:repositoryType "graphdb:SailRepository" ;
        sr:sailImpl [
            sail:sailType "graphdb:Sail" ;
            graphdb:ruleset "rdfsplus-optimized" ;
            graphdb:storage-folder "storage" ;
            graphdb:base-URL "http://example.org/owlim#" ;
            graphdb:repository-type "file-repository" ;
            graphdb:check-for-inconsistencies "false" ;
            graphdb:disable-sameAs "true" ;
            graphdb:enable-context-index "false" ;
            graphdb:enablePredicateList "true" ;
            graphdb:in-memory-literal-properties "true" ;
            graphdb:enable-literal-index "true" ;
            graphdb:throw-QueryEvaluationException-on-timeout "false" ;
            graphdb:query-timeout "0" ;
            graphdb:query-limit-results "0" ;
            graphdb:read-only "false" ;
        ]
    ] .
"""


# ── RDF Namespaces ─────────────────────────────────────────────────────────────
GICS = Namespace("http://gics.msci.com/ontology/")
IFRS = Namespace("http://xbrl.ifrs.org/taxonomy/2025/")
KG   = Namespace("http://ifrs-gics.ontotext.com/ontology/")


def load_calculation_rules() -> list[tuple[str, str, float]]:
    """
    (parent, child, weight) summation triples — weight +1.0 for addition,
    -1.0 for subtraction, e.g. GrossProfit = Revenue - CostOfSales.

    Parsed directly from the IFRS Accounting Taxonomy's own calculation
    linkbase XML (data/taxonomy/linkbases/*/cal_*.xml — Statement of
    Financial Position, Profit or Loss, Comprehensive Income, Changes in
    Equity, Cash Flows) rather than hand-transcribed, so it can't silently
    drift out of sync with the taxonomy: a hand-transcribed copy of this
    same data was previously missing ~90 of the 415 real summation arcs
    the linkbase XML actually defines.

    Each linkbase file defines <link:loc> elements mapping a short local
    label (e.g. "loc_1") to a tag name via its xlink:href fragment, and
    <link:calculationArc> elements connecting two such labels with a
    weight — this resolves the arcs' labels back to tag names via each
    file's own loc map (labels aren't unique across files).
    """
    ns = {
        "link":  "http://www.xbrl.org/2003/linkbase",
        "xlink": "http://www.w3.org/1999/xlink",
    }
    rules: set[tuple[str, str, float]] = set()

    for f in _taxonomy_files(
        "data/taxonomy/linkbases/*/cal_*.xml",
        "IFRSAT-2025/full_ifrs/linkbases/*/cal_*.xml",
    ):
        root = ET.parse(f).getroot()
        label_to_tag = {}
        for loc in root.findall(".//link:loc", ns):
            href = loc.get(f"{{{ns['xlink']}}}href", "")
            if "#ifrs-full_" in href:
                label = loc.get(f"{{{ns['xlink']}}}label")
                label_to_tag[label] = href.split("#ifrs-full_")[-1]

        for arc in root.findall(".//link:calculationArc", ns):
            from_tag = label_to_tag.get(arc.get(f"{{{ns['xlink']}}}from"))
            to_tag   = label_to_tag.get(arc.get(f"{{{ns['xlink']}}}to"))
            weight   = arc.get("weight")
            if from_tag and to_tag and weight:
                rules.add((from_tag, to_tag, float(weight)))

    return sorted(rules)


# ── Helpers ────────────────────────────────────────────────────────────────────

def camel_to_sentence(name: str) -> str:
    s = re.sub(r'([a-z])([A-Z])', r'\1 \2', name)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', s)
    return s.strip()


def load_ifrs_labels() -> dict:
    label_map = {}
    f = next(_taxonomy_files(
        "data/taxonomy/lab_full_ifrs-en_2025-03-27.xml",
        "IFRSAT-2025/full_ifrs/labels/lab_full_ifrs-en_2025-03-27.xml",
    ))
    root = ET.parse(f).getroot()
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
    for tag in ifrs_definition:
        if tag not in label_map:
            label_map[tag] = camel_to_sentence(tag)
    return label_map


# ── GraphDB RDF loader ─────────────────────────────────────────────────────────

class GraphDBLoader:

    def __init__(self):
        self.update_url = UPDATE_URL
        self._ensure_repository()
        self.sparql = SPARQLWrapper(SPARQL_URL)
        self.sparql.setReturnFormat(JSON)
        self._test_connection()

    def _ensure_repository(self):
        """Create the repository if it doesn't already exist."""
        resp = requests.get(f"{GRAPHDB_URL}/rest/repositories")
        if resp.status_code != 200:
            raise ConnectionError(
                f"Cannot reach GraphDB at {GRAPHDB_URL}: {resp.status_code}\n"
                f"Make sure GraphDB is running (docker compose up -d graphdb)"
            )
        existing = {r["id"] for r in resp.json()}
        if REPOSITORY in existing:
            print(f"  ✓ Repository '{REPOSITORY}' already exists")
            return

        create_resp = requests.post(
            f"{GRAPHDB_URL}/rest/repositories",
            files={"config": ("repo-config.ttl", REPO_CONFIG_TTL, "text/turtle")},
        )
        if create_resp.status_code not in (200, 201):
            raise Exception(
                f"Repository creation failed: {create_resp.status_code} "
                f"{create_resp.text[:300]}"
            )
        print(f"  ✓ Repository '{REPOSITORY}' created")

    def _test_connection(self):
        try:
            self.sparql.setQuery("SELECT * WHERE { ?s ?p ?o } LIMIT 1")
            self.sparql.query()
            print(f"  ✓ Connected to GraphDB at {GRAPHDB_URL}")
            print(f"  ✓ Repository: {REPOSITORY}")
        except Exception as e:
            raise ConnectionError(f"Cannot connect to GraphDB: {e}\n"
                                  f"Make sure GraphDB is running at {GRAPHDB_URL}")

    def clear(self):
        """Clear all triples from repository."""
        response = requests.delete(UPDATE_URL)
        if response.status_code not in (200, 204):
            raise Exception(f"Clear failed: {response.status_code}")
        print("  ✓ Repository cleared")

    def _insert_triples(self, g: Graph):
        """Insert an rdflib Graph into GraphDB via REST API."""
        turtle_data = g.serialize(format="turtle")
        response    = requests.post(
            UPDATE_URL,
            data    = turtle_data.encode("utf-8"),
            headers = {"Content-Type": "text/turtle"},
        )
        if response.status_code not in (200, 204):
            raise Exception(f"GraphDB insert failed: {response.status_code} {response.text[:200]}")

    def load_ontology(self):
        """Define the ontology classes and properties."""
        g = Graph()
        g.bind("gics", GICS)
        g.bind("ifrs", IFRS)
        g.bind("kg",   KG)

        # Classes
        for cls in ["Sector", "IndustryGroup", "Industry", "SubIndustry", "XBRLTag"]:
            g.add((KG[cls], RDF.type, RDFS.Class))
            g.add((KG[cls], RDFS.label, Literal(cls)))

        # Properties
        props = {
            "PARENT_OF":       ("GICS hierarchy parent-child relationship", KG.Sector,      KG.IndustryGroup),
            "HAS_RELEVANT_TAG":("Maps a GICS SubIndustry to relevant XBRL tags", KG.SubIndustry, KG.XBRLTag),
            "HAS_CHILD_TAG":   ("XBRL summation rule (additive) — parent tag contains child tag", KG.XBRLTag, KG.XBRLTag),
            "HAS_CHILD_TAG_NEGATIVE": ("XBRL summation rule (subtractive) — parent tag subtracts child tag", KG.XBRLTag, KG.XBRLTag),
        }
        for prop, (comment, domain, range_) in props.items():
            g.add((KG[prop], RDF.type,         RDF["Property"]))
            g.add((KG[prop], RDFS.label,       Literal(prop)))
            g.add((KG[prop], RDFS.comment,     Literal(comment)))
            g.add((KG[prop], RDFS.domain,      domain))
            g.add((KG[prop], RDFS.range,       range_))

        self._insert_triples(g)
        print("  ✓ Ontology loaded")

    def load_gics_hierarchy(self):
        """Load GICS nodes and PARENT_OF relationships."""
        g = Graph()
        g.bind("gics", GICS)
        g.bind("kg",   KG)
        g.bind("rdfs", RDFS)

        counts = {2: 0, 4: 0, 6: 0, 8: 0}
        node_types = {2: KG.Sector, 4: KG.IndustryGroup, 6: KG.Industry, 8: KG.SubIndustry}

        for code, data in gics_definition.items():
            name = data.get("name", "")
            desc = data.get("description", "")
            n    = len(code)

            node_type = node_types.get(n)
            if node_type is None:
                continue

            uri = GICS[code]
            g.add((uri, RDF.type,           node_type))
            g.add((uri, RDFS.label,         Literal(name)))
            g.add((uri, GICS.code,          Literal(code)))

            if desc:
                g.add((uri, RDFS.comment, Literal(desc)))

            # PARENT_OF relationship
            if n > 2:
                parent_code = code[:n-2]
                parent_uri  = GICS[parent_code]
                g.add((parent_uri, KG.PARENT_OF, uri))

            counts[n] += 1

        self._insert_triples(g)
        print(f"  ✓ GICS: {counts[2]} sectors, {counts[4]} groups, "
              f"{counts[6]} industries, {counts[8]} sub-industries")
        print(f"  ✓ PARENT_OF edges: {counts[4]+counts[6]+counts[8]}")

    def load_xbrl_tags(self, label_map: dict):
        """Load all XBRL tag nodes."""
        g     = Graph()
        g.bind("ifrs", IFRS)
        g.bind("kg",   KG)
        g.bind("rdfs", RDFS)

        for name, meta in ifrs_definition.items():
            label      = label_map.get(name, camel_to_sentence(name))
            uri        = IFRS[name]
            is_univ    = name in UNIVERSAL_TAGS

            g.add((uri, RDF.type,         KG.XBRLTag))
            g.add((uri, RDFS.label,       Literal(label)))
            g.add((uri, IFRS.tagName,     Literal(name)))
            g.add((uri, IFRS.isUniversal, Literal(is_univ, datatype=XSD.boolean)))

            if meta.get("balance"):
                g.add((uri, IFRS.balance, Literal(meta["balance"])))
            if meta.get("period_type"):
                g.add((uri, IFRS.periodType, Literal(meta["period_type"])))

        self._insert_triples(g)
        print(f"  ✓ XBRLTag nodes: {len(ifrs_definition)}")

    def load_universal_tags(self):
        """
        Universal tags → HAS_RELEVANT_TAG from every SubIndustry.
        These apply to all companies regardless of sub-industry, and are
        loaded before the sub-industry-specific tags so every SubIndustry
        has at least this baseline set.
        """
        g = Graph()
        g.bind("gics", GICS)
        g.bind("ifrs", IFRS)
        g.bind("kg",   KG)

        si_codes = [c for c in gics_definition if len(c) == 8]
        count    = 0

        for si_code in si_codes:
            si_uri = GICS[si_code]
            for tag in UNIVERSAL_TAGS:
                if tag in ifrs_definition:
                    g.add((si_uri, KG.HAS_RELEVANT_TAG, IFRS[tag]))
                    count += 1

        self._insert_triples(g)
        print(f"  ✓ Universal HAS_RELEVANT_TAG: {count} triples "
              f"({len(UNIVERSAL_TAGS)} tags × {len(si_codes)} sub-industries)")

    def load_subindustry_tags(self, mapping: dict):
        """Load SubIndustry -[HAS_RELEVANT_TAG]-> XBRLTag."""
        g     = Graph()
        g.bind("gics", GICS)
        g.bind("ifrs", IFRS)
        g.bind("kg",   KG)

        total = 0
        for si_code, tags in mapping.items():
            si_uri = GICS[si_code]
            for tag in tags:
                if tag in ifrs_definition:
                    g.add((si_uri, KG.HAS_RELEVANT_TAG, IFRS[tag]))
                    total += 1

        self._insert_triples(g)
        print(f"  ✓ SubIndustry HAS_RELEVANT_TAG: {total} triples")

    def load_has_child_tag(self):
        """
        Load XBRLTag -[HAS_CHILD_TAG]-> XBRLTag summation rules (weight +1.0)
        and XBRLTag -[HAS_CHILD_TAG_NEGATIVE]-> XBRLTag (weight -1.0, e.g.
        GrossProfit = Revenue - CostOfSales). Two predicates rather than a
        single weighted edge — keeps triples flat, no reification needed.
        """
        g = Graph()
        g.bind("ifrs", IFRS)
        g.bind("kg",   KG)

        pos_count, neg_count = 0, 0
        for parent_tag, child_tag, weight in load_calculation_rules():
            if parent_tag not in ifrs_definition or child_tag not in ifrs_definition:
                continue
            if weight > 0:
                g.add((IFRS[parent_tag], KG.HAS_CHILD_TAG, IFRS[child_tag]))
                pos_count += 1
            else:
                g.add((IFRS[parent_tag], KG.HAS_CHILD_TAG_NEGATIVE, IFRS[child_tag]))
                neg_count += 1

        self._insert_triples(g)
        print(f"  ✓ HAS_CHILD_TAG summation rules: {pos_count} additive, {neg_count} subtractive")

    def verify(self):
        """Run verification SPARQL queries."""
        queries = {
            "Total triples": "SELECT (COUNT(*) AS ?c) WHERE { ?s ?p ?o }",
            "Sectors":       "SELECT (COUNT(*) AS ?c) WHERE { ?s a kg:Sector }",
            "XBRLTags":      "SELECT (COUNT(*) AS ?c) WHERE { ?s a kg:XBRLTag }",
            "SubIndustries": "SELECT (COUNT(*) AS ?c) WHERE { ?s a kg:SubIndustry }",
            "PARENT_OF":     "SELECT (COUNT(*) AS ?c) WHERE { ?s kg:PARENT_OF ?o }",
            "HAS_RELEVANT_TAG": "SELECT (COUNT(*) AS ?c) WHERE { ?s kg:HAS_RELEVANT_TAG ?o }",
            "HAS_CHILD_TAG": "SELECT (COUNT(*) AS ?c) WHERE { ?s kg:HAS_CHILD_TAG ?o }",
            "HAS_CHILD_TAG_NEGATIVE": "SELECT (COUNT(*) AS ?c) WHERE { ?s kg:HAS_CHILD_TAG_NEGATIVE ?o }",
        }

        prefixes = """
            PREFIX kg:   <http://ifrs-gics.ontotext.com/ontology/>
            PREFIX ifrs: <http://xbrl.ifrs.org/taxonomy/2025/>
            PREFIX gics: <http://gics.msci.com/ontology/>
        """

        print("\n" + "=" * 55)
        print("VERIFICATION — GraphDB triple counts")
        print("=" * 55)

        for label, query in queries.items():
            self.sparql.setQuery(prefixes + query)
            results = self.sparql.query().convert()
            count   = results["results"]["bindings"][0]["c"]["value"]
            print(f"  {label:25s}: {count}")

        # Sample Regional Banks tags
        print("\n  Sample — Regional Banks (40101015) HAS_RELEVANT_TAG:")
        self.sparql.setQuery(prefixes + """
            SELECT ?tagName ?label WHERE {
                gics:40101015 kg:HAS_RELEVANT_TAG ?tag .
                ?tag ifrs:tagName ?tagName ;
                     rdfs:label   ?label .
            }
            LIMIT 10
        """)
        results = self.sparql.query().convert()
        for r in results["results"]["bindings"]:
            print(f"    {r['tagName']['value']:50s} → {r['label']['value']}")

        # Summation rules — sample a handful of parents (323 rules total, too many to print in full)
        print("\n  Summation rules (HAS_CHILD_TAG / HAS_CHILD_TAG_NEGATIVE), sample:")
        self.sparql.setQuery(prefixes + """
            SELECT ?parent ?child ?sign WHERE {
                { ?parentTag kg:HAS_CHILD_TAG ?childTag . BIND("+" AS ?sign) }
                UNION
                { ?parentTag kg:HAS_CHILD_TAG_NEGATIVE ?childTag . BIND("-" AS ?sign) }
                ?parentTag ifrs:tagName ?parent .
                ?childTag  ifrs:tagName ?child .
            }
            ORDER BY ?parent
        """)
        results  = self.sparql.query().convert()
        parents  = {}
        for r in results["results"]["bindings"]:
            p = r["parent"]["value"]
            c = r["child"]["value"]
            sign = r["sign"]["value"]
            parents.setdefault(p, []).append(f"{sign}{c}")
        for parent, children in list(parents.items())[:8]:
            print(f"    {parent} = {' '.join(children)}")
        if len(parents) > 8:
            print(f"    ... and {len(parents) - 8} more parent totals")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("GraphDB Knowledge Graph Builder")
    print(f"  URL:        {GRAPHDB_URL}")
    print(f"  Repository: {REPOSITORY}")
    print(f"  Input:      {INPUT_JSON}")
    print("=" * 60)

    # ── Load IFRS labels ───────────────────────────────────────────────
    print("\n[1] Loading IFRS labels...")
    label_map = load_ifrs_labels()
    print(f"  {len(label_map)} labels loaded")

    # ── Load SubIndustry → XBRL tag mapping (pre-computed on Katana) ────
    print(f"\n[2] Loading SubIndustry → XBRL tag mapping from {INPUT_JSON}...")
    with open(INPUT_JSON) as f:
        si_mapping = json.load(f)

    total_si   = len(si_mapping)
    total_tags = sum(len(v) for v in si_mapping.values())
    print(f"  {total_si} sub-industries, {total_tags} edges "
          f"(avg {total_tags/total_si:.1f}/SI)")

    # ── Load into GraphDB ──────────────────────────────────────────────
    print("\n[3] Loading into GraphDB...")
    loader = GraphDBLoader()

    print("  Clearing repository...")
    loader.clear()

    print("  Loading ontology...")
    loader.load_ontology()

    print("  Loading GICS hierarchy (PARENT_OF)...")
    loader.load_gics_hierarchy()

    print("  Loading XBRL tag nodes...")
    loader.load_xbrl_tags(label_map)

    print("  Loading universal tags (HAS_RELEVANT_TAG)...")
    loader.load_universal_tags()

    print("  Loading SubIndustry tags (HAS_RELEVANT_TAG)...")
    loader.load_subindustry_tags(si_mapping)

    print("  Loading summation rules (HAS_CHILD_TAG)...")
    loader.load_has_child_tag()

    # ── Verify ────────────────────────────────────────────────────────
    loader.verify()

    print("\n" + "=" * 60)
    print("✅ Knowledge graph loaded into GraphDB!")
    print("=" * 60)
    print(f"\nOpen GraphDB at: {GRAPHDB_URL}")
    print(f"Repository:      {REPOSITORY}")
    print("\nSample SPARQL queries:")
    print("""
  # Get all tags for Regional Banks
  PREFIX kg:   <http://ifrs-gics.ontotext.com/ontology/>
  PREFIX ifrs: <http://xbrl.ifrs.org/taxonomy/2025/>
  PREFIX gics: <http://gics.msci.com/ontology/>

  SELECT ?tagName ?label WHERE {
      gics:40101015 kg:HAS_RELEVANT_TAG ?tag .
      ?tag ifrs:tagName ?tagName ;
           rdfs:label   ?label .
  }

  # Get summation rules for Assets
  SELECT ?child WHERE {
      ifrs:Assets kg:HAS_CHILD_TAG ?childTag .
      ?childTag ifrs:tagName ?child .
  }

  # Full GICS hierarchy for Financials
  SELECT ?ig ?i ?si WHERE {
      gics:40 kg:PARENT_OF ?igNode .
      ?igNode kg:PARENT_OF ?iNode .
      ?iNode  kg:PARENT_OF ?siNode .
      ?igNode rdfs:label ?ig .
      ?iNode  rdfs:label ?i .
      ?siNode rdfs:label ?si .
  }
    """)


if __name__ == "__main__":
    main()