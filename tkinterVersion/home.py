import tkinter as tk
from tkinter import ttk



# --- GUI Setup ---
root = tk.Tk()
root.title("Rank NFL Players")
root.geometry('500x400')

tk.Label(root, text='Choose a position that you want to rank', font=('Arial', 18)).pack()

options = ['QB', 'RB', 'WR', 'TE']
posChoiceCombobox = ttk.Combobox(root, values=options, justify='center')
posChoiceCombobox.current(0)
posChoiceCombobox.pack(pady=10)



root.mainloop()