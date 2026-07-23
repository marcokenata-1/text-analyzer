# text-analyzer — IFRS/GICS/XBRL Standardization Service

Layer 2 of a two-layer financial report standardization pipeline. Layer 1
(a separate `TableExtractor` repo) extracts raw line items from PDF
financial statements. This repo takes that extraction and:

1. **Knowledge Layer** (`/classify`) — identifies the company's GICS
   sub-industry and prunes the ~2,300-tag IFRS XBRL taxonomy down to the
   tags relevant to that sub-industry (Contextual Pruning).
2. **Reasoning Layer** (`/reason`) — the Semantic Mapper assigns each line
   item to a candidate XBRL tag via nearest-neighbor embedding search; a
   ReAct agent (Thought-Action-Observation-Resolution) resolves
   low-confidence items using surrounding context and Ollama.
3. **Validation Layer** (`/validate`) — the Structural Contextualizer
   checks every assigned tag is within the pruned candidate pool, and the
   Summation Check verifies parent/child IFRS totals reconcile (e.g.
   `Assets = CurrentAssets + NoncurrentAssets + ...`) against the
   calculation-linkbase rules derived from the official taxonomy.

## Architecture

```
                     ┌──────────────┐   ┌──────────────┐
                     │   GraphDB    │   │   ChromaDB   │
                     │ (GICS→IFRS   │   │ (tag labels +│
                     │  taxonomy,   │   │  synonyms,   │
                     │  summation   │   │  GICS defs — │
                     │  rules)      │   │  embeddings) │
                     └──────┬───────┘   └──────┬───────┘
                            │                  │
                     ┌──────┴──────────────────┴───────┐
                     │        api.py (FastAPI)          │
                     │  /classify /classify-extraction  │
                     │  /reason  /validate               │
                     └──────────────┬────────────────────┘
                                    │
                              react_agent.py
                              (ReAct / TAOR loop, Ollama)
```

A second, lighter service (`knowledge-api`, `knowledge_api.py`) exposes
just `/classify` against GraphDB alone, with no ChromaDB/Ollama
dependency.

## Prerequisites

- Docker + Docker Compose
- Python 3.11+ (for running scripts outside Docker, e.g. `build_chromadb.py`, `build_graphdb.py`)
- Ollama with `llama3.1` pulled — used by the ReAct agent's low-confidence
  resolution step and by `build_chromadb.py`'s synonym generation.
  - **Local (Mac)**: run Ollama natively (`ollama pull llama3.1`) for
    Metal GPU acceleration — Docker Desktop on Mac has no GPU passthrough.
  - **Deploy (Linux/VPS)**: Ollama runs containerized instead (see below).

## Quick start

### 1. Start the infrastructure

Local development (Mac, native Ollama):

```bash
ollama pull llama3.1          # once, if not already pulled
docker compose -f docker-compose.yml -f docker-compose.local.yml up -d
```

Deploy (Linux host, Ollama containerized):

```bash
docker compose -f docker-compose.yml -f docker-compose.deploy.yml up -d
docker exec local_ollama ollama pull llama3.1   # first run only
```

This brings up:

| Service | Port | Purpose |
|---|---|---|
| `graphdb` | `7200` | GICS↔IFRS taxonomy graph + summation rules (Workbench UI at `/`) |
| `chromadb` | `8001` | Tag label / GICS definition embeddings |
| `knowledge-api` | `8000` | `/classify` only |
| `api` | `8002` | Full pipeline — `/classify`, `/classify-extraction`, `/reason`, `/validate` (docs at `/docs`) |

### 2. Load GraphDB

```bash
pip install -r scripts/requirements-api.txt   # SPARQLWrapper, rdflib, requests, etc.
python3 -c "
import sys; sys.path.insert(0, 'scripts')
import build_graphdb
build_graphdb.main()
"
```

Loads the GICS hierarchy, the IFRS XBRL tag nodes, the universal tags
(applied to every sub-industry), the SubIndustry→tag mapping (from
`data/mappings/subindustry_ifrs_mapping_v3_katana.json` by default — see
`build_graphdb.INPUT_JSON` to point at a different mapping version, e.g.
`subindustry_ifrs_mapping_v9.json`), and the summation calculation rules.

### 3. Load ChromaDB

```bash
python3 -c "
import sys; sys.path.insert(0, 'scripts')
import build_chromadb
build_chromadb.main()
"
```

Embeds every XBRL tag label (plus LLM-generated, programmatically-validated
synonyms for short/ambiguous labels — see `generate_synonym_map()` /
`validate_synonym_map()`) and every GICS Sector/IndustryGroup/Industry/
SubIndustry definition into the `xbrl_tags` and `gics_definitions`
collections.

### 4. Run the pipeline

```bash
curl -X POST http://localhost:8002/reason \
  -H "Content-Type: application/json" \
  -d '{
    "companyName": "Acme Corp",
    "items": [
      {"id": 1, "description": "Cash and cash equivalents", "amount": "12000"},
      {"id": 2, "description": "Trade receivable", "amount": "8500"}
    ]
  }'
```

