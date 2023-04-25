import pandas as pd
import numpy as np
import pprint
pp=pprint.PrettyPrinter()
##4월 14일 기준 user data
##4월 15일 기준 장비 리스트

### 서버 리스트
server={ '카인': 'cain', '디레지에' : 'diregie' ,  '시로코': 'siroco', '프레이':'prey', '카시야스': 'casillas' , '힐더': 'hilder',
         '안톤': 'anton',  '바칼': 'bakal'}
### 장비 리스트
itemname=['weapon','top','shoulder','bottom','shoe','belt','necklaces','bracelet','ring','assistive','gemstone','earrings']

### 커스텀리스트
custom=["블루 베릴","엔트 정령", "숲속의 마녀", "딥 다이버" ]

### 유저 불러오기
userlist=pd.read_csv('userlist.csv',names=['name','server','damage','blank'],dtype=object,encoding='CP949',nrows=3000)

### 장비 불러오기
weapon=pd.read_csv('weapon.csv',names=['name','type','option1','option2','option3','option4','upgrade'],dtype=object,encoding='CP949',nrows=3000)
top=pd.read_csv('top.csv',names=['name','type','option1','option2','option3','option4','upgrade'],dtype=object,encoding='CP949',nrows=3000)
shoulder=pd.read_csv('shoulder.csv',names=['name','type','option1','option2','option3','option4','upgrade'],dtype=object,encoding='CP949',nrows=3000)
bottom=pd.read_csv('bottom.csv',names=['name','type','option1','option2','option3','option4','upgrade'],dtype=object,encoding='CP949',nrows=3000)
shoe=pd.read_csv('shoe.csv',names=['name','type','option1','option2','option3','option4','upgrade'],dtype=object,encoding='CP949',nrows=3000)
belt=pd.read_csv('belt.csv',names=['name','type','option1','option2','option3','option4','upgrade'],dtype=object,encoding='CP949',nrows=3000)
necklaces=pd.read_csv('necklaces.csv',names=['name','type','option1','option2','option3','option4','upgrade'],dtype=object,encoding='CP949',nrows=3000)
bracelet=pd.read_csv('bracelet.csv',names=['name','type','option1','option2','option3','option4','upgrade'],dtype=object,encoding='CP949',nrows=3000)
ring=pd.read_csv('ring.csv',names=['name','type','option1','option2','option3','option4','upgrade'],dtype=object,encoding='CP949',nrows=3000)
assistive=pd.read_csv('assistive.csv',names=['name','type','option1','option2','option3','option4','upgrade'],dtype=object,encoding='CP949',nrows=3000)
gemstone=pd.read_csv('gemstone.csv',names=['name','type','option1','option2','option3','option4','upgrade'],dtype=object,encoding='CP949',nrows=3000)
earrings=pd.read_csv('earrings.csv',names=['name','type','option1','option2','option3','option4','upgrade'],dtype=object,encoding='CP949',nrows=3000)

n=1000
### (상의) 장비 종류 분석
item_dic={}

for i in range(3000):
    equipname=top.loc[i]['name']
    if  equipname in item_dic.keys() : item_dic[equipname]+=1
    else :  item_dic[equipname]=1
item_dic = sorted(item_dic.items(), key=lambda item: item[1])
pp.pprint(item_dic)

### (상의) 장비 옵션 분석
option_dic={}
for i in range(100):
    if top.loc[i]['name']=='블루 베릴 아머' :
        for j in range(1,5):
            optionname=top.loc[i]['option'+str(j)]
            if  optionname in option_dic.keys() : option_dic[optionname]+=1
            else :  option_dic[optionname]=1
total = sum(option_dic.values())
print(total)
option_dic = sorted(option_dic.items())
pp.pprint(option_dic)

