import streamlit as st
import google.generativeai as genai

st.title("Gemini AI Chatbot")

# Configure Gemini API Key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from Gemini
    with st.chat_message("assistant"):
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        st.markdown(response.text)

    st.session_state.messages.append({"role": "assistant", "content": response.text})
