
import streamlit as st

# Title
st.title("Simple Streamlit App")

# Text Input
user_input = st.text_input("Enter some text:")
button_clicked = st.button("Click me!")

# Display entered text when button is clicked
if button_clicked:
    st.write("You entered:", user_input)

