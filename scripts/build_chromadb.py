"""
Vector Database Builder — Knowledge Layer semantic search

Per the research report (Sec 2.5.4, 3.3, 4.2 Phase 1): the Vector Database
indexes high-dimensional representations of GICS definitions and XBRL tags,
giving the Reasoning Layer's Semantic Mapper a nearest-neighbor search over
the same two node types already stored in the GraphDB Knowledge Graph.

Two collections (mirrors the Knowledge Graph node types):
    gics_definitions — one entry per GICS Sector/IndustryGroup/Industry/SubIndustry
    xbrl_tags        — one entry per IFRS XBRL tag

Embeddings use all-MiniLM-L6-v2, a sentence-similarity model trained with
a contrastive objective. The report (Sec 2.4.3) suggests FinBERT for its
financial-domain vocabulary, but empirically FinBERT's embeddings — from a
sentiment-classification head, not a similarity-trained one — performed
markedly worse here than a general-purpose sentence-similarity model on
both GICS paragraph matching and short XBRL label matching. Domain tuning
doesn't help if the embedding space itself isn't optimized for "are these
semantically related."

Setup:
    pip install chromadb sentence-transformers
"""

import json
import re
import chromadb
import ollama
from sentence_transformers import SentenceTransformer

from d_20230318 import definition as gics_definition
from ifrs_tags   import definition as ifrs_definition

from build_graphdb import load_ifrs_labels, camel_to_sentence


# ── Config ─────────────────────────────────────────────────────────────────────
CHROMA_HOST      = "localhost"
CHROMA_PORT      = 8001
MODEL_NAME       = "all-MiniLM-L6-v2"
BATCH_SIZE       = 256
OLLAMA_MODEL     = "llama3.1"

GICS_LEVELS = {2: "Sector", 4: "IndustryGroup", 6: "Industry", 8: "SubIndustry"}


def generate_synonym_map(short_labels: list[tuple[str, str]]) -> dict[str, list[str]]:
    """
    Ask Ollama for common alternate names of short (<=2 word) tag labels —
    e.g. "Revenue" -> "net sales", "turnover". Only short labels are worth
    asking about: a bag-of-words-ish embedding has nothing to disambiguate
    "Revenue" from "Cost Of Sales" on a 1-2 word label, but longer compound
    labels ("Cash Flows From Used In Financing Activities") rarely collide.
    Generated at build time so this tracks whatever tags/labels the current
    IFRS taxonomy defines, instead of a hand-maintained list going stale.

    Whether a synonym actually helps (vs. colliding with a sibling tag) is
    verified afterwards in validate_synonym_map — this function just
    proposes candidates, so the prompt doesn't need to get that judgment
    right itself.
    """
    items = "\n".join(f"{n}. {label}" for n, (_, label) in enumerate(short_labels, 1))
    prompt = f"""You are an IFRS financial reporting expert.

For each numbered financial statement line-item label below, give up to 3
common alternate names a real annual report might use instead — e.g.
"Revenue" -> "net sales", "turnover". Skip any label that has no real
synonym.

{items}

Reply with ONLY a JSON object mapping each number (as a string) to a list
of synonym strings, e.g. {{"1": ["net sales", "turnover"]}}. Omit numbers
with no good synonym. No other text."""
    try:
        resp = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": 0.0},
        )
        raw = re.sub(r"^```(?:json)?|```$", "", resp["message"]["content"].strip(), flags=re.M).strip()
        # raw_decode (not loads): larger batches sometimes get trailing prose
        # appended after a perfectly valid JSON object despite instructions
        # not to — parse just the first JSON value and ignore the rest.
        parsed, _ = json.JSONDecoder().raw_decode(raw)
        synonyms: dict[str, list[str]] = {}
        for n, syns in parsed.items():
            tag, _ = short_labels[int(n) - 1]
            if syns:
                synonyms[tag] = syns
        return synonyms
    except Exception as e:
        print(f"  [synonym gen] failed, continuing without synonyms: {e}")
        return {}


def validate_synonym_map(
    short_labels: list[tuple[str, str]], synonym_map: dict[str, list[str]], model
) -> dict[str, list[str]]:
    """
    Drop any synonym that, if a report literally used that word, would embed
    closer to a *different* short tag than to its own — i.e. verify each
    synonym actually disambiguates rather than trusting the model's own
    judgment call about what's ambiguous (unreliable — see build history).
    """
    tags   = [t for t, _ in short_labels]
    docs   = [
        f"{label} ({', '.join(synonym_map[tag])})" if tag in synonym_map else label
        for tag, label in short_labels
    ]
    doc_embs = model.encode(docs, normalize_embeddings=True)

    cleaned: dict[str, list[str]] = {}
    for tag, syns in synonym_map.items():
        own_idx = tags.index(tag)
        syn_embs = model.encode(syns, normalize_embeddings=True)
        sims     = syn_embs @ doc_embs.T   # (n_syns, n_short_tags)
        kept     = [syn for syn, row in zip(syns, sims) if int(row.argmax()) == own_idx]
        if kept:
            cleaned[tag] = kept
    return cleaned


