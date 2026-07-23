"""
Standardization Service test API — Knowledge + Reasoning layer slice.

Per the research report, UC2 (Knowledge Layer) and UC3 (Reasoning Layer)
are separate endpoints — UC3 performs UC2's steps internally rather than
requiring the client to chain calls:

    /classify, /classify-extraction (UC2 — Knowledge Layer)
        Identity Mapping + Contextual Pruning (Sec 3.5.1): infers the GICS
        sub-industry by walking the hierarchy top-down (Sector ->
        IndustryGroup -> Industry -> SubIndustry), at each level comparing
        a pseudo-document built from the line descriptions against only
        that level's candidates under the previously chosen parent, then
        returns the pruned candidate XBRL tags for that sub-industry via
        the GraphDB HAS_RELEVANT_TAG edges. No per-item tag assignment —
        that's the Semantic Mapper's job (UC3).

    /reason (UC3 — Reasoning Layer)
        Runs UC2 internally, then for every line finds the closest XBRL
        tag via nearest-neighbor search in the xbrl_tags ChromaDB
        collection restricted to UC2's candidate pool (Semantic Mapper,
        Sec 3.5.3), then resolves low-confidence mappings through the
        ReAct Agent's Thought-Action-Observation-Resolution cycle.

    /validate (UC4 — Validation Layer)
        Takes UC3's output ledger and runs two deterministic checks
        (Sec 3.5.4): a Structural Contextualizer (every assigned tag must
        fall within the GraphDB-pruned candidate pool for the identified
        sub-industry) and a Summation Check (Total Reported =
        Sum(Components), enforced via the HAS_CHILD_TAG rules already
        loaded in GraphDB, e.g. Assets = CurrentAssets + NoncurrentAssets
        + Liabilities + Equity). Only checks and reports pass/fail plus
        the issues found — per the report, Logic Recovery (resubmitting
        to /reason) is a separate, Reasoning-Layer-side step, not done
        automatically by this endpoint.

Both GICS inference and Semantic Mapper matching use BAAI/bge-base-en-v1.5
(MODEL_NAME below) — a general-purpose sentence-similarity model. A
finance-tuned alternative (FinLang/finance-embeddings-investopedia) was
evaluated and rejected: it improved fine-grained XBRL tag discrimination
but collapsed GICS classification (multiple unrelated companies converged
on the same wrong SubIndustry) — over-specialization to one financial-text
style generalizing poorly to the broader matching this service needs.
FinBERT (Sec 2.4.3's suggestion) was rejected earlier for the same reason:
a sentiment-classification head, not a similarity-trained embedding, does
markedly worse on both GICS paragraph matching and short XBRL label
matching regardless of domain vocabulary.

Run:
    PYTHONPATH=scripts uvicorn api:app --reload --port 8000
    open http://localhost:8000/docs
"""

import os
import re
from typing import Any, Dict, Optional

import chromadb
import numpy as np
import requests
import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

from parse_extraction    import parse_extractions
from react_agent         import ReActAgent


GRAPHDB_URL      = os.environ.get("GRAPHDB_URL", "http://localhost:7200")
REPOSITORY       = os.environ.get("GRAPHDB_REPOSITORY", "ifrs-gics")
CHROMA_HOST      = os.environ.get("CHROMA_HOST", "localhost")
CHROMA_PORT      = int(os.environ.get("CHROMA_PORT", "8001"))
MODEL_NAME       = "BAAI/bge-base-en-v1.5"
SPARQL_URL       = f"{GRAPHDB_URL}/repositories/{REPOSITORY}"

GICS_LEVELS    = [2, 4, 6, 8]
LEVEL_NAMES    = {2: "Sector", 4: "IndustryGroup", 6: "Industry", 8: "SubIndustry"}
BOILERPLATE    = re.compile(r"^(total|other|net)\b", re.I)
SUM_TOLERANCE  = 0.02   # 2% relative tolerance for the UC4 Summation Check
COMPANY_WEIGHT = 0.7    # favors company signal — see infer_gics_subindustry docstring

