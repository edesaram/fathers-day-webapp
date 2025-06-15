import streamlit as st
import random
import time

# Father's Day message
message_text = (
    "HAPPY FATHER'S DAY THATHI ❤️\n\n"
    "Thank you for being our rock, our guide, and our biggest supporter.\n"
    "Your strength and unconditional love have shaped us to who we are today.\n"
    "We are so grateful for all the lessons, laughs, and late-night talks.\n"
    "You're our hero.\n"
    "Love you always.\n\n"
    "From Jonathan, Mystica, Elisha and Aaron 💙"
)

# Dad jokes
dad_jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾",
    "I only know 25 letters of the alphabet. I don't know y. 🤷",
    "What do you call fake spaghetti? An impasta! 🍝",
    "Why don’t eggs tell jokes? They’d crack each other up. 🥚😂",
    "Dad, can you put my shoes on? No, I don’t think they’ll fit me. 👟"
]

# Page config
st.set_page_config(page_title="Father's Day Surprise 🎁", page_icon="🎁")

# Optional background image
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://media.istockphoto.com/id/1496490916/vector/fathers-day-seamless-wallpaper.jpg?s=1024x1024&w=is&k=20&c=YlEj65eVA_4Wlw4C_Bnr1D0Yse9HHa0BbEgKn4pHYHE=');
        background-size: cover;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🎁 Father's Day Surprise 🎁</h1>", unsafe_allow_html=True)
st.markdown("### 👇 Tap below to begin the magic!")

if 'started' not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    center = st.columns(3)
    with center[1]:
        if st.button("💝 Start Surprise"):
            st.session_state.started = True
            st.experimental_rerun()
else:
    st.markdown("## 🎆 Fireworks Show Begins!")

    emoji_list = ["✨", "🎇", "🌟", "💥", "🎆", "🧨"]
    cols = st.columns(5)

    for _ in range(30):
        for i in range(5):
            with cols[i]:
                st.markdown(f"<div style='font-size:40px; text-align: center'>{random.choice(emoji_list)}</div>", unsafe_allow_html=True)
        time.sleep(0.15)

    st.markdown("---")

    # Message section
    st.subheader("❤️ A Message From Your Kids")
    st.success(message_text)

    # Jokes with expandable style
    st.markdown("---")
    with st.expander("🤣 Want a Dad Joke?"):
        if st.button("Click for a Joke!"):
            st.info(random.choice(dad_jokes))

    st.markdown("---")
    center = st.columns(3)
    with center[1]:
        if st.button("🔁 Replay Surprise"):
            st.session_state.started = False
            st.experimental_rerun()