def build_gics_documents():
    """
    Only the 163 finest-grained SubIndustry entries in d_20230318 carry a real
    description — all 110 Sector/IndustryGroup/Industry entries (the ones the
    classification walk actually starts at) are just a bare 1-3 word name
    ("Materials", "Industrials"). A bare name has nothing to disambiguate on:
    e.g. "Al Yamamah Steel Industries Company" pulled toward "Industrials"
    over "Materials" purely because "Industries" and "Industrials" share a
    root — the same lexical-overlap trap fixed for XBRL tags earlier.
    Fix: roll up each blank entry's own descendant SubIndustry names as its
    description — derived straight from data already in the dataset, so it
    stays correct automatically if the taxonomy changes, no LLM/hardcoding.
    """
    subindustry_names_by_code: dict[str, list[str]] = {}
    for code, data in gics_definition.items():
        if len(code) == 8:
            for prefix_len in (2, 4, 6):
                prefix = code[:prefix_len]
                subindustry_names_by_code.setdefault(prefix, []).append(data.get("name", ""))

    ids, documents, metadatas = [], [], []
    for code, data in gics_definition.items():
        if len(code) not in GICS_LEVELS:
            continue
        name = data.get("name", "")
        desc = data.get("description", "").strip()
        if not desc and len(code) != 8:
            desc = ", ".join(subindustry_names_by_code.get(code, []))
        ids.append(code)
        documents.append(f"{name}: {desc}" if desc else name)
        metadatas.append({
            "code":       code,
            "level":      GICS_LEVELS[len(code)],
            "name":       name,
            "parentCode": code[:-2] if len(code) > 2 else "",
        })
    return ids, documents, metadatas


def build_xbrl_documents(label_map: dict, synonym_map: dict):
    ids, documents, metadatas = [], [], []
    for tag, meta in ifrs_definition.items():
        label    = label_map.get(tag, camel_to_sentence(tag))
        synonyms = synonym_map.get(tag)
        document = f"{label} ({', '.join(synonyms)})" if synonyms else label
        ids.append(tag)
        documents.append(document)
        metadatas.append({
            "tagName":    tag,
            "balance":    meta.get("balance", ""),
            "periodType": meta.get("period_type", ""),
        })
    return ids, documents, metadatas


def embed_and_add(collection, model, ids, documents, metadatas):
    for i in range(0, len(ids), BATCH_SIZE):
        batch_docs  = documents[i:i + BATCH_SIZE]
        embeddings  = model.encode(batch_docs, show_progress_bar=False).tolist()
        collection.add(
            ids        = ids[i:i + BATCH_SIZE],
            documents  = batch_docs,
            metadatas  = metadatas[i:i + BATCH_SIZE],
            embeddings = embeddings,
        )


def main():
    print("=" * 60)
    print("ChromaDB Vector Database Builder")
    print(f"  Server: {CHROMA_HOST}:{CHROMA_PORT}")
    print(f"  Model:  {MODEL_NAME}")
    print("=" * 60)

    print(f"\n[1] Loading {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)

    print("\n[2] Loading IFRS labels...")
    label_map = load_ifrs_labels()
    print(f"  {len(label_map)} labels loaded")

    print(f"\n[2b] Generating synonyms for short/ambiguous labels via {OLLAMA_MODEL}...")
    short_labels = [
        (tag, label_map.get(tag, camel_to_sentence(tag)))
        for tag in ifrs_definition
        if len(label_map.get(tag, camel_to_sentence(tag)).split()) <= 3
    ]
    synonym_map = generate_synonym_map(short_labels)
    synonym_map = validate_synonym_map(short_labels, synonym_map, model)
    print(f"  {len(synonym_map)}/{len(short_labels)} short labels got a verified, non-colliding synonym")

    client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)

    print("\n[3] Building gics_definitions collection...")
    client.delete_collection("gics_definitions") if "gics_definitions" in [c.name for c in client.list_collections()] else None
    gics_collection = client.create_collection(
        "gics_definitions", metadata={"hnsw:space": "cosine"}
    )
    g_ids, g_docs, g_meta = build_gics_documents()
    embed_and_add(gics_collection, model, g_ids, g_docs, g_meta)
    print(f"  ✓ {len(g_ids)} GICS definitions embedded")

    print("\n[4] Building xbrl_tags collection...")
    client.delete_collection("xbrl_tags") if "xbrl_tags" in [c.name for c in client.list_collections()] else None
    xbrl_collection = client.create_collection(
        "xbrl_tags", metadata={"hnsw:space": "cosine"}
    )
    x_ids, x_docs, x_meta = build_xbrl_documents(label_map, synonym_map)
    embed_and_add(xbrl_collection, model, x_ids, x_docs, x_meta)
    print(f"  ✓ {len(x_ids)} XBRL tags embedded")

    print("\n" + "=" * 60)
    print("VERIFICATION")
    print("=" * 60)
    print(f"  gics_definitions count: {gics_collection.count()}")
    print(f"  xbrl_tags count:        {xbrl_collection.count()}")

    sample_query = "bank deposits from customers"
    print(f"\n  Sample query on xbrl_tags: '{sample_query}'")
    q_emb = model.encode([sample_query]).tolist()
    results = xbrl_collection.query(query_embeddings=q_emb, n_results=5)
    for tag_id, doc, dist in zip(
        results["ids"][0], results["documents"][0], results["distances"][0]
    ):
        print(f"    {tag_id:45s} {doc[:45]:45s} dist={dist:.4f}")

    print("\n✅ ChromaDB built.")
    print(f"   client = chromadb.HttpClient(host='{CHROMA_HOST}', port={CHROMA_PORT})")


if __name__ == "__main__":
    main()
