# Micro-Compliment Generator

> Instantly generate a short, personalised compliment for any name or trait — powered by [Groq](https://console.groq.com) and built with [Streamlit](https://streamlit.io).

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://microcompliment-generator-ndugstlpbqiu7g5233glub.streamlit.app/)
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-bf4b8a?logo=github-sponsors)](https://github.com/sponsors/gituserc1140)

---

## What it does

Type a name, a personality trait, or anything you want to celebrate (e.g. *"Sarah"*, *"dog lover"*, *"great listener"*) and the app uses a large language model via Groq to craft a warm, unique compliment of 15 words or fewer — instantly.

## Features

- **Frontend API key input** — paste your Groq key directly in the sidebar; no config files needed
- **Instant results** — powered by `llama-3.1-8b-instant` through Groq's ultra-fast inference
- **Polished dark UI** — gradient background, styled cards, and responsive layout
- **GitHub & Sponsor buttons** — easily accessible from the sidebar

---

## Getting started

### Prerequisites

- Python 3.9 or later
- A free [Groq API key](https://console.groq.com) (no credit card required)

### 1. Clone the repository

```bash
git clone https://github.com/gituserc1140/MicroCompliment-Generator.git
cd MicroCompliment-Generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## How to use

1. Open the app in your browser.
2. In the **sidebar**, paste your **Groq API key** into the password field.
3. In the main area, type a **name or trait** in the text box (e.g. *"Emma"*, *"adventurous"*, *"always early"*).
4. Click **Generate Compliment**.
5. Your personalised compliment appears instantly in the card below.

---

## Optional: store the API key in Streamlit secrets

If you are deploying to [Streamlit Community Cloud](https://streamlit.io/cloud), you can store the key so users do not need to enter it manually:

1. Create `.streamlit/secrets.toml` (never commit this file):
   ```toml
   GROQ_API_KEY = "gsk_your_key_here"
   ```
2. On Streamlit Cloud, add the secret via **App settings → Secrets**.

The sidebar key field takes priority over secrets/environment variables, so users can still override it at runtime.

---

## Deploying to Streamlit Community Cloud

1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo.
3. Set `app.py` as the main file.
4. Add `GROQ_API_KEY` in the **Secrets** section (optional, see above).
5. Click **Deploy**.

---

## Tech stack

| Component | Library / Service |
|-----------|-------------------|
| UI framework | [Streamlit](https://streamlit.io) |
| LLM inference | [Groq](https://console.groq.com) (`llama-3.1-8b-instant`) |
| Python client | [`groq`](https://pypi.org/project/groq/) |

---

## Contributing

Issues and pull requests are welcome! Please open an issue first to discuss any significant changes.

## Support this project

If you find this app useful, consider [sponsoring the author](https://github.com/sponsors/gituserc1140) on GitHub.
