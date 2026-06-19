import streamlit as st
import pandas as pd
from chatbot import property_chatbot
from dotenv import load_dotenv

load_dotenv() # Load your .env file here!

# Path fix for your dataset folder
@st.cache_data
def load_bot_data():
    # If using dataset folder
    return pd.read_csv('dataset/data_viz1.csv')

df = load_bot_data()
property_chatbot(df)











import streamlit as st

st.set_page_config(
    page_title="My first app",
    layout="wide",
)

st.write("My first app")
st.sidebar.success("select a demo above")



