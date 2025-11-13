import streamlit as st # for web interfaces with Python

def main():
    st.title("Times Tables Quiz")
    st.write("Welcome to Times Tables Quiz")
    name = st.text_input("Enter your name")

    if name:
        st.success(f"Hello, {name}")
    else:
        st.info("Please type your name to begin")

if __name__ == "__main__":
    main()