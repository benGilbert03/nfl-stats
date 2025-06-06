import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk

class ComparisonsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        instrLabel = tk.Label(self, text="Click on the player you think is better", font=('Arial', 14))
        instrLabel.pack(pady=10)

        

        


    def makeChoice(self, winningPlayer, losingPlayer, controller): 
        print(winningPlayer['player_name'], ' ', losingPlayer['player_name'])
        controller.sharedData['readyForNextPair'] = True
    

    def displayPair(self, player1, player2, controller):
        p1ImagePath = getImageFromUrl(player1['headshot_url'], size=(300, 225))
        p2ImagePath = getImageFromUrl(player2['headshot_url'], size=(300, 225))
        
        self.p1ImagePath = p1ImagePath
        self.p2ImagePath = p2ImagePath

        imagesFrame = tk.Frame(self)
        imagesFrame.pack()

        p1Image = tk.Label(imagesFrame, image=p1ImagePath)
        p2Image = tk.Label(imagesFrame, image=p2ImagePath)
        p1Image.pack(side='left', padx=10)
        p2Image.pack(side='left', padx=10)

        buttonsFrame = tk.Frame(self)
        buttonsFrame.pack()

        p1Button = tk.Button(buttonsFrame, text=player1['player_name'], command=lambda: self.makeChoice(player1, player2, controller))
        p2Button = tk.Button(buttonsFrame, text=player2['player_name'], command=lambda: self.makeChoice(player2, player1, controller))
        p1Button.pack(side='left')
        p2Button.pack(side='right')

    # TODO: Doesn't progress to next pair. Trying to use boolean in shared data 
    def loopThroughPlayers(self, controller):
        # first pass (0 and 1, 2 and 3, etc...)
        for i in range(0, len(controller.sharedData['players']), 2):
            if (controller.sharedData['readyForNextPair']):
                self.displayPair(controller.sharedData['players'].iloc[i], controller.sharedData['players'].iloc[i+1], controller)
            controller.sharedData['readyForNextPair'] = False

        for i in range(0, len(controller.sharedData['players']) * 2):
            pass


def getImageFromUrl(url, size=None):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    if size:
        image = image.resize(size)
    return ImageTk.PhotoImage(image)