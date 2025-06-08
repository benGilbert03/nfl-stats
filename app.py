import tkinter as tk
from pages.homePage import HomePage
from pages.comparePage import ComparisonsPage
from pages.rankingsPage import DisplayRankingsPage
import pandas as pd

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NFL Player Ranking App")
        self.geometry('600x500')

        # Shared Data (between pages) 
        self.sharedData = {
            'comparisons': [],
            'players': pd.DataFrame(),
            'indexesToCompare': [],
            'comparisons': []
        }

        # Container for all pages
        container = tk.Frame(self)
        container.pack(fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        for F in (HomePage, ComparisonsPage, DisplayRankingsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        # TODO: Uncomment this line once finished developing rankingsPage.py
        self.show_frame("HomePage")
        # self.show_frame('DisplayRankingsPage')


    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()