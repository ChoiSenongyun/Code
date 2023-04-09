import py_dss_interface as dss
import os
import pathlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import sys
import math as mt
import csv
np.set_printoptions(threshold=sys.maxsize)

script_path=os.path.dirname(os.path.abspath(__file__))
dss_file=pathlib.Path(script_path).joinpath("feeder","37Bus","1001.dss")
dss = dss.DSSDLL(r"C:\Program Files\OpenDSS")
dss.text(f"compile [{dss_file}]")

pv_num = dss.pvsystems_count()
load_num = dss.loads_count()
#####################  167 최소 kva 용량 ###################

####################### load factor 증가 ###########################
loadfactor=1
present_loadkw = np.zeros((load_num))
present_loadkvar = np.zeros((load_num))
dss.loads_first()

for i in range(0, load_num):
    present_loadkw[i] = dss.loads_read_kw()
    present_loadkvar[i] = dss.loads_read_kvar()
    dss.loads_next()
dss.loads_first()

for q in range(0, load_num):
    dss.loads_write_kw(round(float(present_loadkw[q] * float(loadfactor)), 2))
    dss.loads_write_kvar(round(float(present_loadkvar[q] * float(loadfactor)), 2))
    dss.loads_next()
####################################################################
############ 총 penetration 횟수 ######################

min_pene=mt.floor(8*167/(2457*loadfactor)*100)
n=100-min_pene + 1

#################################################

############ 한 penetration 당 반복 횟수 결정 ######################
m=100
#################################################

normal=np.empty((0,5))
normal_bus=np.empty((0,9))
normal_kva=np.empty((0,9))
normal = np.append(normal, np.array([['penetration','max_voltage','maxbus','maxtime', 'Case Number']]), axis=0)


all_bus_name = dss.circuit_all_bus_names()
all_bus_name.remove('sourcebus')
all_bus_name.remove('799')
all_bus_name.remove('799r')
pv_location=np.empty((0,8))

max_vol=np.zeros((n,m))
min_vol=np.zeros((n,m))
case=1

def decide_kva(list,pene,loadfactor):  ### penetration 에 맞게 pv kva 값 정하는 함수
    min_pene = mt.floor(8 * 167 / (2457 * loadfactor) * 100)
    plus=mt.ceil(2457*pene*loadfactor/100-167*8)  ##### 8개 pv중에 증가시켜줘야 하는 kva 값
    if pene==min_pene:
        return list
    else :
        for i in range(0,len(list)):
            delta=np.random.randint(0,plus+1)  ### 첫번째 pv kva 증가 값
            list[i]=list[i]+delta
            plus=plus-delta ### 남은 증가값
        return list

while case<1000:        ####### penetration 27 ~ 100% 로 1% 씩 증가  총 n번 반복 ##############   ############ 1% penetration 당 20번의 random case 실행###############
            penetration=np.random.randint(70,101)
            pv_kva = np.array([167, 167, 167, 167, 167, 167, 167, 167])  ######## 기본 최소 pv kva ###########
            random_pv_kva=decide_kva(pv_kva,penetration,loadfactor)
            random_pv_bus = random.sample(all_bus_name, 8)
            pv_location=np.append(pv_location,np.array([random_pv_bus]),axis=0)
            """random bus postion"""
            for o in range(1,9):
                pv_kva_text="PVSystem.PV"+str(o)+".bus1="+str(int(random_pv_bus[o-1]))
                dss.text(pv_kva_text)
                #print(dss.cktelement_read_bus_names())


            """random pv kva"""
            dss.pvsystems_first()
            for j in range(1, pv_num + 1):
                dss.pvsystems_write_kva_rated(random_pv_kva[j-1])
                dss.pvsystems_write_pmpp(random_pv_kva[j-1])
                dss.pvsystems_next()

        ##########################################################################
            node_name = dss.circuit_all_node_names()
            all_v = np.array([node_name])
            dss.dss_reset()
            dss.text("solve mode = daily")
            dss.text("set stepsize=1h")
            for i in range(1, 25):
                dss.text("set number=1")
                dss.text("set casename =%dh" % i)
                dss.text("solve")

                all_v = np.r_[all_v, [dss.circuit_all_bus_vmag_pu()]]
            all_volt = np.delete(all_v, [0, 1, 2, 3, 4, 5], axis=1)
            d = all_volt[1:, :].astype(np.float64)
            max_voltage=np.max(d)
            a = np.where(d == np.max(d))
            c = a[1].tolist()
            maxbus = all_volt[0, c[0]]
            maxtime = a[0].tolist()[0] + 1
            if max_voltage < 1.05:
                normal = np.append(normal,
                                np.array([[max_voltage, penetration, maxbus, maxtime, case]]), axis=0)
                normal_bus = np.append(normal_bus, np.array([np.append(random_pv_bus,case)]), axis=0)
                normal_kva = np.append(normal_kva, np.array([np.append(random_pv_kva,case)]), axis=0)
                case += 1
                print(case)

########################################################



"""
index=np.arange(1,len(maxabnormal),1)

select_index=np.random.choice(index,2)    ########### 1.05pu 넘는 case 중 2개 선택 ##########
select_case_1=maxabnormal[select_index[0]]
select_case_2=maxabnormal[select_index[1]]
"""

with open('best_100.csv','w') as file :
    write = csv.writer(file)
    write.writerows(normal)
with open('best_100_bus.csv','w') as file :
    write = csv.writer(file)
    write.writerows(normal_bus)
with open('best_100_kva.csv','w') as file :
    write = csv.writer(file)
    write.writerows(normal_kva)

