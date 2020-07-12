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
clf = DecisionTreeClassifier(random_state = 0,max_features=5)
import os
print(os.getcwd())
df = pd.read_csv('debug_table.tsv',sep='\t')
X_train = df[df.columns.values[:-1]]
Y_train = df[df.columns.values[-1:]]
# Step 3: Train the model on the data
clf.fit(X_train, Y_train)# Step 4: Predict labels of unseen (test) data
string = tree.export_text(clf)
import matplotlib.pyplot as plt

fn=['classical leave','single leave','complex shape','roundy shape','sticky','has nuts','water','type']
cn=['oak','maple','birch','jug','ryabina']
#fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (25,25), dpi=300)
tree.plot_tree(clf,
               feature_names = fn,
               class_names=cn,
               filled = True)
plt.show()
from random import *


string = tree.export_text(clf)
from tree_parser import DecisionTreeParser
decision_guide = DecisionTreeParser(string,['classical leave',
                                                    'single leave',
                                                    'complex shape',
                                                    'roundy shape',
                                                    'sticky', 'has nuts', 'water'])
result_clf = decision_guide.get_first_question()
seq = []
i=0
seq=[0]
print('info: is leaf', result_clf.is_leaf, 'QQ: ', result_clf.current_question, 'QN: ', result_clf.next_question)
while not result_clf.is_leaf:
    print('iter '+str(i))
    seq.append(1)
    print(seq)

    result_clf = decision_guide.update_classification(seq)
    print('info: is leaf', result_clf.is_leaf,'QQ: ', result_clf.current_question, 'QN: ',result_clf.next_question)
    i += 1
print('Result ', result_clf.is_leaf, result_clf.target_name, 'in ', i)



tree.plot_tree(clf,
               feature_names = fn,
               class_names=cn,
               filled = True)
tree.export_text(clf)
plt.show()
