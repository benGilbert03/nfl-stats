import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk
import random as rd
import math

class ComparisonsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        instrLabel = tk.Label(self, text="Click on the player you think is better", font=('Arial', 14))
        instrLabel.pack(pady=10)

        self.imagesFrame = None
        self.buttonsFrame = None
        self.count = 0

        
    def makeChoice(self, winningPlayerIndex, losingPlayerIndex, controller):
        self.count += 1 
        print(f'{self.count}: ({winningPlayerIndex}, {losingPlayerIndex})')
        controller.sharedData['comparisons'].append((winningPlayerIndex, losingPlayerIndex))
        controller.sharedData['indexesToCompare'].pop(0)
        if (len(controller.sharedData['indexesToCompare']) == 0):
            rankPage = controller.frames['DisplayRankingsPage']
            controller.show_frame('DisplayRankingsPage')
            rankPage.displayRankings(controller)
        else:
            self.displayPair(controller)
        
    

    def displayPair(self, controller):
        p1Index, p2Index = controller.sharedData['indexesToCompare'][0]
        
        player1 = controller.sharedData['players'].iloc[p1Index]
        player2 = controller.sharedData['players'].iloc[p2Index]

        p1ImagePath = getImageFromUrl(player1['headshot_url'], size=(300, 225))
        p2ImagePath = getImageFromUrl(player2['headshot_url'], size=(300, 225))
        
        self.p1ImagePath = p1ImagePath
        self.p2ImagePath = p2ImagePath

        if self.imagesFrame:
            self.imagesFrame.destroy()
        if self.buttonsFrame:
            self.buttonsFrame.destroy() 

        self.imagesFrame = tk.Frame(self)
        self.imagesFrame.pack()

        p1Image = tk.Label(self.imagesFrame, image=p1ImagePath)
        p2Image = tk.Label(self.imagesFrame, image=p2ImagePath)
        p1Image.pack(side='left', padx=10)
        p2Image.pack(side='left', padx=10)

        self.buttonsFrame = tk.Frame(self)
        self.buttonsFrame.pack()

        p1Button = tk.Button(self.buttonsFrame, text=player1['player_name'], command=lambda: self.makeChoice(p1Index, p2Index, controller))
        p2Button = tk.Button(self.buttonsFrame, text=player2['player_name'], command=lambda: self.makeChoice(p2Index, p1Index, controller))
        p1Button.pack(side='left', padx=120)
        p2Button.pack(side='right', padx=80)
        return

    def loopThroughPlayers(self, controller):
        if 'indexesToCompare' not in controller.sharedData:
            controller.sharedData['indexesToCompare'] = []
        if 'comparisons' not in controller.sharedData:
            controller.sharedData['comparisons'] = []

        # first pass (0 and 1, 2 and 3, etc...)
        for i in range(0, len(controller.sharedData['players']) - 1, 2):
            controller.sharedData['indexesToCompare'].append((i, i+1))

        # Second and third: random players that aren't already being compared
        for i in range(0, math.ceil(len(controller.sharedData['players']) * 3.5)):
            p1Index = rd.randrange(0, len(controller.sharedData['players']))
            p2Index = rd.randrange(0, len(controller.sharedData['players']))

            while (p1Index == p2Index or (p1Index, p2Index) in controller.sharedData['indexesToCompare'] or (p2Index, p1Index) in controller.sharedData['indexesToCompare']):
                p1Index = rd.randrange(0, len(controller.sharedData['players']))
                p2Index = rd.randrange(0, len(controller.sharedData['players']))
                
            controller.sharedData['indexesToCompare'].append((p1Index, p2Index))

        self.displayPair(controller)
        

def getImageFromUrl(url, size=None):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    if size:
        image = image.resize(size)
    return ImageTk.PhotoImage(image)

# 26 comparisons it stopped working and gave this error:
# Exception in Tkinter callback
# Traceback (most recent call last):
#   File "C:\Python312\Lib\tkinter\__init__.py", line 1968, in __call__
#     return self.func(*args)
#            ^^^^^^^^^^^^^^^^
#   File "C:\Users\ben03\personal-projects\nfl-stats\pages\comparePage.py", line 61, in <lambda>
#     p1Button = tk.Button(self.buttonsFrame, text=player1['player_name'], command=lambda: self.makeChoice(player1, player2, controller))
#                                                                                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\ben03\personal-projects\nfl-stats\pages\comparePage.py", line 29, in makeChoice
#     self.displayPair(controller)
#   File "C:\Users\ben03\personal-projects\nfl-stats\pages\comparePage.py", line 36, in displayPair
#     player1 = controller.sharedData['players'].iloc[p1Index]
#               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
#   File "C:\Users\ben03\AppData\Roaming\Python\Python312\site-packages\pandas\core\indexing.py", line 1073, in __getitem__
#     return self._getitem_axis(maybe_callable, axis=axis)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\ben03\AppData\Roaming\Python\Python312\site-packages\pandas\core\indexing.py", line 1625, in _getitem_axis
#     self._validate_integer(key, axis)
#   File "C:\Users\ben03\AppData\Roaming\Python\Python312\site-packages\pandas\core\indexing.py", line 1557, in _validate_integer
#     raise IndexError("single positional indexer is out-of-bounds")
# IndexError: single positional indexer is out-of-bounds