HireFlow AI — Recruitment Evidence Workspace
An explainable, human-reviewed recruitment document analysis prototype.

HireFlow AI is an educational capstone project that helps a reviewer compare the documented content of a resume with the requirements of a job description. It highlights recognized requirements, shows supporting excerpts where available, identifies requirements without recorded evidence, and keeps the final interpretation with a human reviewer.
Educational demonstration only. HireFlow is not a validated hiring assessment and must not be used to automatically screen, score, rank, reject, or hire real applicants. Use fictional candidate information for demonstrations.

Application preview
 screenshots of actual Streamlit application to docs/screenshots/ 

	
## System Architecture

HireFlow AI uses Streamlit for the interface, LangGraph for
evidence-review orchestration, and SQLite for persistent records.

For architecture diagrams, data flow, and component details,
see [Architecture Documentation](docs/ARCHITECTURE.md).

Features
- Job management: Create and save job descriptions in SQLite.
- Resume intake: Review PDF, DOCX, and TXT documents (5 MB upload limit; PDFs limited to 15 pages).
- Evidence-oriented extraction: Identify skills using a documented, deterministic vocabulary and show saved supporting text excerpts.
- LangGraph workflow: Process requirements and resume evidence, including an insufficient-evidence branch.
- Human review queue: Revisit saved analyses and record human follow-up notes and states.
- Analytics dashboard: View review activity, follow-up status, and requirements represented in saved reviews.
- Evidence reporting: Inspect supported and not-evidenced requirements and export a CSV evidence report.
- Reproducible tests: Run automated tests and golden-example evaluations.
How to interpret the output: A recognized term or supporting passage is document evidence, not proof of proficiency. A requirement labeled not evidenced is not proof that the candidate lacks that skill.
Technology
Python 3.11 · Streamlit · LangGraph · SQLite · pytest · Plotly (dashboard charts)

The core demonstration uses rule-based extraction and does not require an LLM API key. The optional rag.py module is a semantic-retrieval experiment; it is not part of the hiring evidence decision flow.
Quick start — Windows PowerShell
From the repository root:
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
If PowerShell blocks virtual-environment activation, you can run Set-ExecutionPolicy -Scope Process Bypass in that terminal session and retry activation.
Prepare fictional demo data
python -m data.seed_db
python -m data.seed_demo
data.seed_db is the existing starter-data command; data.seed_demo populates the analytics with fictional review records. The seed generator is intended to avoid duplicates on repeated runs. If you prefer an empty workspace, skip the optional seed commands and create a job in the UI.
Start the application
python -m streamlit run app/main.py
Open the local URL printed by Streamlit (typically http://localhost:8501). Use Manage jobs to create a position or Start a review to select an available role and analyze a fictional resume.
Optional environment settings
The application supports rule-based mode without an API key. Where applicable, set EXTRACTION_MODE=rules in a local .env file. Use .env.example only for placeholder values. Never commit .env or a real API key.
Try the demonstration
1. Open Home to see dashboard metrics and, after seeding, fictional analytics data.
2. Open Start a review, select Junior Data Analyst, and choose the fictional Asha Mehta sample (or upload a fictional PDF, DOCX, or TXT resume).
3. Run the analysis and inspect the recognized requirements, saved evidence excerpts, and items needing human verification.
4. Open Human review queue, select the new record, enter a follow-up note, and save it.
5. Open the evidence report and download the CSV to inspect the result outside the application.
6. Repeat with Backend Python Developer and the fictional Rohan Sen sample to demonstrate different evidence and possible limitations of keyword-based matching.
The sample jobs and resumes are maintained under data/demo/. If you add PDF samples for GitHub reviewers, use fictional identities and commit those sample files explicitly. The SQLite database is generated locally and should remain excluded from version control.
Architecture
Streamlit interface
       |
       v
Job description + resume intake
       |
       v
LangGraph workflow
  -> requirement extraction
  -> resume evidence extraction
  -> compare OR insufficient-evidence branch
       |
       v
SQLite review record
       |
       +--> evidence report / CSV export
       +--> analytics dashboard
       +--> human review queue and follow-up notes
The workflow is intentionally designed to assist human review, not make an automated employment decision. The skill vocabulary and aliases are defined in app/tools.py and can be extended with documented terms. Matching is heuristic, not a validated assessment of competence.
Tests and evaluation
python -m pytest tests/ -q
python -m eval.run_golden
python -m eval.run_stage3
The test suite includes golden examples for supported and missing skills, negated claims, and an instruction-injection example. The Stage 3 evaluation includes fictional scenarios for Data Analyst, Python API Developer, and Frontend Developer roles.

eval/stage3_results.json contains the results of the latest locally run Stage 3 evaluation if you generate and commit it. Treat results as reproducible development checks, not evidence of hiring validity. Run all three commands again before submission and report the actual results rather than a hardcoded pass rate.
Repository guide
app/                  Streamlit UI, workflow, extraction, persistence, reports
app/tools.py          Skill vocabulary and evidence extraction helpers
data/demo/            Fictional jobs and resumes
data/seed_db.py        Starter database/demo initialization
data/seed_demo.py      Synthetic review records for dashboard demonstration
eval/                 Golden cases and evaluation runner
tests/                Automated checks
docs/screenshots/     Actual application screenshots (add before submission)
.streamlit/           Streamlit theme configuration
requirements.txt      Python dependencies
.env.example          Placeholder configuration (no secrets)
README.md             Project overview and setup
Some directories or optional files may differ in your local checkout; commit only files that actually exist.
Data handling and limitations
- Synthetic data only: All demonstration candidate records must be fictional.
- Local persistence: The MVP stores candidate references and extracted evidence in a local SQLite database rather than storing complete uploaded resume text. The database is excluded from Git.
- Limited matching: Vocabulary-based extraction can miss synonyms, misread negations, or confuse a mention with demonstrated experience.
- No automated hiring: Review states and notes are administrative follow-ups, not hiring recommendations or decisions.
- Not production ready: Authentication, multi-user permissions, consent and retention controls, OCR, security hardening, and independent validation are not implemented.
- Experimental modules: Persistent production RAG and production LLM extraction are not part of the validated core workflow.
Future improvements
Potential next steps include a broader validated skill ontology, stronger contextual and negation handling, independently evaluated evidence extraction, permission controls, and production-ready deployment practices.
HireFlow AI is a capstone demonstration of explainable document review and human oversight—not a system for making employment decisions.
