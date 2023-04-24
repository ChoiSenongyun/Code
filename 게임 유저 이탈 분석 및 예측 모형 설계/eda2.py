import os
import pandas as pd
import pprint as pp
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler
import seaborn as sns

minmax_scaler = MinMaxScaler()
robust_scaler = RobustScaler()
stand_scaler = StandardScaler()
pp=pp.PrettyPrinter()
path=os.getcwd()

### data 불러오기
#train_activity= pd.read_csv(path+'\\final_data_rev\\train\\train_activity.csv', sep =',' )
train_label= pd.read_csv(path+'\\final_data_rev\\train\\train_label.csv', sep =',' )
#train_guild= pd.read_csv(path+'\\final_data_rev\\train\\train_guild.csv', sep =',' )
#train_party= pd.read_csv(path+'\\final_data_rev\\train\\train_party.csv', sep =',' )
train_payment= pd.read_csv(path+'\\final_data_rev\\train\\train_payment.csv', sep =',' )
#train_trade= pd.read_csv(path+'\\final_data_rev\\train\\train_trade.csv', sep =',' )

### 문파 소속 여부 확인 하는 csv 생성
"""
train_label['retained'],train_label['week'],train_label['month'],train_label['2month'],train_label['cnt_guild']=0,0,0,0,0
for j in range(len(train_label)):
    index = train_guild['guild_member_acc_id'].str.contains(train_label['acc_id'].loc[j])
    r,w,m,mm=0,0,0,0
    count=len(train_guild[index])
    print(j,train_guild[index])
    for i in range(count):
        temp=train_guild[index].iloc[i]['guild_member_acc_id'].split(',')
        for id in temp:
            templabel=train_label[train_label['acc_id']==id]['label'].values
            print(templabel)
            if len(templabel) >= 1:
                if templabel == 'week':
                    w += 1
                elif templabel == 'retained':
                    r += 1
                elif templabel == 'month':
                    m += 1
                elif templabel == '2month':
                    mm += 1
    train_label['retained'].iloc[j]=r
    train_label['week'].iloc[j] = w
    train_label['month'].iloc[j] = m
    train_label['2month'].iloc[j] = mm
    train_label['cnt_guild'].iloc[j] = count
train_label.to_csv('train_labelguild.csv')
"""

#train_labelguild= pd.read_csv(path+'\\final_data_rev\\train\\train_labelguild.csv', sep =',' )

### 가입한 길드 갯수
"""
plt.subplot(1,4,1)
sns.countplot(x='cnt_guild',data=train_labelguild[train_labelguild['label']=='retained'])
plt.title('retained')
plt.ylabel('')
plt.subplot(1,4,2)
sns.countplot(x='cnt_guild',data=train_labelguild[train_labelguild['label']=='week'])
plt.title('week')
plt.ylabel('')
plt.subplot(1,4,3)
sns.countplot(x='cnt_guild',data=train_labelguild[train_labelguild['label']=='month'])
plt.title('month')
plt.ylabel('')
plt.subplot(1,4,4)
sns.countplot(x='cnt_guild',data=train_labelguild[train_labelguild['label']=='2month'])
plt.title('2month')
plt.ylabel('')
plt.show()
"""

#### 결제정보

### scaling
payment_amount=train_payment['payment_amount'].to_numpy()
payment_amount=payment_amount.reshape(-1,1)
train_payment['payment_amount']=robust_scaler.fit_transform(payment_amount)

### 평균, 합 구하기
#avg_train_payment=train_payment.groupby('acc_id',as_index=False).mean()
sum_train_payment=train_payment.groupby('acc_id',as_index=False).sum()

### label값 대입
train_payment=pd.merge(train_payment,train_label,on="acc_id")
sum_train_payment=pd.merge(sum_train_payment,train_label,on="acc_id")

### payment_amount 확인
pp.pprint(sum_train_payment.groupby('label').describe()['payment_amount'].T)


plt.subplot(1,4,1)
plt.hist(sum_train_payment[sum_train_payment['label']=='retained']['payment_amount'],edgecolor='black',color='red')
plt.title('retained')
plt.ylabel('')
plt.subplot(1,4,2)
plt.hist(sum_train_payment[sum_train_payment['label']=='week']['payment_amount'],edgecolor='black',color='yellow')
plt.title('week')
plt.ylabel('')
plt.subplot(1,4,3)
plt.hist(sum_train_payment[sum_train_payment['label']=='month']['payment_amount'],edgecolor='black',color='green')
plt.title('month')
plt.ylabel('')
plt.subplot(1,4,4)
plt.hist(sum_train_payment[sum_train_payment['label']=='2month']['payment_amount'],edgecolor='black',color='orange')
plt.title('2month')
plt.ylabel('')
plt.show()