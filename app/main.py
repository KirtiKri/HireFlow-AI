"""HireFlow guided evidence review. Run: python -m streamlit run app/main.py"""
import json
import hashlib
from pathlib import Path
from datetime import datetime, timedelta
import streamlit as st
from app.database import init_db, add_job, get_jobs, get_reviews, add_review
from app.document import extract_text
from app.multimodal import extract_visual_text
from app.graph import graph
from app.review_actions import init_actions, get_action, save_action
from app.styles import apply_styles
from app.evidence_chat import render_chat
from app.evidence_report import render_evidence_report, render_trace
from app.ui_components import intro, explain_steps, show_result, motion_hero, evidence_explorer, review_stage_hero, review_journey, workflow_trace_visual, queue_status_strip
from app.charts import review_activity_chart, review_status_chart, requirements_chart, skill_constellation_chart

def navigate_to(destination):
    st.session_state["page"] = destination

ROOT = Path(__file__).resolve().parent.parent
DEMO_JOBS = json.loads((ROOT / 'data/demo/jobs.json').read_text(encoding='utf-8'))
DEMO_RESUMES = json.loads((ROOT / 'data/demo/resumes.json').read_text(encoding='utf-8'))
st.set_page_config(page_title='HireFlow | Recruitment Workspace', layout='wide', initial_sidebar_state='expanded')
apply_styles()
st.markdown('''<div class="hf-global-header" role="banner">
  <div class="hf-global-brand"><span class="hf-global-monogram">H<span>✳</span></span>
    <span class="hf-global-title">HireFlow <em>AI</em><small>THE EVIDENCE ATELIER</small></span></div>
  <div class="hf-global-right"><span class="hf-header-squiggle">✳</span><span class="hf-header-copy">LOOK CLOSER. SEE CLEARER.</span><span class="hf-header-status"><i></i> LOCAL DEMO</span></div>
</div>''', unsafe_allow_html=True)
init_db()
init_actions()

if 'page' not in st.session_state:
    st.session_state.page = 'Home'
if 'active_job' not in st.session_state:
    st.session_state.active_job = None

with st.sidebar:
    st.markdown('''<div class="hf-rail-intro"><span class="hf-rail-index">✳ &nbsp; YOUR WORKSPACE</span><strong>Find your way <em>around.</em></strong><span>Explore the studio, one step at a time.</span></div>''', unsafe_allow_html=True)
    st.radio('Navigate', ['Home', 'Start a review', 'Manage jobs', 'Human review queue'],
             key='page', label_visibility='collapsed',
             format_func=lambda page: {
                 'Home': '⌂   Home',
                 'Start a review': '⌕   Start a review',
                 'Manage jobs': '▣   Manage jobs',
                 'Human review queue': '☑   Human review queue',
             }[page])
    st.markdown('<div class="hf-rail-guide-label">NEED A LITTLE GUIDANCE? <span>↘</span></div>', unsafe_allow_html=True)
    with st.expander('✦  How HireFlow works', expanded=False):
        explain_steps()
        st.caption('A missing mention means not evidenced, never that a person lacks a skill.')
    st.markdown('<div class="hf-sidebar-footer"><span class="hf-status-dot"></span> SANDBOX ENVIRONMENT<br><small>Fictional records · Human decisions only</small></div>', unsafe_allow_html=True)

jobs = get_jobs()
reviews = get_reviews()
job_lookup = {int(j['id']): j for j in jobs}

