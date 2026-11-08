"""Shared page copy and readable evidence display."""
import json
from html import escape
import streamlit as st

def intro(kicker, title, description):
    st.markdown(f'<div class="eyebrow">{escape(str(kicker))}</div>', unsafe_allow_html=True)
    st.title(title)
    st.write(description)

def explain_steps():
    st.markdown('''<div class="hf-help-steps">
    <div class="hf-help-intro">THE FIELD GUIDE <span>✳</span></div>
    <p>Four moves. One clearer picture.</p>
    <div class="hf-help-item"><b>01</b><div><strong>Choose the role</strong><small>Start with the job requirements.</small></div></div>
    <div class="hf-help-item"><b>02</b><div><strong>Add a document</strong><small>Use a fictional resume or upload one.</small></div></div>
    <div class="hf-help-item"><b>03</b><div><strong>Find the passages</strong><small>See evidence and unanswered questions.</small></div></div>
    <div class="hf-help-item"><b>04</b><div><strong>Human follow-up</strong><small>Record what needs verification.</small></div></div>
    </div>''', unsafe_allow_html=True)


def show_result(result, review_id):
    st.success(f'Document review #{review_id} saved. Human assessment is still required.')
    left, right = st.columns(2, gap='large')
    with left:
        st.subheader('Requirements evidenced')
        supported = result.get('supported_skills', [])
        st.write(', '.join(supported) if supported else 'No requirements evidenced by this analysis.')
    with right:
        st.subheader('Not evidenced in this resume')
        missing = result.get('missing_skills', [])
        st.write(', '.join(missing) if missing else 'No listed requirements left unmatched.')
    st.subheader('Supporting resume passages')
    evidence = result.get('evidence', {})
    if evidence:
        for skill, passage in evidence.items():
            st.markdown(f'**{skill.title()}**')
            st.text(passage)
    else:
        st.info('No validated excerpts were found. This does not establish lack of ability.')
    with st.expander('Technical details — optional'):
        st.write('**Workflow steps:**', ' → '.join(result.get('trace', [])))
        st.write('**Analysis notes:**', result.get('notes', []))
        st.write('**Semantic retrieval:**')
        st.json(result.get('retrieved_evidence', []))
    st.caption('Skill mentions are not proof of proficiency. Never use this report as an automatic employment decision.')


def motion_hero():
    """Editorial paper-collage illustration: static HTML/CSS, no external requests."""
    st.markdown('''<section class="hf-atelier-hero" aria-label="HireFlow evidence studio">
      <div class="hf-atelier-grain" aria-hidden="true"></div>
      <div class="hf-atelier-copy">
        <div class="hf-atelier-topline"><span class="hf-atelier-star">✳</span> THE EVIDENCE ATELIER <span class="hf-atelier-no">EST. 2026 / 001</span></div>
        <h1>Look closer.<br><em>See clearer.</em></h1>
        <p>Resumes tell stories. We help you find the passages behind the claims — and the questions worth asking next.</p>
        <div class="hf-atelier-foot"><span>✦ SOURCE-BASED FINDINGS</span><span>✦ FICTIONAL DEMO DATA</span></div>
      </div>
      <div class="hf-atelier-scene" aria-hidden="true">
        <div class="hf-atelier-sun"></div><div class="hf-atelier-halo"></div>
        <div class="hf-atelier-back-paper"><span>DOCUMENT<br>STUDY / 01</span><div class="hf-atelier-back-line"></div><div class="hf-atelier-back-line short"></div></div>
        <div class="hf-atelier-paper hf-chat-paper">
          <div class="hf-paper-top"><span>✳</span> ASK THE EVIDENCE <span>AI / 001</span></div>
          <div class="hf-chat-title">A question.<br><em>A clearer answer.</em></div>
          <div class="hf-chat-bubble hf-chat-question">What supports Python experience?</div>
          <div class="hf-chat-bubble hf-chat-answer"><strong>✦ Evidence found</strong><br>Python is mentioned in a project. <span class="hf-chat-cite">[E1]</span></div>
          <div class="hf-chat-bubble hf-chat-followup">◇ What still needs clarification?</div>
          <div class="hf-chat-foot">✧ GROUNDED ANSWERS &nbsp; · &nbsp; HUMAN REVIEW</div>
        </div>
        <div class="hf-atelier-label one">✦ ASK THE EVIDENCE</div>
        <div class="hf-atelier-label two">✳ VERIFY THE SOURCE</div>
        <div class="hf-atelier-flower">✿</div>
        <div class="hf-scene-human-tag">✦ HUMAN-LED</div>
        <svg class="hf-atelier-arrow" viewBox="0 0 160 100" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M5 10 C35 75 90 10 144 74" stroke="#1C453C" stroke-width="3" stroke-dasharray="7 8" stroke-linecap="round"/><path d="M127 72 L145 76 L145 57" stroke="#1C453C" stroke-width="3" stroke-linecap="round"/></svg>
      </div>
    </section>''', unsafe_allow_html=True)


