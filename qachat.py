from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response =  chat.send_message(question, stream=True)
    return response

# Initializing Streamlit App
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat-history' not in st.session_state:
    st.session_state['chat-history']=[]

input= st.text_input("Input: ", key=input)
submit = st.button("Ask the Question")

if submit and input:
    response = get_gemini_response(input)

# Adding user query and response to session chat history
    st.session_state['chat-history'].append(("You", input))
    st.subheader("The response is")

    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat-history'].append(("Bot",chunk.text))
st.subheader("The chat history is: ")

for role, text in st.session_state['chat-history']:
    st.write(f"{role}: {text}")
