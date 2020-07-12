import os

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.tree import export_text
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from constants import *
from tree_parser import DecisionTreeParser
print(os.getcwd())



clf = DecisionTreeClassifier(random_state = 0,max_features=5)

df = pd.read_csv('data_table.tsv',sep='\t')
X_train = df[df.columns.values[3:-4]]
Y_train = df['target']
clf.fit(X_train, Y_train)
string = export_text(clf)
questions = [questions_dict[name] for name in feature_names]

# Plot TREE
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (50,50), dpi=200)
plot_tree(clf,
               feature_names = questions,
               class_names=df['name'],filled=True,proportion=False,
                fontsize=20,node_ids = True,rounded=True)
plt.savefig('decision_tree.png')
plt.show()

# Follow the path on the TREE


decision_guide = DecisionTreeParser(string,feature_names)
result_clf = decision_guide.get_first_question()
seq = []
i=0

print('info: is leaf', result_clf.is_leaf, 'QQ: ', result_clf.current_question, 'QN: ', result_clf.next_question)
while not result_clf.is_leaf:
    result_clf = decision_guide.update_classification(seq)

print('Result ', result_clf.is_leaf, result_clf.target_name, 'in ', i)

