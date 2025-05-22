import tkinter as tk
from tkinter import *
from tkinter import ttk
from backend.fetchPlayers import getWeekOneStarters
import pandas as pd
import random as rd

def pickBetweenPlayers():
    allPlayers = getWeekOneStarters([2024], [positionChoices.get()])
    allPlayers = allPlayers.reset_index(drop=True)
    rows = len(allPlayers)

    # In first set of comparisons, go through the list and compare one and two, three and four, and so on
    for i in range(0, rows, 2):
        print(i, ': ', allPlayers.loc[allPlayers.index == i])
        print(i, ': ', allPlayers.iloc[allPlayers.index == i + 1])



    # After first set of comparisons, comparisons should be random until there is, on average 3 to 5 comparisons for each



# Main app window
root = tk.Tk()
root.title("Rank NFL Players")
root.geometry("400x300")

w = Label(root, text='What position do you want to rank?')
w.pack()

options = ['QB', 'WR', 'RB', 'TE', 'OL', 'DL', 'DB', 'LB', 'K', 'P', 'LS']
positionChoices = ttk.Combobox(root, values=options, state="readonly")
positionChoices.current(0)
positionChoices.pack()

tk.Button(root, text='Submit', command=pickBetweenPlayers).pack()


# Should probably get all required data from user, i.e. pick between two players n times, 
# then send it to a function in another file that handles the ranking and returns a list. 
# From there, show the list it returns. 
# Need to get a year too!!!!


# Run the GUI
root.mainloop()
