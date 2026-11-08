"""Seed 25 explicitly fictional HireFlow reviews; repeatable without duplicates.

Run from project root: python -m data.seed_demo
Optional: python -m data.seed_demo --reset-demo
"""
import argparse
import json
from datetime import datetime, timedelta, timezone
from app.database import connect, init_db, add_job, add_review
from app.review_actions import init_actions, save_action

PREFIX = 'SYNTH-DEMO-'
ROLES = [
    ('Python Data Analyst', 'Python SQL pandas Excel visualization', ['python', 'sql', 'pandas', 'excel', 'visualization']),
    ('Backend Developer', 'Python SQL Git Docker APIs', ['python', 'sql', 'git', 'docker', 'apis']),
    ('BI Analyst', 'SQL Excel Power BI dashboards communication', ['sql', 'excel', 'power bi', 'dashboards', 'communication']),
    ('Junior ML Engineer', 'Python pandas scikit-learn Git statistics', ['python', 'pandas', 'scikit-learn', 'git', 'statistics']),
    ('Operations Analyst', 'Excel SQL reporting documentation communication', ['excel', 'sql', 'reporting', 'documentation', 'communication']),
]

def seed(reset_demo=False):
    init_db()
    init_actions()
    with connect() as conn:
        if reset_demo:
            ids = [r['id'] for r in conn.execute('SELECT id FROM reviews WHERE candidate_name LIKE ?', (PREFIX + '%',))]
            for review_id in ids:
                conn.execute('DELETE FROM human_review_actions WHERE review_id=?', (review_id,))
                conn.execute('DELETE FROM reviews WHERE id=?', (review_id,))
        existing = {r['candidate_name'] for r in conn.execute('SELECT candidate_name FROM reviews WHERE candidate_name LIKE ?', (PREFIX + '%',))}
    with connect() as conn:
        role_ids = {}
        for title, description, _ in ROLES:
            row = conn.execute('SELECT id FROM jobs WHERE title=? AND description=? ORDER BY id LIMIT 1', (title + ' [SYNTHETIC DEMO]', description)).fetchone()
            role_ids[title] = row['id'] if row else add_job(title + ' [SYNTHETIC DEMO]', description)
    inserted = 0
    for i in range(25):
        ref = f'{PREFIX}{i+1:03d}'
        if ref in existing:
            continue
        title, _, requirements = ROLES[i % len(ROLES)]
        # These are explicitly synthetic *mentions*, not independently verified competence.
        observed = [skill for j, skill in enumerate(requirements) if (i + j * 3) % 5 != 0]
        unsupported = [skill for skill in requirements if skill not in observed]
        evidence = {skill: f'SYNTHETIC SAMPLE EXCERPT: fictional resume mentions {skill}. Not verified.' for skill in observed}
        review_id = add_review(role_ids[title], ref, observed, observed, unsupported, evidence, 'human_review_required')
        state = ('reviewed' if i % 4 in (0, 1) else 'pending' if i % 4 == 2 else 'needs_more_information')
        save_action(review_id, state, 'Synthetic demonstration only. No hiring decision or credential verification.')
        day = datetime.now(timezone.utc) - timedelta(days=(24 - i) // 3)
        with connect() as conn:
            conn.execute('UPDATE reviews SET created_at=? WHERE id=?', (day.strftime('%Y-%m-%d %H:%M:%S'), review_id))
        inserted += 1
    return inserted

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reset-demo', action='store_true', help='Replace only SYNTH-DEMO-* review rows')
    args = parser.parse_args()
    count = seed(reset_demo=args.reset_demo)
    print(f'Added {count} fictional reviews. Existing demo reviews were not duplicated.')
