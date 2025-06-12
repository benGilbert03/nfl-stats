import numpy as np

class Player():
    def __init__(self, name, id, position, image, year, elo=1500, stats = None):
        self.name = name
        self.id = id
        self.position = position
        self.image = image
        self.year = year
        self.elo = elo

    def calculateElo(self, points, games):
        stat = points / games
        



