import streamlit as st
from llm import generate_sarcastic_reply
from tone_prompts import TONE_PRESETS

st.set_page_config(page_title="Sarcastic Chatbot", layout="centered")
st.title("🤖 Sarcastic AI Chatbot")
st.caption("300% more sarcastic than your EX 😏")

# Tone selection
tone = st.selectbox("Choose Your Bot's Vibe 🎭", list(TONE_PRESETS.keys()))

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for speaker, message in st.session_state.chat_history:
    with st.chat_message("user" if speaker == "User" else "assistant"):
        st.markdown(message)

# Chat input
user_input = st.chat_input("Type Greatest thoughts...")

if user_input:
    # Add and show user message
    st.session_state.chat_history.append(("User", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    with st.chat_message("assistant"):
        with st.spinner("Typing..."):
            reply = generate_sarcastic_reply(
                st.session_state.chat_history, user_input, tone
            )
            st.markdown(reply)

    # Add bot reply to history
    st.session_state.chat_history.append(("AI", reply))