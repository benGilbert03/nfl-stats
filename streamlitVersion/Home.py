import streamlit as st
from fetchPlayers import getWeekOneStarters

if 'players' not in st.session_state:
    st.session_state['players'] = None

st.set_page_config(page_title="NFL Player Rankings", layout="centered")
st.title("NFL Player Rankings App")
st.write("Choose which position you want to rank, then go to Compare Players using the sidebar")

positions = ['QB', 'RB', 'WR', 'TE']
chosenPosition = st.selectbox("Choose One", positions)

def setPosition(pos):
    st.session_state['players'] = getWeekOneStarters([2024], [pos])

st.button(label='Submit Position Choice', on_click=setPosition, args=(chosenPosition,))



# on_click=setPosition, args = (chosenPosition)