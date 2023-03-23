import streamlit as st

def main():
    st.title("put your command here")

    input_text = st.text_input("Enter your text:")
    if input_text:
        st.write(f"Your input text: {input_text}")

main()
