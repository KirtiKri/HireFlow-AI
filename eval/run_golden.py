"""Golden behavior tests; runs the same graph as the UI, with RAG disabled."""
import json
from pathlib import Path
from app.graph import graph

def main():
    cases = json.loads(Path("eval/golden.json").read_text(encoding="utf-8"))
    failed = 0
    for case in cases:
        result = graph.invoke({"job_description":case["job"], "resume_text":case["resume"], "trace":[], "use_rag":False})
        passed = result.get("supported_skills") == sorted(case["supported"]) and result.get("status") == case["status"]
        print(f"{case['id']}: {'PASS' if passed else 'FAIL'} | observed={result.get('supported_skills')} | status={result.get('status')}")
        failed += not passed
    if failed:
        raise SystemExit(f"{failed} golden cases failed")
    print("All golden cases passed")

if __name__ == "__main__":
    main()
