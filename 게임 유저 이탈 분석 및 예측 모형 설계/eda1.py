import os
import pandas as pd
import pprint as pp
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
import seaborn as sns

minmax_scaler = MinMaxScaler()
robust_scaler = RobustScaler()
pp=pp.PrettyPrinter()
path=os.getcwd()

### data 불러오기
train_activity= pd.read_csv(path+'\\final_data_rev\\train\\train_activity.csv', sep =',' )
train_label= pd.read_csv(path+'\\final_data_rev\\train\\train_label.csv', sep =',' )
#train_guild= pd.read_csv(path+'\\final_data_rev\\train\\train_guild.csv', sep =',' )
#train_party= pd.read_csv(path+'\\final_data_rev\\train\\train_party.csv', sep =',' )
#train_payment= pd.read_csv(path+'\\final_data_rev\\train\\train_payment.csv', sep =',' )
#train_trade= pd.read_csv(path+'\\final_data_rev\\train\\train_trade.csv', sep =',' )

### scaling
#### play_time minmax
play_time=train_activity['play_time'].to_numpy()
play_time=play_time.reshape(-1,1)
train_activity['play_time']=minmax_scaler.fit_transform(play_time)

#### cnt_enter_raid minmax
cnt_enter_raid=train_activity['cnt_enter_raid'].to_numpy()
cnt_enter_raid=cnt_enter_raid.reshape(-1,1)
train_activity['cnt_enter_raid']=robust_scaler.fit_transform(cnt_enter_raid)
#### cnt_clear_raid minmax
cnt_clear_raid=train_activity['cnt_clear_raid'].to_numpy()
cnt_clear_raid=cnt_clear_raid.reshape(-1,1)
train_activity['cnt_clear_raid']=robust_scaler.fit_transform(cnt_clear_raid)
#### cnt_enter_raid_light robust
cnt_enter_raid_light=train_activity['cnt_enter_raid_light'].to_numpy()
cnt_enter_raid_light=cnt_enter_raid_light.reshape(-1,1)
train_activity['cnt_enter_raid_light']=robust_scaler.fit_transform(cnt_enter_raid_light)



#### cnt_enter_inzone_light robust
cnt_enter_inzone_light=train_activity['cnt_enter_inzone_light'].to_numpy()
cnt_enter_inzone_light=cnt_enter_inzone_light.reshape(-1,1)
train_activity['cnt_enter_inzone_light']=robust_scaler.fit_transform(cnt_enter_inzone_light)
#### cnt_enter_inzone_solo robust
cnt_enter_inzone_solo=train_activity['cnt_enter_inzone_solo'].to_numpy()
cnt_enter_inzone_solo=cnt_enter_inzone_solo.reshape(-1,1)
train_activity['cnt_enter_inzone_solo']=robust_scaler.fit_transform(cnt_enter_inzone_solo)
#### cnt_enter_inzone_skilled robust
cnt_enter_inzone_skilled=train_activity['cnt_enter_inzone_skilled'].to_numpy()
cnt_enter_inzone_skilled=cnt_enter_inzone_skilled.reshape(-1,1)
train_activity['cnt_enter_inzone_skilled']=robust_scaler.fit_transform(cnt_enter_inzone_skilled)
#### cnt_enter_inzone_normal robust
cnt_enter_inzone_normal=train_activity['cnt_enter_inzone_normal'].to_numpy()
cnt_enter_inzone_normal=cnt_enter_inzone_normal.reshape(-1,1)
train_activity['cnt_enter_inzone_normal']=robust_scaler.fit_transform(cnt_enter_inzone_normal)


#### getmoney robust  (이상치가 크기 때문)
get_money=train_activity['get_money'].to_numpy()
get_money=get_money.reshape(-1,1)
train_activity['get_money']=robust_scaler.fit_transform(play_time)
"""
#### chat robust
get_money,whisper_chat,district_chat,party_chat=train_activity['get_money'].to_numpy()
get_money=get_money.reshape(-1,1)
train_activity['get_money']=robust_scaler.fit_transform(play_time)
"""



### 평균, 합 구하기
#avg_train_activity=train_activity.groupby('acc_id',as_index=False).mean()
sum_train_activity=train_activity.groupby('acc_id',as_index=False).sum()

### 접속한 주 구하기
sum_train_activity['cnt_week']=train_activity.groupby('acc_id',as_index=False).count()['making_cnt']

### label값 대입
train_activity=pd.merge(train_activity,train_label,on="acc_id")
sum_train_activity=pd.merge(sum_train_activity,train_label,on="acc_id")

