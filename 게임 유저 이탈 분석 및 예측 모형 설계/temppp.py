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
from sklearn.model_selection import train_test_split
import os
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

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
rfc = LogisticRegression()
#(random_state=40,max_depth=15,max_features=30,min_samples_split=25)

rfc.fit(X_train, y_train)

### score 확인
print("훈련 세트 정확도: {:.3f}".format(rfc.score(X_train, y_train)))
print("테스트 세트 정확도: {:.3f}".format(rfc.score(X_test, y_test)))
#print("특성 중요도:\n{}".format(rfc.feature_importances_))


### 라벨 별정확도
y_trainpred=rfc.predict(X_train)


print("Train")
print(confusion_matrix(y_train, y_trainpred))



y_testpred=rfc.predict(X_test)

print("Test")
print(confusion_matrix(y_test, y_testpred))