PREFIXES = """
    PREFIX kg:   <http://ifrs-gics.ontotext.com/ontology/>
    PREFIX gics: <http://gics.msci.com/ontology/>
    PREFIX ifrs: <http://xbrl.ifrs.org/taxonomy/2025/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""


class LineItem(BaseModel):
    id: int
    description: str
    note: Optional[str] = ""
    amount: Optional[str] = ""


class ClassifyRequest(BaseModel):
    companyName: Optional[str] = None
    items: list[LineItem]


class ExtractionRequest(BaseModel):
    companyName: Optional[str] = None
    extraction: Dict[str, Any]


class GicsResult(BaseModel):
    code: str
    name: str
    level: str
    confidence: float
    path: list[str]


class MappingResult(BaseModel):
    id: int
    description: str
    amount: str
    tag: Optional[str]
    tagLabel: Optional[str]
    distance: Optional[float]


class KnowledgeResponse(BaseModel):
    """UC2 — Knowledge Layer: GICS identification + pruned candidate tags, no per-item assignment."""
    gics: GicsResult
    candidateTags: list[str]


class TaorStepOut(BaseModel):
    step: str
    content: str


class ReasonedMappingResult(BaseModel):
    id: int
    description: str
    amount: str
    tag: Optional[str]
    tagLabel: Optional[str]
    distance: Optional[float]
    resolvedBy: str
    confidence: str
    reactTrace: list[TaorStepOut]


class ReasoningResponse(BaseModel):
    gics: GicsResult
    mappings: list[ReasonedMappingResult]


class StructuralIssue(BaseModel):
    id: int
    tag: str
    issue: str


class SummationIssue(BaseModel):
    parentTag: str
    reportedAmount: float
    computedAmount: float
    difference: float
    childIds: list[int]


class LedgerResponse(BaseModel):
    """UC4 — Validation Layer output. The report calls this the 'Ledger'."""
    passed: bool
    gics: GicsResult
    mappings: list[ReasonedMappingResult]
    structuralIssues: list[StructuralIssue]
    summationIssues: list[SummationIssue]


app = FastAPI(title="Domain Mapping Agent — test API")

_model           = None
_xbrl_collection = None
_gics_by_level   = None   # {level: (ids, embeddings, names)}
_react_agent     = None


@app.on_event("startup")
def load_resources():
    global _model, _xbrl_collection, _gics_by_level, _react_agent
    _model           = SentenceTransformer(MODEL_NAME)
    client           = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
    _xbrl_collection = client.get_collection("xbrl_tags")

    # Load GICS embeddings from the same gics_definitions collection
    # build_chromadb.py builds, rather than re-deriving our own copy from
    # raw gics_definition here: a second independent copy previously went
    # stale relative to the one actually used by build_chromadb.py's fixes
    # (blank Sector/IndustryGroup/Industry descriptions rolled up from their
    # descendant SubIndustry names) — this was live but silently unused.
    gics_collection = client.get_collection("gics_definitions")
    gics_data = gics_collection.get(include=["embeddings", "metadatas"])
    _gics_by_level = {}
    for level in GICS_LEVELS:
        mask  = [i for i, code in enumerate(gics_data["ids"]) if len(code) == level]
        ids   = [gics_data["ids"][i] for i in mask]
        embs  = torch.tensor(np.array([gics_data["embeddings"][i] for i in mask]), dtype=torch.float32)
        names = {gics_data["ids"][i]: gics_data["metadatas"][i]["name"] for i in mask}
        _gics_by_level[level] = (ids, embs, names)

    _react_agent = ReActAgent(model=_model, xbrl_collection=_xbrl_collection)


def fetch_company_description(company_name: str) -> Optional[str]:
    """
    Query the DuckDuckGo Instant Answer API for a company's business description.
    Returns the abstract text (usually a Wikipedia summary), or None on failure.
    No API key required; uses requests which is already a dependency.
    """
    try:
        resp = requests.get(
            "https://api.duckduckgo.com/",
            params={"q": company_name, "format": "json", "no_html": "1", "skip_disambig": "1"},
            timeout=5,
        )
        data = resp.json()
        abstract = data.get("AbstractText", "").strip()
        if abstract:
            return abstract
        # Fallback: first related topic text
        for topic in data.get("RelatedTopics", []):
            text = topic.get("Text", "").strip()
            if text:
                return text
    except Exception:
        pass
    return None


def fetch_company_sector(company_name: str) -> Optional[str]:
    """
    Query Yahoo Finance's ticker search for a company's real sector/industry.
    Far more reliable than fetch_company_description above: DuckDuckGo's
    Instant Answer API only resolves Wikipedia-notable entities and returns
    nothing for most small/mid-cap listings (verified empty even on an exact,
    correct company name), whereas Yahoo's search covers Tadawul-listed
    companies of any size and returns a real sector/industry tag, not just
    prose — a much stronger GICS classification signal than a bare name.
    Prefers a Saudi Exchange match since this pipeline targets Tadawul
    filings; falls back to the first equity match otherwise.
    """
    try:
        resp = requests.get(
            "https://query1.finance.yahoo.com/v1/finance/search",
            params={"q": company_name},
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=5,
        )
        quotes = [q for q in resp.json().get("quotes", []) if q.get("quoteType") == "EQUITY"]
        if not quotes:
            return None
        best = next((q for q in quotes if q.get("exchDisp") == "Saudi Stock Exchange"), quotes[0])
        sector, industry = best.get("sectorDisp", ""), best.get("industryDisp", "")
        if sector or industry:
            # Deliberately NOT including the company's own name here: legal-
            # entity words in it ("Industries", "Holding", "Group") can pull
            # the GICS match toward an unrelated but lexically similar Sector
            # (e.g. "Industries" -> "Industrials") — see build_gics_documents
            # in build_chromadb.py for the same trap at the XBRL-tag level.
            return f"{sector} sector, {industry} industry.".strip()
        return best.get("longname") or best.get("shortname") or None
    except Exception:
        return None


def infer_gics_subindustry(
    descriptions: list[str],
    company_description: Optional[str] = None,
) -> tuple[str, str, float, list[str]]:
    """
    Walk Sector -> IndustryGroup -> Industry -> SubIndustry, narrowing to
    children of the previously chosen parent at each step.

    company_description and the line-item descriptions are embedded
    *separately* and blended with a fixed weight, not concatenated into one
    string: a filing can have 30-65+ line items, so a single company
    description sentence gets averaged away by sheer word count if it's
    just prepended to one long joined string. Blending fixed-size sentence
    embeddings keeps the company signal's weight independent of item count.
    """
    signal = [d for d in descriptions if not BOILERPLATE.match(d.strip())] or descriptions
    items_emb = _model.encode([". ".join(signal)], convert_to_tensor=True, normalize_embeddings=True)
    if company_description:
        company_emb = _model.encode([company_description], convert_to_tensor=True, normalize_embeddings=True)
        q_emb = COMPANY_WEIGHT * company_emb + (1 - COMPANY_WEIGHT) * items_emb
        q_emb = q_emb / q_emb.norm(dim=1, keepdim=True)
    else:
        q_emb = items_emb

    prefix, path, final_code, final_name, final_score = "", [], "", "", 0.0
    for level in GICS_LEVELS:
        ids, embs, names = _gics_by_level[level]
        mask = [i for i, code in enumerate(ids) if code.startswith(prefix)]
        if not mask:
            break
        sub_embs = embs[mask]
        sims     = torch.matmul(q_emb, sub_embs.T)[0]
        best     = int(torch.argmax(sims).item())
        idx      = mask[best]
        final_code, final_score = ids[idx], sims[best].item()
        final_name = names[final_code]
        path.append(f"{final_code} {final_name}")
        prefix = final_code

    return final_code, final_name, final_score, path


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


def map_line_to_tag(description: str, candidate_tags: list[str]):
    if not description.strip() or not candidate_tags:
        return None, None, None
    emb    = _model.encode([description]).tolist()
    result = _xbrl_collection.query(
        query_embeddings=emb, n_results=1, where={"tagName": {"$in": candidate_tags}}
    )
    if not result["ids"][0]:
        return None, None, None
    return result["ids"][0][0], result["documents"][0][0], result["distances"][0][0]


def fetch_summation_rules() -> dict[str, list[tuple[str, float]]]:
    """
    Every HAS_CHILD_TAG (+1.0) / HAS_CHILD_TAG_NEGATIVE (-1.0) parent->child
    pair in GraphDB, grouped by parent tag as (child, weight) — sourced from
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


