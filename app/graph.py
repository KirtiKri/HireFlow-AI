"""Human-in-the-loop evidence review workflow. No automated hiring decisions."""
from langgraph.graph import StateGraph, START, END
from app.schemas import ReviewState
from app.agents import extract_resume_skills, compare_requirements
from app.tools import find_skills

def requirements_node(state: ReviewState) -> dict:
    return {"required_skills": find_skills(state.get("job_description", "")) if state.get("job_description") else state.get("required_skills", []),
            "trace": state.get("trace", []) + ["requirements"]}

def extract_node(state: ReviewState) -> dict:
    result = extract_resume_skills(state.get("resume_text", ""))
    return {**result, "trace": state.get("trace", []) + ["extract"]}

def retrieve_node(state: ReviewState) -> dict:
    if not state.get("use_rag", False):
        return {"retrieved_evidence": [], "trace": state.get("trace", []) + ["retrieve_skipped"]}
    from app.rag import index_document, search_document
    doc_id = state.get("document_id", "demo")
    try:
        index_document(doc_id, state.get("resume_text", ""))
        results = []
        for skill in state.get("required_skills", []):
            for hit in search_document(doc_id, skill, top_k=1):
                results.append({"skill_query": skill, **hit})
        return {"retrieved_evidence": results, "trace": state.get("trace", []) + ["retrieve"]}
    except Exception as exc:
        return {"retrieved_evidence": [],
                "notes": state.get("notes", []) + [f"Retrieval failed: {type(exc).__name__}"],
                "trace": state.get("trace", []) + ["retrieve_failed"]}

def compare_node(state: ReviewState) -> dict:
    result = compare_requirements(state.get("required_skills", []), state.get("observed_skills", []))
    return {**result, "status": "human_review_required", "trace": state.get("trace", []) + ["compare"]}

def insufficient_node(state: ReviewState) -> dict:
    return {"supported_skills": [], "missing_skills": state.get("required_skills", []),
            "status": "insufficient_evidence", "trace": state.get("trace", []) + ["insufficient_evidence"]}

def route(state: ReviewState) -> str:
    return "compare" if state.get("observed_skills") and state.get("required_skills") else "insufficient"

builder = StateGraph(ReviewState)
for name, fn in [("requirements", requirements_node), ("extract", extract_node),
                 ("retrieve", retrieve_node), ("compare", compare_node),
                 ("insufficient", insufficient_node)]:
    builder.add_node(name, fn)
builder.add_edge(START, "requirements")
builder.add_edge("requirements", "extract")
builder.add_edge("extract", "retrieve")
builder.add_conditional_edges("retrieve", route, {"compare": "compare", "insufficient": "insufficient"})
builder.add_edge("compare", END)
builder.add_edge("insufficient", END)
graph = builder.compile()
