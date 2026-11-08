import os
import tempfile
from pathlib import Path
from unittest.mock import patch

from data.seed_demo import seed
from app.database import get_reviews
from app.review_actions import get_action


def test_seed_idempotent_and_review_statuses():
    with tempfile.TemporaryDirectory() as folder:
        with patch.dict(os.environ, {'DATABASE_PATH': str(Path(folder) / 'test.db')}):
            assert seed() == 25
            assert seed() == 0
            reviews = get_reviews()
            assert len(reviews) == 25
            assert all(r['candidate_name'].startswith('SYNTH-DEMO-') for r in reviews)
            assert {get_action(r['id'])['state'] for r in reviews} == {
                'pending', 'reviewed', 'needs_more_information'
            }
            assert seed(reset_demo=True) == 25
            assert len(get_reviews()) == 25
