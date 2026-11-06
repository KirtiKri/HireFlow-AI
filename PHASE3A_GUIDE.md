# HireFlow Phase 3A — Stability patch

This is a targeted patch based on the uploaded project files. It does not replace the LangGraph or database implementation.

## Apply

1. Back up your existing `app/main.py`.
2. Copy `app/main.py` from this package into `HireFlow-AI/app/main.py` (replace existing).
3. Copy `tests/test_review_persistence.py` into `HireFlow-AI/tests/`.
4. Replace the root `.env.example` with the safe template included here. **Do not overwrite your local `.env`**.
5. Revoke the API key previously placed in `.env.example` and create a new key; update only local `.env`.

## Run

From the HireFlow-AI root with the virtual environment active:

```powershell
python -m pytest tests/test_review_persistence.py -q
python -m streamlit run app/main.py
```

## Manual acceptance checks

1. Home -> Start guided review works.
2. Start a review -> select sample job and fictional candidate -> Analyze resume.
3. Open human review queue works.
4. Save a `Needs more information` note; refresh and verify it remains.
5. Change status to `Reviewed`; refresh and verify it remains.

Note: `app/main.py` imports additional project modules not supplied with the upload, so complete end-to-end runtime testing must be performed in your local project.
