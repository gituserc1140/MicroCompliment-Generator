# Micro-Compliment Generator

A simple Streamlit app that generates short, unique compliments using the Groq API.

## Setup
1. Install dependencies:
   ```bash
pip install -r requirements.txt
```
2. Add your Groq API key to Streamlit secrets:
   Create a file named `.streamlit/secrets.toml` and add your API key:
   ```toml
groq_api_key = "your_groq_api_key_here"
```
3. Run the app:
   ```bash
streamlit run app.py
```

## Usage
- Enter a name or trait in the input box.
- Click "Generate Compliment" to receive a micro-compliment.