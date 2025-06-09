import nfl_data_py as nfl

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
ids = nfl.import_ids(columns = ['gsis_id', 'name'])
ids = ids[ids['name'] == 'Caleb Williams']
# print(ids['gsis_id'])

seasonal = nfl.import_seasonal_data([2024])
seasonal = seasonal[seasonal['player_id'] == '00-0039918']
printRow(seasonal)


def getStats(players):
    pass





