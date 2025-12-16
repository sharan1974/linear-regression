import streamlit as st


st.set_page_config(page_title="My Streamlit App", layout="centered")


st.title("🚀 My Streamlit App")
st.write("This app is ready to be uploaded to GitHub and Streamlit Cloud.")


name = st.text_input("Enter your name")


if st.button("Submit"):
if name:
st.success(f"Hello, {name}! 👋")
else:
st.warning("Please enter your name")  ```
