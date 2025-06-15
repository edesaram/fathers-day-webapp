import streamlit as st
import random
import time

# Page config
st.set_page_config(page_title="Father's Day Surprise 🎁", page_icon="🎁", layout="wide")

# 🎇 Background GIF Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@500;700&display=swap');

    body {
        background-image: url('https://media.giphy.com/media/3o6ZsY8uFCDRrL6U9C/giphy.gif');
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }

    html, body, [class*="css"] {
        font-family: 'Raleway', sans-serif;
        color: #fff !important;
        background-color: rgba(0, 0, 0, 0.6) !important;
    }

    .firework {
        font-size: 45px;
        animation: pop 0.3s ease-in-out;
    }

    @keyframes pop {
        0% { transform: scale(0.5); opacity: 0.5; }
        100% { transform: scale(1.2); opacity: 1; }
    }

    .big-text {
        font-size: 28px;
        text-align: center;
        padding: 20px;
    }

    </style>
""", unsafe_allow_html=True)

# Message & jokes
message_text = """
❤️ **HAPPY FATHER'S DAY THATHI** ❤️  
Thank you for being our rock, our guide, and our biggest supporter.  
Your strength and unconditional love have shaped us into who we are today.  
We're so grateful for all the lessons, laughs, and late-night talks.  
You're our hero. Love you always.  
From Jonathan, Mystica, Elisha, and Aaron 💙
"""

dad_jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
    "What do you call fake spaghetti? An impasta! 🍝",
    "How do you organize a space party? You planet! 🪐",
    "I'm on a seafood diet. I see food and I eat it. 🍽️",
    "I would tell you a joke about construction, but I’m still working on it. 🛠️"
]

firework_emojis = ["✨", "🎇", "🌟", "💥", "🎆", "🧨", "🌠", "🎉", "💫"]

# App logic
if 'started' not in st.session_state:
    st.session_state.started = False
    st.rerun()

st.markdown("<h1 style='text-align: center;'>🎁 Father's Day Surprise 🎁</h1>", unsafe_allow_html=True)

if not st.session_state.started:
    st.markdown("<div class='big-text'>👇 Tap the button below to start the magic!</div>", unsafe_allow_html=True)
    center = st.columns(3)
    with center[1]:
        if st.button("💝 Start Surprise"):
            st.session_state.started = True
            st.rerun()
else:
    # Fireworks animation
    st.markdown("### 🎆 Fireworks Show 🎆")
    cols = st.columns(7)
    placeholders = [col.empty() for col in cols]

    for _ in range(20):
        for placeholder in placeholders:
            placeholder.markdown(f"<div class='firework' style='text-align:center'>{random.choice(firework_emojis)}</div>", unsafe_allow_html=True)
        time.sleep(0.2)

    st.markdown("---")

    # Message reveal
    st.markdown("## 💌 A Special Message for You")
    st.success(message_text)

    st.markdown("---")

    # Dad jokes
    with st.expander("🤣 Want a Dad Joke?"):
        if st.button("Click for a Joke!"):
            st.info(random.choice(dad_jokes))

    st.markdown("---")

    # Replay button
    center = st.columns(3)
    with center[1]:
        if st.button("🔁 Replay the Magic"):
            st.session_state.started = False
            st.rerun()
