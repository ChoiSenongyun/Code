from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pprint
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold

import os

p = pprint.PrettyPrinter( indent=4,compact=True)
path=os.getcwd()

### random forest에 쓰일 최종 column
train_pd=pd.read_csv("final2.csv")

train_np=train_pd.to_numpy()
columns=train_pd.columns

print(columns)

### train, test 데이터로 분리
data=train_pd.drop(['Unnamed: 0.1','Unnamed: 0','acc_id','label','newlabel'],axis='columns')
columnname=data.columns
print(columnname)
print(len(columnname))
data=data.to_numpy()
target=train_pd['newlabel']
target=target.to_numpy()
X_train, X_test, y_train, y_test = train_test_split(data, target, stratify=target, random_state=40)


### RandomForest
rfc = RandomForestClassifier(random_state=40,max_depth=17, n_estimators=13 ,max_features=34)
#10,11,6/19,14,6/33,14,6
#10,12,5/20,15,6/30,20,6
skf=StratifiedKFold(n_splits=5,shuffle=True,random_state=40)
score=cross_val_score(rfc,data,target,cv=skf)
print(score)
print(score.mean())



