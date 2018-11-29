import pandas as pd
import numpy as np
import graphviz

from sklearn import tree
from sklearn.datasets import load_wine

data = load_wine()

df = pd.DataFrame(data.data, columns = data.feature_names)

data = df.loc[:, df.columns != 'alcohol']
target = df['alcohol']

X = data
y = target.astype('int') #Algo disliked floats so turned to int
#It worked but shouldn't do this often. 


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("wineTree") 