"""
决策树 
"""
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt
from matplotlib import image as pltimg
import pydotplus
import graphviz

df = pd.read_csv("Machine_learning_tutorial/shows.csv")

d = {"UK":0,"USA":1,"N":2}
df["Nationality"] = df["Nationality"].map(d)
d = {"YES":1,"NO":0}
df["Go"] = df["Go"].map(d)

"""
划分特征列和目标列
"""
features = ["Age","Experience","Rank","Nationality"]
X = df[features]
y = df["Go"]

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X,y)
data = tree.export_graphviz(dtree,out_file = None,feature_names = features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png("Machine_learning_tutorial/decisionTree.png")

img = pltimg.imread("Machine_learning_tutorial/decisionTree.png")
imgplot = plt.imshow(img)
plt.show()