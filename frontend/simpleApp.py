import tkinter as tk
from tkinter import messagebox
import random
from backend.fetchPlayers import getWeekOneStarters


# Main app window
root = tk.Tk()
root.title("Rank NFL Players")
root.geometry("400x300")


# print(getWeekOneStarters([2024], ['QB']))


# Run the GUI
root.mainloop()
