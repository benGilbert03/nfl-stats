import nfl_data_py as nfl
import pandas as pd

seasonStats = pd.DataFrame(nfl.import_seasonal_data([2024]))

player = seasonStats[seasonStats['player_id'] == '00-0039918']
cols = player.columns

errors = []

for col in cols:
    try:
        print(player[col])
    except KeyError as e:
        errors.append(col)
print()
for error in errors:
    print(error)

#print(seasonStats)