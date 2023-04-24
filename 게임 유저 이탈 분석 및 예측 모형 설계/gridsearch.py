import graphviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from sklearn.model_selection import GridSearchCV
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pprint
from sklearn.ensemble import RandomForestClassifier
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


### GridSearch

parameters = {'max_depth':list(range(16,18,1)), 'n_estimators':list(range(12,14,1)),  'max_features':list(range(33,37,2)) }

#최고 정확도: 0.8371882645432503

### GridSearch  DecisionTreeClassifier
rfc = RandomForestClassifier(random_state=40)
grid = GridSearchCV(rfc, param_grid=parameters,cv=5)
grid.fit(X_train,y_train)

### 정확도 확인
print('최적 파라미터:', grid.best_params_)
print('최고 정확도:', grid.best_score_)

