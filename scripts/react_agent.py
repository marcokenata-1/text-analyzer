"""
ReAct Agent — Reasoning Layer (§3.5.2)

Implements the Thought-Action-Observation-Resolution (TAOR) cycle for
resolving low-confidence XBRL mappings produced by the Semantic Mapper.

Called after the initial ChromaDB nearest-neighbor pass.  Items whose
cosine distance exceeds LOW_CONF_THRESHOLD enter the loop; high-confidence
items pass through unchanged.

Each TAOR cycle:
  Thought     — assess surrounding context; identify semantic anchors
  Action      — re-query ChromaDB with anchor-enriched description; get top-N
  Observation — check whether any candidate satisfies summation constraints
  Resolution  — accept via summation, Ollama reasoning, or best-candidate fallback

Auditability: every cycle step is recorded in react_trace so the full
reasoning path is inspectable (§2.4.1 non-functional requirement).
"""

import re
from dataclasses import dataclass, field
from typing import Optional

import ollama
from sentence_transformers import util


# ── Thresholds ────────────────────────────────────────────────────────────────

LOW_CONF_THRESHOLD = 0.55   # cosine distance above which TAOR triggers
MAX_ITERATIONS     = 3      # TAOR cycle cap per item
CONTEXT_WINDOW     = 3      # neighbours each side included in Thought step
SUM_TOLERANCE      = 0.02   # 2 % relative tolerance for summation Observation
OLLAMA_MODEL       = "llama3.1"

# Physically-adjacent rows in the source table are often from unrelated notes
# (e.g. a tax disclosure sitting next to a PP&E note) — being nearby and
# individually high-confidence isn't evidence the two items are topically
# related. Anchors must also be semantically close to the item itself.
# 0.35 cleanly separates real cases: unrelated pairs score ~0.11-0.20,
# genuinely related ones ~0.73-0.95.
ANCHOR_SIM_THRESHOLD = 0.35

TOTAL_PATTERN = re.compile(r"^(total|net\s+total|sub.?total)\b", re.I)


# ── Data classes ──────────────────────────────────────────────────────────────

@dataclass
class TaorStep:
    step: str       # "thought" | "action" | "observation" | "resolution"
    content: str


@dataclass
class ReactResult:
    id: int
    description: str
    amount: str
    tag: Optional[str]
    tag_label: Optional[str]
    distance: Optional[float]
    resolved_by: str    # "semantic_mapper" | "react_loop" | "unresolved"
    confidence: str     # "high" | "low" | "unresolved"
    react_trace: list = field(default_factory=list)   # list[TaorStep]


# ── Agent ─────────────────────────────────────────────────────────────────────

