from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import os
import pprint
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix

p = pprint.PrettyPrinter( indent=4,compact=True)
path=os.getcwd()


def get_stacking_base_datasets(model, X_train_n, y_train_n, X_test_n, n_folds):
    kf = KFold(n_splits=n_folds, shuffle=True, random_state=11)
    # 빈 배열 생성
    train_fold_pred = np.zeros((X_train_n.shape[0], 1))
    test_pred = np.zeros((X_test_n.shape[0], n_folds))

    for folder_counter, (train_index, valid_index) in enumerate(kf.split(X_train_n)):
        print('폴드 세트 : ', folder_counter, ' 시작')
        X_tr = X_train_n[train_index]
        y_tr = y_train_n[train_index]
        X_te = X_train_n[valid_index]

        # 폴드 내 모델 학습
        model.fit(X_tr, y_tr)
        train_fold_pred[valid_index, :] = model.predict(X_te).reshape(-1, 1)  # y_train 예측, 폴드 끝나면 concat해야함
        test_pred[:, folder_counter] = model.predict(X_test_n)  # y_test 예측, 폴드 끝나면 평균 낼거임

    test_pred_mean = np.mean(test_pred, axis=1).reshape(-1, 1)

    return train_fold_pred, test_pred_mean  # 하나의 모델에 대한 학습데이터, 테스트 데이터 생성

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

### 개별 모델
knn_clf = KNeighborsClassifier(n_neighbors = 1)
rf_clf = RandomForestClassifier(random_state=40,max_depth=17, n_estimators=13 ,max_features=34)
dt_clf = DecisionTreeClassifier(random_state=40,max_depth=15,max_features=30,min_samples_split=25)
ada_clf = AdaBoostClassifier()
lr_final = LogisticRegression()

### 개별 모델 적용
knn_train, knn_test = get_stacking_base_datasets(knn_clf, X_train, y_train, X_test, 5)
rf_train, rf_test = get_stacking_base_datasets(rf_clf, X_train, y_train, X_test, 5)
dt_train, dt_test = get_stacking_base_datasets(dt_clf, X_train, y_train, X_test, 5)
ada_train, ada_test = get_stacking_base_datasets(ada_clf, X_train, y_train, X_test, 5)

# 개별 모델로부터 나온 y_train 예측값들 옆으로 붙이기
Stack_final_X_train = np.concatenate((knn_train,rf_train,dt_train,ada_train), axis=1)
# 개별 모델로부터 나온 y_test 예측값들 옆으로 붙이기
Stack_final_X_test = np.concatenate((knn_test,rf_test,dt_test,ada_test), axis=1)


rf_clf.fit(Stack_final_X_train, y_train)
#stack_final = lr_final.predict(Stack_final_X_test)

### score 확인
print("훈련 세트 정확도: {:.3f}".format(rf_clf.score(Stack_final_X_train, y_train)))
print("테스트 세트 정확도: {:.3f}".format(rf_clf.score(Stack_final_X_test, y_test)))
#print("특성 중요도:\n{}".format(rfc.feature_importances_))


### 라벨 별정확도
y_trainpred=rf_clf.predict(Stack_final_X_train)
print(y_trainpred)

print("Train")
print(confusion_matrix(y_train, y_trainpred))



y_testpred=rf_clf.predict(Stack_final_X_test)

print("Test")
print(confusion_matrix(y_test, y_testpred))


