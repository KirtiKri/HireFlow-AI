import os
import sqlite3
from pathlib import Path

DEFAULT_DB = "data/hireflow.db"

def connect():
    path = Path(os.getenv("DATABASE_PATH", DEFAULT_DB))
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with connect() as conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id INTEGER NOT NULL REFERENCES jobs(id),
            candidate_name TEXT NOT NULL,
            observed_skills TEXT NOT NULL,
            supported_skills TEXT NOT NULL,
            missing_skills TEXT NOT NULL,
            evidence_json TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """)

def add_job(title: str, description: str) -> int:
    if not title.strip() or not description.strip():
        raise ValueError("Title and description are required")
    with connect() as conn:
        cursor = conn.execute("INSERT INTO jobs(title, description) VALUES (?, ?)", (title.strip(), description.strip()))
        return cursor.lastrowid

def get_jobs():
    with connect() as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM jobs ORDER BY id DESC")]

def get_job(job_id: int):
    with connect() as conn:
        row = conn.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)).fetchone()
        return dict(row) if row else None

def add_review(job_id: int, candidate_name: str, observed: list[str], supported: list[str], missing: list[str], evidence: dict, status: str) -> int:
    import json
    with connect() as conn:
        cursor = conn.execute("""INSERT INTO reviews(job_id, candidate_name, observed_skills, supported_skills, missing_skills, evidence_json, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)""", (job_id, candidate_name, json.dumps(observed), json.dumps(supported), json.dumps(missing), json.dumps(evidence), status))
        return cursor.lastrowid

def get_reviews():
    with connect() as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM reviews ORDER BY id DESC")]
