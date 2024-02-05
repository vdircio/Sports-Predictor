import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from urllib.request import urlretrieve
# estimators - built-in machine learning algorithms and models
# estimators can be fitted to some data using its fit method

nba_url = 'https://www.kaggle.com/datasets/vivovinco/2023-2024-nba-player-stats?select=2023-2024+NBA+Player+Stats+-+Regular.csv'
try:
    df = pd.read_csv(nba_url)
    print(df.head())
except Exception as e:
    print("Error:", e)


# clf = RandomForestClassifier(random_state = 0)
# X = [[ 1,  2,  3],  # 2 samples, 3 features
#      [11, 12, 13]]
# y = [0, 1]  # classes of each sample
# clf.fit(X, y)

