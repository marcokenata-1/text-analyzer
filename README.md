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
  api.py                     Full FastAPI service (UC2+UC3+UC4)
  knowledge_api.py           Lightweight /classify-only service
  react_agent.py             ReAct/TAOR loop for low-confidence tag resolution
  parse_extraction.py        Layer 1 extraction JSON -> line items
  build_graphdb.py           Loads GICS/IFRS knowledge graph into GraphDB
  build_chromadb.py          Embeds tag labels + GICS definitions into ChromaDB
  verify_graphdb.py          Standalone diagnostic — sanity-checks a loaded graph
  test_react_resolve_order.py
                              Sanity check for react_agent.py's concurrent resolve()
  katana/
    finbert_qwen_v9.py         Katana HPC batch mapper (FinBERT + Qwen3-14B) —
                                regenerates subindustry_ifrs_mapping_v9.json
    run_v9.pbs                 PBS job script for the above (UNSW Katana HPC)
  d_20230318.py, ifrs_tags.py, universal_ifrs_tags.py
                              Static GICS/IFRS taxonomy definitions
  Dockerfile.api              Builds the api.py image
  Dockerfile.knowledge-api    Builds the knowledge_api.py image
  requirements-api.txt, requirements-knowledge-api.txt
                              Per-image pip dependencies
  archive/                    Superseded/legacy scripts (old Neo4j-era code, prior
                               mapper versions) — gitignored, kept locally only,
                               not part of the running pipeline

data/                      Not committed — see "Generating the data" below
  mappings/                SubIndustry->XBRL tag mapping files, extraction fixtures
  taxonomy/                 Official IFRS Accounting Taxonomy (schema, labels, linkbases)
  chromadb/, chroma_db/     Local ChromaDB persistent storage

logs/                       Not committed — saved /reason + /validate output
                             per test fixture, regenerate by rerunning the
                             pipeline (see Quick start)