def parse_amount(raw: Optional[str]) -> Optional[float]:
    """'1,234' -> 1234.0, '(1,234)' -> -1234.0 (accounting negative), '' / junk -> None."""
    if not raw or not raw.strip():
        return None
    s = raw.strip().replace(",", "").lstrip("$").strip()
    negative = s.startswith("(") and s.endswith(")")
    if negative:
        s = s[1:-1]
    try:
        value = float(s)
    except ValueError:
        return None
    return -value if negative else value


def _resolve_knowledge(items: list[LineItem], company_name: Optional[str]):
    """UC2 core: GICS identification + Contextual Pruning. Shared by /classify, /classify-extraction, /reason."""
    described = [it for it in items if it.description.strip()]
    if not described:
        raise HTTPException(status_code=400, detail="No non-empty descriptions in input")

    company_desc = None
    if company_name:
        # Yahoo's sector/industry tag is a much stronger GICS signal than
        # DuckDuckGo's prose abstract, and actually covers small/mid-cap
        # Tadawul listings; DuckDuckGo only serves as a secondary fallback.
        company_desc = fetch_company_sector(company_name) or fetch_company_description(company_name)

    code, name, confidence, path = infer_gics_subindustry(
        [it.description for it in described],
        # Fall back to the bare company name when no description was found
        # rather than dropping it entirely: names like "Arabian Drilling
        # Company" still carry real industry signal a pure line-item
        # vocabulary doesn't.
        company_description=company_desc or company_name,
    )
    candidate_tags = fetch_relevant_tags(code)
    gics = GicsResult(code=code, name=name, level="SubIndustry", confidence=confidence, path=path)
    return gics, candidate_tags


