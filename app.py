import streamlit as st
import json
import hashlib
from api import ner,sentiment,emotion
from db import load_users, save_users, hash_password, register_user, login_user
from templates import ner_ui, sentiment_ui, emotion_ui


st.set_page_config(page_title="My NLP App", layout="centered")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_name = ""

if not st.session_state.logged_in:
    tabs = st.tabs(["Login", "Register"])

    with tabs[0]:
        st.markdown("<h2 style='text-align: center;'>🔐 Login</h2>", unsafe_allow_html=True)
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            success, info = login_user(email, password)
            if success:
                st.session_state.logged_in = True
                st.session_state.user_name = info
                st.rerun()

            else:
                st.error(info)

    with tabs[1]:
        st.markdown("<h2 style='text-align: center;'>📝 Register</h2>", unsafe_allow_html=True)
        name = st.text_input("Name")
        email = st.text_input("Email", key="reg_email")
        password = st.text_input("Password", type="password", key="reg_pass")
        if st.button("Register"):
            success, msg = register_user(name, email, password)
            if success:
                st.success(msg)
                st.info("Please login now.")
            else:
                st.warning(msg)
else:
    st.sidebar.success(f"Welcome, {st.session_state.user_name}")
    page = st.sidebar.selectbox("Choose Task", ["Home", "NER", "Sentiment Analysis", "Emotion Detection", "Logout"])

    if page == "Logout":
        st.session_state.logged_in = False
        st.session_state.user_name = ""
        st.rerun()

    elif page == "Home":
        st.markdown("<h1 style='text-align:center;'>✨ Welcome to NLP Web App ✨</h1>", unsafe_allow_html=True)
        st.write("Use the sidebar to explore different features like NER, Sentiment, and Emotion detection.")

    elif page == "NER":
        ner_ui.show_ner_ui()


    elif page == "Sentiment Analysis":

        sentiment_ui.show_sentiment_ui()

    elif page == "Emotion Detection":

        emotion_ui.show_emotion_ui()
