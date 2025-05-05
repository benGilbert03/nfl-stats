import nfl_data_py as nfl
import pandas as pd

def getPlayers(years, position):
    if (isinstance(years, list) and isinstance(position, list)):
        # get rosters for the years provided and puth them in a data frame
        players = pd.DataFrame(nfl.import_seasonal_rosters(years))

        
        for p in position:
            try:
                players = players[players['position'] == p]
            except KeyError as e:
                print("Error ", e)
            break

    return players

# Get starters
def getStarters(years, position):
    getPlayers(years, position)
    
    
    
    return None



def printPlayers(players):
    count = 1
    for _, row in players.iterrows():
        print(count, ":", row['player_name'])
        count += 1


#printPlayers(getPlayers([2024], ['WR']))

print(pd.DataFrame(nfl.import_depth_charts([2024])).columns)