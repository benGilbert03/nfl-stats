import nfl_data_py as nfl
import pandas as pd
from Classes import Player 


# Returns a dataframe with all players of a certain position in the given year
def __getPlayers(years: list, position: list):
    if (isinstance(years, list) and isinstance(position, list)):
        # get rosters for the years provided and put them in a data frame
        players = pd.DataFrame(nfl.import_seasonal_rosters(years))
        
        # Set the dataframe to only have players at that position
        for p in position:
            try:
                players = players[players['position'] == p]
            except KeyError as e:
                print("Error ", e)
            break

        players = players[['player_name', 'player_id', 'headshot_url', 'week', 'season']]
        return players
    else: 
        return None

# Get week one starters (1 QB, 3 RB, 1 TE, 3 WR, 5 OL, 4 DL, 4 DB, 2 LB, 1 K, 1 P, 1 LS)
# Returns a dataframe with the week one starters at the given position or None
# club_code is the the team the player was on week one
def getWeekOneStarters(years, position):
    players = __getPlayers(years, position)
    depthCharts = pd.DataFrame(nfl.import_depth_charts(years))
    depthCharts = depthCharts[depthCharts['depth_team'] == '1']

    # merge players and depth charts on id 
    toReturn = players.merge(depthCharts, how='inner', left_on='player_id', right_on='gsis_id')

    # get only week one starters
    toReturn = toReturn[toReturn['week_y'] == 1]
    toReturn.drop_duplicates(subset=['gsis_id'], inplace=True)
    toReturn = toReturn.reset_index(drop='True')

    toReturn = toReturn[['player_name', 'player_id', 'headshot_url', 'position', 'season_x', 'club_code']]
    toReturn.rename(columns={'season_x' : 'year'}, inplace=True)

    pList = []

    for _, p in toReturn.iterrows():
        pList.append(Player(name=p['player_name'], id=p['player_id'], position=p['position'], image=p['headshot_url'], year=p['year']))

    return pList



def printPlayers(players):
    count = 1
    for _, row in players.iterrows():
        if (row['club_code'] == 'CHI'):
            print(count, ":", row['player_name'], ', ', row['club_code'], ', ', row['headshot_url'])
        count += 1

# printPlayers(getWeekOneStarters([2024], ['WR']))
p = getWeekOneStarters([2024], ['QB'])
# p = getPlayers([2024], ['QB'])
# print(p)

# print(nfl.import_seasonal_rosters([2024]).columns)