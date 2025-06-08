import tkinter as tk
from rankPlayers import rank
import math

class DisplayRankingsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        instrLabel = tk.Label(self, text="Rankings", font=('Arial', 14))
        instrLabel.pack(pady=10)

        self.listFrame = tk.Frame(self)
        self.listFrame.pack()


    def displayRankings(self, controller):
        count = 1
        rowInd = 1
        rankedIndexes = rank(comparisons=controller.sharedData['comparisons'], players=controller.sharedData['players'])
        
        for index in rankedIndexes:
            tk.Label(self.listFrame, text=f"{count}: {controller.sharedData['players'].iloc[index[0]]['player_name']}").grid(row=rowInd, column= count // 17 + 1)
            count += 1
            if rowInd < 16:
                rowInd += 1
            else:
                rowInd = 1
















