import pandas as pd
from sklearn.ensemble import RandomForestClassifier
# estimators - built-in machine learning algorithms and models
# estimators can be fitted to some data using its fit method

clf = RandomForestClassifier(random_state = 0)
X = [[ 1,  2,  3],  # 2 samples, 3 features
     [11, 12, 13]]
y = [0, 1]  # classes of each sample
clf.fit(X, y)