@app.post("/classify", response_model=KnowledgeResponse)
def classify(request: ClassifyRequest):
    """
    UC2 — Knowledge Layer only. Identifies the GICS sub-industry and returns
    the pruned candidate XBRL tags for it — no per-item tag assignment (that's
    the Semantic Mapper's job, see /reason).

    If companyName is provided, fetches a business description online
    (DuckDuckGo / Wikipedia) and uses it as a strong prior for GICS
    inference before falling back to the line-item signal.
    """
    gics, candidate_tags = _resolve_knowledge(request.items, request.companyName)
    return KnowledgeResponse(gics=gics, candidateTags=candidate_tags)


@app.post("/classify-extraction", response_model=KnowledgeResponse)
def classify_extraction(request: ExtractionRequest):
    """
    UC2 — Knowledge Layer only, accepts raw Layer 1 extraction JSON.

    Body:
        companyName  (optional) — used to fetch a business description online
                                   (DuckDuckGo) for better GICS inference.
        extraction   (required) — the full extractions.json dict produced by
                                   the PDF pipeline (SpaCy/Camelot).

    The parser finds financial tables generically (no company-specific logic),
    extracts line-item descriptions and most-recent-year amounts, then runs
    the same GICS identification + Contextual Pruning as /classify.
    """
    detected_name, raw_items = parse_extractions(request.extraction)
    if not raw_items:
        raise HTTPException(status_code=422, detail="No financial line items found in extraction payload")

    items = [LineItem(id=r["id"], description=r["description"], amount=r["amount"]) for r in raw_items]

    # Caller-supplied name takes priority; fall back to auto-detected
    name_for_lookup = request.companyName or detected_name
    gics, candidate_tags = _resolve_knowledge(items, name_for_lookup)
    return KnowledgeResponse(gics=gics, candidateTags=candidate_tags)