docs/                       Research report
```

### File dependencies

Static taxonomy data — no local imports, the base layer everything else
reads from:
- `d_20230318.py` — GICS Sector/IndustryGroup/Industry/SubIndustry hierarchy
- `ifrs_tags.py` — the ~2,300 XBRL tag definitions
- `universal_ifrs_tags.py` — the ~55 tags applied to every sub-industry

Pipeline / offline scripts:
- `build_graphdb.py` imports `d_20230318.py`, `ifrs_tags.py`,
  `universal_ifrs_tags.py` — also reads `data/taxonomy/` directly (falls
  back to reading straight out of `IFRSAT-2025.zip` if the flat files
  under `data/taxonomy/` aren't present, so a fresh setup doesn't strictly
  need the manual extraction step below).
- `build_chromadb.py` imports `d_20230318.py`, `ifrs_tags.py`, and
  `build_graphdb.py` itself (reuses its label-loading + camelCase-to-
  sentence helpers rather than duplicating them).
- `verify_graphdb.py` imports `universal_ifrs_tags.py` — run manually
  after `build_graphdb.py` to sanity-check what actually loaded.
- `katana/finbert_qwen_v9.py` imports `d_20230318.py`, `ifrs_tags.py`,
  `universal_ifrs_tags.py` — these live one level up in `scripts/`, not
  alongside it, so it isn't self-contained: deploying to the HPC cluster
  means `scp`-ing all three together with it and `run_v9.pbs` (see
  "Regenerating a SubIndustry→tag mapping" below). Not imported by
  anything else in this repo.

Services:
- `api.py` imports `parse_extraction.py` and `react_agent.py` — packaged
  by `Dockerfile.api` together with those two files.
- `knowledge_api.py` imports `d_20230318.py` — packaged by
  `Dockerfile.knowledge-api` together with it.
- `parse_extraction.py` and `react_agent.py` have no local imports of
  their own (only third-party: `requests`; `ollama` + `sentence-transformers`).

Tests:
- `test_react_resolve_order.py` imports `react_agent.py` — run directly
  (`python3 scripts/test_react_resolve_order.py`), no server/fixtures needed.

**Setup order** follows the dependency chain: taxonomy files on disk (or
`IFRSAT-2025.zip`) → `build_graphdb.py` → optionally `verify_graphdb.py`
→ `build_chromadb.py` → `api.py` / `knowledge_api.py` can now start.

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
2. **Either** extract it: copy `full_ifrs-cor_*.xsd` and
   `labels/lab_full_ifrs-en_*.xml` from the zip's `full_ifrs/` folder to
   `data/taxonomy/`, and the entire `linkbases/` folder to
   `data/taxonomy/linkbases/` (all standards, not a subset —
   `load_calculation_rules()` only reads the `cal_*.xml` files within it,
   but the full linkbase tree is still the actual official source of
   truth to keep on hand) — **or** just drop the zip itself, unextracted,
   at the repo root as `IFRSAT-2025.zip`. `build_graphdb.py` checks for
   the flat extracted files first and falls back to reading straight out
   of the zip if they're missing, so the zip alone is enough to get
   running (useful for a fresh VM/clone where you don't want to bother
   reorganizing paths by hand) — extracting is only worth it if you want
   the flat files individually browsable on disk.
3. Rerun `build_graphdb.main()` to reload GraphDB with the updated rules.
4. If the new taxonomy adds/renames tags, `scripts/ifrs_tags.py` (the
   static tag definition dict) needs regenerating too — not automated
   yet, would need to be parsed from the new `full_ifrs-cor_*.xsd`.

**`scripts/d_20230318.py`** — GICS Sector/IndustryGroup/Industry/
SubIndustry codes, names, and descriptions. Unlike the IFRS taxonomy,
MSCI/S&P Dow Jones Indices (who jointly maintain GICS) don't publish it
as a structured, machine-readable package — just PDF methodology/
structure documents, periodically revised. This file was generated via
the [`gics`](https://github.com/dorklein/py-gics) Python package
(`pip install gics`), whose bundled data versions are named after their
GICS effective date — `20230318` is that package's default version and
matches this file's name. Updating to a newer GICS revision means
checking whether `py-gics` has added a newer version, or otherwise
transcribing the new MSCI GICS Methodology PDF by hand — there's no
XML-parsing equivalent to `load_calculation_rules()` available here.

To reproduce the rest from a fresh clone:

**`data/mappings/subindustry_ifrs_mapping_v3_katana.json`** (the current
GraphDB production default) and **`data/mappings/extractions*.json`**
(Layer 1 test fixtures) — these came from earlier pipeline runs and Layer 1
(the separate `TableExtractor` repo) respectively; no script in this repo
regenerates them from scratch. If you don't have copies, you'll need a
SubIndustry→tag mapping and at least one extraction JSON to get started —
see `katana/finbert_qwen_v9.py` below for a way to produce a fresh mapping.

**`data/mappings/subindustry_ifrs_mapping_v9.json`** (and any newer
mapping version) — regenerate via the Katana HPC batch mapper, see
"Regenerating a SubIndustry→tag mapping" below.

**`data/chromadb/`, `data/chroma_db/`** — regenerate via `build_chromadb.py`
(step 3 above); this is pure derived state from `data/mappings/` and the
static taxonomy definitions, safe to delete and rebuild anytime.

**`logs/`** — regenerate by rerunning `/reason` + `/validate` against your
extraction fixtures (step 4 above) and saving the responses.

## Regenerating a SubIndustry→tag mapping (Katana HPC)

`katana/finbert_qwen_v9.py` is a two-stage mapper: FinBERT bi-encoder
shortlists candidate tags per GICS SubIndustry, then Qwen3-14B selects the
ones that are actually relevant. It imports `d_20230318.py`, `ifrs_tags.py`,
and `universal_ifrs_tags.py` from one level up in `scripts/`, so all three
need to go along with it — it isn't runnable from just its own folder. To
rerun it on UNSW's Katana HPC:

```bash
scp scripts/d_20230318.py scripts/ifrs_tags.py scripts/universal_ifrs_tags.py \
    scripts/katana/finbert_qwen_v9.py scripts/katana/run_v9.pbs \
    katana:~/thesis/
ssh katana
qsub run_v9.pbs
```

Output lands at `data/mappings/subindustry_ifrs_mapping_v9.json`; point
`build_graphdb.INPUT_JSON` at it and rerun `build_graphdb.main()` to load
it into GraphDB.
