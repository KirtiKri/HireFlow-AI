from app.graph import graph

def test_review_requires_human():
    out = graph.invoke({"job_description": "Python and SQL", "resume_text": "Built a Python app", "trace": []})
    assert out["status"] == "human_review_required"
    assert out["supported_skills"] == ["python"]
    assert out["missing_skills"] == ["sql"]

def test_insufficient_evidence():
    out = graph.invoke({"job_description": "Python", "resume_text": "Motivated learner", "trace": []})
    assert out["status"] == "insufficient_evidence"
