import numpy as np
import matplotlib.pyplot as plt
mo=np.loadtxt('xy.dat')
x=mo[:,0]
y=mo[:,1]
yer=mo[:,2]

s=np.sum(1/yer**2)
sx=np.sum(x/(yer**2))
sy=np.sum(y/(yer**2))
sxx=np.sum((x**2)/(yer**2))
sxy=np.sum(x*y/(yer**2))
d=s*sxx-(sx**2)
a=(sxx*sy-sx*sxy)/d
b=(s*sxy-sx*sy)/d

aer=np.sqrt(sxx/d)
ber=np.sqrt(s/d)


plt.errorbar(x,y,yer,color='black',fmt='o',label='data')
plt.plot(x,a+b*x,label='Chi-square fit',color='red')
plt.fill_between(x,(a+aer)+(b+ber)*x,(a-aer)+(b-ber)*x,color='r',edgecolor='none',alpha=0.3)
plt.legend()
plt.show()



#####reduced chi square
print((np.sum(((y-a-b*x)/yer)**2)/12))
