import streamlit as st
from rankPlayers import addComparison
from rankPlayers import rank
import pandas as pd
import random as rd

if 'cols' not in st.session_state:
    st.session_state['cols'] = [1,2]


# Adds winner to list of comparisons
def choiceMade(winner, loser):
    st.session_state['cols'][0] += 1
    st.session_state['cols'][1] += 1
    addComparison(winner, loser)
    nextPair()
    return

# Moves on to next pair of players to compare and adds comparison to list of comparisons
def nextPair():
    if not st.session_state['indexesToCompare'] == []:
        pair = st.session_state['indexesToCompare'][0]
        st.session_state['indexesToCompare'].pop(0)

        index1 = pair[0]
        index2 = pair[1]
        player1 = st.session_state['players'].iloc[index1]
        player2 = st.session_state['players'].iloc[index2]

        col1, col2 = st.columns(2, gap='large')

        with col1:
            st.image(player1['headshot_url'])
            
        with col2:
            st.image(player2['headshot_url'])
            
        st.divider()
        col3, col4 = st.columns(2, gap='large')

        
        with col3:
            st.button(label=player1['full_name'], key=f'col{st.session_state['cols'][0]}', use_container_width=True, on_click=choiceMade, args=(index1, index2))
        with col4:
            st.button(label=player2['full_name'], key=f'col{st.session_state['cols'][1]}', use_container_width=True, on_click=choiceMade, args=(index2, index1))
    else:
        return



st.title("Compare Two NFL Players")

if st.session_state['players'].empty:
    st.info('Choose a position first')
else :
    st.write("Click the button under the player you think is better. Once you complete enough comparisons, you will be able to see your rankings.")

    # Create a list of the players to be compared (needs to have 4 * n comparisons)
    st.session_state['indexesToCompare'] = []
    n = len(st.session_state['players'])
    for i in range(0, n, 2):
        st.session_state['indexesToCompare'].append((i, i+2))


    for i in range(0, 3 * n):
        p1 = rd.randint(0, n)
        p2 = rd.randint(0, n)

        while p1 == p2:
            p2 = rd.randint(0, n)

        while (p1, p2) in st.session_state['indexesToCompare']:
            p2 = rd.randint(0, n)
        st.session_state['indexesToCompare'].append((p1, p2))

    st.divider()

    if not st.session_state['indexesToCompare'] == []:
        nextPair()
    
    if st.session_state['indexesToCompare']  == []:
        st.success('You have done all required comparisons!')
        tp1, tp2 = rank()
        st.write('normalized strengths: ', tp1)
        st.write('ranked items: ', tp2)
        
        



    

