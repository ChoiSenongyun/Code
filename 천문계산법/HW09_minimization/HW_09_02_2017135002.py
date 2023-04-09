import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import time

halo=np.loadtxt('halo.dat')
r=halo[:,0]
d=halo[:,1]
derr=halo[:,2]


def sis(dd):
    return np.sum( (( d-(dd/(r**2)) )/derr )**2  )

def nfw(x):
    dd,rr=x
    return np.sum( ((d-((dd*rr)/(r*(1+r/rr)**2) ))/derr)**2 )

sisdir=minimize(sis,d[0],method='Powell')
sisdown=minimize(sis,d[0],method='Nelder-Mead')
nfwdir=minimize(nfw,[d[0],r[0]],method='Powell')
nfwdown=minimize(nfw,[d[0],r[0]],method='Nelder-Mead')

###### 소요 시간 측정 ############
start=time.time()
nfwdir=minimize(nfw,[d[0],r[0]],method='Powell')
end=time.time()
print(end-start)



print(sisdown)
print(sisdir)
print(nfwdir)
print(nfwdown)



"""
############# reduced square 계산############
avgs=(sisdir['x']+sisdown['x'])/2
avgn=(nfwdir['x']+nfwdir['x'])/2
print(avgs)
print(avgn)
print(  sis(avgs)/99 )
print(  nfw(avgn)/98 )



########### uncertainity 계산 #########
h=0.000001

sisderr=1/np.sqrt(  (  sis(avgs+h) - 2*sis(avgs)  +sis(avgs-h) )/h**2 )

nfwderr=1/np.sqrt(  (  nfw([avgn[0]+h,avgn[1]]) - 2*nfw([avgn[0],avgn[1]])
                       +nfw([avgn[0]-h,avgn[1]]) )/h**2 )

nfwrerr=1/np.sqrt(  (  nfw([avgn[0],avgn[1]+h]) - 2*nfw([avgn[0],avgn[1]])
                       +nfw([avgn[0],avgn[1]-h]) )/h**2 )
print(sisderr)
print(nfwderr)
print(nfwrerr)



######plot############
###########sis plot###########
t=np.linspace(0,100,1000)
plt.errorbar(r,d,derr,color='black',fmt='o',label='data',capsize=1)
plt.plot(t,avgs/t**2,label='SIS',color='red')
plt.xlim(1,100)
plt.ylim(0.001,100)
plt.text(18,10,'Reduced chi suare=2.604')
plt.text(18,5,'d=37.93')
plt.title('SIS')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

###########nfw plot###########
t=np.linspace(0,100,1000)
plt.errorbar(r,d,derr,color='black',fmt='o',label='data',capsize=1)
plt.plot(t,avgn[0]*avgn[1]/(t*(1+t/avgn[1])**2),label='NFW',color='red')
plt.xlim(1,100)
plt.ylim(0.001,100)
plt.text(18,10,'Reduced chi suare=1.2235')
plt.text(18,5,'d=1.11')
plt.text(18,3,'r=14.92')
plt.title('NFW')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
"""