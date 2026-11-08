# HireFlow — guarded evidence chat update

This is an **incremental patch**, not a full replacement repository. Install the earlier Ask the Evidence chatbot first if it is not already installed.

## Copy into your existing project

- Replace `app/evidence_chat.py`.
- Add `app/chat_guardrails.py`.
- Add `tests/test_chat_guardrails.py`.
- Keep the earlier `app/main.py` chatbot integration and `tests/test_evidence_chat.py` unchanged.

## Add to your main README

### Optional evidence chat and guardrails

The *Ask the Evidence* assistant is scoped to saved fictional review excerpts. Input checks reject empty/oversized questions, obvious prompt-override attempts, and direct hiring/ranking requests. Conversation history is bounded and role-filtered. Model output must be valid JSON with exactly `answer` and `citations`, referencing existing excerpt IDs; invalid responses fail closed. The UI displays verbatim saved excerpts alongside citations for human verification. These are **heuristic guardrails**: valid citation IDs do not prove a claim is supported, and prompt injection cannot be completely prevented. The assistant must not be used for real hiring decisions.

The chat is optional: without `GROQ_API_KEY` and `LLM_MODEL` in local `.env`, the review workflow remains available. Never commit secrets or real resumes.

## Requirements

No new dependencies: the existing `requirements.txt` already includes `groq`, `python-dotenv`, and `pytest`.

## Verify

```powershell
python -m pytest -q tests/test_evidence_chat.py tests/test_chat_guardrails.py
python -m pytest -q
python -m streamlit run app/main.py
```

**Limitations:** Input pattern checks are not exhaustive; output citation checks validate IDs and structure, not semantic entailment. Reviewers must verify all conclusions against original documents.
