import os
import pandas as pd
import pydotplus
from IPython.display import Image
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_graphviz
#CART stands for Classification And Regression Tree. # read in the CSV file
data = pd.read_csv("drug200.csv")
# encode non-numeric values using label encoding
le = LabelEncoder()
for col in data.columns:
if data[col].dtype == 'object':
data[col] = le.fit_transform(data[col])
# separate the features (X) and target variable
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
# train a CART model
cart_model = DecisionTreeClassifier() cart_model.fit(X, y)
# define class_names`
class_names = ["drugA", "drugB", "drugC", "drugX", "drugY"]
# visualize the resulting decision tree
export_graphviz(cart_model, out_file="tree.dot", feature_names=X.columns, class_names=class_names,rounded=True,filled=True)
# set the PATH variable for Graphviz
os.environ["PATH"] += os.pathsep + '/usr/local/Cellar/graphviz/2.49.0/bin' # convert the DOT file to a PNG image
graph = pydotplus.graph_from_dot_file("tree.dot") # save the image to a file
graph.write_png("tree.png")
# display the image
Image(graph.create_png())