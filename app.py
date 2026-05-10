import streamlit as st
import requests

st.set_page_config(page_title="AI Article Generator")

st.title("🤖 AI Article Generator")

topic = st.text_input("Enter Topic")

if st.button("Generate"):

    try:

        response = requests.post(
            "https://vishwanath-ai.app.n8n.cloud/webhook/article-generator",
            json={
                "topic": topic
            },
            timeout=60
        )

        article = response.text

        st.subheader("Generated Article")

        st.write(article)

    except Exception as e:

        st.error(str(e))