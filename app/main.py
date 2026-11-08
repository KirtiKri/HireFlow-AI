"""HireFlow guided evidence review. Run: python -m streamlit run app/main.py"""
import json
from pathlib import Path
import streamlit as st
from app.database import init_db, add_job, get_jobs, get_reviews, add_review
from app.document import extract_text
from app.graph import graph
from app.review_actions import init_actions, get_action, save_action
from app.styles import apply_styles
from app.evidence_report import render_evidence_report, render_trace
from app.ui_components import intro, explain_steps, show_result
from app.charts import review_activity_chart, review_status_chart, requirements_chart

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
    st.subheader('Review analytics')
    activity_col, status_col = st.columns(2, gap='large')
    with activity_col:
        st.markdown('#### Document review activity')
        fig = review_activity_chart(reviews)
        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info('Run a sample review to see activity.')
    with status_col:
        st.markdown('#### Human follow-up status')
        fig = review_status_chart(reviews, get_action)
        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info('Human review statuses will appear here.')
    st.markdown('#### Requirements with documented evidence')
    fig = requirements_chart(reviews)
    if fig is not None:
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info('Analyze sample resumes to populate this chart.')
    st.divider()
    st.subheader('Recent activity')
    if reviews:
        rows = [{'Review': f"#{r['id']}", 'Candidate reference':r['candidate_name'],
                 'Job':job_lookup.get(r['job_id'], {}).get('title','Archived job'),
                 'Human follow-up':get_action(r['id'])['state'].replace('_',' ').title()} for r in reviews[:6]]
        st.dataframe(rows, hide_index=True, use_container_width=True)
    else:
        st.info('No reviews yet. Select “Start guided review” to create your first one.')

elif st.session_state.page == 'Manage jobs':
    intro('WORKSPACE / JOBS', 'Manage job descriptions',
          'Save the role requirements you want to compare with resume evidence.')
    example_names = ['Blank job'] + [j['title'] for j in DEMO_JOBS]
    chosen = st.selectbox('Start with', example_names)
    sample = next((j for j in DEMO_JOBS if j['title'] == chosen), None)
    with st.form('create_job'):
        title = st.text_input('Job title', value=sample['title'] if sample else '')
        description = st.text_area('Required skills and job description',
                                   value=sample['description'] if sample else '', height=180)
        submitted = st.form_submit_button('Save job description', type='primary')
    if submitted:
        try:
            job_id = add_job(title, description)
            st.session_state.active_job = job_id
            st.success(f'Job saved as #{job_id}. You can now use it in Start a review.')
        except ValueError as exc:
            st.error(str(exc))
    st.subheader('Saved jobs')
    if jobs:
        st.dataframe([{'ID':j['id'],'Job title':j['title'],'Created':j['created_at']} for j in jobs],
                     hide_index=True, use_container_width=True)
    else:
        st.info('No jobs saved yet. Select a sample above to begin.')

