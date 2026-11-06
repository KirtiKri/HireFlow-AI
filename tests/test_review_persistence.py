"""Run: python -m pytest tests/test_review_persistence.py -q"""
import json
from app import database
from app import review_actions


def test_review_notes_persist(tmp_path, monkeypatch):
    monkeypatch.setenv('DATABASE_PATH', str(tmp_path / 'test_hireflow.db'))
    database.init_db()
    review_actions.init_actions()
    job_id = database.add_job('Sample Data Analyst', 'Python and SQL')
    review_id = database.add_review(
        job_id, 'FICTIONAL-001', ['python'], ['python'], ['sql'],
        {'python': 'Used Python for a sample project'}, 'human_review_required',
    )
    assert review_actions.get_action(review_id)['state'] == 'pending'
    review_actions.save_action(review_id, 'needs_more_information', 'Request a SQL example.')
    saved = review_actions.get_action(review_id)
    assert saved['state'] == 'needs_more_information'
    assert saved['reviewer_note'] == 'Request a SQL example.'
    assert json.loads(database.get_reviews()[0]['supported_skills']) == ['python']
    review_actions.save_action(review_id, 'reviewed', 'Evidence checked.')
    assert review_actions.get_action(review_id)['state'] == 'reviewed'


def test_invalid_status_is_rejected(tmp_path, monkeypatch):
    monkeypatch.setenv('DATABASE_PATH', str(tmp_path / 'test_hireflow.db'))
    try:
        review_actions.save_action(1, 'hired', 'Do not allow this.')
    except ValueError:
        pass
    else:
        raise AssertionError('Invalid status was accepted')