class ReActAgent:
    """
    Wraps the Semantic Mapper output, runs TAOR on low-confidence items.

    Args:
        model           — loaded SentenceTransformer (shared with api.py)
        xbrl_collection — ChromaDB collection for xbrl_tags
        use_ollama      — set False to skip the Ollama Resolution step
    """

    def __init__(self, model, xbrl_collection, use_ollama: bool = True):
        self.model           = model
        self.xbrl_collection = xbrl_collection
        self.use_ollama      = use_ollama

    # ── Public interface ──────────────────────────────────────────────────────

    def resolve(
        self,
        items: list,             # list[LineItem] from api.py
        initial_mappings: list,  # list[MappingResult] from Semantic Mapper
        candidate_tags: list,    # GICS-pruned XBRL tag names
    ) -> list:
        """
        Process all items.  High-confidence pass through; low-confidence
        enter the TAOR loop.  Returns list[ReactResult] in the same order.
        """
        mapping_by_id = {m.id: m for m in initial_mappings}
        item_by_id    = {it.id: it for it in items}
        id_order      = [it.id for it in items]

        results = []
        for item in items:
            m = mapping_by_id.get(item.id)

            if m is None:
                results.append(ReactResult(
                    id=item.id, description=item.description, amount=item.amount or "",
                    tag=None, tag_label=None, distance=None,
                    resolved_by="unresolved", confidence="unresolved",
                ))
                continue

            # High confidence — pass straight through
            if m.distance is not None and m.distance < LOW_CONF_THRESHOLD:
                results.append(ReactResult(
                    id=item.id, description=item.description, amount=item.amount or "",
                    tag=m.tag, tag_label=m.tagLabel, distance=m.distance,
                    resolved_by="semantic_mapper", confidence="high",
                ))
            else:
                results.append(self._run_taor(
                    item=item,
                    current_mapping=m,
                    id_order=id_order,
                    item_by_id=item_by_id,
                    mapping_by_id=mapping_by_id,
                    candidate_tags=candidate_tags,
                ))

        return results

    # ── TAOR loop ─────────────────────────────────────────────────────────────

    def _run_taor(
        self, item, current_mapping, id_order, item_by_id, mapping_by_id, candidate_tags
    ) -> ReactResult:
        trace = []
        best_tag   = current_mapping.tag
        best_label = current_mapping.tagLabel
        best_dist  = current_mapping.distance

        for iteration in range(MAX_ITERATIONS):

            # ── THOUGHT ──────────────────────────────────────────────────
            neighbours, anchors = self._get_context(
                item, id_order, item_by_id, mapping_by_id
            )
            dist_str = f"{best_dist:.3f}" if best_dist is not None else "N/A"
            anchor_summary = [
                (a.description, mapping_by_id[a.id].tag)
                for a in anchors
                if mapping_by_id.get(a.id) and mapping_by_id[a.id].tag
            ]
            trace.append(TaorStep("thought", (
                f"Iteration {iteration + 1}: '{item.description}' "
                f"(distance={dist_str}, current tag={best_tag}). "
                f"Neighbours: {[n.description for n in neighbours]}. "
                f"Anchors (high-conf): {anchor_summary}."
            )))

            # ── ACTION ───────────────────────────────────────────────────
            anchor_labels = " ".join(
                mapping_by_id[a.id].tagLabel or ""
                for a in anchors
                if mapping_by_id.get(a.id) and mapping_by_id[a.id].tagLabel
            )
            enriched = f"{item.description} {anchor_labels}".strip()
            candidates = self._top_candidates(enriched, candidate_tags, n=5)
            trace.append(TaorStep("action", (
                f"Re-queried ChromaDB with: '{enriched}'. "
                f"Candidates: {[(c[0], round(c[2], 3)) for c in candidates]}."
            )))

            if not candidates:
                trace.append(TaorStep("observation", "No candidates returned."))
                trace.append(TaorStep("resolution", "Keeping current mapping."))
                break

            # ── OBSERVATION ──────────────────────────────────────────────
            obs_text, sum_winner = self._check_summation(
                item, candidates, id_order, item_by_id
            )
            trace.append(TaorStep("observation", obs_text))

            # ── RESOLUTION ───────────────────────────────────────────────
            if sum_winner:
                tag, label, dist = sum_winner
                trace.append(TaorStep("resolution", f"Summation check passed — accepted {tag}."))
                return ReactResult(
                    id=item.id, description=item.description, amount=item.amount or "",
                    tag=tag, tag_label=label, distance=dist,
                    resolved_by="react_loop", confidence="high", react_trace=trace,
                )

            if self.use_ollama:
                ollama_tag = self._ollama_resolve(item, candidates, anchors, mapping_by_id)
                if ollama_tag:
                    matched = next((c for c in candidates if c[0] == ollama_tag), None)
                    if matched:
                        tag, label, dist = matched
                        trace.append(TaorStep("resolution", f"Ollama resolved — accepted {tag}."))
                        return ReactResult(
                            id=item.id, description=item.description, amount=item.amount or "",
                            tag=tag, tag_label=label, distance=dist,
                            resolved_by="react_loop", confidence="low", react_trace=trace,
                        )

            # No improvement this iteration — update best candidate and loop
            if candidates and (best_dist is None or candidates[0][2] < best_dist):
                best_tag, best_label, best_dist = candidates[0]
            trace.append(TaorStep(
                "resolution",
                f"No resolution in iteration {iteration + 1}. Best so far: {best_tag}.",
            ))

        return ReactResult(
            id=item.id, description=item.description, amount=item.amount or "",
            tag=best_tag, tag_label=best_label, distance=best_dist,
            resolved_by="react_loop" if best_tag != current_mapping.tag else "unresolved",
            confidence="low", react_trace=trace,
        )

    # ── Helper: context ───────────────────────────────────────────────────────

    def _get_context(self, item, id_order, item_by_id, mapping_by_id):
        """Return (neighbours, anchors). Anchors are high-confidence neighbours
        that are also topically related to `item` — physical adjacency in the
        source table plus the neighbour's own confidence isn't enough, since
        unrelated notes commonly sit next to each other in the extraction."""
        idx   = id_order.index(item.id)
        start = max(0, idx - CONTEXT_WINDOW)
        end   = min(len(id_order), idx + CONTEXT_WINDOW + 1)
        neighbours = [
            item_by_id[i] for i in id_order[start:end] if i != item.id
        ]
        confident = [
            n for n in neighbours
            if (m := mapping_by_id.get(n.id))
            and m.distance is not None
            and m.distance < LOW_CONF_THRESHOLD
        ]
        if not confident:
            return neighbours, []

        embs = self.model.encode([item.description] + [n.description for n in confident])
        sims = util.cos_sim(embs[0], embs[1:])[0]
        anchors = [n for n, sim in zip(confident, sims) if sim >= ANCHOR_SIM_THRESHOLD]
        return neighbours, anchors

    # ── Helper: ChromaDB query ────────────────────────────────────────────────

    def _top_candidates(self, query: str, candidate_tags: list, n: int = 5):
        """
        Return list of (tag_name, label, distance) tuples, best first.
        """
        if not query.strip() or not candidate_tags:
            return []
        try:
            emb    = self.model.encode([query]).tolist()
            result = self.xbrl_collection.query(
                query_embeddings=emb,
                n_results=min(n, len(candidate_tags)),
                where={"tagName": {"$in": candidate_tags}},
            )
            if not result["ids"][0]:
                return []
            return list(zip(
                result["ids"][0],
                result["documents"][0],
                result["distances"][0],
            ))
        except Exception:
            return []

    # ── Helper: summation observation ─────────────────────────────────────────

    def _check_summation(self, item, candidates, id_order, item_by_id):
        """
        For items whose description starts with "Total / Net total / Subtotal",
        verify that the sum of the preceding section's non-total line items
        matches the reported amount within SUM_TOLERANCE.

        Returns (observation_text, winning_candidate_or_None).
        """
        if not item.amount:
            return "No amount available — summation check skipped.", None

        try:
            target = float(item.amount)
        except (ValueError, TypeError):
            return "Amount not numeric — summation check skipped.", None

        if not TOTAL_PATTERN.match(item.description.strip()):
            return "Item is not a section total — summation check not applicable.", None

        idx = id_order.index(item.id)

        # Walk back to find the previous total (or start of list)
        section_start = 0
        for i in range(idx - 1, -1, -1):
            prev = item_by_id[id_order[i]]
            if TOTAL_PATTERN.match(prev.description.strip()):
                section_start = i + 1
                break

        child_amounts = []
        for cid in id_order[section_start:idx]:
            child = item_by_id[cid]
            try:
                child_amounts.append(float(child.amount))
            except (ValueError, TypeError):
                pass

        if not child_amounts:
            return "No child amounts found in section — summation check skipped.", None

        child_sum = sum(child_amounts)
        rel_delta = abs(child_sum - target) / max(abs(target), 1)
        obs = (
            f"Section sum of {len(child_amounts)} items = {child_sum:.0f}, "
            f"reported total = {target:.0f}, relative delta = {rel_delta:.2%}."
        )

        if rel_delta <= SUM_TOLERANCE:
            obs += " Summation balanced — accepting best candidate."
            return obs, candidates[0] if candidates else None

        obs += f" Imbalanced (threshold {SUM_TOLERANCE:.0%}) — summation cannot resolve."
        return obs, None

    # ── Helper: Ollama resolution ─────────────────────────────────────────────

    def _ollama_resolve(self, item, candidates, anchors, mapping_by_id) -> Optional[str]:
        """
        Ask Ollama to pick the best candidate tag given surrounding context.
        Returns the tag name string, or None if Ollama fails or abstains.
        """
        anchor_lines = "\n".join(
            f"  - '{a.description}' → {mapping_by_id[a.id].tag}"
            for a in anchors
            if mapping_by_id.get(a.id) and mapping_by_id[a.id].tag
        ) or "  (none)"

        cand_lines = "\n".join(
            f"  {i + 1}. {tag}  ({label})"
            for i, (tag, label, _) in enumerate(candidates)
        )

        prompt = f"""You are an IFRS financial reporting expert.

Line item: "{item.description}"  amount: {item.amount}

High-confidence neighbouring items (for accounting context):
{anchor_lines}

Candidate XBRL tags (ranked by embedding similarity):
{cand_lines}

First, in one sentence: does this line item represent money OWED BY the
entity (a liability/expense) or OWED TO the entity (an asset/income)? Tag
names containing "Liabilities" or "Payable" are the entity's obligations;
"Assets" or "Receivable" are amounts due to the entity — embedding similarity
alone often can't tell these apart for short tax/duty labels, so reason about
it explicitly. Then pick the candidate consistent with that direction.

Reply with your one-sentence reasoning, then on a new line write exactly:
ANSWER: <number>
using 0 if none fit."""

        try:
            resp = ollama.chat(
                model=OLLAMA_MODEL,
                messages=[{"role": "user", "content": prompt}],
                options={"temperature": 0.0},
            )
            raw   = resp["message"]["content"].strip()
            match = re.search(r"ANSWER:\s*([0-9]+)", raw, re.I) or re.search(r"\b([0-9]+)\b", raw)
            if match:
                n = int(match.group(1))
                if 1 <= n <= len(candidates):
                    return candidates[n - 1][0]
        except Exception as e:
            print(f"[ReAct] Ollama error: {e}")
        return None
