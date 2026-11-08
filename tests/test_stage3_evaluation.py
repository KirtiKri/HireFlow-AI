"""Golden evaluation checks for the current rules-based LangGraph pipeline."""
from eval.run_stage3 import evaluate


def test_stage3_golden_cases():
    results = evaluate()
    assert len(results) == 3
    failures = [r for r in results if not r['passed']]
    assert not failures, failures
