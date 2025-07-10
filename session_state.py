import streamlit as st

def initialize_session():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'user_name' not in st.session_state:
        st.session_state.user_name = ""
