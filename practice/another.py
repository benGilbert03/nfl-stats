import nfl_data_py as nfl
import pandas as pd

seasonStats = pd.DataFrame(nfl.import_seasonal_data([2024]))

# (For 2024 at least)
# Caleb Williams gsis_id = 00-0039918
# pfr_id = WillCa03

# Rome Odunze
# gsis_id = 00-0039919
# pfr_id = OdunRo00

player = seasonStats[seasonStats['player_id'] == '00-0039918']
cols = player.columns

errors = []

# for col in cols:
#     try:
#         print(player[col])
#     except KeyError as e:
#         errors.append(col)
# print()
# for error in errors:
#     print(error)

#print(seasonStats)

# df = pd.DataFrame(nfl.import_ids())
# df = df[df['gsis_id'] == '00-0039918']
# print(df['pfr_id'])

# df = pd.DataFrame(nfl.import_ids())
# df = df[df['position'] == 'WR']
# df = df[df['team'] == 'CHI']
# print(df)

df = pd.DataFrame(nfl.import_ids())
print(df)