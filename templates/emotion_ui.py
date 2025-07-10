import streamlit as st
from api import emotion

def show_emotion_ui():
    st.markdown("<h1 style='text-align: center;'>🎭 Emotion Detection</h1>", unsafe_allow_html=True)

    text = st.text_area("Enter text", height=200)

    if st.button("Detect Emotion", use_container_width=True):
        if text.strip() == "":
            st.warning("Please enter some text.")
            return

        with st.spinner("Analyzing..."):
            try:
                response = emotion(text)

                # ✅ Sort and pick the top emotion
                top = sorted(response, key=lambda x: x.get("score", 0), reverse=True)[0]
                st.success(f"**Detected Emotion:** `{top.get('label', 'N/A').capitalize()}` with score `{top.get('score', 0):.2f}`")

                # ✅ Show all results
                st.subheader("All Emotion Scores:")
                for item in response:
                    st.markdown(f"- **{item.get('label', 'N/A').capitalize()}**: `{item.get('score', 0):.2f}`")

            except Exception as e:
                st.error(f"Unexpected response format: {e}")
                st.json(response)
