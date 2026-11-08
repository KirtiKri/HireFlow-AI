from types import SimpleNamespace
from app.evidence_chat import answer_question, source_passages


def fake_client(payload):
    def create(**kwargs):
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=payload))])
    return SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=create)))


def test_sources_are_numbered_and_bounded():
    src = source_passages({'python': 'I used Python on a project.', 'sql': 'SQL database'})
    assert [s['id'] for s in src] == ['E1', 'E2']


def test_no_evidence_abstains():
    result = answer_question('Has Python?', {}, [], [])
    assert result['mode'] == 'no_evidence'


def test_grounded_answer():
    client = fake_client('{"answer":"Python is mentioned.","citations":["E1"]}')
    result = answer_question('Python?', {'python':'Built with Python'}, ['python'], [], client=client)
    assert result['mode'] == 'grounded' and result['citations'] == ['E1']


def test_hallucinated_citation_rejected():
    client = fake_client('{"answer":"Experienced in AWS","citations":["E99"]}')
    result = answer_question('AWS?', {'python':'Built with Python'}, ['python'], [], client=client)
    assert result['mode'] == 'unverified'


def test_uncited_factual_answer_abstains():
    client = fake_client('{"answer":"Has 10 years of experience","citations":[]}')
    result = answer_question('How long?', {'python':'Built with Python'}, ['python'], [], client=client)
    assert result['mode'] == 'insufficient'


def test_question_length_validation():
    try:
        answer_question('x'*601, {'a':'b'}, [], [])
        assert False
    except ValueError:
        pass
