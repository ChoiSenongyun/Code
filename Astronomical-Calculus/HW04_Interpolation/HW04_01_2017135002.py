import numpy as np
import matplotlib.pyplot as plt
j,m=np.loadtxt('sn.dat',usecols=(1,2),skiprows=1,unpack=True)
jd=np.linspace(min(j),max(j),102)
jd=jd[1:101]
bm=[]
mm=0
for a in range(100):
    mm=0
    for b in range(16):
        if j[b]<jd[a]<j[b+1]:
            mm=m[b]+(m[b+1]-m[b])/(j[b+1]-j[b])*(jd[a]-j[b])
            bm.append(mm)
plt.scatter(j,m,s=50,c='r',marker='x')
plt.scatter(jd,bm,s=4)
plt.gca().invert_yaxis()
plt.title('Linear Interpolation')
plt.xlabel('Julian Date')
plt.ylabel('B-mag')
plt.show()
