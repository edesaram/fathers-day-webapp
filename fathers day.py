import streamlit as st
import random
import time

# Page config
st.set_page_config(page_title="Father's Day Surprise 🎁", page_icon="🎁", layout="wide")

# ✨ Custom CSS with a blue gradient background
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Raleway:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Raleway', sans-serif;
        background: linear-gradient(to right, #a1c4fd, #c2e9fb);
        color: #000000;
    }

    .title {
        font-family: 'Pacifico', cursive;
        text-align: center;
        font-size: 48px;
        padding: 20px;
        color: #004080;
    }

    .subtitle {
        font-size: 24px;
        text-align: center;
        color: #004080;
    }

    .firework {
        font-size: 40px;
        animation: sparkle 0.3s ease-in-out;
        text-align: center;
    }

    @keyframes sparkle {
        0% { transform: scale(0.5); opacity: 0.2; }
        50% { transform: scale(1.2); opacity: 1; }
        100% { transform: scale(1); opacity: 0.7; }
    }

    .message-box {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1);
        margin: 20px auto;
    }

    </style>
""", unsafe_allow_html=True)

# Father's Day message
message_text = """
❤️ **HAPPY FATHER'S DAY THATHI** ❤️  
Thank you for being our rock, our guide, and our biggest supporter.  
Your strength and unconditional love have shaped us into who we are today.  
We're so grateful for all the lessons, laughs, and late-night talks.  
You're our hero. Love you always.  
From Jonathan, Mystica, Elisha, and Aaron 💙
"""

# Dad jokes
dad_jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
    "What do you call fake spaghetti? An impasta! 🍝",
    "How do you organize a space party? You planet! 🪐",
    "I would tell you a joke about construction, but I’m still working on it. 🛠️",
    "Dad, can you put my shoes on? No, I don’t think they’ll fit me. 👟"
]

emoji_list = ["✨", "🎇", "🌟", "💥", "🎆", "🧨", "🌠", "🎉", "💫"]

# Session state
if 'started' not in st.session_state:
    st.session_state.started = False
    st.rerun()

# Title and prompt
st.markdown("<div class='title'>🎁 Father's Day Surprise 🎁</div>", unsafe_allow_html=True)

if not st.session_state.started:
    st.markdown("<div class='subtitle'>👇 Tap the button below to begin the magic!</div>", unsafe_allow_html=True)
    center = st.columns(3)
    with center[1]:
        if st.button("💝 Start Surprise"):
            st.session_state.started = True
            st.rerun()
else:
    # Fireworks show
    st.markdown("<div class='subtitle'>🎆 Fireworks Show 🎆</div>", unsafe_allow_html=True)
    cols = st.columns(7)
    placeholders = [col.empty() for col in cols]

    for _ in range(25):
        for i, placeholder in enumerate(placeholders):
            placeholder.markdown(f"<div class='firework'>{random.choice(emoji_list)}</div>", unsafe_allow_html=True)
        time.sleep(0.18)

    # Message box
    st.markdown("<div class='message-box'>", unsafe_allow_html=True)
    st.markdown("### 💌 A Message from Us")
    st.markdown(message_text)
    st.markdown("</div>", unsafe_allow_html=True)

    # Dad jokes
    st.markdown("---")
    with st.expander("🤣 Want a Dad Joke?"):
        if st.button("Click for a Joke!"):
            st.info(random.choice(dad_jokes))

    # Replay
    st.markdown("---")
    center = st.columns(3)
    with center[1]:
        if st.button("🔁 Replay the Magic"):
            st.session_state.started = False
            st.rerun()
