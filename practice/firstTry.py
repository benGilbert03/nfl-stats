import nfl_data_py as nfl
import pandas as pd

frame = pd.DataFrame(nfl.import_depth_charts([2024]))

# frame = frame[frame['gsis_id'] == '00-0039918']

frame = frame[frame['last_name'] == 'Bagent']
frame = frame[frame['week'] == 1]
print(frame)