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
#train_payment= pd.read_csv(path+'\\final_data_rev\\train\\train_payment.csv', sep =',' )
train_trade= pd.read_csv(path+'\\final_data_rev\\train\\train_trade.csv', sep =',' )

### scaling
item_amount=train_trade['item_amount'].to_numpy()
item_amount=item_amount.reshape(-1,1)
train_trade['item_amount']=minmax_scaler.fit_transform(item_amount)


### payment_amount 확인
pp.pprint(train_trade.describe()['item_amount'].T)

train_label['item_amount']=0
for j in range(len(train_label)):
    index1 = train_trade['source_acc_id'].str.contains(train_label['acc_id'].loc[j])
    index2 = train_trade['target_acc_id'].str.contains(train_label['acc_id'].loc[j])
    summ=train_trade[index1]['item_amount'].sum()+train_trade[index2]['item_amount'].sum()
    print(j,summ)
    train_label['item_amount'].iloc[j] = summ

train_label.to_csv('train_labeltrade.csv')