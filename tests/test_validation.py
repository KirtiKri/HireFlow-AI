from app.validation import verified_evidence

def test_negated_skill_is_not_evidence():
    assert verified_evidence("I have never used Python.", ["python"]) == {}

def test_explicit_skill_is_evidence():
    assert "python" in verified_evidence("Built Python applications.", ["python"])
