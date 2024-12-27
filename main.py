import json
import requests
import os
from dotenv import load_dotenv
import streamlit as st
import requests
import webbrowser

load_dotenv()

api_key = os.getenv("api_key")

st.set_page_config(
    page_title="SparshGPT",
    page_icon="image-removebg-preview.png",
    layout="wide",
)


st.image("image-removebg-preview.png")
st.title("SparshGPT🫦")


st.sidebar.title("About")
if st.sidebar.button("Profile"):
    pass
if st.sidebar.button("GitHub"):
    webbrowser.open_new_tab("https://github.com/sparsh0106")
if st.sidebar.button("LinkedIn"):
    webbrowser.open_new_tab("https://www.linkedin.com/in/")
if st.sidebar.button("Instagram"):
    webbrowser.open_new_tab("https://www.instagram.com/sparsh0106")
if st.sidebar.button("Discord Server"):
    pass
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")

st.sidebar.write("")

st.sidebar.write("")

st.sidebar.write("")
st.sidebar.write("")


st.sidebar.write("")
st.sidebar.write("")

st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")

st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")

st.sidebar.write("[5p4r584g4rw4l0106@gmail.com](mailto:5p4r584g4rw4l0106@gmail.com)\n+919312422987")


st.subheader("Enter your input")
user_input = st.text_input("")


def generate():
    model = "gpt-4o-mini"
    messages = [
        {
            "role": "system",
            "content": "answer"
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    data = {
        "model": model,
        "messages": messages
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post("https://aiproxy.sanand.workers.dev/openai/v1/chat/completions", headers=headers,data=json.dumps(data))

    result = response.json()
    answer = result["choices"][0]["message"]["content"]
    st.info(f"{answer}")


if st.button("Generate"):
    generate()

