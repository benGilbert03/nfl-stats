import nfl_data_py as nfl
import pandas as pd

# print(pd.DataFrame(nfl.import_depth_charts([2024])).columns)

# dc = pd.DataFrame(nfl.import_depth_charts([2024]))

# dc = dc[dc['full_name'] == 'Caleb Williams']
# print(dc)

# df = pd.DataFrame(nfl.import_seasonal_pfr('pass', [2024]))
# df = df[df['pfr_id'] == 'WillCa03']
# print(df)

# df = pd.DataFrame(nfl.import_snap_counts([2024]))
# df = df[df['pfr_player_id'] == 'WillCa03']
# print(df)

df = pd.DataFrame(nfl.import_snap_counts([2024]))
df = df[df['pfr_player_id'] == 'OdunRo00']
print(df)