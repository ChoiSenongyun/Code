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
from sklearn.model_selection import train_test_split

np.set_printoptions(threshold=sys.maxsize)

script_path=os.path.dirname(os.path.abspath(__file__))
dss_file=pathlib.Path(script_path).joinpath("feeder","37Bus","1001.dss")
dss = dss.DSSDLL(r"C:\Program Files\OpenDSS")
dss.text(f"compile [{dss_file}]")

pv_num=dss.pvsystems_count()
load_num=dss.loads_count()

ddtype=[('pene','<f8'),('max_voltage','<f8'),('maxbus','S5') ,('maxtime','<f8') ,('min_voltage','<f8'),('minbus','S5') ,('mintime','<f8') ,('casenumber','<f8') ]
dtype=[('pene','<f8'),('max_voltage','<f8'),('maxbus','S5') ,('maxtime','<f8') ,('casenumber','<f8') ]
normal = np.genfromtxt("C:/Users/kkang/PycharmProjects/datastructure/feeder/37Bus/normal.csv",dtype=ddtype, delimiter=',',skip_header=True)
normal_bus = np.genfromtxt("C:/Users/kkang/PycharmProjects/datastructure/feeder/37Bus/normal_bus.csv", delimiter=',')
normal_kva = np.genfromtxt("C:/Users/kkang/PycharmProjects/datastructure/feeder/37Bus/normal_kva.csv", delimiter=',')

best=np.delete(normal, np.where((normal['max_voltage']>1.05)  ),axis=0)
best_bus=np.delete(normal_bus, np.where((normal['max_voltage']>1.05) ),axis=0)
best_kva=np.delete(normal_kva, np.where((normal['max_voltage']>1.05)  ),axis=0)


worst=np.delete(normal, np.where( (normal['max_voltage']<1.05)   ),axis=0)
worst_bus=np.delete(normal_bus, np.where((normal['max_voltage']<1.05)  ),axis=0)
worst_kva=np.delete(normal_kva, np.where((normal['max_voltage']<1.05)  ),axis=0)

worst_over80=np.delete(worst, np.where( (worst['pene']<80)   ),axis=0)
worst_bus_over80=np.delete(worst_bus, np.where((worst['pene']<80)  ),axis=0)
worst_kva_over80=np.delete(worst_kva, np.where((worst['pene']<80)  ),axis=0)

best_over80=np.delete(best, np.where( (best['pene']<80)   ),axis=0)
best_bus_over80=np.delete(best_bus, np.where((best['pene']<80)  ),axis=0)
best_kva_over80=np.delete(best_kva, np.where((best['pene']<80)  ),axis=0)

worst_1000 = np.genfromtxt("C:/Users/kkang/PycharmProjects/datastructure/feeder/37Bus/worst_100.csv",dtype=dtype, delimiter=',',skip_header=True)
worst_1000_bus = np.genfromtxt("C:/Users/kkang/PycharmProjects/datastructure/feeder/37Bus/worst_100_bus.csv", delimiter=',')
worst_1000_kva = np.genfromtxt("C:/Users/kkang/PycharmProjects/datastructure/feeder/37Bus/worst_100_kva.csv", delimiter=',')

best_1000 = np.genfromtxt("C:/Users/kkang/PycharmProjects/datastructure/feeder/37Bus/best_100.csv",dtype=dtype, delimiter=',',skip_header=True)
best_1000_bus = np.genfromtxt("C:/Users/kkang/PycharmProjects/datastructure/feeder/37Bus/best_100_bus.csv", delimiter=',')
best_1000_kva = np.genfromtxt("C:/Users/kkang/PycharmProjects/datastructure/feeder/37Bus/best_100_kva.csv", delimiter=',')


################################################################################################
all_bus_name = dss.circuit_all_bus_names()
all_bus_name.remove('sourcebus')
all_bus_name.remove('799')
all_bus_name.remove('799r')
all_bus_name=np.array(all_bus_name)
case_number=999*2
x_number=len(all_bus_name)

x_train=np.zeros((case_number,x_number))

for i in range(case_number):
    for j in range(pv_num):
        if i%2==0:
            a = np.where(all_bus_name == str(int(worst_1000_bus[i//2][j])))
            x_train[i][a[0].tolist()[0]]=worst_1000_kva[i//2][j]
        if i%2==1:
            a = np.where(all_bus_name == str(int(best_1000_bus[i//2][j])))
            x_train[i][a[0].tolist()[0]]=best_1000_kva[i//2][j]
x_train = np.insert(x_train, 0, 1, axis=1)



y_train=np.zeros((case_number,2))
for i  in range(case_number):
    if i%2==0:
        y_train[i][1]=1
    if i % 2 == 1:
        y_train[i][0]=1


def regression(x, y):
    xtx = np.transpose(x).dot(x)
    return np.linalg.inv(xtx ).dot(np.transpose(x)).dot(y)

w=regression(x_train,y_train)
################################################################################
"""
# worst case에 경우에 대해서 train
x_test=np.zeros((len(worst),x_number))
for i in range(len(worst)):
    for j in range(pv_num):
        a = np.where(all_bus_name == str(int(worst_bus[i][j])))
        x_test[i][a[0].tolist()[0]]=worst_kva[i][j]

x_test = np.insert(x_test, 0, 1, axis=1)
y_test=x_test.dot(w)


for i in range(0, len(y_test)):
    for j in range(0, 2):
        if y_test[i][j] == np.max(y_test[i]):
            y_test[i][j] = 1
        else:
            y_test[i][j] = 0
"""

################################################################################
"""
# worst_over80 case에 경우에 대해서 test
x_test=np.zeros((len(worst_over80),x_number))
for i in range(len(worst_over80)):
    for j in range(pv_num):
        a = np.where(all_bus_name == str(int(worst_bus_over80[i][j])))
        x_test[i][a[0].tolist()[0]]=worst_kva_over80[i][j]

x_test = np.insert(x_test, 0, 1, axis=1)
y_test=x_test.dot(w)


for i in range(0, len(y_test)):
    for j in range(0, 2):
        if y_test[i][j] == np.max(y_test[i]):
            y_test[i][j] = 1
        else:
            y_test[i][j] = 0
 """
################################################################################

# best_over80 case 에 경우에 대해서 test
x_test=np.zeros((len(best_over80),x_number))
for i in range(len(best_over80)):
    for j in range(pv_num):
        a = np.where(all_bus_name == str(int(best_bus_over80[i][j])))
        x_test[i][a[0].tolist()[0]]=best_kva_over80[i][j]

x_test = np.insert(x_test, 0, 1, axis=1)
y_test=x_test.dot(w)


for i in range(0, len(y_test)):
    for j in range(0, 2):
        if y_test[i][j] == np.max(y_test[i]):
            y_test[i][j] = 1
        else:
            y_test[i][j] = 0

print(worst_over80)
print(y_test)