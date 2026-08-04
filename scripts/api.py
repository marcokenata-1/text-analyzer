"""
Standardization Service test API: Knowledge + Reasoning layer slice.

UC2 and UC3 are separate endpoints, but UC3 runs UC2 internally rather than
making the client chain calls:

    /classify, /classify-extraction (UC2, Knowledge Layer)
        Identifies the GICS sub-industry by walking Sector -> IndustryGroup
        -> Industry -> SubIndustry, at each level matching a pseudo-document
        of the line descriptions against only that level's children of the
        previously chosen parent. Returns the pruned candidate XBRL tags for
        that sub-industry (GraphDB HAS_RELEVANT_TAG). There's no per-item
        tag assignment here; that's the Semantic Mapper's job (UC3).

    /reason (UC3, Reasoning Layer)
        Runs UC2, then nearest-neighbor matches each line to an XBRL tag in
        ChromaDB (restricted to UC2's candidate pool), then resolves
        low-confidence matches via the ReAct Agent's TAOR cycle.

    /validate (UC4, Validation Layer)
        Takes UC3's output ledger and runs two checks: every assigned tag
        must be in the GICS-pruned candidate pool (Structural
        Contextualizer), and Total Reported = Sum(Components) per the
        GraphDB HAS_CHILD_TAG rules (Summation Check). Reports pass/fail
        plus the issues found; resubmitting to /reason for Logic Recovery
        is left to the caller.

Both GICS inference and tag matching use BAAI/bge-base-en-v1.5 (MODEL_NAME),
a general-purpose sentence-similarity model. Finance-tuned alternatives
(FinBERT, FinLang/finance-embeddings-investopedia) were tried and rejected:
both did markedly worse on GICS classification, and FinLang also hurt XBRL
tag discrimination. Domain tuning doesn't help if the embedding space
isn't optimized for general semantic similarity in the first place.

The actual logic lives in sibling modules; this file is just the FastAPI
wiring on top of them:
    schemas.py         request/response models
    gics.py             GICS sub-industry classification (UC2)
    graphdb_client.py   SPARQL access (candidate tags, summation rules)
    validation.py       UC4 checks
    react_agent.py      TAOR resolution loop (UC3)
    parse_extraction.py Layer 1 extraction JSON -> LineItems

Run:
    PYTHONPATH=scripts uvicorn api:app --reload --port 8000
    open http://localhost:8000/docs
"""

import os
from typing import Optional

import chromadb
from fastapi import FastAPI, HTTPException
from sentence_transformers import SentenceTransformer

import gics
import graphdb_client
import validation
from parse_extraction import parse_extractions
from react_agent import ReActAgent
from schemas import (
    ClassifyRequest, ExtractionRequest, GicsResult, KnowledgeResponse,
    LedgerResponse, LineItem, MappingResult, ReasonedMappingResult,
    ReasoningResponse, TaorStepOut,
)

CHROMA_HOST = os.environ.get("CHROMA_HOST", "localhost")
CHROMA_PORT = int(os.environ.get("CHROMA_PORT", "8001"))
MODEL_NAME  = "BAAI/bge-base-en-v1.5"

app = FastAPI(title="Domain Mapping Agent (test API)")

_model           = None
_xbrl_collection = None
_gics_classifier = None   # gics.GicsClassifier
_react_agent     = None


@app.on_event("startup")
def load_resources():
    global _model, _xbrl_collection, _gics_classifier, _react_agent
    _model           = SentenceTransformer(MODEL_NAME)
    client           = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
    _xbrl_collection = client.get_collection("xbrl_tags")

    gics_collection  = client.get_collection("gics_definitions")
    _gics_classifier = gics.GicsClassifier(_model, gics.load_gics_index(gics_collection))

    _react_agent = ReActAgent(model=_model, xbrl_collection=_xbrl_collection)


def map_line_to_tag(description: str, candidate_tags: list[str]):
    """Semantic Mapper: nearest XBRL tag to `description` in ChromaDB, restricted to candidate_tags."""
    if not description.strip() or not candidate_tags:
        return None, None, None
    emb    = _model.encode([description]).tolist()
    result = _xbrl_collection.query(
        query_embeddings=emb, n_results=1, where={"tagName": {"$in": candidate_tags}}
    )
    if not result["ids"][0]:
        return None, None, None
    return result["ids"][0][0], result["documents"][0][0], result["distances"][0][0]


