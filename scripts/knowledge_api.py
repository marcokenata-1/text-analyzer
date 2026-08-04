"""
Knowledge Layer service: UC2 only.

Identity Mapping (company -> GICS) and Contextual Pruning (narrow the XBRL
taxonomy to the identified sub-industry's relevant tags), backed entirely by
GraphDB. Returns the pruned candidate XBRL tags for a sub-industry; there's
no per-item tag assignment here, that's the Semantic Mapper's job in the
Reasoning Layer (UC3, see api.py's /reason).

This is a lighter deployment of UC2 than api.py's /classify: its only
runtime dependency is GraphDB, no ChromaDB or Ollama needed.

Run:
    PYTHONPATH=scripts uvicorn knowledge_api:app --reload --port 8000
    open http://localhost:8000/docs
"""

import os
import re
from typing import Optional

import requests
import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

from d_20230318 import definition as gics_definition


GRAPHDB_URL  = os.environ.get("GRAPHDB_URL", "http://localhost:7200")
REPOSITORY   = os.environ.get("GRAPHDB_REPOSITORY", "ifrs-gics")
SPARQL_URL   = f"{GRAPHDB_URL}/repositories/{REPOSITORY}"

MODEL_NAME   = "BAAI/bge-base-en-v1.5"

GICS_LEVELS  = [2, 4, 6, 8]
BOILERPLATE  = re.compile(r"^(total|other|net)\b", re.I)

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


class GicsResult(BaseModel):
    code: str
    name: str
    level: str
    confidence: float
    path: list[str]


class KnowledgeResponse(BaseModel):
    """UC2, Knowledge Layer: GICS identification + pruned candidate tags, no per-item assignment."""
    gics: GicsResult
    candidateTags: list[str]


app = FastAPI(title="Knowledge Layer (/classify, UC2 only)")

_model         = None
_gics_by_level = None   # {level: (ids, embeddings, names)}


@app.on_event("startup")
def load_resources():
    global _model, _gics_by_level
    _model = SentenceTransformer(MODEL_NAME)

    _gics_by_level = {}
    for level in GICS_LEVELS:
        codes = {k: v for k, v in gics_definition.items() if len(k) == level}
        ids   = list(codes.keys())
        docs  = [f"{v.get('name', '')}: {v.get('description', '')}" for v in codes.values()]
        embs  = _model.encode(docs, convert_to_tensor=True, normalize_embeddings=True)
        names = {k: v.get("name", "") for k, v in codes.items()}
        _gics_by_level[level] = (ids, embs, names)


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
        for topic in data.get("RelatedTopics", []):
            text = topic.get("Text", "").strip()
            if text:
                return text
    except Exception:
        pass
    return None


def infer_gics_subindustry(
    descriptions: list[str],
    company_description: Optional[str] = None,
) -> tuple[str, str, float, list[str]]:
    """
    Walk Sector -> IndustryGroup -> Industry -> SubIndustry, narrowing to
    children of the previously chosen parent at each step. The query is a
    single pseudo-document built from all non-boilerplate line descriptions.
    """
    signal = [d for d in descriptions if not BOILERPLATE.match(d.strip())] or descriptions
    pseudo_doc = ". ".join(signal)
    if company_description:
        pseudo_doc = company_description + ". " + pseudo_doc
    q_emb = _model.encode([pseudo_doc], convert_to_tensor=True, normalize_embeddings=True)

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


def fetch_relevant_tags(si_code: str) -> list[str]:
    """Pruned candidate XBRL tags for a sub-industry, via GraphDB HAS_RELEVANT_TAG."""
    query = PREFIXES + f"""
        SELECT ?tagName WHERE {{
            gics:{si_code} kg:HAS_RELEVANT_TAG ?t .
            ?t ifrs:tagName ?tagName .
        }}
    """
    resp = requests.get(
        SPARQL_URL,
        params={"query": query},
        headers={"Accept": "application/sparql-results+json"},
    )
    if resp.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail=f"GraphDB query failed: {resp.status_code} {resp.text[:200]}",
        )
    bindings = resp.json()["results"]["bindings"]
    return [b["tagName"]["value"] for b in bindings]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/classify", response_model=KnowledgeResponse)
def classify(request: ClassifyRequest):
    """
    UC2, Knowledge Layer only. Identifies the GICS sub-industry and returns
    its pruned candidate XBRL tags (no per-item assignment; that's the
    Semantic Mapper's job in UC3). If companyName is given, an online
    business-description lookup is used as a prior for GICS inference
    alongside the line-item signal.
    """
    items     = request.items
    described = [it for it in items if it.description.strip()]
    if not described:
        raise HTTPException(status_code=400, detail="No non-empty descriptions in input")

    company_desc = None
    if request.companyName:
        company_desc = fetch_company_description(request.companyName)

    code, name, confidence, path = infer_gics_subindustry(
        [it.description for it in described],
        company_description=company_desc,
    )
    candidate_tags = fetch_relevant_tags(code)

    return KnowledgeResponse(
        gics=GicsResult(code=code, name=name, level="SubIndustry",
                        confidence=confidence, path=path),
        candidateTags=candidate_tags,
    )
