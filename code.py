import streamlit as st
st.title("Hello World")
st.write("This is a simple Streamlit app by Rohit.")
agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("Thank you for agreeing!")
else:    st.write("Please agree to the terms and conditions to proceed.")
name = st.text_input("Enter your name") 
genre = st.radio("Select your genre", ["Male", "Female", "Other"])
num1 = st.number_input("Enter a number").real
num2 = st.number_input("Enter another number").real
if st.button("Calculate Sum"):
    st.write("Sum =", num1 + num2)