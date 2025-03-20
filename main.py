# DAILY PYTHON CHALLENGE
# PRACTICE
#  QUIZ GAME

import streamlit as st
import random
import time

import streamlit as st

def load_css():
    try:
        with open("styles.css", "r") as f:  # Ensure "r" mode for reading
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("⚠ CSS file not found. Make sure 'styles.css' is in the same folder.")

load_css()

# CREATE A QUESTION BANK
question_bank = [
    {"question": "What is the capital of France?", "options": ["London", "Paris", "Berlin", "Madrid"], "answer": "B"},
    {"question": "What is 5 + 7?", "options": ["10", "12", "15", "9"], "answer": "B"},
    {"question": "Who developed the theory of relativity?", "options": ["Newton", "Einstein", "Galileo", "Tesla"], "answer": "B"},
    {"question": "What is the largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "C"},
    {"question": "Which element has the chemical symbol 'O'?", "options": ["Oxygen", "Gold", "Osmium", "Opal"], "answer": "A"},
]

# RANDOMIZED QUESTION SELECTION
select_questions = random.sample(question_bank,5)

# CREATE THE  QUIZ INTERFACE

st.title("🧠 Quiz Game")
score = 0

for i, q in enumerate(select_questions):
    st.subheader(f"Question {i+1}: {q['question']}")
    choice = st.radio("Select an answer:", ["A", "B", "C", "D"], index=None, key=f"q{i}")

    if choice:
        if choice == q["answer"]:
            st.success("✅ Correct! 🎉")
            score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer is {q['answer']}.")

st.subheader(f"🎯 Final Score: {score}/5")


# APPLY CSS FOR STYLE