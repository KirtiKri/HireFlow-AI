"""Run fixed, fictional golden cases through the actual LangGraph pipeline.

From the project root: python -m eval.run_stage3
No SQLite writes, network calls, or live candidate data are needed in rules mode.
"""
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

from app.graph import graph
from app.evidence_report import build_evidence_rows

CASES = Path(__file__).with_name('stage3_cases.json')
REPORT = Path(__file__).with_name('stage3_results.json')


def evaluate():
    cases = json.loads(CASES.read_text(encoding='utf-8'))
    results = []
    with patch.dict(os.environ, {'EXTRACTION_MODE': 'rules'}):
        for case in cases:
            output = graph.invoke({'job_description': case['job'],
                                   'resume_text': case['resume'], 'trace': [], 'use_rag': False})
            supported = set(output.get('supported_skills', []))
            missing = set(output.get('missing_skills', []))
            expected_supported = set(case['supported'])
            expected_missing = set(case['missing'])
            rows = build_evidence_rows(output)
            row_by_skill = {r['Requirement']: r for r in rows}
            required = expected_supported | expected_missing
            checks = {
                'supported_exact': supported == expected_supported,
                'missing_exact': missing == expected_missing,
                'report_covers_requirements': set(row_by_skill) == required,
                'supported_have_passages': all(
                    row_by_skill.get(skill, {}).get('Finding') == 'Evidence passage recorded'
                    for skill in expected_supported),
                'missing_marked_not_evidenced': all(
                    row_by_skill.get(skill, {}).get('Finding') == 'Not evidenced in saved review'
                    for skill in expected_missing),
                'trace_contains_core_steps': {'requirements', 'extract', 'compare'}.issubset(
                    set(output.get('trace', []))),
            }
            results.append({'id': case['id'], 'role': case['role'],
                            'passed': all(checks.values()), 'checks': checks,
                            'actual_supported': sorted(supported), 'actual_missing': sorted(missing),
                            'expected_supported': sorted(expected_supported),
                            'expected_missing': sorted(expected_missing),
                            'trace': output.get('trace', [])})
    return results


def main():
    results = evaluate()
    payload = {'generated_at_utc': datetime.now(timezone.utc).isoformat(),
               'evaluation_mode': 'deterministic rules baseline; fictional test cases',
               'passed_cases': sum(r['passed'] for r in results),
               'total_cases': len(results), 'results': results}
    REPORT.write_text(json.dumps(payload, indent=2), encoding='utf-8')
    for result in results:
        print(f"{result['id']}: {'PASS' if result['passed'] else 'FAIL'} — {result['role']}")
        for name, passed in result['checks'].items():
            if not passed:
                print(f'  FAILED: {name}')
                print('  Expected supported:', result['expected_supported'])
                print('  Actual supported:', result['actual_supported'])
                print('  Expected missing:', result['expected_missing'])
                print('  Actual missing:', result['actual_missing'])
    print(f"{payload['passed_cases']}/{payload['total_cases']} cases passed")
    print(f'Results saved: {REPORT}')
    return 0 if payload['passed_cases'] == payload['total_cases'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
