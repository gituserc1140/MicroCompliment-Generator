import os

import streamlit as st
from groq import Groq

_GITHUB_URL = "https://github.com/gituserc1140/MicroCompliment-Generator"
_GITHUB_SPONSOR_URL = "https://github.com/sponsors/gituserc1140"
_GROQ_MODEL = "llama-3.1-8b-instant"

_CSS = """
<style>
/* ── Page background ───────────────────────────────────────────── */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    min-height: 100vh;
}
[data-testid="stHeader"] { background: transparent; }

/* ── Hero banner ───────────────────────────────────────────────── */
.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}
.hero h1 {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, #f9a8d4, #a78bfa, #60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.3rem;
}
.hero p {
    color: #cbd5e1;
    font-size: 1.05rem;
    margin-top: 0;
}

/* ── Compliment result card ────────────────────────────────────── */
.compliment-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(167,139,250,0.45);
    border-radius: 16px;
    padding: 1.6rem 2rem;
    color: #f1f5f9;
    font-size: 1.3rem;
    font-weight: 500;
    line-height: 1.6;
    text-align: center;
    margin-top: 1.2rem;
    letter-spacing: 0.01em;
}

/* ── Error card ────────────────────────────────────────────────── */
.error-card {
    background: rgba(239,68,68,0.12);
    border: 1px solid rgba(239,68,68,0.45);
    border-radius: 14px;
    padding: 1.2rem 1.6rem;
    color: #fca5a5;
    font-size: 0.97rem;
    margin-top: 1rem;
}

/* ── Main button ───────────────────────────────────────────────── */
[data-testid="stButton"] button {
    background: linear-gradient(135deg, #7c3aed, #db2777) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.55rem 1.4rem !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    transition: opacity 0.2s !important;
}
[data-testid="stButton"] button:hover { opacity: 0.85 !important; }

/* ── Sidebar ───────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: rgba(15,12,41,0.88);
    border-right: 1px solid rgba(167,139,250,0.2);
}
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div { color: #cbd5e1 !important; }
[data-testid="stSidebar"] h2 {
    color: #a78bfa !important;
    font-size: 1.1rem;
}

/* ── GitHub link buttons ───────────────────────────────────────── */
.gh-links { display: flex; flex-direction: column; gap: 0.5rem; margin-top: 0.4rem; }
.gh-links a {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.45rem 1rem;
    border-radius: 8px;
    font-size: 0.88rem;
    font-weight: 600;
    text-decoration: none !important;
    transition: opacity 0.2s;
}
.gh-links a:hover { opacity: 0.82; }
.gh-repo { background: #24292f; color: #f0f6fc !important; border: 1px solid #444c56; }
.gh-sponsor { background: #bf4b8a; color: #fff !important; border: 1px solid #9e3370; }

/* ── Warning / alert text ──────────────────────────────────────── */
[data-testid="stAlert"] p { color: #ffffff !important; }

/* ── Spinner text ──────────────────────────────────────────────── */
[data-testid="stSpinner"] p { color: #a5b4fc !important; }
</style>
"""

_SIDEBAR_LINKS = f"""
<div class="gh-links">
    <a class="gh-repo" href="{_GITHUB_URL}" target="_blank">
        <svg height="16" width="16" viewBox="0 0 16 16" fill="currentColor">
            <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38
            0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13
            -.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66
            .07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15
            -.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27
            .68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12
            .51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48
            0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
        </svg>
        View on GitHub
    </a>
    <a class="gh-sponsor" href="{_GITHUB_SPONSOR_URL}" target="_blank">
        <svg height="16" width="16" viewBox="0 0 16 16" fill="currentColor">
            <path d="M4.25 2.5c-1.336 0-2.75 1.164-2.75 3 0 2.15 1.58 4.144 3.365
            5.682A20.565 20.565 0 008 13.393a20.561 20.561 0 003.135-2.211C12.92
            9.644 14.5 7.65 14.5 5.5c0-1.836-1.414-3-2.75-3-1.373 0-2.609.986-3.029
            2.456a.75.75 0 01-1.442 0C6.859 3.486 5.623 2.5 4.25 2.5z"/>
        </svg>
        Sponsor this project
    </a>
</div>
"""


def get_configured_api_key() -> str:
    if "GROQ_API_KEY" in st.secrets:
        return st.secrets["GROQ_API_KEY"]
    return os.getenv("GROQ_API_KEY", "")


def generate_compliment(name_or_trait: str, api_key: str) -> str:
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model=_GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a warm, creative compliment writer. "
                    "Reply with a single short, genuine, personalised compliment of 15 words or fewer. "
                    "No quotes, no punctuation beyond the sentence, no explanation — just the compliment."
                ),
            },
            {
                "role": "user",
                "content": f"Write a compliment for: {name_or_trait}",
            },
        ],
        max_tokens=40,
        temperature=0.9,
    )
    content = response.choices[0].message.content
    if not content:
        raise ValueError("The model returned an empty response. Please try again.")
    return content.strip().strip('"')


def main():
    st.set_page_config(
        page_title="Micro-Compliment Generator",
        page_icon=None,
        layout="centered",
    )
    st.markdown(_CSS, unsafe_allow_html=True)

    # ── Hero header ────────────────────────────────────────────────
    st.markdown(
        """
        <div class="hero">
            <h1>Micro-Compliment Generator</h1>
            <p>Enter a name or trait and receive an instant, personalised compliment.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Sidebar ────────────────────────────────────────────────────
    st.sidebar.header("Settings")
    api_key_input = st.sidebar.text_input(
        "Groq API Key",
        type="password",
        placeholder="gsk_…",
        help="Get a free key at console.groq.com — no credit card required.",
    )
    st.sidebar.markdown(
        '<small><a href="https://console.groq.com/keys" target="_blank" '
        'style="color:#a78bfa;text-decoration:none;">🔑 Get a free API key</a></small>',
        unsafe_allow_html=True,
    )
    st.sidebar.markdown("---")
    st.sidebar.markdown(_SIDEBAR_LINKS, unsafe_allow_html=True)

    api_key = api_key_input.strip() or get_configured_api_key()

    if not api_key:
        st.warning("Please enter your Groq API key in the sidebar to continue.")
        st.stop()

    # ── Main input ─────────────────────────────────────────────────
    name_or_trait = st.text_input(
        "Who or what deserves a compliment?",
        placeholder="e.g. Sarah, curious, dog lover, great listener…",
    )

    if st.button("Generate Compliment", use_container_width=True):
        if name_or_trait.strip():
            with st.spinner("Crafting your compliment…"):
                try:
                    compliment = generate_compliment(name_or_trait.strip(), api_key)
                    st.markdown(
                        f'<div class="compliment-card">{compliment}</div>',
                        unsafe_allow_html=True,
                    )
                except ValueError as exc:
                    st.markdown(
                        f'<div class="error-card">Error: {exc}</div>',
                        unsafe_allow_html=True,
                    )
                except Exception:
                    st.markdown(
                        '<div class="error-card">Unable to generate a compliment. '
                        "Please check your API key and try again.</div>",
                        unsafe_allow_html=True,
                    )
        else:
            st.warning("Please enter a name or trait first.")


if __name__ == "__main__":
    main()
