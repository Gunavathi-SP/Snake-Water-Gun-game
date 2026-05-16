import streamlit as st
import random

st.title("🐍 Snake Water Gun Game")

choices = {
    "Snake": 1,
    "Water": -1,
    "Gun": 0
}

reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

user_choice = st.radio(
    "Choose one:",
    ("Snake", "Water", "Gun")
)

if st.button("Play Game 🎮"):

    computer = random.choice([-1, 0, 1])
    you = choices[user_choice]

    st.write(f"🤖 Computer chose: {reverseDict[computer]}")
    st.write(f"🧑 You chose: {user_choice}")

    if computer == you:
        st.success("It's a Draw 😆")

    elif (
        (computer == -1 and you == 1) or
        (computer == 1 and you == 0) or
        (computer == 0 and you == -1)
    ):
        st.success("You Win 🤩!!!")

    else:
        st.error("You Lose 😢")
