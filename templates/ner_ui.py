import streamlit as st
from api import ner

def show_ner_ui():
    st.markdown("<h1 style='text-align: center;'>🧠 Named Entity Recognition (NER)</h1>", unsafe_allow_html=True)

    text = st.text_area("Enter text", height=200)

    if st.button("Analyze", use_container_width=True):
        if text.strip() == "":
            st.warning("Please enter some text.")
            return

        with st.spinner("Analyzing..."):
            try:
                entities = ner(text)  # Call your local NER model function

                if not entities:
                    st.info("No named entities found.")
                    return

                st.subheader("Detected Entities:")
                for ent in entities:
                    st.markdown(
                        f"- **{ent.get('word', '')}** ({ent.get('entity_group', 'N/A')}) – Score: `{ent.get('score', 0):.2f}`"
                    )

            except Exception as e:
                st.error(f"Error during NER analysis: {e}")
