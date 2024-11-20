import streamlit as st
import requests

def get_llama_response(input_text):
    response = requests.post("http://localhost:8000/info/invoke",
                             json= {'input':{'topic':input_text}} )
    return response.json()['output']

st.title("Langchain demo with llama 3.1 api chain")
input_text =  st.text_input("Write information about ")

if input_text:
    st.write(get_llama_response(input_text))