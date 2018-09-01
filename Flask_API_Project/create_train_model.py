################
# CREATE MODEL
################

import numpy as np
from sklearn.externals import joblib
from sklearn import linear_model

clf = linear_model.LogisticRegression()
X = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10]]
y = [0,0,0,0,0,1,1,1,1,1]

clf.fit(X,y)
joblib.dump(clf, 'classifier.pkl')
