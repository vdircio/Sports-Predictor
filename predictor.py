import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from urllib.request import urlretrieve
# estimators - built-in machine learning algorithms and models
# estimators can be fitted to some data using its fit method

pd.set_option('display.max_rows', 10)  # Maximum number of rows to display
pd.set_option('display.max_columns', 10)  # Maximum number of columns to display
pd.set_option('display.width', 100)  # Width of the display in characters


csv_file_path = "2023-2024NBAPlayerStats.csv"
df = pd.read_csv(csv_file_path, encoding='latin1')
    


# clf = RandomForestClassifier(random_state = 0)
# X = [[ 1,  2,  3],  # 2 samples, 3 features
#      [11, 12, 13]]
# y = [0, 1]  # classes of each sample
# clf.fit(X, y)

