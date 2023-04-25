import requests
import pprint
import json
from urllib import parse
import pandas as pd
import numpy as np
import time
import csv
pp=pprint.PrettyPrinter()
### userlist 읽어오기
userlist=pd.read_csv('userlist.csv',names=['name','server','damage','blank'],dtype=object,encoding='CP949')

### 장비 순서
# ['로드','칭호','가죽 상의','가죽 머리어깨','가죽 하의','가죽 신발','가죽 허리','목걸이','팔찌','반지','보조장비','마법석','귀걸이']
### 서버 리스트
serverdic={ '카인': 'cain', '디레지에' : 'diregie' ,  '시로코': 'siroco', '프레이':'prey', '카시야스': 'casillas' , '힐더': 'hilder',
         '안톤': 'anton',  '바칼': 'bakal'}
### 장비 이름, 옵션 담을 리스트
weapon,top,shoulder,bottom,shoe,belt,necklaces,bracelet,ring,assistive,gemstone,earrings=[],[],[],[],[],[],[],[],[],[],[],[]
equipment=[[],[],[],[],[],[],[],[],[],[],[],[]]
for i in range(2800,3000):
    # 계속 반복시 api 오류 발생
    if i!=0 and i%100==0 : time.sleep(5)
    ### 캐릭터 검색
    url='https://api.neople.co.kr/df/servers/'+serverdic[userlist['server'][i]]+'/characters?characterName='+ str(parse.quote(userlist['name'][i]))+'&apikey=pjnFLkjFRlANcG4dfRElCIwSItwUqO3z'
    response=requests.get(url)
    contents=response.text
    contents=json.loads(contents)
    # 캐릭터 검색이 안될 경우는 Nan으로
    if contents['rows']==[] :
        for j in range(13):
            itemname, itemtype, option1, option2, option3, option4, upgradeitem = 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan'
            if j == 0:
                equipment[j].append([itemname, itemtype, option1, option2, option3, option4, upgradeitem])
            elif j > 1:
                equipment[j - 1].append([itemname, itemtype, option1, option2, option3, option4, upgradeitem])
        print(i,"empty")
    else :
        print(i,contents['rows'][0]['serverId'],contents['rows'][0]['characterId'])
        serverId, characterId=contents['rows'][0]['serverId'], contents['rows'][0]['characterId']
        ### 캐릭터 장착 장비
        url='https://api.neople.co.kr/df/servers/'+str(serverId)+'/characters/'+str(characterId)+ \
            '/equip/equipment?apikey=pjnFLkjFRlANcG4dfRElCIwSItwUqO3z'
        response=requests.get(url)
        contents=response.text
        contents=json.loads(contents)
        ### 장비 장착하지 않았을경우
        if contents['equipment']==[]:
            for j in range(13):
                itemname, itemtype, option1, option2, option3, option4, upgradeitem = 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan'
                if j == 0:
                    equipment[j].append([itemname, itemtype, option1, option2, option3, option4, upgradeitem])
                elif j > 1:
                    equipment[j - 1].append([itemname, itemtype, option1, option2, option3, option4, upgradeitem])
            print(i, "empty")
        else :
            for j in range(13):
                print(j)
                try :
                    if j!=1:
                        if contents['equipment'][j]['itemAvailableLevel']==105 and (contents['equipment'][j]['itemRarity']=='에픽' or contents['equipment'][j]['itemRarity']=='레전더리' ) \
                                and 'growInfo' in contents['equipment'][j].keys() :
                            itemname=contents['equipment'][j]['itemName']
                            itemtype=contents['equipment'][j]['itemTypeDetail']
                            option1=contents['equipment'][j]['growInfo']['options'][0]['explainDetail'].replace('\n',"+")
                            option1 = option1.replace(',', '/')
                            option2=contents['equipment'][j]['growInfo']['options'][1]['explainDetail'].replace('\n',"+")
                            option2 = option2.replace(',', '/')
                            option3=contents['equipment'][j]['growInfo']['options'][2]['explainDetail'].replace('\n',"+")
                            option3 = option3.replace(',', '/')
                            option4=contents['equipment'][j]['growInfo']['options'][3]['explainDetail'].replace('\n',"+")
                            option4 = option4.replace(',', '/')
                            if  'upgradeInfo' in contents['equipment'][j].keys():
                                upgradeitem=contents['equipment'][j]['upgradeInfo']['itemName']
                            else :
                                upgradeitem='Nan'
                        elif  contents['equipment'][j]['itemAvailableLevel']==105 and contents['equipment'][j]['itemRarity']=='에픽' or '레전더리' and 'bakalInfo' in contents['equipment'][j].keys() :
                            itemname=contents['equipment'][j]['itemName']
                            itemtype=contents['equipment'][j]['itemTypeDetail']
                            option1=contents['equipment'][j]['bakalInfo']['options'][0]['explainDetail'].replace('\n',"+")
                            option2=contents['equipment'][j]['bakalInfo']['options'][1]['explainDetail'].replace('\n',"+")
                            option3='Nan'
                            option4='Nan'
                            if  'upgradeInfo' in contents['equipment'][j].keys():
                                upgradeitem=contents['equipment'][j]['upgradeInfo']['itemName']
                            else :
                                upgradeitem='Nan'
                        else :
                            itemname,itemtype,option1,option2,option3,option4,upgradeitem='Nan','Nan','Nan','Nan','Nan','Nan','Nan'
                except IndexError :
                    itemname, itemtype, option1, option2, option3, option4, upgradeitem = 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan', 'Nan'

                if j==0 :

                    equipment[j].append([itemname,itemtype,option1,option2,option3,option4,upgradeitem])

                elif j>1 :

                    equipment[j-1].append([itemname,itemtype,option1,option2,option3,option4,upgradeitem])
equipment=np.array(equipment,dtype=object)
equpmentname=['weapon','top','shoulder','bottom','shoe','belt','necklaces','bracelet','ring','assistive','gemstone','earrings']

for i in range(12):
    np.savetxt(equpmentname[i]+'.csv', equipment[i],delimiter=",",fmt="%s")
"""
for i in range(12):
    with open(equpmentname[i]+'.csv','a', newline="") as myfile:
        wr=csv.writer(myfile)
        wr.writerows(equipment[i])
"""







