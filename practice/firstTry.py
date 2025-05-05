import nfl_data_py as nfl
import pandas as pd

print(pd.DataFrame(nfl.import_depth_charts([2024])).columns)

dc = pd.DataFrame(nfl.import_depth_charts([2024]))

dc = dc[dc['full_name'] == 'Caleb Williams']
print(dc)