"""
GICS sub-industry classification for api.py: Identity Mapping (company
name -> GICS) used by UC2's Contextual Pruning. Mirrors the ReActAgent
pattern: load the embedding index once, then reuse a GicsClassifier
instance per request.

knowledge_api.py has its own, deliberately simpler standalone version of
this (string concatenation instead of weighted embedding blending), not
shared with this module. See infer_subindustry's docstring for why.
"""

import re
from typing import Optional

import numpy as np
import requests
import torch

GICS_LEVELS    = [2, 4, 6, 8]
BOILERPLATE    = re.compile(r"^(total|other|net)\b", re.I)
COMPANY_WEIGHT = 0.7   # favors company signal, see infer_subindustry docstring


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
    More reliable than fetch_company_description above: DuckDuckGo only
    resolves Wikipedia-notable entities and returns nothing for most
    small/mid-cap listings, while Yahoo covers Tadawul-listed companies of
    any size and returns an actual sector/industry tag rather than prose.
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
            # Deliberately excludes the company's own name: legal-entity
            # words in it ("Industries", "Holding") can pull the GICS match
            # toward an unrelated but lexically similar Sector.
            return f"{sector} sector, {industry} industry.".strip()
        return best.get("longname") or best.get("shortname") or None
    except Exception:
        return None


def load_gics_index(gics_collection) -> dict:
    """
    Load {level: (ids, embeddings, names)} from the gics_definitions
    ChromaDB collection build_chromadb.py builds, rather than re-deriving
    it from raw gics_definition here. A second copy previously went stale
    relative to build_chromadb.py's fixes.
    """
    data = gics_collection.get(include=["embeddings", "metadatas"])
    gics_by_level = {}
    for level in GICS_LEVELS:
        mask  = [i for i, code in enumerate(data["ids"]) if len(code) == level]
        ids   = [data["ids"][i] for i in mask]
        embs  = torch.tensor(np.array([data["embeddings"][i] for i in mask]), dtype=torch.float32)
        names = {data["ids"][i]: data["metadatas"][i]["name"] for i in mask}
        gics_by_level[level] = (ids, embs, names)
    return gics_by_level


class GicsClassifier:
    """Walks Sector -> IndustryGroup -> Industry -> SubIndustry, narrowing
    to children of the previously chosen parent at each step."""

    def __init__(self, model, gics_by_level: dict):
        self.model = model
        self.gics_by_level = gics_by_level

    def infer_subindustry(
        self,
        descriptions: list[str],
        company_description: Optional[str] = None,
    ) -> tuple[str, str, float, list[str]]:
        """
        company_description and the line-item descriptions are embedded
        separately and blended with a fixed weight rather than concatenated:
        a filing can have 30-65+ line items, so prepending one company
        description sentence to a long joined string just gets it averaged
        away. Blending fixed-size embeddings keeps its weight independent of
        item count.
        """
        signal = [d for d in descriptions if not BOILERPLATE.match(d.strip())] or descriptions
        items_emb = self.model.encode([". ".join(signal)], convert_to_tensor=True, normalize_embeddings=True)
        if company_description:
            company_emb = self.model.encode([company_description], convert_to_tensor=True, normalize_embeddings=True)
            q_emb = COMPANY_WEIGHT * company_emb + (1 - COMPANY_WEIGHT) * items_emb
            q_emb = q_emb / q_emb.norm(dim=1, keepdim=True)
        else:
            q_emb = items_emb

        prefix, path, final_code, final_name, final_score = "", [], "", "", 0.0
        for level in GICS_LEVELS:
            ids, embs, names = self.gics_by_level[level]
            mask = [i for i, code in enumerate(ids) if code.startswith(prefix)]
            if not mask:
                break
            # .to(q_emb.device): embs was built as a plain CPU tensor, but
            # q_emb lands on whatever device the model itself runs on (e.g.
            # MPS on Apple Silicon), and torch.matmul needs both on one device.
            sub_embs = embs[mask].to(q_emb.device)
            sims     = torch.matmul(q_emb, sub_embs.T)[0]
            best     = int(torch.argmax(sims).item())
            idx      = mask[best]
            final_code, final_score = ids[idx], sims[best].item()
            final_name = names[final_code]
            path.append(f"{final_code} {final_name}")
            prefix = final_code

        return final_code, final_name, final_score, path