def _resolve_knowledge(items: list[LineItem], company_name: Optional[str]):
    """UC2 core: GICS identification + Contextual Pruning. Shared by /classify, /classify-extraction, /reason."""
    described = [it for it in items if it.description.strip()]
    if not described:
        raise HTTPException(status_code=400, detail="No non-empty descriptions in input")

    company_desc = None
    if company_name:
        # Yahoo's sector/industry tag is a stronger GICS signal and covers
        # small/mid-cap Tadawul listings; DuckDuckGo is a fallback.
        company_desc = gics.fetch_company_sector(company_name) or gics.fetch_company_description(company_name)

    # Fall back to the bare company name rather than dropping it: names like
    # "Arabian Drilling Company" still carry real industry signal.
    code, name, confidence, path = _gics_classifier.infer_subindustry(
        [it.description for it in described],
        company_description=company_desc or company_name,
    )
    candidate_tags = graphdb_client.fetch_relevant_tags(code)
    gics_result = GicsResult(code=code, name=name, level="SubIndustry", confidence=confidence, path=path)
    return gics_result, candidate_tags


@app.post("/classify", response_model=KnowledgeResponse)
def classify(request: ClassifyRequest):
    """
    UC2, Knowledge Layer only. Identifies the GICS sub-industry and returns
    its pruned candidate XBRL tags (no per-item assignment, see /reason).
    If companyName is given, an online business-description lookup is used
    as a prior for GICS inference alongside the line-item signal.
    """
    gics_result, candidate_tags = _resolve_knowledge(request.items, request.companyName)
    return KnowledgeResponse(gics=gics_result, candidateTags=candidate_tags)


@app.post("/classify-extraction", response_model=KnowledgeResponse)
def classify_extraction(request: ExtractionRequest):
    """
    UC2, accepting the raw Layer 1 extraction JSON (extractions.json from
    the SpaCy/Camelot PDF pipeline) instead of a pre-parsed item list. Finds
    financial tables generically, extracts descriptions and most-recent-year
    amounts, then runs the same GICS identification as /classify. companyName
    is optional and falls back to auto-detection from the extraction.
    """
    detected_name, raw_items = parse_extractions(request.extraction)
    if not raw_items:
        raise HTTPException(status_code=422, detail="No financial line items found in extraction payload")

    items = [LineItem(id=r["id"], description=r["description"], amount=r["amount"]) for r in raw_items]

    # Caller-supplied name takes priority; fall back to auto-detected
    name_for_lookup = request.companyName or detected_name
    gics_result, candidate_tags = _resolve_knowledge(items, name_for_lookup)
    return KnowledgeResponse(gics=gics_result, candidateTags=candidate_tags)


@app.post("/reason", response_model=ReasoningResponse)
def reason(request: ClassifyRequest):
    """
    UC3, Reasoning Layer. Runs UC2 internally, nearest-neighbor matches
    each line to an XBRL tag via ChromaDB, then resolves low-confidence
    matches through the ReAct Agent's TAOR cycle. High-confidence matches
    pass through unchanged.
    """
    gics_result, candidate_tags = _resolve_knowledge(request.items, request.companyName)

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

    return ReasoningResponse(gics=gics_result, mappings=mappings)


@app.post("/validate", response_model=LedgerResponse)
def validate(request: ReasoningResponse):
    """
    UC4, Validation Layer. Takes UC3's (/reason) output ledger and runs two
    checks: every assigned tag must fall within the GICS-pruned candidate
    pool (also flags multiple items mapped to the same summation-parent tag,
    see validation.find_conflicted_tags), and for every HAS_CHILD_TAG rule,
    Total Reported = Sum(Components) within a 2% relative tolerance. Returns
    the ledger unchanged plus a pass/fail verdict and the issues found;
    resubmitting to /reason for Logic Recovery is left to the caller.
    """
    candidate_tags  = set(graphdb_client.fetch_relevant_tags(request.gics.code))
    summation_rules = graphdb_client.fetch_summation_rules()
    amounts_by_tag  = validation.group_amounts_by_tag(request.mappings)

    structural_issues = validation.check_structural_pool(request.mappings, candidate_tags, request.gics.name)
    conflicted_tags, conflict_issues = validation.find_conflicted_tags(amounts_by_tag, summation_rules)
    structural_issues += conflict_issues

    summation_issues = validation.check_summations(amounts_by_tag, summation_rules, conflicted_tags)

    return LedgerResponse(
        passed=not structural_issues and not summation_issues,
        gics=request.gics,
        mappings=request.mappings,
        structuralIssues=structural_issues,
        summationIssues=summation_issues,
    )
