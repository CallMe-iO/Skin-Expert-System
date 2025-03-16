import streamlit as st

def load_custom_css():
    st.markdown("""
    <style>
        /* Tema dokter */
        .stApp { background-color: #f5f5f5; }
        .stButton>button { background-color: #4CAF50; color: white; }
        .css-1d391kg { padding: 1rem; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)