if st.session_state.page == 'Home':
    motion_hero()
    st.markdown('<div class="hf-editorial-rule"><span>01 / THE STUDIO</span><span>THE EVIDENCE, NOT THE ASSUMPTION</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="hf-editorial-heading"><div><small>YOUR WORKSPACE AT A GLANCE</small><h2>Good questions.<br><i>Better evidence.</i></h2></div><p>Explore saved roles, review documents, and record what still needs a human follow-up.</p></div>', unsafe_allow_html=True)
    a, b, c, d = st.columns(4, gap='medium')
    a.metric('Job descriptions', len(jobs), help='Saved job descriptions')
    b.metric('Evidence reviews', len(reviews), help='Reviews stored in SQLite')
    pending_count = sum(get_action(r['id'])['state'] == 'pending' for r in reviews)
    c.metric('Awaiting follow-up', pending_count, help='Human review action pending')
    d.metric('Reviewed by humans', sum(get_action(r['id'])['state'] == 'reviewed' for r in reviews), help='Administrative follow-up status')
    left, right = st.columns([1, 1], gap='medium')
    with left:
        st.button('✦  Start guided review', type='primary', use_container_width=True,
                  on_click=navigate_to, args=('Start a review',), key='home_start_review')
    with right:
        st.button('↗  Explore saved roles', use_container_width=True,
                  on_click=navigate_to, args=('Manage jobs',), key='home_manage_jobs')
    st.markdown('''
    <div style="margin:1.25rem 0 .6rem;padding:1.3rem 1.5rem;
      border:1px solid #B9D1BE;border-left:6px solid #356C52;
      border-radius:16px;background:linear-gradient(110deg,#E8F0E6,#FFF9EE);
      color:#173E34">
      <div style="font-size:.72rem;letter-spacing:.14em;font-weight:800;color:#47755D">NEW · GROUNDED AI ASSISTANT</div>
      <div style="font-family:Georgia,serif;font-size:1.65rem;font-weight:700;margin:.35rem 0">✦ Ask the Evidence</div>
      <div style="font-size:.96rem;line-height:1.6">Ask questions about saved resume evidence, inspect cited excerpts, and explore what still needs human clarification. Input and output guardrails help keep the assistant within scope.</div>
    </div>
    ''', unsafe_allow_html=True)
    if reviews:
        st.button('✦  Try Ask the Evidence on a saved review', type='primary',
                  use_container_width=True, key='home_try_evidence_chat',
                  on_click=navigate_to, args=('Human review queue',))
    else:
        st.caption('Run your first fictional review to unlock the evidence assistant.')
        st.button('✦  Create a review to try the assistant', type='primary',
                  use_container_width=True, key='home_create_chat_review',
                  on_click=navigate_to, args=('Start a review',))
    st.divider()
    st.markdown('<div class="hf-section-label">EVIDENCE UNIVERSE <span>FROM SAVED REVIEWS</span></div>', unsafe_allow_html=True)
    st.subheader('Skill constellation')
    st.caption('Each node represents a requirement with documented mentions across fictional reviews. Node size reflects mention frequency, not candidate quality.')
    constellation = skill_constellation_chart(reviews)
    if constellation is not None:
        st.plotly_chart(constellation, use_container_width=True)
    else:
        st.info('Run sample reviews to illuminate the skill constellation.')
    st.divider()
    st.markdown('<div class="hf-section-label">INSIGHTS / ANALYTICS</div>', unsafe_allow_html=True)
    st.subheader('Review analytics')
    filter_left, filter_right = st.columns([1, 1], gap='medium')
    with filter_left:
        period = st.selectbox('Time range', ['All time', 'Last 7 days', 'Last 30 days', 'Last 90 days'], key='analytics_period')
    with filter_right:
        role_options = ['All roles'] + sorted({j['title'] for j in jobs})
        selected_role = st.selectbox('Job role', role_options, key='analytics_role')
    analytics_reviews = list(reviews)
    if selected_role != 'All roles':
        matching_ids = {int(j['id']) for j in jobs if j['title'] == selected_role}
        analytics_reviews = [r for r in analytics_reviews if int(r['job_id']) in matching_ids]
    if period != 'All time':
        days = {'Last 7 days': 7, 'Last 30 days': 30, 'Last 90 days': 90}[period]
        cutoff = datetime.now() - timedelta(days=days)
        def within_range(review):
            try:
                return datetime.fromisoformat(str(review['created_at']).replace('Z', '+00:00')).replace(tzinfo=None) >= cutoff
            except (ValueError, TypeError):
                return False
        analytics_reviews = [r for r in analytics_reviews if within_range(r)]
    st.caption(f'Showing {len(analytics_reviews)} of {len(reviews)} saved reviews · Filters apply to the charts below')
    activity_col, status_col = st.columns(2, gap='large')
    with activity_col:
        st.markdown('#### Document review activity')
        fig = review_activity_chart(analytics_reviews)
        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info('Run a sample review to see activity.')
    with status_col:
        st.markdown('#### Human follow-up status')
        fig = review_status_chart(analytics_reviews, get_action)
        if fig is not None:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info('Human review statuses will appear here.')
    st.markdown('#### Requirements with documented evidence')
    fig = requirements_chart(analytics_reviews)
    if fig is not None:
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info('Analyze sample resumes to populate this chart.')
    st.divider()
    st.markdown('<div class="hf-section-label">ACTIVITY LOG</div>', unsafe_allow_html=True)
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
    st.markdown('<div class="hf-section-label">ROLE LIBRARY</div>', unsafe_allow_html=True)
    st.subheader('Saved jobs')
    if jobs:
        st.dataframe([{'ID':j['id'],'Job title':j['title'],'Created':j['created_at']} for j in jobs],
                     hide_index=True, use_container_width=True)
    else:
        st.info('No jobs saved yet. Select a sample above to begin.')

