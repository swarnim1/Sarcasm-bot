import streamlit as st
from llm import generate_sarcastic_reply
from tone_prompts import TONE_PRESETS

st.set_page_config(page_title="Sarcastic Chatbot", layout="centered")
# Footer 
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 12px;
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        color: #FF4B4B;
        background: transparent;
        animation: glowPulse 2.5s infinite ease-in-out;
        z-index: 9999;
    }

    @keyframes glowPulse {
        0% {
            color: #ffcccc;
            text-shadow: 0 0 2px #ffcccc;
            opacity: 0.2;
        }
        50% {
            color: #FF4B4B;
            text-shadow: 0 0 10px #FF4B4B, 0 0 20px #FF4B4B;
            opacity: 1;
        }
        100% {
            color: #ffcccc;
            text-shadow: 0 0 2px #ffcccc;
            opacity: 0.2;
        }
    }
    </style>

    <div class="footer">
        Made with ❤️ by <b>Swarnim Dixit</b>
    </div>
    """,
    unsafe_allow_html=True
)


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
user_input = st.chat_input("Don’t worry, I’ll pretend it’s a smart question.")

if user_input:
    # Add and show user message
    st.session_state.chat_history.append(("User", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    with st.chat_message("assistant"):
        with st.spinner("Typing something unnecessarily clever..."):
            reply = generate_sarcastic_reply(
                st.session_state.chat_history, user_input, tone
            )
            st.markdown(reply)

    # Add bot reply to history
    st.session_state.chat_history.append(("AI", reply))

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        padding: 10px;
        background-color: #ffffff00;
        text-align: center;
        font-size: 15px;
        color: #FF4B4B;
        z-index: 9999;
    }
    </style>

    <div class="footer">
        Made with ❤️ by <b>Swarnim Dixit</b>
    </div>
    """,
    unsafe_allow_html=True
)