import nfl_data_py as nfl
import pandas as pd

# Returns all quarterbacks from given year
def getQuarterbacks(years):
    if (isinstance(years, list)):
        # get rosters for the years provided and put them in a pandas dataframe
        players = pd.DataFrame(nfl.import_seasonal_rosters(years))
    
        # get only the quarterbacks
        qbs = players[players['position'] == 'QB']
    
        return qbs
    else: 
        return None
    

# If 
def getStartingQuarterbacks(years):
    qbs = getQuarterbacks(years)

    
def printPlayers(players):
    count = 1
    for _, row in players.iterrows():
        print(count, ":", row['player_name'])
        count += 1

printPlayers(getQuarterbacks([2024]))