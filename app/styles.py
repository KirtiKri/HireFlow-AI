"""Accessible, restrained Streamlit presentation. No custom interactive HTML."""
import streamlit as st

def apply_styles():
    st.markdown('''<style>
    .stMain .block-container {max-width: 1180px; padding-top: 1.25rem; padding-bottom: 3rem;}
    h1,h2,h3 {letter-spacing: -.03em; color: #183B35;}
    h1 {font-weight: 730;}
    [data-testid="stSidebar"] {background: #F0F2ED; border-right: 1px solid #D4DCD5;}
    [data-testid="stMetric"] {border-top: 3px solid #245449; border-bottom: 1px solid #D4DCD5; padding: 1rem 0;}
    .stButton > button, .stFormSubmitButton > button {border-radius: 3px; min-height: 2.7rem; font-weight: 600;}
    div[data-baseweb="select"] > div, .stTextInput input, .stTextArea textarea {border-radius: 3px;}
    .eyebrow {color:#64756E; text-transform:uppercase; font-size:.76rem; font-weight:700; letter-spacing:.11em;}
    .step-hint {border-left: 3px solid #B36C4E; padding: .6rem 1rem; background:#F8F4EE; margin:.5rem 0 1rem;}
    .review-note {font-size:.86rem; color:#52645D;}
    </style>''', unsafe_allow_html=True)