option_list=['500px 범위 내 감전 상태인 대상 하나 당 피해 증가','500px 범위 내 기절 상태인 대상 하나 당 피해 증가','500px 범위 내 둔화 상태인 대상 하나 당 피해 증가','500px 범위 내 구속 상태인 대상 하나 당 피해 증가',
             '500px 범위 내 빙결 상태인 대상 하나 당 피해 증가','500px 범위 내 석화 상태인 대상 하나 당 피해 증가','500px 범위 내 수면 상태인 대상 하나 당 피해 증가','500px 범위 내 혼란 상태인 대상 하나 당 피해 증가',
             '500px 범위 내 화상 상태인 대상 하나 당 피해 증가','500px 범위 내 암흑 상태인 대상 하나 당 피해 증가','500px 범위 내 저주 상태인 대상 하나 당 피해 증가','500px 범위 내 중독 상태인 대상 하나 당 피해 증가',
             '500px 범위 내 출혈 상태인 대상 하나 당 피해 증가','5회 공격 시마다 아래 효과 적용','HP 1분당 460.2 회복','HP MAX +5%','HP MAX +600','MP 1분당 348 회복','MP MAX +5%','MP MAX +945','감전 데미지 30% 증가+피격 시 받는 데미지 20% 증가',
             '공격 속도 +8%+캐스팅 속도 +12%','공격 시 HP 2200 회복','공격 시 MP 3500 회복','공격 시 강화 스택 1개 획득','공격 시 피해 증가','명속성 강화 15 증가','명속성 저항 10 증가','모든 속성 강화 10 증가',
             '모든 속성 강화 15 증가+모든 속성 저항 10 감소','모든 속성 저항 8 증가',
             '모든 직업 15Lv 스킬 범위 15% 증가+모든 직업 15Lv 스킬 공격력 5% 증가','모든 직업 20Lv 스킬 범위 15% 증가+모든 직업 20Lv 스킬 공격력 5% 증가','모든 직업 25Lv 스킬 범위 15% 증가+모든 직업 25Lv 스킬 공격력 5% 증가',
             '모든 직업 30Lv 스킬 범위 15% 증가+모든 직업 30Lv 스킬 공격력 5% 증가','모든 직업 35Lv 스킬 범위 15% 증가+모든 직업 35Lv 스킬 공격력 5% 증가','모든 직업 40Lv 스킬 범위 15% 증가+모든 직업 40Lv 스킬 공격력 5% 증가',
             '모든 직업 45Lv 스킬 범위 15% 증가+모든 직업 45Lv 스킬 공격력 5% 증가','모든 직업 60Lv 스킬 범위 15% 증가+모든 직업 60Lv 스킬 공격력 5% 증가','모든 직업 70Lv 스킬 범위 15% 증가+모든 직업 70Lv 스킬 공격력 5% 증가',
             '모든 직업 75Lv 스킬 범위 15% 증가+모든 직업 75Lv 스킬 공격력 5% 증가','모든 직업 80Lv 스킬 범위 15% 증가+모든 직업 80Lv 스킬 공격력 5% 증가','물리 방어력 +7000+마법 방어력 +7000','물리 방어력 5% 증가+마법 방어력 5% 증가',
             '물리 크리티컬 히트 +5%+마법 크리티컬 히트 +5%','물리 크리티컬 히트 +7%+마법 크리티컬 히트 +7%+모든 상태 이상 내성 10% 감소','백어택 피격 시 받는 데미지 20% 감소','비 카운터 피격 시 받는 데미지 20% 감소',
             '수속성 강화 15 증가','수속성 저항 10 증가','스킬 MP 소모량 7% 감소','암속성 강화 15 증가','암속성 저항 10 증가','이동 속도 +8%','적중률 +10%','점프력 20 증가+점프 시 이동 속도 30% 증가',
             '정면 피격 시 받는 데미지 20% 감소','중독 데미지 30% 증가+피격 시 받는 데미지 20% 증가','출혈 데미지 30% 증가+피격 시 받는 데미지 20% 증가','카운터 피격 시 받는 데미지 20% 감소',
             '피격 시 30초 동안 5회 피격 시 파괴되는 슈퍼아머 적용 (쿨타임 5초)','피격 시 60초 동안 명속성 저항 20 증가 (쿨타임 5초/ 최대 1중첩)','피격 시 60초 동안 수속성 저항 20 증가 (쿨타임 5초/ 최대 1중첩)',
             '피격 시 60초 동안 암속성 저항 20 증가 (쿨타임 5초/ 최대 1중첩)','피격 시 60초 동안 화속성 저항 20 증가 (쿨타임 5초/ 최대 1중첩)','화상 데미지 30% 증가+피격 시 받는 데미지 20% 증가','화속성 강화 15 증가',
             '화속성 저항 10 증가','회피율 +8%']
new_dic={}
count=0
for option in option_dic:
    for j in option_list:
        if j in option[0] :
            if  j in new_dic.keys() : new_dic[j]+=option[1]
            else :  new_dic[j]=option[1]
pp.pprint(new_dic)
#new_dic['카운터 피격 시 받는 데미지 20% 감소']=24

new_dic = sorted(new_dic.items(), key=lambda item: item[1])
pp.pprint(new_dic)