def evidence_explorer(st, evidence, supported, missing, *, key_prefix="evidence"):
    """Interactive, source-grounded requirement explorer; no scoring or ranking."""
    supported = list(dict.fromkeys(str(x) for x in (supported or [])))
    missing = list(dict.fromkeys(str(x) for x in (missing or [])))
    evidence = evidence if isinstance(evidence, dict) else {}
    st.markdown('<div class="hf-section-label">EVIDENCE EXPLORER <span>SELECT A REQUIREMENT TO INSPECT</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="hf-explorer-banner"><span class="hf-explorer-spark">✦</span><div><strong>Follow the evidence</strong><small>Every finding is a document mention, not proof of proficiency or a hiring recommendation.</small></div><span class="hf-explorer-orb">◎</span></div>', unsafe_allow_html=True)
    options = [("Documented", x) for x in supported] + [("Not evidenced", x) for x in missing]
    if not options:
        st.info('No requirements were identified for this review.')
        return
    chosen = st.selectbox('Explore requirement', options, format_func=lambda item: f'{"✓" if item[0] == "Documented" else "◇"}  {item[1].title()} · {item[0]}', key=f'{key_prefix}_requirement')
    status, skill = chosen
    if status == 'Documented':
        passage = next((v for k,v in evidence.items() if str(k).lower() == skill.lower()), None)
        st.markdown('<div class="hf-evidence-label hf-evidence-found">✓ DOCUMENTED MENTION</div>', unsafe_allow_html=True)
        if passage:
            st.markdown('<div class="hf-passage-heading">SOURCE PASSAGE</div>', unsafe_allow_html=True)
            st.info(str(passage))
        else:
            st.warning('A mention was recorded, but no supporting passage is stored for this requirement. Verify the source manually.')
    else:
        st.markdown('<div class="hf-evidence-label hf-evidence-gap">◇ NOT EVIDENCED</div>', unsafe_allow_html=True)
        st.warning('No supporting mention was identified in the analyzed text. This does not mean the candidate lacks the skill.')
    st.caption('Human verification is required before any employment-related action.')


# Stage 3 presentation components. All user-provided text is rendered with Streamlit widgets.
def review_stage_hero():
    """Decorative illustration; no fabricated review results."""
    st.markdown("""<section class="hf-review-hero" aria-label="Evidence review studio">
      <div class="hf-rh-copy"><span class="hf-rh-kicker">✦ THE EVIDENCE STUDIO / 03 STAGES</span>
      <h2>From document to <em>discovery.</em></h2>
      <p>Bring a role and a fictional resume together. Explore what is documented, identify what needs clarification, and hand the findings to a human reviewer.</p>
      <div class="hf-rh-pills"><span>◈ Inspect</span><span>✧ Trace</span><span>◎ Verify</span></div></div>
      <div class="hf-rh-scene" aria-hidden="true"><div class="hf-rh-halo"></div>
        <div class="hf-rh-sheet"><div class="hf-rh-sheet-head">▤ &nbsp; DOCUMENT / 001 <span>✦</span></div>
          <div class="hf-rh-avatar"></div><div class="hf-rh-line long"></div><div class="hf-rh-line"></div>
          <div class="hf-rh-highlight">✓ &nbsp; Evidence passage</div><div class="hf-rh-line short"></div>
          <div class="hf-rh-highlight muted">◇ &nbsp; Follow-up needed</div></div>
        <div class="hf-rh-orbit one">✧</div><div class="hf-rh-orbit two">◈</div>
        <div class="hf-rh-tag">✦ &nbsp; Human-led analysis</div>
      </div></section>""", unsafe_allow_html=True)


def review_journey(active):
    """A section locator, not a live processing indicator."""
    names = [('01', 'Select a role'), ('02', 'Add a resume'), ('03', 'Explore evidence')]
    blocks = []
    for number, name in names:
        state = 'active' if int(number) == active else ('done' if int(number) < active else 'upcoming')
        blocks.append(f'<div class="hf-j-item {state}"><span class="hf-j-num">{number}</span><span>{name}</span></div>')
    st.markdown('<div class="hf-journey" aria-label="Review stages">' + '<span class="hf-j-separator">✦</span>'.join(blocks) + '</div>', unsafe_allow_html=True)


def workflow_trace_visual(trace):
    """Show only actual trace entries returned by LangGraph."""
    st.markdown('<div class="hf-section-label">WORKFLOW RECORD <span>ACTUAL EXECUTION TRACE</span></div>', unsafe_allow_html=True)
    if not trace:
        st.info('No workflow trace was returned for this review.')
        return
    st.caption('These stages come from the completed graph result; this is not a live node animation.')
    cols = st.columns(min(len(trace), 4))
    for i, item in enumerate(trace):
        with cols[i % len(cols)]:
            st.markdown('<div class="hf-trace-card"><span class="hf-trace-check">✓</span><small>STAGE '+str(i+1).zfill(2)+'</small><strong>'+escape(str(item))+'</strong></div>', unsafe_allow_html=True)


def queue_status_strip(reviews, get_action):
    """Display actual persisted human follow-up counts, not hiring decisions."""
    states = [get_action(r['id']).get('state', 'pending') for r in reviews]
    cards = [('◷', 'Pending', states.count('pending'), 'amber'),
             ('◇', 'Needs information', states.count('needs_more_information'), 'coral'),
             ('✓', 'Reviewed', states.count('reviewed'), 'mint')]
    st.markdown('<div class="hf-section-label">HUMAN OVERSIGHT <span>ADMINISTRATIVE FOLLOW-UP ONLY</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="hf-queue-strip">' + ''.join(
        f'<div class="hf-queue-stat {tone}"><span class="hf-queue-symbol">{icon}</span><strong>{count}</strong><small>{label}</small></div>'
        for icon,label,count,tone in cards) + '</div>', unsafe_allow_html=True)
