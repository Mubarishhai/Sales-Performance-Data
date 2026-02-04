import streamlit as st
import matplotlib.pyplot as plt
from step import load_and_clean_data  # 👈 import your cleaning function

st.set_page_config(page_title="Sales Dashboard", layout="wide")

@st.cache_data
def load_data():
    return load_and_clean_data("sales_data_sample.csv")

df = load_data()