"""
pp.pprint(sum_train_activity.groupby('label').describe()['cnt_clear_inzone_light'].T)
plt.scatter(sum_train_activity['label'],sum_train_activity['cnt_clear_inzone_light'],s=1)
plt.show()
"""
### play_time 분석
"""
pp.pprint(sum_train_activity.groupby('label').describe()['play_time'].T)
#plt.scatter(sum_train_activity['label'],sum_train_activity['play_time'],s=1)
plt.boxplot([sum_train_activity[sum_train_activity['label']=='retained']['play_time'],
            sum_train_activity[sum_train_activity['label']=='week']['play_time'],
             sum_train_activity[sum_train_activity['label']=='month']['play_time'],
             sum_train_activity[sum_train_activity['label']=='2month']['play_time']],
            showmeans=True,labels=['retained', 'week', 'month', '2month'])
plt.ylabel('play_time')
plt.show()
"""

### cnt_dt 분석
"""
pp.pprint(sum_train_activity.groupby('label').describe()['cnt_dt'].T)
#plt.scatter(sum_train_activity['label'],sum_train_activity['cnt_dt'],s=1)
plt.boxplot([sum_train_activity[sum_train_activity['label']=='retained']['cnt_dt'],
            sum_train_activity[sum_train_activity['label']=='week']['cnt_dt'],
             sum_train_activity[sum_train_activity['label']=='month']['cnt_dt'],
             sum_train_activity[sum_train_activity['label']=='2month']['cnt_dt']],
            showmeans=True,labels=['retained', 'week', 'month', '2month'])

plt.ylabel('cnt_dt')
plt.show()
"""

### 접속한 주 갯수
"""
plt.subplot(1,4,1)
sns.countplot(x='cnt_week',data=sum_train_activity[sum_train_activity['label']=='retained'])
plt.title('retained')
plt.ylabel('')
plt.subplot(1,4,2)
sns.countplot(x='cnt_week',data=sum_train_activity[sum_train_activity['label']=='week'])
plt.title('week')
plt.ylabel('')
plt.subplot(1,4,3)
sns.countplot(x='cnt_week',data=sum_train_activity[sum_train_activity['label']=='month'])
plt.title('month')
plt.ylabel('')
plt.subplot(1,4,4)
sns.countplot(x='cnt_week',data=sum_train_activity[sum_train_activity['label']=='2month'])
plt.title('2month')
plt.ylabel('')
plt.show()
"""

### 라이트 인던 입장 횟수
"""
pp.pprint(sum_train_activity.groupby('label').describe()['cnt_enter_inzone_light'].T)
#plt.scatter(sum_train_activity['label'],sum_train_activity['cnt_enter_inzone_light'],s=1)
plt.boxplot([sum_train_activity[sum_train_activity['label']=='retained']['cnt_enter_inzone_light'],
            sum_train_activity[sum_train_activity['label']=='week']['cnt_enter_inzone_light'],
             sum_train_activity[sum_train_activity['label']=='month']['cnt_enter_inzone_light'],
             sum_train_activity[sum_train_activity['label']=='2month']['cnt_enter_inzone_light']],
            showmeans=True,labels=['retained', 'week', 'month', '2month'])
plt.ylabel('cnt_enter_inzone_light')
plt.show()
"""

### 숙련 인던 입장 횟수
"""
pp.pprint(sum_train_activity.groupby('label').describe()['cnt_enter_inzone_skilled'].T)
#plt.scatter(sum_train_activity['label'],sum_train_activity['cnt_enter_inzone_light'],s=1)
plt.boxplot([sum_train_activity[sum_train_activity['label']=='retained']['cnt_enter_inzone_skilled'],
            sum_train_activity[sum_train_activity['label']=='week']['cnt_enter_inzone_skilled'],
             sum_train_activity[sum_train_activity['label']=='month']['cnt_enter_inzone_skilled'],
             sum_train_activity[sum_train_activity['label']=='2month']['cnt_enter_inzone_skilled']],
            showmeans=True,labels=['retained', 'week', 'month', '2month'])
plt.ylabel('cnt_enter_inzone_skilled')
plt.show()
"""

"""
### 레이드 횟수 분석
pp.pprint(sum_train_activity.groupby('label').describe()['cnt_enter_inzone_normal'].T)
plt.scatter(sum_train_activity['label'],sum_train_activity['cnt_enter_inzone_normal'],s=1)
plt.show()
### 레이드 횟수 분석
pp.pprint(sum_train_activity.groupby('label').describe()['cnt_enter_inzone_light'].T)
plt.scatter(sum_train_activity['label'],sum_train_activity['cnt_enter_inzone_light'],s=1)
plt.show()
### 레이드 횟수 분석
pp.pprint(sum_train_activity.groupby('label').describe()['cnt_enter_inzone_skilled'].T)
plt.scatter(sum_train_activity['label'],sum_train_activity['cnt_enter_inzone_skilled'],s=1)
plt.show()
### 레이드 횟수 분석
pp.pprint(sum_train_activity.groupby('label').describe()['cnt_enter_inzone_solo'].T)
plt.scatter(sum_train_activity['label'],sum_train_activity['cnt_enter_inzone_solo'],s=1)
plt.show()
"""


