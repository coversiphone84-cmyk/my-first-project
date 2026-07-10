import streamlit as st
from google import genai

# Page setting
st.set_page_config(page_title="Usman's Chatbot", layout="centered")
st.title("🤖 Usman ka Apna AI Chatbot")


API_KEY = "AQ.Ab8RN6ItvF-3BTRF0aB567GD0dBRtyavnDscN_voowIm6B45yQ"

# Client initialize karein
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=API_KEY)

# Chat session start karein gemini-2.5-flash ke sath
if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.client.chats.create(model="gemini-2.5-flash")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani baatein screen par dikhane ke liye loop
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box
if user_input := st.chat_input("Google AI se kuch bhi poochein..."):
    # User ka message screen par dikhaein
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        # AI se response lein
        response = st.session_state.chat.send_message(user_input)
        
        # AI ka response screen par dikhaein
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error aaya hai: {e}")
