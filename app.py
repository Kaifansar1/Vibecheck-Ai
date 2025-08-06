import streamlit as st
import random
from roast_engine import generate_roast
from compliment_engine import generate_compliment

# --- App Configuration ---
st.set_page_config(page_title="VibeCheck AI", layout="centered")

# --- Session State for Leaderboard ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Sidebar Options ---
st.sidebar.title("🎛️ Controls")
dark_mode = st.sidebar.checkbox("🌙 Enable Dark Mode")
mode = st.sidebar.radio("Choose Mode", ["Roast", "Compliment", "Random"])
audio_enabled = st.sidebar.checkbox("🔊 Enable Voice")
share_text = st.sidebar.button("📤 Share Last Vibe")

# --- Dark Mode Styling ---
if dark_mode:
    st.markdown("""
        <style>
        body {
            background-color: #1e1e1e;
            color: #f5f5f5;
        }
        .stTextInput>div>div>input {
            color: #f5f5f5;
        }
        </style>
    """, unsafe_allow_html=True)

# --- App Title ---
st.title("🎭 VibeCheck AI")
st.subheader("Let AI roast or toast your vibe.")

# --- User Input ---
name = st.text_input("Enter your name")

if st.button("🔥 Hit Me!"):
    if mode == "Random":
        mode = random.choice(["Roast", "Compliment"])

    if name.strip() == "":
        st.warning("Please enter your name first!")
    else:
        if mode == "Roast":
            result = generate_roast(name)
            emoji = "😈"
        else:
            result = generate_compliment(name)
            emoji = "✨"

        st.success(f"{emoji} {result}")
        st.session_state.history.append((mode, result))

        # Voice generation
        if audio_enabled:
            from gtts import gTTS
            from io import BytesIO
            tts = gTTS(text=result)
            mp3_fp = BytesIO()
            tts.write_to_fp(mp3_fp)
            st.audio(mp3_fp.getvalue(), format="audio/mp3")

# --- Leaderboard / History ---
if st.session_state.history:
    st.markdown("---")
    st.markdown("📊 **Leaderboard This Session**")
    for i, (m, txt) in enumerate(reversed(st.session_state.history[-5:]), 1):
        st.markdown(f"**{i}.** *{m}* - {txt}")

# --- Share feature ---
if share_text and st.session_state.history:
    st.markdown("✅ Copy the last vibe:")
    st.code(st.session_state.history[-1][1])

# --- Fancy Footer / Watermark ---
st.markdown("""
    <style>
    .footer {
        position: relative;
        bottom: 0;
        width: 100%;
        padding-top: 20px;
        text-align: center;
        font-size: 0.9em;
        color: #888;
        transition: color 0.3s ease;
    }
    .footer:hover {
        color: #f63366;
    }
    .footer a {
        color: inherit;
        text-decoration: none;
        font-weight: bold;
    }
    </style>

    <div class="footer">
        🚀 Developed by 
        <a href="https://www.linkedin.com/in/kaif-ansarib9/" target="_blank">Kaif Ansari</a> |
        <a href="https://github.com/Kaifansar1" target="_blank">GitHub</a><br>
        Built using 🐍 Python, 🤖 Streamlit & 🎨 GPT-Powered AI
    </div>
""", unsafe_allow_html=True)
