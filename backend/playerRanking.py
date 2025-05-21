import nfl_data_py as nfl
import pandas as pd
import fetchPlayers as fetch

position = input("Enter the position of players you want to rank (QB, WR, RB, etc): ")
year = int(input("Enter the year you want to rank players from: "))

position = [position]
year = [year]

# print(position, year)

players = fetch.getWeekOneStarters(year, position)
print(players)