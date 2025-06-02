import pandas as pd
import streamlit as st

if 'comparisons' not in st.session_state:
    st.session_state['comparisons'] = []

def add_comparison(winner, loser):
    st.session_state['comparisons'].append((winner, loser))

def get_comparisons():
    return pd.DataFrame(st.session_state['comparisons'], columns=['Winner', 'Loser'])