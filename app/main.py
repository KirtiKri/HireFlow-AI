"""HireFlow guided evidence review. Run: python -m streamlit run app/main.py"""
import json
from pathlib import Path
import streamlit as st
from app.database import init_db, add_job, get_jobs, get_reviews, add_review
from app.document import extract_text
from app.graph import graph
from app.review_actions import init_actions, get_action, save_action
from app.styles import apply_styles
from app.ui_components import intro, explain_steps, show_result
from app.charts import (
    review_activity_chart,
    review_status_chart,
    requirements_chart,
)

def navigate_to(destination):
    st.session_state["page"] = destination

ROOT = Path(__file__).resolve().parent.parent
DEMO_JOBS = json.loads((ROOT / 'data/demo/jobs.json').read_text(encoding='utf-8'))
DEMO_RESUMES = json.loads((ROOT / 'data/demo/resumes.json').read_text(encoding='utf-8'))
st.set_page_config(page_title='HireFlow | Recruitment Workspace', layout='wide', initial_sidebar_state='expanded')
apply_styles()
init_db()
init_actions()

if 'page' not in st.session_state:
    st.session_state.page = 'Home'
if 'active_job' not in st.session_state:
    st.session_state.active_job = None

with st.sidebar:
    st.markdown('## HIREFLOW')
    st.caption('RECRUITMENT EVIDENCE WORKSPACE')
    st.divider()
    st.radio('Navigate', ['Home', 'Start a review', 'Manage jobs', 'Human review queue'], key='page')
    st.divider()
    st.caption('DEMONSTRATION ENVIRONMENT')
    st.caption('Fictional candidate data only. Human judgment is required for all employment decisions.')

jobs = get_jobs()
reviews = get_reviews()
job_lookup = {int(j['id']): j for j in jobs}

if st.session_state.page == 'Home':
    intro('WORKSPACE / OVERVIEW', 'Welcome to HireFlow',
          'Review what a resume actually says against a job description. No technical setup is needed to try a sample.')
    a, b, c = st.columns(3)
    a.metric('Job descriptions', len(jobs))
    b.metric('Document reviews', len(reviews))
    c.metric('Awaiting human notes', sum(get_action(r['id'])['state'] == 'pending' for r in reviews))
    st.divider()
    left, right = st.columns([1.5, 1], gap='large')
    with left:
        st.subheader('Try your first document review')
        st.write('Use a fictional candidate and a sample job. You can complete the demonstration in under two minutes.')
        st.button('Start guided review', type='primary', use_container_width=True,
                  on_click=navigate_to, args=('Start a review',), key='home_start_review')
        st.markdown('#### What the system will show')
        st.write('Requirements found in the resume, supporting passages, information not evidenced, and a record for a human reviewer.')
    with right:
        explain_steps()
       
    st.divider()
    st.subheader("Review analytics")

    left_chart, right_chart = st.columns(2, gap="large")

    with left_chart:
        st.markdown("#### Document review activity")
        fig = review_activity_chart(reviews)
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Run a sample review to see activity.")

    with right_chart:
        st.markdown("#### Human follow-up status")
        fig = review_status_chart(reviews, get_action)
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Human review statuses will appear here.")

    st.markdown("#### Requirements with documented evidence")
    fig = requirements_chart(reviews)

    if fig:
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Analyze sample resumes to populate this chart.")

elif st.session_state.page == 'Manage jobs':
    intro('WORKSPACE / JOBS', 'Manage job descriptions',
          'Save the role requirements you want to compare with resume evidence.')