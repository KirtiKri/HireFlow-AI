"""Explainable, non-decisional evidence reports for HireFlow."""
import csv
import io
import json
from collections.abc import Mapping
from html import escape

from app.compat import stretch


def _as_list(value):
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except (TypeError, ValueError):
            return []
    return [str(x) for x in value] if isinstance(value, list) else []


def _as_evidence(value):
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except (TypeError, ValueError):
            return {}
    return value if isinstance(value, Mapping) else {}


def _passage(value):
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, Mapping):
        for key in ('passage', 'text', 'snippet', 'quote', 'evidence'):
            if isinstance(value.get(key), str):
                return value[key].strip()
    if isinstance(value, list):
        return ' | '.join(filter(None, (_passage(v) for v in value)))
    return ''


def normalize_review(review):
    """Read a graph result OR a saved database row into one consistent shape.

    Returns ``supported``, ``missing`` and ``observed`` skill lists, plus
    ``passages`` mapping a casefolded skill name to its saved passage text.
    """
    review = review if isinstance(review, Mapping) else {}
    evidence = _as_evidence(review.get('evidence_json', review.get('evidence', {})))
    return {
        'supported': _as_list(review.get('supported_skills', [])),
        'missing': _as_list(review.get('missing_skills', [])),
        'observed': _as_list(review.get('observed_skills', [])),
        'passages': {str(k).casefold(): _passage(v) for k, v in evidence.items()},
    }


def build_evidence_rows(review):
    """Only label a skill evidenced when saved evidence text exists."""
    supported = _as_list(review.get('supported_skills', []))
    missing = _as_list(review.get('missing_skills', []))
    evidence = _as_evidence(review.get('evidence_json', review.get('evidence', {})))
    lookup = {str(k).casefold(): _passage(v) for k, v in evidence.items()}
    skills = list(dict.fromkeys(supported + missing))
    rows = []
    for skill in skills:
        passage = lookup.get(skill.casefold(), '')
        if skill in supported and passage:
            finding = 'Evidence passage recorded'
        elif skill in supported:
            finding = 'Mention flagged; passage unavailable'
        else:
            finding = 'Not evidenced in saved review'
        rows.append({'Requirement': skill, 'Finding': finding,
                     'Saved passage': passage or '—',
                     'Human follow-up': ('Verify context, recency, and depth' if passage
                                         else 'Request supporting examples or clarification')})
    return rows


def report_csv(rows):
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=['Requirement', 'Finding', 'Saved passage', 'Human follow-up'])
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode('utf-8-sig')


def render_evidence_report(st, review, review_id=None):
    rows = build_evidence_rows(review)
    st.markdown('<p class="hf-sec">Explainable evidence report</p>'
                '<p class="hf-sec-sub">Evidence indicates document mentions, not verified competence '
                'or hiring suitability.</p>', unsafe_allow_html=True)
    if not rows:
        st.info('No parsed requirements were saved for this review.')
        return
    st.dataframe(rows, hide_index=True, **stretch(st.dataframe))
    st.download_button('Download evidence report (CSV)', data=report_csv(rows),
                       file_name=f'hireflow_evidence_review_{review_id or "current"}.csv',
                       mime='text/csv', key=f'evidence_csv_{review_id or "current"}')
    st.markdown('<div class="hf-callout"><b>Reading this report.</b> Missing evidence is not proof '
                'that a candidate lacks a skill. A human reviewer must verify all findings.</div>',
                unsafe_allow_html=True)


_TRACE_LABELS = {
    'requirements': 'Requirements identified from the job description',
    'extract': 'Skills and excerpts extracted from the resume',
    'retrieve': 'Semantic retrieval of supporting passages',
    'retrieve_skipped': 'Semantic retrieval skipped (not enabled)',
    'retrieve_failed': 'Semantic retrieval failed (recorded as a note)',
    'compare': 'Requirements compared with resume evidence',
    'insufficient_evidence': 'Insufficient evidence: no comparison was possible',
}


def render_trace(st, result):
    trace = result.get('trace', []) if isinstance(result, Mapping) else []
    st.markdown('<p class="hf-sec">Workflow trace</p>'
                '<p class="hf-sec-sub">The LangGraph steps that ran for this review, in order.</p>',
                unsafe_allow_html=True)
    if not trace:
        st.info('Execution trace is not available for this review.')
        return
    items = ''.join(
        f'<li><span class="hf-tl-n">{i}</span>'
        f'<b>{escape(str(step).replace("_", " ").title())}</b>'
        f'<span>{escape(_TRACE_LABELS.get(str(step), "Workflow step"))}</span></li>'
        for i, step in enumerate(trace, start=1))
    st.markdown(f'<div class="hf-panel" style="padding:18px 20px"><ul class="hf-tl">{items}</ul></div>',
                unsafe_allow_html=True)
