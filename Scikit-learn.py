# DT
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# training dataset
X = np.array([[0,1,1], [1,0,1], [1,1,1], [0,1,1], [0,0,1]])
y = np.array([1,0,1,1,0])

clf =  DecisionTreeClassifier()
clf = clf.fit(X, y) # training a model

# predicting
# test dataset
X_test = np.array([[0, 0, 0], [1, 1, 0]])
y_test = np.array([0, 1])

predicted = clf.predict(X_test)
predicted

# visualizing
from sklearn import tree
import graphviz

dot_data = tree.export_graphviz(clf, filled=True, out_file=None)
graph = graphviz.Source(dot_data)
graph
