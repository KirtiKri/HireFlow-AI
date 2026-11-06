# HireFlow AI — Recruitment Evidence Workspace

An educational capstone prototype for human-reviewed recruitment document analysis.

## Current functionality
- Create job descriptions in SQLite
- Upload PDF, DOCX, TXT resumes (5 MB max; PDFs 15 pages max)
- Deterministic vocabulary-based skill detection and source excerpts
- LangGraph workflow with an insufficient-evidence branch
- Persistent review history, Streamlit dashboard, pytest and golden tests

**Not yet implemented:** production LLM extraction, persistent RAG, authentication, actual hiring workflow, robust skill ontology, resume OCR, deployment, security hardening. The `rag.py` module is an optional semantic retrieval experiment, not part of the review decision flow.

This is **not** a validated hiring assessment. Never use it to automatically screen, rank, reject, or hire real candidates. Use synthetic resumes for demonstrations.

## Setup (Windows PowerShell)
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m streamlit run app/main.py
```
Run from the project root. If activation is blocked, run `Set-ExecutionPolicy -Scope Process Bypass` and activate again.

## Optional demo job
```powershell
python -m data.seed_db
```

## Tests
```powershell
python -m pytest -q
python -m eval.run_golden
```

## Architecture
Streamlit → LangGraph requirements → extraction → (compare OR insufficient evidence) → SQLite record → human review.

## Data privacy
The MVP stores candidate references and extracted skill evidence, not full uploaded resume text. The local database is excluded from Git. Use fictional data. Authentication, retention controls, and consent handling are required before any real deployment.

## Next stages
Confirm official Recruitment problem statement; implement validated extraction, persistent policy RAG with citations, evaluation and UI refinement.

# HireFlow — Guided UI upgrade

## Install into your existing Phase 2 + golden-example project

Copy these files into the same relative paths, replacing `app/main.py` and `.streamlit/config.toml`:

- `app/main.py` — guided navigation and demo flow
- `app/styles.py` — consistent visual styling
- `app/ui_components.py` — reusable text and evidence presentation
- `app/review_actions.py` — persistent human follow-up notes (new SQLite table)
- `data/demo/jobs.json` — two fictional job descriptions
- `data/demo/resumes.json` — three fictional candidate resumes
- `.streamlit/config.toml` — theme

Do **not** delete your existing `data/hireflow.db`. The new `human_review_actions` table is created automatically.

From your project root, run:

```powershell
python -m streamlit run app/main.py
```

Open **Start a review** → choose **Junior Data Analyst** → choose **Asha Mehta** → click **Analyze resume**. Then open **Human review queue**, select the new review, enter a note, and save.

For a second demonstration, choose **Backend Python Developer** and **Rohan Sen**. The text explicitly negates Docker experience and describes FastAPI as learning in progress. The heuristic extraction should be reviewed for false positives/negatives; do not interpret the output as a measure of competence.

The project supports rule-based mode without an API key. For reproducible demonstrations, set `EXTRACTION_MODE=rules` in `.env`. RAG is optional and can be enabled under Advanced settings. This UI upgrade does not change the existing graph or golden tests.

## Known limitations

- The demo resumes are synthetic and contain no real personal information.
- The heuristic extractor can miss synonyms, misunderstand negations, and misinterpret context.
- The evidence shown is not a hiring recommendation or verified qualification.
- There is no authentication or multi-user permission system. Use locally for demonstration only.
- Saved reviewer notes are administrative follow-ups, not hiring outcomes.
