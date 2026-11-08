"""Regression checks for conservative evidence matching."""
import pytest
from app.validation import verified_evidence, skill_supported

@pytest.mark.parametrize("text", [
    "I have never used Python.",
    "I do not know Python.",
    "No experience with Python.",
    "Currently learning Python.",
    "I want to learn Python.",
    "Unfamiliar with Python.",
    "Python: no experience.",
    "Python - beginner.",
])
def test_unverified_skill_claims_are_not_support(text):
    assert verified_evidence(text, ["python"]) == {}

def test_positive_claim_in_separate_clause_survives_negation():
    evidence = verified_evidence("Never used Docker; built Python services.", ["docker", "python"])
    assert "docker" not in evidence
    assert "python" in evidence

def test_explicit_mention_is_not_proficiency():
    assert skill_supported("sql", "Wrote SQL queries for a class project")

def test_word_boundaries_prevent_java_false_positive():
    assert not skill_supported("java", "Developed JavaScript interfaces")
