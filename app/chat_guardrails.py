"""Conservative input/output validation for the optional evidence assistant.

These deterministic checks reduce risk; they cannot prove semantic entailment.
"""
import re

MAX_QUESTION = 600
MAX_ANSWER = 1500
MAX_HISTORY = 4
MAX_SOURCE_CHARS = 1100

# Only block clear attempts to override instructions, not benign questions about injections.
INJECTION = re.compile(r"(?i)(ignore|override|disregard|forget)\s+(all\s+)?(previous|prior|system|developer)\s+(instructions|rules|messages)|(?:reveal|print|show)\s+(?:the\s+)?(?:system\s+prompt|api\s+key|secret\s+key)")
DECISION = re.compile(r"(?i)\b(?:should\s+(?:we|i)\s+hire|hire\s+or\s+reject|rank\s+(?:the\s+)?candidates?|best\s+candidate|reject\s+(?:this|the)\s+candidate|infer\s+(?:their|the)\s+(?:race|religion|gender|age|disability))\b")
DANGEROUS_OUTPUT = re.compile(r"(?i)\b(?:hire\s+(?:this|the)\s+candidate|reject\s+(?:this|the)\s+candidate|candidate\s+(?:should|must)\s+be\s+(?:hired|rejected)|(?:is|appears)\s+(?:male|female|pregnant|disabled))\b")

class GuardrailError(ValueError):
    pass


def validate_question(question):
    if not isinstance(question, str) or not question.strip() or len(question.strip()) > MAX_QUESTION:
        raise GuardrailError('Enter a question of 1–600 characters.')
    q = question.strip()
    if INJECTION.search(q):
        raise GuardrailError('Please ask about the saved evidence, not system instructions or secrets.')
    if DECISION.search(q):
        raise GuardrailError('HireFlow cannot rank candidates or make hiring decisions. Ask about documented evidence instead.')
    return q


def sanitize_history(history):
    result = []
    for msg in (history or [])[-MAX_HISTORY:]:
        if not isinstance(msg, dict) or msg.get('role') not in ('user', 'assistant'):
            continue
        content = msg.get('content', '')
        if not isinstance(content, str):
            continue
        result.append({'role': msg['role'], 'content': content[:700]})
    return result


def validate_response(data, sources):
    if not isinstance(data, dict) or set(data) != {'answer', 'citations'}:
        return None
    answer, citations = data['answer'], data['citations']
    if not isinstance(answer, str) or not answer.strip() or len(answer) > MAX_ANSWER:
        return None
    if not isinstance(citations, list) or len(citations) > 6 or any(not isinstance(c, str) for c in citations):
        return None
    valid = {s['id'] for s in sources}
    if any(c not in valid for c in citations) or DANGEROUS_OUTPUT.search(answer):
        return None
    # Citation IDs prove only source membership, NOT that an inference is true.
    # Show exact excerpts separately so users can verify claims themselves.
    return {'answer': re.sub(r'\[E\d+\]', '', answer).strip(),
            'citations': list(dict.fromkeys(citations))}
