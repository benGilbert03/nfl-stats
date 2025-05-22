import nfl_data_py as nfl
import pandas as pd


# Returns a dataframe with all players of a certain position in the given year
def getPlayers(years, position):
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
        # return the dataframe
        return players
    else: 
        return None

# Get week one starters (1 QB, 3 RB, 1 TE, 3 WR, 5 OL, 4 DL, 4 DB, 2 LB, 1 K, 1 P, 1 LS)
# Returns a dataframe with the week one starters at the given position or None
# club_code is the the team the player was on week one
def getWeekOneStarters(years, position):
    players = getPlayers(years, position)
    depthCharts = pd.DataFrame(nfl.import_depth_charts(years))
    depthCharts = depthCharts[depthCharts['depth_team'] == '1']

    # merge players and depth charts on id 
    toReturn = players.merge(depthCharts, how='inner', left_on='player_id', right_on='gsis_id')

    # get only week one starters
    toReturn = toReturn[toReturn['week_y'] == 1]
    toReturn.drop_duplicates(subset=['gsis_id'], inplace=True)
    toReturn = toReturn.reset_index(drop='True')

    return toReturn



def printPlayers(players):
    count = 1
    for _, row in players.iterrows():
        if (row['club_code'] == 'CHI'):
            print(count, ":", row['player_name'], ', ', row['club_code'])
        count += 1