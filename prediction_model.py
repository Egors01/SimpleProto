import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn import tree

from sklearn.datasets import load_iris
load_irisdata = load_iris()
df = pd.DataFrame(load_irisdata.data, columns=load_irisdata.feature_names)
df['target'] = load_irisdata.target

X_train, X_test, Y_train, Y_test = train_test_split(df[load_irisdata.feature_names], df['target'], random_state=0)
clf = DecisionTreeClassifier(max_depth = 2,
                             random_state = 0,min_samples_split=1)
import os
print(os.getcwd())
df = pd.read_csv('debug_table.tsv',sep='\t')
X_train = df[df.columns.values[:-1]]
Y_train = df[df.columns.values[-1:]]
# Step 3: Train the model on the data
clf.fit(X_train, Y_train)# Step 4: Predict labels of unseen (test) data
# Not doing this step in the tutorial
# clf.predict(X_test)
import matplotlib.pyplot as plt
tree.plot_tree(clf,rounded=True)
plt.show()
fn=['classical leave','single leave','complex shape','roundy shape','sticky','has nuts','water','type']
cn=['oak','maple','birch','jug','ryabina']
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
tree.plot_tree(clf,
               feature_names = fn,
               class_names=cn,
               filled = True)

plt.show()
clf.decision_path(X_test)
tree.plot_tree(clf,rounded=True,class_names=True,proportion=True,feature_names=load_irisdata.feature_names);
print()