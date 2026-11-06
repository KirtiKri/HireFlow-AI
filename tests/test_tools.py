from app.tools import find_skills, evidence_for
from app.agents import compare_requirements

def test_skills_word_boundaries():
    assert find_skills("I use Python, SQL and Git") == ["python", "sql", "git"]
    assert "java" not in find_skills("javascript")

def test_comparison():
    out = compare_requirements(["python", "sql"], ["python"])
    assert out["supported_skills"] == ["python"]
    assert out["missing_skills"] == ["sql"]

def test_evidence():
    assert "Python" in evidence_for("Built Python applications.", ["python"])["python"]
