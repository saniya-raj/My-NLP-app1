import streamlit as st
from api import sentiment

def show_sentiment_ui():
    st.markdown("<h2 style='text-align: center;'>📊 Sentiment Analysis</h2>", unsafe_allow_html=True)
    text = st.text_area("Enter text", height=150)
    if st.button("Analyze"):
        response = sentiment(text)
        if isinstance(response, dict) and 'error' in response:
            st.error(response['error'])
            return

        results = response[0]
        top = results[0]
        st.success(f"**Top Sentiment:** {top['label']} ({round(top['score']*100,2)}%)")
        for r in results:
            st.progress(r['score'], text=f"{r['label']} — {round(r['score']*100,2)}%")
