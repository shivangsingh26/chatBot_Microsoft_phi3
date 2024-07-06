import streamlit as st
from model import BasicBot

@st.cache_resource
def load_model():
    return BasicBot()

basic_bot = load_model()

st.title("LLM Powered Bot")

query = st.text_input("Enter your query")

def ask_question():
    print(basic_bot.user_data)
    return basic_bot.handle_interaction(query)

def get_data():
    data = ""
    for key, value in basic_bot.user_data.items():
        data += f"{key}: {value}\n"
    return data

if st.button("Result"):
    st.write(f"{get_data()}\n{ask_question()}")