@app.post("/reason", response_model=ReasoningResponse)
def reason(request: ClassifyRequest):
    """
    UC3 — Reasoning Layer. Self-sufficient: runs UC2 (GICS identification +
    Contextual Pruning) internally, then the Semantic Mapper (nearest-neighbor
    XBRL tag match per line via ChromaDB), then the ReAct Agent's TAOR cycle
    on low-confidence mappings. High-confidence items pass through the
    Semantic Mapper's result unchanged; ambiguous ones are resolved via
    semantic anchoring and Ollama.
    """
    gics, candidate_tags = _resolve_knowledge(request.items, request.companyName)

    initial_mappings = []
    for it in request.items:
        tag, label, dist = map_line_to_tag(it.description, candidate_tags)
        initial_mappings.append(MappingResult(
            id=it.id, description=it.description, amount=it.amount or "",
            tag=tag, tagLabel=label, distance=dist,
        ))

    react_results = _react_agent.resolve(
        items=initial_mappings,
        initial_mappings=initial_mappings,
        candidate_tags=candidate_tags,
    )

    mappings = [
        ReasonedMappingResult(
            id=r.id,
            description=r.description,
            amount=r.amount,
            tag=r.tag,
            tagLabel=r.tag_label,
            distance=r.distance,
            resolvedBy=r.resolved_by,
            confidence=r.confidence,
            reactTrace=[TaorStepOut(step=s.step, content=s.content) for s in r.react_trace],
        )
        for r in react_results
    ]

    return ReasoningResponse(gics=gics, mappings=mappings)


def _check_structural_pool(mappings, candidate_tags: set[str], gics_name: str) -> list[StructuralIssue]:
    """Every assigned tag must fall within the GICS-pruned candidate pool —
    a guard against the ReAct Agent or Semantic Mapper drifting outside it."""
    return [
        StructuralIssue(
            id=m.id, tag=m.tag,
            issue=f"'{m.tag}' is not in the pruned candidate pool for {gics_name}",
        )
        for m in mappings
        if m.tag and m.tag not in candidate_tags
    ]


def _group_amounts_by_tag(mappings) -> dict[str, list[tuple[int, float]]]:
    amounts_by_tag: dict[str, list[tuple[int, float]]] = {}
    for m in mappings:
        if not m.tag:
            continue
        amount = parse_amount(m.amount)
        if amount is None:
            continue
        amounts_by_tag.setdefault(m.tag, []).append((m.id, amount))
    return amounts_by_tag


def _find_conflicted_tags(
    amounts_by_tag: dict[str, list[tuple[int, float]]],
    summation_rules: dict[str, list[tuple[str, float]]],
) -> tuple[set[str], list[StructuralIssue]]:
    """
    A tag used as a summation parent represents one report-level total by
    definition — if >1 item maps directly to it, that's an unresolved
    mapping conflict (e.g. a cash-flow line lexically overlapping a balance
    total's label), not additional components to sum. Summing them silently
    corrupts "reported" — surface the conflict instead and skip the check
    for that tag rather than report a diff computed from a bad number.

    A conflicted tag is equally untrustworthy wherever else it's used — a
    tag like EquityAttributableToOwnersOfParent is both a check's own
    "reported" value AND a child contributing to Equity's "computed" sum;
    skipping only the former still lets the same bad entries corrupt the
    latter. The returned set is meant to be excluded from every parent's
    child_entries too, not just its own check.
    """
    conflicted_tags: set[str] = set()
    issues = []
    for parent_tag in summation_rules:
        entries = amounts_by_tag.get(parent_tag, [])
        if len(entries) > 1:
            conflicted_tags.add(parent_tag)
            ids = ", ".join(str(id_) for id_, _ in entries)
            issues.append(StructuralIssue(
                id=entries[0][0], tag=parent_tag,
                issue=f"{len(entries)} items (ids: {ids}) mapped directly to summary tag "
                      f"'{parent_tag}' — expected exactly one; summation check skipped for this tag",
            ))
    return conflicted_tags, issues


