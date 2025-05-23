import tkinter as tk
from comparePlayers import comparePlayers
from rankings import rankings

class App(tk.Tk):
    def __init__(self): 
        super().__init__()
        self.title("Rank NFL Players at Positions")

        self.shared_data = {}

        container = tk.Frame(self)
        container.pack(fill="both", expand = True)

        self.frames = {}

        for F in (comparePlayers, Rankings):
            page = F(parent=container, controller=self)
            self.frames[F.__name__] = page
            page.grid(row=0, column=0, stikcy="nsew")
        
        self.show_frame("comparePlayers")