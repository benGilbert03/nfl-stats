import tkinter as tk
from tkinter import messagebox
import random

# Main app window
root = tk.Tk()
root.title("Rank NFL Players")
root.geometry("400x300")

# Entry fields for two items
tk.Label(root, text="Item 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Item 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Comparison function
def compare_items():
    item1 = entry1.get()
    item2 = entry2.get()

    if not item1 or not item2:
        messagebox.showwarning("Input Error", "Please enter both items.")
        return

    winner = random.choice([item1, item2])
    result_label.config(text=f"Winner: {winner}")

# Compare button
compare_button = tk.Button(root, text="Compare", command=compare_items)
compare_button.pack(pady=5)

# Run the GUI
root.mainloop()
