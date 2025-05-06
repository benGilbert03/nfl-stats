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

# Get starters
# Based on percentage of snaps played 
# Go through every player at that position and find out who had the most snaps
# Or top n players in snaps
# Returns a dataframe with the top 1 - n players in snap count at a position
def getStarters(years, position):
    players = getPlayers(years, position)
    # Sort players by team so all players on a team are next to each other
    players = players.sort_values(by = 'team')

    #Get ids of players (use pfr_id for snap count
    ids = pd.DataFrame(nfl.import_ids())

    #Get snap counts
    snapCounts = pd.DataFrame(nfl.import_snap_counts(years))
    snapCounts = snapCounts.sort_values(by = 'team')

    # Create a dataframe that holds all players from a team
    team = pd.DataFrame()
    teamIds = pd.DataFrame()
    teamSnapCounts = pd.DataFrame()

    # DataFrame with teams in it to iterate through
    allTeams = pd.DataFrame(nfl.import_team_desc())

    # Dataframe holding all starters for teams by team
    starters = pd.DataFrame()

    # Iterate through ids dataframe and add them to the team dataframe
    for row in allTeams ():
        # Current team to compare to
        currentTeam = row['team']
        team = players[players[team] == currentTeam]
        teamIds = ids[ids[team] == currentTeam]
        teamSnapCounts = snapCounts[snapCounts[ids = teamIds]]


    return None



def printPlayers(players):
    count = 1
    for _, row in players.iterrows():
        print(count, ":", row['player_name'])
        count += 1


# printPlayers(getPlayers([2024], ['DB']))

# print(pd.DataFrame(nfl.import_depth_charts([2024])).columns)

# print(pd.DataFrame(nfl.import_sc_lines([2024])).columns)

print(getStarters([2024], ['QB']))