"""Extract supported skill mentions; optional LLM never bypasses evidence checks."""
import os
from app.tools import find_skills
from app.validation import verified_evidence

def extract_resume_skills(resume_text: str) -> dict:
    mode = os.getenv("EXTRACTION_MODE", "rules").lower()
    notes = []
    if mode == "groq":
        try:
            from app.llm import extract_with_llm
            proposed = [s.lower().strip() for s in extract_with_llm(resume_text)]
            notes.append("Groq proposed skills; deterministic evidence validation applied")
        except Exception as exc:
            # No silent switch: record the failure and use conservative fallback.
            proposed = find_skills(resume_text)
            notes.append(f"LLM unavailable ({type(exc).__name__}); rules fallback")
    else:
        proposed = find_skills(resume_text)
        notes.append("Rules baseline")
    evidence = verified_evidence(resume_text, sorted(set(proposed)))
    return {"observed_skills": sorted(evidence), "evidence": evidence, "notes": notes}

def compare_requirements(required: list[str], observed: list[str]) -> dict:
    return {"supported_skills": sorted(set(required) & set(observed)),
            "missing_skills": sorted(set(required) - set(observed))}
