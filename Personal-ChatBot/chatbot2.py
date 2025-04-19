import os
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Access the GEMINI_API_KEY from the environment variables
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Generative AI API with the key
genai.configure(api_key=api_key)

# Initialize the GenerativeModel
model = genai.GenerativeModel('gemini-1.5-flash')

# Configure page
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

# Custom CSS for better styling
st.markdown("""
    <style>
    .stTextInput > label {
        font-size: 20px;
        color: #333;
    }
    .stButton > button {
        font-size: 18px;
        padding: 10px;
        background-color: #4CAF50;
        color: white;
    }
    .message {
        padding: 10px;
        margin: 5px 0;
        border-radius: 10px;
        max-width: 70%;
    }
    .user_message {
        background-color: #DCF8C6;
        align-self: flex-end;
    }
    .bot_message {
        background-color: #E2E2E2;
        align-self: flex-start;
    }
    .timestamp {
        font-size: 12px;
        color: #888;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chatbot function (replace with your logic)
def chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Callback function to handle input and clear it
def send_message():
    user_input = st.session_state.input
    if user_input:
        # Save user's message
        st.session_state["messages"].append({
            "role": "user", 
            "content": user_input, 
            "time": datetime.now().strftime("%H:%M:%S")
        })
        
        # Get bot's response
        bot_reply = chatbot_response(user_input)
        
        # Save bot's response
        st.session_state["messages"].append({
            "role": "bot", 
            "content": bot_reply, 
            "time": datetime.now().strftime("%H:%M:%S")
        })
        
        # Clear input after sending
        st.session_state.input = ""

# UI Layout
st.title("🤖 Chatbot")

# Display chat history
for message in st.session_state["messages"]:
    if message["role"] == "user":
        st.markdown(f'<div class="message user_message">{message["content"]}<div class="timestamp">{message["time"]}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message bot_message">{message["content"]}<div class="timestamp">{message["time"]}</div></div>', unsafe_allow_html=True)

# User input with callback
st.text_input("Type your message here...", key="input", on_change=send_message)

