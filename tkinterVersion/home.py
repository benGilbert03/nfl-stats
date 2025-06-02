import tkinter as tk
from tkinter import ttk



# --- GUI Setup ---
root = tk.Tk()
root.title("Rank NFL Players")

options = ['QB', 'RB', 'WR', 'TE']
combo = ttk.Combobox(root, values=options, justify='center')
combo.current(0)
combo.pack(pady=10)



root.mainloop()