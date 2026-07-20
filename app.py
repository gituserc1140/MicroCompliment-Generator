import streamlit as st
import requests

st.title("Micro-Compliment Generator")

# Groq API endpoint and key
GROQ_API_URL = "https://api.groq.com/v1/generate"
GROQ_API_KEY = st.secrets["groq_api_key"]  # Store API key in Streamlit secrets

# Function to generate compliment
def generate_compliment(user_input):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": f"Generate a short, unique compliment for someone with this name or trait: {user_input}. Keep it under 15 words.",
        "max_tokens": 20,
        "temperature": 0.7
    }
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        return "Sorry, I couldn't generate a compliment at the moment."

# User input
user_input = st.text_input("Enter a name or trait:")

if st.button("Generate Compliment"):
    if user_input:
        with st.spinner("Generating compliment..."):
            compliment = generate_compliment(user_input)
            st.success(compliment)
    else:
        st.warning("Please enter a name or trait.")