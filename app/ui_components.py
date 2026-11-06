"""Shared page copy and readable evidence display."""
import json
import streamlit as st

def intro(kicker, title, description):
    st.markdown(f'<div class="eyebrow">{kicker}</div>', unsafe_allow_html=True)
    st.title(title)
    st.write(description)

def explain_steps():
    st.markdown('**How it works**')
    st.markdown('1. **Choose a job** — tell the system which requirements to check.\n'
                '2. **Provide a resume** — upload a document or use a fictional example.\n'
                '3. **Analyze evidence** — review cited text and missing information.\n'
                '4. **Add a human note** — record what needs further verification.')

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
