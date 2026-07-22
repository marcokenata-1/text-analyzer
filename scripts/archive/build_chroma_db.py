"""
Build a Chroma vector database from the GICS subindustry -> IFRS tag mapping.

Source data:
    data/mappings/subindustry_ifrs_mapping_v3_katana.json
        { subindustry_code (GICS, 8-digit): [IFRSTagName, ...], ... }
    scripts/d_20230318.py   -> GICS hierarchy names/descriptions
    scripts/ifrs_tags.py    -> IFRS tag labels/balance/period_type

Two collections are created in a persistent Chroma store at data/chroma_db:
    subindustries  - one document per GICS subindustry (163 docs). Document
                      text combines the GICS hierarchy path, description, and
                      the labels of every IFRS tag relevant to it. Useful for
                      "which subindustry does this business/concept belong to".
    ifrs_tags      - one document per unique IFRS tag (423 docs). Document
                      text is the tag's human-readable label. Metadata lists
                      every subindustry code that uses the tag. Useful for
                      "which subindustries report this accounting concept".

Setup:
    pip install chromadb

Usage:
    python scripts/build_chroma_db.py
"""

import json
import sys
from pathlib import Path

import chromadb

sys.path.insert(0, str(Path(__file__).parent))
from d_20230318 import definition as gics_definition
from ifrs_tags import definition as ifrs_definition

MAPPING_FILE = "data/mappings/subindustry_ifrs_mapping_v3_katana.json"
CHROMA_DIR = "data/chroma_db"


def gics_path(code: str) -> dict:
    """Return {sector, industry_group, industry, subindustry} names for an 8-digit GICS code."""
    return {
        "sector": gics_definition.get(code[:2], {}).get("name", ""),
        "industry_group": gics_definition.get(code[:4], {}).get("name", ""),
        "industry": gics_definition.get(code[:6], {}).get("name", ""),
        "subindustry": gics_definition.get(code, {}).get("name", ""),
    }


def build_subindustry_documents(mapping: dict) -> tuple[list, list, list]:
    ids, documents, metadatas = [], [], []

    for code, tags in mapping.items():
        info = gics_definition.get(code, {})
        path = gics_path(code)
        tag_labels = [ifrs_definition.get(t, {}).get("label", t) for t in tags]

        text_parts = [
            f"GICS sub-industry: {path['subindustry']}",
            f"Sector: {path['sector']}",
            f"Industry group: {path['industry_group']}",
            f"Industry: {path['industry']}",
        ]
        if info.get("description"):
            text_parts.append(f"Description: {info['description']}")
        if tag_labels:
            text_parts.append("Relevant IFRS concepts: " + "; ".join(tag_labels))

        ids.append(code)
        documents.append("\n".join(text_parts))
        metadatas.append(
            {
                "code": code,
                "subindustry": path["subindustry"],
                "industry": path["industry"],
                "industry_group": path["industry_group"],
                "sector": path["sector"],
                "tag_count": len(tags),
                "tags": json.dumps(tags),
            }
        )

    return ids, documents, metadatas


def build_tag_documents(mapping: dict) -> tuple[list, list, list]:
    tag_to_codes: dict[str, list[str]] = {}
    for code, tags in mapping.items():
        for tag in tags:
            tag_to_codes.setdefault(tag, []).append(code)

    ids, documents, metadatas = [], [], []
    for tag, codes in tag_to_codes.items():
        info = ifrs_definition.get(tag, {})
        label = info.get("label", tag)

        ids.append(tag)
        documents.append(label)
        metadatas.append(
            {
                "tag": tag,
                "balance": info.get("balance", ""),
                "period_type": info.get("period_type", ""),
                "subindustry_count": len(codes),
                "subindustry_codes": json.dumps(codes),
            }
        )

    return ids, documents, metadatas


def upsert_in_batches(collection, ids, documents, metadatas, batch_size=200):
    for i in range(0, len(ids), batch_size):
        collection.upsert(
            ids=ids[i : i + batch_size],
            documents=documents[i : i + batch_size],
            metadatas=metadatas[i : i + batch_size],
        )


def main():
    with open(MAPPING_FILE) as f:
        mapping = json.load(f)

    client = chromadb.PersistentClient(path=CHROMA_DIR)

    sub_ids, sub_docs, sub_meta = build_subindustry_documents(mapping)
    sub_collection = client.get_or_create_collection("subindustries")
    upsert_in_batches(sub_collection, sub_ids, sub_docs, sub_meta)
    print(f"subindustries collection: {sub_collection.count()} documents")

    tag_ids, tag_docs, tag_meta = build_tag_documents(mapping)
    tag_collection = client.get_or_create_collection("ifrs_tags")
    upsert_in_batches(tag_collection, tag_ids, tag_docs, tag_meta)
    print(f"ifrs_tags collection: {tag_collection.count()} documents")

    print(f"Persisted to {CHROMA_DIR}")


if __name__ == "__main__":
    main()
