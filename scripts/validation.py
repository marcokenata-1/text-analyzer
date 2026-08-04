"""
UC4 Validation Layer checks, run by api.py's /validate endpoint against
UC3's (/reason) output ledger: every assigned tag must fall within the
GICS-pruned candidate pool (Structural Contextualizer), and Total Reported
must equal Sum(Components) per GraphDB's HAS_CHILD_TAG rules (Summation
Check).
"""

from typing import Optional

from schemas import StructuralIssue, SummationIssue

SUM_TOLERANCE = 0.02   # 2% relative tolerance for the Summation Check


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


def check_structural_pool(mappings, candidate_tags: set[str], gics_name: str) -> list[StructuralIssue]:
    """Every assigned tag must fall within the GICS-pruned candidate pool.
    Guards against the ReAct Agent or Semantic Mapper drifting outside it."""
    return [
        StructuralIssue(
            id=m.id, tag=m.tag,
            issue=f"'{m.tag}' is not in the pruned candidate pool for {gics_name}",
        )
        for m in mappings
        if m.tag and m.tag not in candidate_tags
    ]


def group_amounts_by_tag(mappings) -> dict[str, list[tuple[int, float]]]:
    amounts_by_tag: dict[str, list[tuple[int, float]]] = {}
    for m in mappings:
        if not m.tag:
            continue
        amount = parse_amount(m.amount)
        if amount is None:
            continue
        amounts_by_tag.setdefault(m.tag, []).append((m.id, amount))
    return amounts_by_tag


def find_conflicted_tags(
    amounts_by_tag: dict[str, list[tuple[int, float]]],
    summation_rules: dict[str, list[tuple[str, float]]],
) -> tuple[set[str], list[StructuralIssue]]:
    """
    A summation-parent tag represents one report-level total by definition.
    If more than one item maps directly to it, that's an unresolved mapping
    conflict, not extra components to sum, and summing them would silently
    corrupt "reported". Surface the conflict and skip the check for that tag.

    Conflicted tags are excluded from every parent's child_entries too, not
    just their own check: a tag can be both a total in its own right and a
    child contributing to another tag's sum.
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
                      f"'{parent_tag}', expected exactly one; summation check skipped for this tag",
            ))
    return conflicted_tags, issues


def check_summations(
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
        # abs(amt): parse_amount already turned "(1,234)" into a negative,
        # which encodes the same "subtract this" intent as a -1 weight.
        # Normalize to magnitude first so the weight alone decides the sign.
        child_entries = [
            (id_, weight * abs(amt))
            for child_tag, weight in weighted_children
            if child_tag not in conflicted_tags
            for id_, amt in amounts_by_tag.get(child_tag, [])
        ]
        if not child_entries:
            continue  # no components assigned in this ledger, nothing to check

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
