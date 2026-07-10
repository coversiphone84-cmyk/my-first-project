import streamlit as st
from google import genai

st.set_page_config(page_title="Usman's Chatbot", layout="centered")
st.title("🤖 Usman ka Apna AI Chatbot")

# Aapki wahi naye wali key
API_KEY = "AQ.Ab8RN6LwrFvibxAlTNao6xrLlXHzM_z51RVt8rUcZEqwKFuzGg"

# Client setup naye token ke mutabiq
if "client" not in st.session_state:
    st.session_state.client = genai.Client(
        api_key=API_KEY, 
        http_options={'headers': {'Authorization': f'Bearer {API_KEY}'}}
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani baatein screen par dikhane ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box
if user_input := st.chat_input("Hi, kaise ho?"):
    # User ka message screen par dikhaein
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        # CHAT SESSION KE BAJAAY DIRECT RESPONSE (Is se AQ wali key block nahi hogi)
        response = st.session_state.client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_input,
        )
        
        # AI ka response screen par dikhaein
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
    except Exception as e:
        st.error(f"Oho! Koi masla aaya hai: {e}")
