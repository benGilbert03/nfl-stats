import tkinter as tk
from pages.homePage import HomePage
from pages.comparePage import ComparisonsPage
from pages.rankingsPage import DisplayRankingsPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NFL Player Ranking App")
        self.geometry('500x400')

        # Shared Data (between pages) 
        self.sharedData = {
            'comparisons': []
        }

        # Container for all pages
        container = tk.Frame(self)
        container.pack(fill='both', expand=True)

        self.frames = {}

        for F in (HomePage, ComparisonsPage, DisplayRankingsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()