import tkinter as tk

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Page One")
        label.pack(pady=10)

        button = tk.Button(self, text="Back to Start", command=lambda: controller.show_frame("StartPage"))
        button.pack()