elif st.session_state.page == 'Start a review':
    intro('WORKSPACE / GUIDED REVIEW', 'Review a resume',
          'Follow three steps. You can use a ready-made example or upload your own fictional document.')
    st.markdown('### Step 1 of 3 — Select the job')
    mode = st.radio('Job source', ['Use a sample job', 'Choose a saved job'], horizontal=True)
    if mode == 'Use a sample job':
        sample_job = st.selectbox('Choose a role', DEMO_JOBS, format_func=lambda j:j['title'])
        st.caption('The sample job will be saved automatically when you run the review.')
        job_description = sample_job['description']
        selected_job_id = None
    elif jobs:
        selected_job = st.selectbox('Saved job', jobs, format_func=lambda j:f"{j['title']} (#{j['id']})")
        job_description = selected_job['description']
        selected_job_id = selected_job['id']
    else:
        st.warning('No saved jobs. Select a sample job or create one in Manage jobs.')
        st.stop()
    with st.expander('Read the job requirements'):
        st.write(job_description)
    st.divider()
    st.markdown('### Step 2 of 3 — Provide a resume')
    source = st.radio('Resume source', ['Try a fictional candidate', 'Upload a resume'], horizontal=True)
    if source == 'Try a fictional candidate':
        person = st.selectbox('Choose a candidate example', DEMO_RESUMES, format_func=lambda x:x['label'])
        candidate_ref = person['label'].split(' — ')[0] + ' (DEMO)'
        resume_text = person['text']
        with st.expander('Preview fictional resume', expanded=True):
            st.text(resume_text)
    else:
        candidate_ref = st.text_input('Candidate reference (use a fictional ID)', placeholder='e.g. DEMO-014')
        uploaded = st.file_uploader('Choose a resume (PDF, DOCX or TXT)', type=['pdf','docx','txt'])
        resume_text = None
        if uploaded is not None:
            try:
                resume_text = extract_text(uploaded.name, uploaded.getvalue())
                st.success(f'{uploaded.name} was read successfully.')
                with st.expander('Preview extracted text'):
                    st.text(resume_text[:6000])
            except Exception as exc:
                st.error(f'Could not read document: {exc}')
    st.divider()
    st.markdown('### Step 3 of 3 — Analyze the evidence')
    with st.expander('Advanced settings (optional)'):
        use_rag = st.checkbox('Use semantic evidence retrieval', value=False,
                              help='Indexes the document in ChromaDB; may take longer on first use.')
        st.caption('The system always requires a human reviewer. Semantic search adds supporting passages, not an automated hiring decision.')
    if st.button('Analyze resume', type='primary', disabled=not resume_text or not candidate_ref.strip(), use_container_width=True):
        try:
            with st.spinner('Reading evidence and running the review workflow...'):
                if selected_job_id is None:
                    # Reuse an identical saved sample job instead of duplicating on each run.
                    match = next((j for j in get_jobs() if j['title'] == sample_job['title'] and j['description'] == job_description), None)
                    job_id = match['id'] if match else add_job(sample_job['title'], job_description)
                else:
                    job_id = selected_job_id
                result = graph.invoke({'job_id':job_id, 'candidate_name':candidate_ref.strip(),
                                       'job_description':job_description, 'resume_text':resume_text,
                                       'trace':[], 'use_rag':use_rag,
                                       'document_id':f'demo-job-{job_id}-review-{len(get_reviews())+1}'})
                review_id = add_review(job_id, candidate_ref.strip(), result.get('observed_skills', []),
                                       result.get('supported_skills', []), result.get('missing_skills', []),
                                       result.get('evidence', {}), result['status'])
            st.session_state.latest_result = result
            st.session_state.latest_review_id = review_id
        except Exception as exc:
            st.error(f'Analysis failed: {exc}')
    if st.session_state.get('latest_result'):
        st.divider()
        show_result(st.session_state.latest_result, st.session_state.latest_review_id)
        render_evidence_report(st, st.session_state.latest_result, st.session_state.latest_review_id)
        render_trace(st, st.session_state.latest_result)
        st.button('Open human review queue', on_click=navigate_to,
                  args=('Human review queue',), key='open_human_review')

elif st.session_state.page == 'Human review queue':
    intro('WORKSPACE / HUMAN OVERSIGHT', 'Human review queue',
          'Inspect saved evidence and record what a person needs to verify. This is not an approval or rejection system.')
    if not reviews:
        st.info('No reviews yet. Run a fictional example from Start a review first.')
        st.button('Start a review', on_click=navigate_to,
                  args=('Start a review',), key='queue_start_review')
       
    else:
        rows = [{'Review':r['id'], 'Candidate reference':r['candidate_name'],
                 'Job':job_lookup.get(r['job_id'],{}).get('title','Archived job'),
                 'Follow-up':get_action(r['id'])['state'].replace('_',' ').title()} for r in reviews]
        st.dataframe(rows, hide_index=True, use_container_width=True)
        chosen = st.selectbox('Open a saved review', reviews,
                              format_func=lambda r:f"#{r['id']} — {r['candidate_name']}")
        st.subheader('Recorded evidence')
        left,right = st.columns(2)
        with left:
            st.markdown('**Requirements evidenced**')
            st.write(', '.join(json.loads(chosen['supported_skills'])) or 'None identified')
        with right:
            st.markdown('**Requirements not evidenced**')
            st.write(', '.join(json.loads(chosen['missing_skills'])) or 'None identified')
        evidence = json.loads(chosen['evidence_json'])
        with st.expander('View supporting passages'):
            if evidence:
                for skill, passage in evidence.items():
                    st.markdown(f'**{skill.title()}**')
                    st.text(passage)
            else:
                st.write('No evidence excerpts saved.')
        render_evidence_report(st, chosen, chosen['id'])
        action = get_action(chosen['id'])
        with st.form(f"human_action_{chosen['id']}"):
            options = {'Pending':'pending','Reviewed':'reviewed','Needs more information':'needs_more_information'}
            current = next((k for k,v in options.items() if v == action['state']), 'Pending')
            status = st.selectbox('Human follow-up status', list(options), index=list(options).index(current))
            note = st.text_area('Reviewer note', value=action['reviewer_note'], max_chars=2000,
                                placeholder='Example: Ask for a portfolio link demonstrating Docker experience.')
            if st.form_submit_button('Save reviewer note', type='primary'):
                save_action(chosen['id'], options[status], note)
                st.success('Human follow-up note saved.')
                st.rerun()
        st.caption('Administrative review statuses do not represent hiring, interview, or rejection decisions.')
