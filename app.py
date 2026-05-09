import streamlit as st
import requests

# Page title
st.set_page_config(page_title="AI Article Generator")

st.title("🤖 AI Article Generator")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chats
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
prompt = st.chat_input("Enter your topic...")

if prompt:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    try:

        # Send request to n8n webhook
        response = requests.post(
            "https://vishwanath-ai.app.n8n.cloud/webhook/article-generator",
            json={
                "topic": prompt
            },
            timeout=120
        )

        # Convert response to JSON
        data = response.json()

        # Debug response (optional)
        # st.write(data)

        # Get article text
        if isinstance(data, dict):
            article = data.get("article", str(data))
        else:
            article = str(data)

    except Exception as e:
        article = f"Error: {str(e)}"

    # Show AI response
    with st.chat_message("assistant"):
        st.markdown(article)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": article
    })