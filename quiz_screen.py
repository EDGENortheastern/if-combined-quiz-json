# quiz_screen.py
import streamlit as st
from question_generator import generate_question


def quiz_screen() -> None:
    total = st.session_state.get("total_questions", 10)
    qnum = st.session_state.question_number

    # If we've finished all questions, go to end screen
    if qnum > total:
        st.session_state.screen = "end"
        st.rerun()
        return

    # Make sure we have a current question
    if st.session_state.question is None:
        st.session_state.question = generate_question()

    num1, num2, correct = st.session_state.question

    st.header(f"Question {qnum} of {total}")
    st.write(f"What is {num1} × {num2}?")

    # Text input so they can leave it blank initially
    answer_str = st.text_input(
        "Your answer",
        key=f"answer_{qnum}",  # different widget per question
    )

    if st.button("Submit answer"):
        # Basic validation
        if not answer_str.strip():
            st.error("Please enter an answer.")
            return

        try:
            answer = int(answer_str)
        except ValueError:
            st.error("Please enter a whole number.")
            return

        # Check correctness
        if answer == correct:
            st.session_state.score += 1
            st.success("Correct!")
        else:
            st.warning(f"Not quite. The correct answer was {correct}.")

        # Move on to the next question
        st.session_state.question_number += 1
        st.session_state.question = None  # force a new question next time

        # If that was the last question, switch to end screen
        if st.session_state.question_number > total:
            st.session_state.screen = "end"

        st.rerun()

    st.write(f"Current score: {st.session_state.score}")
