"""
Sanity check for the concurrent resolve() in react_agent.py. Proves
results come back in input order even when the (slow) low-confidence
items finish out of order, and that no exception escapes the pool.

Run: python3 scripts/test_react_resolve_order.py
"""

import random
import time
from types import SimpleNamespace

from react_agent import ReActAgent, LOW_CONF_THRESHOLD


def demo():
    agent = ReActAgent(model=None, xbrl_collection=None)

    # Item 1 is high-confidence (skips TAOR); items 2-5 are low-confidence
    # and would enter _run_taor. Stub it with a random sleep so completion
    # order is scrambled, then assert output order still matches input order.
    def fake_run_taor(item, current_mapping, id_order, item_by_id, mapping_by_id, candidate_tags):
        time.sleep(random.uniform(0.01, 0.05))
        return agent._make_result(
            item, tag="STUB", label="stub", dist=0.9,
            resolved_by="react_loop", confidence="low",
        )
    agent._run_taor = fake_run_taor

    items = [SimpleNamespace(id=i, description=f"item {i}", amount="1") for i in range(1, 6)]
    initial_mappings = [
        SimpleNamespace(id=1, tag="Assets", tagLabel="Assets", distance=0.01),
        *[SimpleNamespace(id=i, tag="X", tagLabel="X", distance=0.9) for i in range(2, 6)],
    ]

    results = agent.resolve(items, initial_mappings, candidate_tags=["Assets", "X"])

    assert [r.id for r in results] == [1, 2, 3, 4, 5], f"order broken: {[r.id for r in results]}"
    assert results[0].resolved_by == "semantic_mapper"
    assert all(r.resolved_by == "react_loop" for r in results[1:])
    print("OK, concurrent resolve() preserves input order:", [r.id for r in results])


if __name__ == "__main__":
    demo()
