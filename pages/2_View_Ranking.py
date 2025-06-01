import streamlit as st
import pandas as pd
from data import get_comparisons

st.title("Player Rankings")

df = get_comparisons()

if df.empty:
    st.info("No comparisons yet")
else:
    win_counts = df['Winner'].value_counts().reset_index()
    win_counts.columns = ['Player', 'Wins']
    st.dataframe(win_counts)