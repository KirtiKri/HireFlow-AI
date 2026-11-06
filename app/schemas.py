from typing import TypedDict

class ReviewState(TypedDict, total=False):
    job_description: str
    job_id: int
    candidate_name: str
    resume_text: str
    required_skills: list[str]
    observed_skills: list[str]
    supported_skills: list[str]
    missing_skills: list[str]
    evidence: dict[str, str]
    retrieved_evidence: list[dict]
    notes: list[str]
    status: str
    trace: list[str]
    review_id: int
    use_rag: bool
    document_id: str
