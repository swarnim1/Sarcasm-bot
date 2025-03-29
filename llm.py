import google.generativeai as genai
from tone_prompts import TONE_PRESETS

# Gemini API key
genai.configure(api_key="AIzaSyBpjBcQofCTyVBUiuyKZxpt7TVIavLfdtk")

model = genai.GenerativeModel("gemini-2.0-flash-lite")

def generate_sarcastic_reply(chat_history, user_input, tone="Delhi Boy Hindi"):
    context = "\n".join([f"{sender}: {msg}" for sender, msg in chat_history])
    
    persona_prompt = TONE_PRESETS.get(tone, TONE_PRESETS["Delhi Boy Hindi"])

    prompt = f"""
{persona_prompt}
Keep your conversation small and precise
Here's the conversation so far:
{context}
User: {user_input}
AI:"""
    
    response = model.generate_content(prompt)
    return response.text.strip()