Feed the `/reason` response straight into `/validate`:

```bash
curl -X POST http://localhost:8002/validate \
  -H "Content-Type: application/json" \
  -d @reason_response.json
```

Or start from raw Layer 1 extraction JSON via `/classify-extraction`,
which runs the same parser (`parse_extraction.py`) used for the fixtures
in `data/mappings/extractions*.json`.

## Directory layout

```
scripts/
  api.py                  Full FastAPI service (UC2+UC3+UC4)
  knowledge_api.py         Lightweight /classify-only service
  react_agent.py            ReAct/TAOR loop for low-confidence tag resolution
  parse_extraction.py       Layer 1 extraction JSON -> line items
  build_graphdb.py          Loads GICS/IFRS knowledge graph into GraphDB
  build_chromadb.py         Embeds tag labels + GICS definitions into ChromaDB
  finbert_qwen_v9.py         Katana HPC batch mapper (FinBERT + Qwen3-14B) —
                             regenerates subindustry_ifrs_mapping_v9.json
  run_v9.pbs                 PBS job script for the above (UNSW Katana HPC)
  d_20230318.py, ifrs_tags.py, universal_ifrs_tags.py
                             Static GICS/IFRS taxonomy definitions

data/                      Not committed — see "Generating the data" below
  mappings/                SubIndustry->XBRL tag mapping files, extraction fixtures
  taxonomy/                 Official IFRS Accounting Taxonomy (schema, labels, linkbases)
  chromadb/, chroma_db/     Local ChromaDB persistent storage

logs/                       Not committed — saved /reason + /validate output
                             per test fixture, regenerate by rerunning the
                             pipeline (see Quick start)
docs/                       Research report
```

## Generating the data

All of `data/` and `logs/` are gitignored — none of it is source, all of
it is either regenerable pipeline output or external reference data with
a documented way to obtain it.

**`data/taxonomy/`** — the official IFRS Accounting Taxonomy package
(`full_ifrs-cor_*.xsd`, `lab_full_ifrs-en_*.xml`, and the `linkbases/`
folder, which `build_graphdb.load_calculation_rules()` parses directly
instead of using a hand-maintained rule list):
1. Download the **full package** zip (e.g. `IFRSAT-2025.zip`, not an
   individual standard) from the
   [IFRS Accounting Taxonomy page](https://www.ifrs.org/issued-standards/ifrs-taxonomy/)
   (free registration required) — the full package includes every
   standard's calculation linkbase, not just IAS 1/IAS 7.
2. From the zip's `full_ifrs/` folder, copy `full_ifrs-cor_*.xsd` and
   `labels/lab_full_ifrs-en_*.xml` to `data/taxonomy/`, and the entire
   `linkbases/` folder to `data/taxonomy/linkbases/` (all standards, not
   a subset — `load_calculation_rules()` only reads the `cal_*.xml` files
   within it, but the full linkbase tree is still the actual official
   source of truth to keep on hand).
3. Rerun `build_graphdb.main()` to reload GraphDB with the updated rules.
4. If the new taxonomy adds/renames tags, `scripts/ifrs_tags.py` (the
   static tag definition dict) needs regenerating too — not automated
   yet, would need to be parsed from the new `full_ifrs-cor_*.xsd`.

To reproduce the rest from a fresh clone:

**`data/mappings/subindustry_ifrs_mapping_v3_katana.json`** (the current
GraphDB production default) and **`data/mappings/extractions*.json`**
(Layer 1 test fixtures) — these came from earlier pipeline runs and Layer 1
(the separate `TableExtractor` repo) respectively; no script in this repo
regenerates them from scratch. If you don't have copies, you'll need a
SubIndustry→tag mapping and at least one extraction JSON to get started —
see `finbert_qwen_v9.py` below for a way to produce a fresh mapping.

**`data/mappings/subindustry_ifrs_mapping_v9.json`** (and any newer
mapping version) — regenerate via the Katana HPC batch mapper, see
"Regenerating a SubIndustry→tag mapping" below.

**`data/chromadb/`, `data/chroma_db/`** — regenerate via `build_chromadb.py`
(step 3 above); this is pure derived state from `data/mappings/` and the
static taxonomy definitions, safe to delete and rebuild anytime.

**`logs/`** — regenerate by rerunning `/reason` + `/validate` against your
extraction fixtures (step 4 above) and saving the responses.

## Regenerating a SubIndustry→tag mapping (Katana HPC)

`finbert_qwen_v9.py` is a two-stage mapper: FinBERT bi-encoder shortlists
candidate tags per GICS SubIndustry, then Qwen3-14B selects the ones that
are actually relevant. To rerun it on UNSW's Katana HPC:

```bash
scp finbert_qwen_v9.py run_v9.pbs katana:~/thesis/
ssh katana
qsub run_v9.pbs
```

Output lands at `data/mappings/subindustry_ifrs_mapping_v9.json`; point
`build_graphdb.INPUT_JSON` at it and rerun `build_graphdb.main()` to load
it into GraphDB.
