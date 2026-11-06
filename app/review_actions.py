"""Separate human-review notes; never modify automated evidence into hiring decisions."""
from app.database import connect

ALLOWED = {'pending', 'reviewed', 'needs_more_information'}

def init_actions():
    with connect() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS human_review_actions (
            review_id INTEGER PRIMARY KEY, state TEXT NOT NULL DEFAULT 'pending',
            reviewer_note TEXT NOT NULL DEFAULT '', updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )''')

def get_action(review_id):
    init_actions()
    with connect() as conn:
        row = conn.execute('SELECT * FROM human_review_actions WHERE review_id=?', (review_id,)).fetchone()
    return dict(row) if row else {'review_id':review_id, 'state':'pending', 'reviewer_note':''}

def save_action(review_id, state, note):
    if state not in ALLOWED:
        raise ValueError('Invalid review state')
    if len(note) > 2000:
        raise ValueError('Note must be 2000 characters or fewer')
    init_actions()
    with connect() as conn:
        conn.execute('''INSERT INTO human_review_actions(review_id,state,reviewer_note)
            VALUES(?,?,?) ON CONFLICT(review_id) DO UPDATE SET state=excluded.state,
            reviewer_note=excluded.reviewer_note,updated_at=CURRENT_TIMESTAMP''', (review_id,state,note.strip()))