elif st.session_state.page == 'Start a review':
    intro('WORKSPACE / GUIDED REVIEW', 'Review a resume',
          'Follow three steps. You can use a ready-made example or upload your own fictional document.')
    review_stage_hero()
    review_journey(1)
    st.markdown('<div class="hf-step"><span>01</span><div><strong>Select the role</strong><small>Define the requirements to inspect</small></div></div>', unsafe_allow_html=True)
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
    review_journey(2)
    st.markdown('<div class="hf-step"><span>02</span><div><strong>Provide a resume</strong><small>Choose a fictional profile or upload a document</small></div></div>', unsafe_allow_html=True)
    source = st.radio('Resume source', ['Try a fictional candidate', 'Upload a resume'], horizontal=True)
    if source == 'Try a fictional candidate':
        person = st.selectbox('Choose a candidate example', DEMO_RESUMES, format_func=lambda x:x['label'])
        candidate_ref = person['label'].split(' — ')[0] + ' (DEMO)'
        resume_text = person['text']
        with st.expander('Preview fictional resume', expanded=True):
            st.text(resume_text)
    else:
        candidate_ref = st.text_input('Candidate reference (use a fictional ID)', placeholder='e.g. DEMO-014')
        uploaded = st.file_uploader('Choose a fictional resume (PDF, DOCX, TXT, PNG or JPG)',
                                    type=['pdf', 'docx', 'txt', 'png', 'jpg', 'jpeg'])
        resume_text = None
        if uploaded is not None:
            contents = uploaded.getvalue()
            extension = Path(uploaded.name).suffix.lower()
            needs_visual = extension in {'.png', '.jpg', '.jpeg'}
            if extension == '.pdf':
                try:
                    resume_text = extract_text(uploaded.name, contents)
                    st.success('Text-based PDF read locally; no vision API needed.')
                except ValueError as exc:
                    if 'No extractable text' in str(exc):
                        needs_visual = True
                    else:
                        st.error(f'Could not read PDF: {exc}')
            elif not needs_visual:
                try:
                    resume_text = extract_text(uploaded.name, contents)
                    st.success('Document text extracted locally.')
                except Exception as exc:
                    st.error(f'Could not read document: {exc}')
            if needs_visual:
                st.info('Visual document detected. Image transcription is optional and may send '
                        'document content to Groq. Use fictional documents only; transcription '
                        'may contain errors and must be verified against the original.')
                consent = st.checkbox('I confirm this is fictional data and consent to sending '
                                      'its images to the configured Groq vision model.',
                                      key='vision_consent')
                if st.button('Transcribe visual document', disabled=not consent):
                    try:
                        with st.spinner('Reading visible text with the vision model...'):
                            st.session_state.visual_result = {
                                'name': uploaded.name, 'contents_hash': hashlib.sha256(contents).hexdigest(),
                                'text': extract_visual_text(uploaded.name, contents),
                            }
                    except Exception as exc:
                        st.error(f'Visual transcription failed: {exc}')
                cached = st.session_state.get('visual_result', {})
                if (cached.get('name') == uploaded.name and
                    cached.get('contents_hash') == hashlib.sha256(contents).hexdigest()):
                    resume_text = cached['text']
                    st.warning('AI-transcribed text: check the preview against the original before analysis.')
            if resume_text:
                with st.expander('Preview extracted text', expanded=needs_visual):
                    st.text(resume_text[:6000])
    st.divider()
    review_journey(3)
    st.markdown('<div class="hf-step"><span>03</span><div><strong>Analyze the evidence</strong><small>Human review is always required</small></div></div>', unsafe_allow_html=True)
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
        st.markdown('<a href="#ask-the-evidence" style="display:inline-block;background:#E4EEE4;color:#173E34;padding:.65rem 1rem;border:1px solid #B9D1BE;border-radius:10px;text-decoration:none;font-weight:700;margin:.3rem 0 1rem">✦ Jump to AI Evidence Assistant ↓</a>', unsafe_allow_html=True)
        st.divider()
        workflow_trace_visual(st.session_state.latest_result.get('trace', []))
        show_result(st.session_state.latest_result, st.session_state.latest_review_id)
        evidence_explorer(st, st.session_state.latest_result.get('evidence', {}),
                          st.session_state.latest_result.get('supported_skills', []),
                          st.session_state.latest_result.get('missing_skills', []),
                          key_prefix=f"latest_{st.session_state.latest_review_id}")
        render_evidence_report(st, st.session_state.latest_result, st.session_state.latest_review_id)
        render_trace(st, st.session_state.latest_result)
        render_chat(st, st.session_state.latest_review_id,
                    st.session_state.latest_result.get("evidence", {}),
                    st.session_state.latest_result.get("supported_skills", []),
                    st.session_state.latest_result.get("missing_skills", []))
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
        st.markdown('<a href="#ask-the-evidence" style="display:inline-block;background:#E4EEE4;color:#173E34;padding:.65rem 1rem;border:1px solid #B9D1BE;border-radius:10px;text-decoration:none;font-weight:700;margin:.3rem 0 1rem">✦ Jump to AI Evidence Assistant ↓</a>', unsafe_allow_html=True)
        queue_status_strip(reviews, get_action)
        st.markdown('<div class="hf-section-label">REVIEW REGISTER</div>', unsafe_allow_html=True)
        search_col, filter_col = st.columns([2, 1])
        with search_col:
            search_query = st.text_input('Search reviews', placeholder='Candidate reference, role, or review number', key='queue_search')
        with filter_col:
            queue_filter = st.selectbox('Follow-up status', ['All statuses', 'Pending', 'Reviewed', 'Needs more information'], key='queue_filter')
        filtered = []
        for r in reviews:
            job_title = job_lookup.get(r['job_id'], {}).get('title', 'Archived job')
            state = get_action(r['id'])['state'].replace('_', ' ').title()
            searchable = f"{r['id']} {r['candidate_name']} {job_title}".lower()
            if search_query.strip().lower() in searchable and (queue_filter == 'All statuses' or state == queue_filter):
                filtered.append(r)
        rows = [{'Review':r['id'], 'Candidate reference':r['candidate_name'],
                 'Job':job_lookup.get(r['job_id'],{}).get('title','Archived job'),
                 'Follow-up':get_action(r['id'])['state'].replace('_',' ').title()} for r in filtered]
        if rows:
            st.dataframe(rows, hide_index=True, use_container_width=True)
        else:
            st.info('No reviews match your search or filter.')
        chosen = st.selectbox('Open a saved review', filtered,
                              format_func=lambda r:f"#{r['id']} — {r['candidate_name']}") if filtered else None
        if chosen is None:
            st.stop()
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
        evidence_explorer(st, evidence, json.loads(chosen['supported_skills']),
                          json.loads(chosen['missing_skills']), key_prefix=f"queue_{chosen['id']}")
        render_evidence_report(st, chosen, chosen['id'])
        render_chat(st, chosen["id"], evidence,
                    json.loads(chosen["supported_skills"]),
                    json.loads(chosen["missing_skills"]))
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
