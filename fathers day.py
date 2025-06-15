import streamlit as st
import random
import time

message_text = (
    "HAPPY FATHER'S DAY THATHI\n\n"
    "Thank you for being our rock, our guide, and our biggest supporter.\n"
    "Your strength and unconditional love have shaped us to who we are today.\n"
    "We are so grateful for all the lessons, laughs, and late-night talks.\n"
    "You're our hero.\n"
    "Love you always.\n\n"
    "From Jonathan, Mystica, Elisha and Aaron 💙"
)

dad_jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I only know 25 letters of the alphabet. I don't know y.",
    "What do you call fake spaghetti? An impasta!",
    "Why don’t eggs tell jokes? They’d crack each other up.",
    "Dad, can you put my shoes on? No, I don’t think they’ll fit me."
]

st.set_page_config(page_title="Father's Day Surprise", page_icon="🎁")
st.title("🎁 Father's Day Surprise")

if 'started' not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    if st.button("Start Surprise 💝"):
        st.session_state.started = True
        st.experimental_rerun()
else:
    st.markdown("### 🎇 Fireworks!")
    for _ in range(20):
        x = random.choice(["✨", "🎇", "🌟", "💥"])
        st.markdown(f"<div style='font-size:30px'>{x}</div>", unsafe_allow_html=True)
        time.sleep(0.1)

    st.markdown("---")
    st.subheader("❤️ A Message From Your Kids")
    st.markdown(f"<pre style='color:blue; font-size:16px'>{message_text}</pre>", unsafe_allow_html=True)

    st.markdown("---")
    if st.button("Tell Me a Dad Joke 😄"):
        st.info(random.choice(dad_jokes))

    def reset():
        st.session_state['started'] = False

    st.button("🎉 Replay Surprise", on_click=reset)
