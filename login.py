import streamlit as st
from session_state import initialize_session
from db import register_user, login_user


initialize_session()


if not st.session_state.logged_in:
    st.image("https://i.imgur.com/dB5sC5D.png", width=150)  # Add your own image or logo URL
    st.markdown("<h1 style='text-align: center; color: #4b4b4b;'>Welcome to My NLP App</h1>", unsafe_allow_html=True)

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
                st.experimental_rerun()
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
        st.experimental_rerun()

    elif page == "Home":
        st.markdown("<h1 style='text-align:center;'>✨ Welcome to NLP Web App ✨</h1>", unsafe_allow_html=True)
        st.write("Use the sidebar to explore different features like NER, Sentiment, and Emotion detection.")

    elif page == "NER":
        from templates.ner_ui import show_ner_ui
        show_ner_ui()

    elif page == "Sentiment Analysis":
        from templates.sentiment_ui import show_sentiment_ui
        show_sentiment_ui()

    elif page == "Emotion Detection":
        from templates.emotion_ui import show_emotion_ui
        show_emotion_ui()

