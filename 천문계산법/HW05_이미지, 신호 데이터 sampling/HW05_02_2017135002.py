from scipy.interpolate import CubicSpline as cs
import matplotlib.pyplot as plt
import numpy as np

############################100개의 간격################################

t1=np.linspace(0,20,101)
t2=np.linspace(0,20,1000)
x=np.sin(t1)
cb=cs(t1,x)
plt.scatter(t1,x,s=50,c='r',marker='x')
plt.plot(t2,cb(t2),t2,np.sin(t2))
plt.title('Sample N=100')
plt.show()
######원래의 그래프로 n=100일때의 차이 비교#########
plt.scatter(t2,cb(t2)-np.sin(t2),s=1)
plt.title('Sample N=100')
plt.show()

############################20개의 간격################################
"""
t1=np.linspace(0,20,21)
t2=np.linspace(0,20,1000)
x=np.sin(t1)
cb=cs(t1,x)
plt.scatter(t1,x,s=50,c='r',marker='x')
plt.plot(t2,cb(t2),t2,np.sin(t2))
plt.title('Sample N=20')
plt.show()
######원래의 그래프로 n=20일때의 차이 비교#########
plt.scatter(t2,cb(t2)-np.sin(t2),s=1)
plt.title('Sample N=20')
plt.show()

"""
############################10개의 간격################################
"""
t1=np.linspace(0,20,11)
t2=np.linspace(0,20,1000)
x=np.sin(t1)
cb=cs(t1,x)
plt.scatter(t1,x,s=50,c='r',marker='x')
plt.plot(t2,cb(t2),t2,np.sin(t2))
plt.title('Sample N=10')
plt.show()
######원래의 그래프로 n=10일때의 차이 비교#########
plt.scatter(t2,cb(t2)-np.sin(t2),s=1)
plt.title('Sample N=10')
plt.show()
"""

############################4개의 간격################################

"""
t1=np.linspace(0,20,5)
t2=np.linspace(0,20,1000)
x=np.sin(t1)
cb=cs(t1,x)
plt.scatter(t1,x,s=50,c='r',marker='x')
plt.plot(t2,cb(t2),t2,np.sin(t2))
plt.title('Sample N=4')
plt.show()
######원래의 그래프로 n=4일때의 차이 비교#########
plt.scatter(t2,cb(t2)-np.sin(t2),s=1)
plt.title('Sample N=4')
plt.show()
"""