def _check_summations(
    amounts_by_tag: dict[str, list[tuple[int, float]]],
    summation_rules: dict[str, list[tuple[str, float]]],
    conflicted_tags: set[str],
) -> list[SummationIssue]:
    """For every HAS_CHILD_TAG rule, if the parent tag has exactly one
    reported amount and at least one (non-conflicted) child was assigned,
    verify Total Reported = Sum(Component Extracted) within SUM_TOLERANCE."""
    issues = []
    for parent_tag, weighted_children in summation_rules.items():
        if parent_tag not in amounts_by_tag or len(amounts_by_tag[parent_tag]) != 1:
            continue
        # (id, signed_amount) for every child tag actually assigned in this ledger.
        # abs(amt): `amt` already carries the PDF's parenthesis-as-negative
        # convention (parse_amount), which independently encodes "subtract this" —
        # the same intent as a -1 calculation weight. Applying both double-flips
        # the sign, so normalize to magnitude before the weight decides sign.
        child_entries = [
            (id_, weight * abs(amt))
            for child_tag, weight in weighted_children
            if child_tag not in conflicted_tags
            for id_, amt in amounts_by_tag.get(child_tag, [])
        ]
        if not child_entries:
            continue  # no components assigned in this ledger — nothing to check

        reported = sum(amt for _, amt in amounts_by_tag[parent_tag])
        computed = sum(amt for _, amt in child_entries)
        difference   = abs(reported - computed)
        relative_gap = difference / abs(reported) if reported else float(computed != 0)

        if relative_gap > SUM_TOLERANCE:
            issues.append(SummationIssue(
                parentTag=parent_tag, reportedAmount=reported, computedAmount=computed,
                difference=difference, childIds=[id_ for id_, _ in child_entries],
            ))
    return issues


@app.post("/validate", response_model=LedgerResponse)
def validate(request: ReasoningResponse):
    """
    UC4 — Validation Layer. Takes UC3's (/reason) output ledger and runs:

      1. Structural Contextualizer — every assigned tag must fall within
         the GraphDB-pruned candidate pool for the identified sub-industry
         (Sec 3.5.1's Contextual Pruning, re-checked here as a guard
         against the ReAct Agent or Semantic Mapper drifting outside it).
         Also flags conflicting mappings — multiple items mapped directly
         to the same summation-parent tag (see _find_conflicted_tags).
      2. Summation Check — for every HAS_CHILD_TAG rule in the Knowledge
         Graph, if both the parent tag and at least one child tag were
         assigned amounts in this ledger, verify
             Total Reported = Sum(Component Extracted)
         within a 2% relative tolerance (Sec 3.3's Deterministic
         Validation concept).

    Returns the ledger unchanged plus a pass/fail verdict and the list of
    issues found. Per the report, Logic Recovery — resubmitting to
    /reason for autonomous re-evaluation — is a Reasoning Layer step
    triggered by the caller on a rejection signal, not done automatically
    by this endpoint.
    """
    candidate_tags  = set(fetch_relevant_tags(request.gics.code))
    summation_rules = fetch_summation_rules()
    amounts_by_tag  = _group_amounts_by_tag(request.mappings)

    structural_issues = _check_structural_pool(request.mappings, candidate_tags, request.gics.name)
    conflicted_tags, conflict_issues = _find_conflicted_tags(amounts_by_tag, summation_rules)
    structural_issues += conflict_issues

    summation_issues = _check_summations(amounts_by_tag, summation_rules, conflicted_tags)

    return LedgerResponse(
        passed=not structural_issues and not summation_issues,
        gics=request.gics,
        mappings=request.mappings,
        structuralIssues=structural_issues,
        summationIssues=summation_issues,
    )
