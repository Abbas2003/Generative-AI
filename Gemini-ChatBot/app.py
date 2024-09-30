import os
import streamlit as st  
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai


# Load environment variables from .env file
load_dotenv()

# Access the GEMINI_API_KEY from the environment variables
api_key = "AIzaSyCgwV3oXhiERE9l_tB1-RM4j4HFDSHd4jI"

# Configure the Generative AI API with the key
genai.configure(api_key=api_key)

# Initialize the GenerativeModel
model = genai.GenerativeModel('gemini-1.5-flash')

def responceFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# Configure page
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

# streamlit UI
st.title("🤖GEMINI ChatBot")
st.subheader("Designed by M. Abbas ")
st.write("It uses Google API")


user_input = st.text_input("Enter your prompt: ")
if st.button("Get response"):
    if user_input:
        output = responceFromModel(user_input)
        st.write(f"ChatBot response: \n {output}")
    else:
        st.write("Please enter a prompt")
        
