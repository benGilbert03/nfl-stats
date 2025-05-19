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

# Get week one starters (1 QB, 1 RB, 1 TE, 3 WR, )
# Returns a dataframe with the week one starters at the given position or None
def getWeekOneStarters(years, position):
    players = getPlayers(years, position)
    depthCharts = pd.DataFrame(nfl.import_depth_charts(years))
    depthCharts = depthCharts[depthCharts['depth_team'] == '1']

    # merge players and depth charts on id 
    toReturn = players.merge(depthCharts, how='inner', left_on='player_id', right_on='gsis_id')

    # print(toReturn.columns)
    # print(depthCharts.columns)
    
    # get only week one starters
    toReturn = toReturn[toReturn['week_y'] == 1]

    return toReturn



def printPlayers(players):
    count = 1
    for _, row in players.iterrows():
        print(count, ":", row['player_name'])
        count += 1




# print(printPlayers(getWeekOneStarters([2024], ['QB'])))

frame = getWeekOneStarters([2024], ['QB'])
print(frame)


# for _, row in frame.iterrows():
#     print(row.to_dict())
#     print()