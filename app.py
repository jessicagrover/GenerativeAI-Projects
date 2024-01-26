from dotenv import load_dotenv
load_dotenv() # Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini pro model and get responses

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# initialize our streamlit app
st.set_page_config(page_title="QnA Demo")

st.header("Gemini Application")

input=st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# When submit is clicked
if submit:
    response = get_gemini_response(input)
    st.header("The response is")
    st.write(response)
