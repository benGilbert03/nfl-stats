import nfl_data_py as nfl
from fetchPlayers import getWeekOneStarters

# Helper method that prints a row of a dataframe
def printRow(row):
    for col in row.columns:
        print(row[col])

# ------------ import_seasonal_pfr ----------------
# Gives useful, more advanced stats, but not everything (gives on target throw percentage, bad throw percentage, missing things like yards per game)
# print(nfl.import_seasonal_pfr('pass', [2024]).columns)

# passing = nfl.import_seasonal_pfr('pass', [2024])
# passing = passing[passing['player'] == 'Caleb Williams']
# print(passing)
# printRow(passing)


# -------------- import_ngs_data --------------------
# Also has helpful advanced stats (completion percentage over expected)
# ngsData = nfl.import_ngs_data(years=[2024], stat_type='rushing')
# print(ngsData.columns)


# ------------- import_seasonal_data ----------------
# Need gsis_id to access (called player_id in season_data df, get from import_ids)
# Has counting stats
# ids = nfl.import_ids(columns = ['gsis_id', 'name'])
# ids = ids[ids['name'] == 'Caleb Williams']
# print(ids['gsis_id'])

seasonal = nfl.import_seasonal_data([2024])
seasonal = seasonal[seasonal['player_id'] == '00-0039918']
# printRow(seasonal)

# Returns a dataframe with the stats used to determine an initial elo rating
def getStats(players):
    data = nfl.import_seasonal_data([int(players.iloc[0]['year'])])
    data = data[['player_id', 'fantasy_points_ppr', 'games']]
    for _, player in players.iterrows():
        id = player['player_id']
        print(id)

    # if players.iloc[0]['position'] == 'QB':
    #     pass            
    # elif players.iloc[0]['position'] == 'RB':
    #     pass
    # elif players.iloc[0]['position'] == 'WR':
    #     pass
    # elif players.iloc[0]['position'] == 'TE':
    #     pass
    # else:
    #     return None




print(getStats(getWeekOneStarters([2024], ['QB'])))