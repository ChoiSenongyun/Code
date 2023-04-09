import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import copy
data=np.loadtxt('twohalo.dat')
r=data[:,0]
d=data[:,1]
derr=data[:,2]
h=0.000001

##sigma가 Determines the uncertainty in ydata 의 역활  안하면 값 이상하게 나옴##########

def nfw(R,rr1,dd1):
    return dd1 / ((R / rr1) * (1 + R / rr1) ** 2)
def snfw(R,rr1,rr2,dd1,dd2):
    return dd1/ ((R/rr1)*(1+R/rr1)**2) + dd2/ ((R/rr2)*(1+R/rr2)**2)


####1개의 NFW 일때 Fitting######
popt0, pcov0=curve_fit(nfw,r,d,sigma=derr)
print(popt0)

plt.errorbar(r,d,derr,color='black',fmt='x',label='data',capsize=0.5)
plt.plot(r,nfw(r,popt0[0],popt0[1]))
plt.ylim(0.0001,10)
plt.xscale('log')
plt.yscale('log')
plt.show()


###2개의 NFW 일때  Fitting##########
popt,pcov=curve_fit(snfw,r,d,sigma=derr)
print(popt)
r1=popt[0]
r2=popt[1]
d1=popt[2]
d2=popt[3]


###########################그래프 그리기#############################

plt.errorbar(r,d,derr,color='black',fmt='x',label='data',capsize=0.5)
plt.plot(r,nfw(r,r1,d1))
plt.plot(r,nfw(r,r2,d2))
plt.plot(r,snfw(r,r1,r2,d1,d2))
plt.ylim(0.0001,10)
plt.xscale('log')
plt.yscale('log')
plt.show()


############ log likehood 계산#######################
#2개의 nfw 합으로 fitting
def like(rr1,rr2,dd1,dd2):
    return np.sum(   (d- snfw(r,rr1,rr2,dd1,dd2)) **2 /(2*derr**2)  )
#1개의 nfw 로 fitting 했을때
def onelike(rr1,dd1):
    return np.sum((d - nfw(r, rr1, dd1)) ** 2 / (2 * derr ** 2))
##########Reduced chi square 1개일때랑 2개일때 비교###########
print((like(r1,r2,d1,d2)*2)/(len(r)-4))
print((onelike(popt0[0],popt0[1])*2)/(len(r)-2))


"""
########################################Uncertainity 계산######################################################
zero=( like(r1+h,r2,d1,d2)-2*like(r1,r2,d1,d2)+like(r1-h,r2,d1,d2) )/h**2
one=( ( like(r1+h,r2+h,d1,d2) - like(r1+h,r2-h,d1,d2)) - (like(r1-h,r2+h,d1,d2)-like(r1-h,r2-h,d1,d2)) )/4*h**2
two=( ( like(r1+h,r2,d1+h,d2) - like(r1+h,r2,d1-h,d2)) - (like(r1-h,r2,d1+h,d2)-like(r1-h,r2,d1-h,d2)) )/4*h**2
three=( ( like(r1+h,r2,d1,d2+h) - like(r1+h,r2,d1,d2-h)) - (like(r1-h,r2,d1,d2+h)-like(r1-h,r2,d1,d2-h)) )/4*h**2

four=( ( like(r1+h,r2+h,d1,d2) - like(r1-h,r2+h,d1,d2)) - (like(r1+h,r2-h,d1,d2)-like(r1-h,r2-h,d1,d2)) )/4*h**2
five=( like(r1,r2+h,d1,d2)-2*like(r1,r2,d1,d2)+like(r1,r2-h,d1,d2) )/h**2
six=( ( like(r1,r2+h,d1+h,d2) - like(r1,r2+h,d1-h,d2)) - (like(r1,r2-h,d1+h,d2)-like(r1,r2-h,d1-h,d2)) )/4*h**2
seven=( ( like(r1,r2+h,d1,d2+h) - like(r1,r2+h,d1,d2-h)) - (like(r1,r2-h,d1,d2+h)-like(r1,r2-h,d1,d2-h)) )/4*h**2

eight=( ( like(r1+h,r2,d1+h,d2) - like(r1-h,r2,d1+h,d2)) - (like(r1+h,r2,d1-h,d2)-like(r1-h,r2,d1-h,d2)) )/4*h**2
nine=( ( like(r1,r2+h,d1+h,d2) - like(r1,r2-h,d1+h,d2)) - (like(r1,r2+h,d1-h,d2)-like(r1,r2-h,d1-h,d2)) )/4*h**2
ten=( like(r1,r2,d1+h,d2)-2*like(r1,r2,d1,d2)+like(r1,r2,d1-h,d2) )/h**2
eleven=( ( like(r1,r2,d1+h,d2+h) - like(r1,r2,d1+h,d2-h)) - (like(r1,r2,d1-h,d2+h)-like(r1,r2,d1-h,d2-h)) )/4*h**2

tweleve=( ( like(r1+h,r2,d1,d2+h) - like(r1-h,r2,d1,d2+h)) - (like(r1+h,r2,d1,d2-h)-like(r1-h,r2,d1,d2-h)) )/4*h**2
thirteen=( ( like(r1,r2+h,d1,d2+h) - like(r1,r2-h,d1,d2+h)) - (like(r1,r2+h,d1,d2-h)-like(r1,r2-h,d1,d2-h)) )/4*h**2
fourteen=( ( like(r1,r2,d1+h,d2+h) - like(r1,r2,d1-h,d2+h)) - (like(r1,r2,d1+h,d2-h)-like(r1,r2,d1-h,d2-h)) )/4*h**2
fifthteen=( like(r1,r2,d1,d2+h)-2*like(r1,r2,d1,d2)+like(r1,r2,d1,d2-h) )/h**2

H=[[zero,one,two,three],
   [four,five,six,seven],
   [eight,nine,ten,eleven],
   [tweleve,thirteen,fourteen,fifthteen]]
C=np.linalg.inv(H)
print(C)
########################Uncertainity 값#########################################
rc1=np.sqrt(C[0][0])
rc2=np.sqrt(C[1][1])
dc1=np.sqrt(C[2][2])
dc2=np.sqrt(C[3][3])
print(rc1,rc2,dc1,dc2)
"""

###########################파라미터 간에 관계 알아보깅############################
rs1=np.linspace(23,24,100)
rs2=np.linspace(2.5,4,100)
ds1=np.linspace(0.19,0.23,100)
ds2=np.linspace(1,5.5,100)

##################contour 지점 찾는 함수######################
def findcon(x):
    x.sort()
    A=0
    B=0
    i=0
    j=0
    while A<=0.68:
        A+=x[len(x)-1-i]
        i+=1
    while B<=0.95:
        B+=x[len(x)-1-j]
        j+=1
    return x[len(x)-1-i],x[len(x)-1-j]
"""

#########################rs1 rs2의 관계###########################
rsrs=[]
for i in range(100):
    for j in range(100):
        rsrs.append(-like(rs1[j],rs2[i],d1,d2))
rsrs=np.array(rsrs)
rsrsloglike=rsrs-max(rsrs)
rsrslike=np.exp(rsrsloglike)
rsrslikenormal=rsrslike/np.sum(rsrslike)

a,b=findcon(copy.deepcopy(rsrslikenormal))

plt.imshow(rsrslikenormal.reshape(100,100,order='C'),extent=[23,24,4,2.5])
plt.contour(rs1,rs2,rsrslikenormal.reshape(100,100),levels=[b,a],colors='black')
plt.gca().invert_yaxis()
plt.show()

plt.imshow(np.reshape(rsrsloglike,(100,100)),extent=[23,24,4,2.5])
plt.contour(rs1,rs2,np.reshape(rsrsloglike,(100,100)),levels=[np.log(b*np.sum(rsrslike)),np.log(a*np.sum(rsrslike))],colors='black')
plt.gca().invert_yaxis()
plt.show()
"""
"""
#########################rs1 ds1의 관계###########################
rsd1=[]
for i in range(100):
    for j in range(100):
        rsd1.append(-like(rs1[j],r2,ds1[i],d2))

rsd1loglike=np.array(rsd1)
rsd1like=np.exp(rsd1)
rsd1likenormal=rsd1like/np.sum(rsd1like)

a,b=findcon(copy.deepcopy(rsd1likenormal))

plt.imshow(rsd1likenormal.reshape(100,100,order='C'),aspect='auto',extent=[23,24,0.23,0.19])
plt.contour(rs1,ds1,rsd1likenormal.reshape(100,100,order='C'),levels=[b,a],colors='black')
plt.gca().invert_yaxis()
plt.show()

plt.imshow(np.reshape(rsd1loglike,(100,100)),aspect='auto',extent=[23,24,0.23,0.19])
plt.contour(rs1,ds1,np.reshape(rsd1loglike,(100,100)),levels=[np.log(b*np.sum(rsd1like)),np.log(a*np.sum(rsd1like))],colors='black')
plt.gca().invert_yaxis()
plt.show()
"""
"""
#########################rs1 ds2의 관계###########################
rsd2=[]
for i in range(100):
    for j in range(100):
        rsd2.append(-like(rs1[j],r2,d1,ds2[i]))


rsd2=np.array(rsd2)
rsd2loglike=rsd2-max(rsd2)
rsd2like=np.exp(rsd2loglike)
rsd2likenormal=rsd2like/np.sum(rsd2like)

a,b=findcon(copy.deepcopy(rsd2likenormal))

plt.imshow(rsd2likenormal.reshape(100,100,order='C'),aspect='auto',extent=[23,24,5.5,1])
plt.contour(rs1,ds2,rsd2likenormal.reshape(100,100,order='C'),levels=[b,a],colors='black')
plt.gca().invert_yaxis()
plt.show()

plt.imshow(np.reshape(rsd2loglike,(100,100)),aspect='auto',extent=[23,24,5.5,1])
plt.contour(rs1,ds2,np.reshape(rsd2loglike,(100,100)),levels=[np.log(b*np.sum(rsd2like)),np.log(a*np.sum(rsd2like))],colors='black')
plt.gca().invert_yaxis()
plt.show()
"""

"""
#########################rs2 ds1의 관계###########################
rsd3=[]
for i in range(100):
    for j in range(100):
        rsd3.append(-like(r1,rs2[j],ds1[i],d2))


rsd3=np.array(rsd3)
rsd3loglike=rsd3-max(rsd3)
rsd3like=np.exp(rsd3loglike)
rsd3likenormal=rsd3like/np.sum(rsd3like)

a,b=findcon(copy.deepcopy(rsd3likenormal))

plt.imshow(rsd3likenormal.reshape(100,100,order='C'),aspect='auto',extent=[2.5,4,0.23,0.19])
plt.contour(rs2,ds1,rsd3likenormal.reshape(100,100,order='C'),levels=[b,a],colors='black')
plt.gca().invert_yaxis()
plt.show()

plt.imshow(np.reshape(rsd3loglike,(100,100)),aspect='auto',extent=[2.5,4,0.23,0.19])
plt.contour(rs2,ds1,np.reshape(rsd3loglike,(100,100)),levels=[np.log(b*np.sum(rsd3like)),np.log(a*np.sum(rsd3like))],colors='black')
plt.gca().invert_yaxis()
plt.show()

"""
"""
#########################rs2 ds2의 관계###########################
rsd4=[]
for i in range(100):
    for j in range(100):
        rsd4.append(-like(r1,rs2[j],d1,ds2[i]))


rsd4=np.array(rsd4)
rsd4loglike=rsd4-max(rsd4)
rsd4like=np.exp(rsd4loglike)
rsd4likenormal=rsd4like/np.sum(rsd4like)

a,b=findcon(copy.deepcopy(rsd4likenormal))

plt.imshow(rsd4likenormal.reshape(100,100,order='C'),aspect='auto',extent=[2.5,4,5.5,1])
plt.contour(rs2,ds2,rsd4likenormal.reshape(100,100,order='C'),levels=[b,a],colors='black')
plt.gca().invert_yaxis()
plt.show()

plt.imshow(np.reshape(rsd4loglike,(100,100)),aspect='auto',extent=[2.5,4,5.5,1])
plt.contour(rs2,ds2,np.reshape(rsd4loglike,(100,100)),levels=[np.log(b*np.sum(rsd4like)),np.log(a*np.sum(rsd4like))],colors='black')
plt.gca().invert_yaxis()
plt.show()
"""
"""
#########################ds1 ds2의 관계###########################
dsds=[]
for i in range(100):
    for j in range(100):
        dsds.append(-like(r1,r2,ds1[j],ds2[i]))


dsds=np.array(dsds)
dsdsloglike=dsds-max(dsds)
dsdslike=np.exp(dsdsloglike)
dsdslikenormal=dsdslike/np.sum(dsdslike)

a,b=findcon(copy.deepcopy(dsdslikenormal))

plt.imshow(dsdslikenormal.reshape(100,100,order='C'),aspect='auto',extent=[0.19,0.23,5.5,1])
plt.contour(ds1,ds2,dsdslikenormal.reshape(100,100,order='C'),levels=[b,a],colors='black')
plt.gca().invert_yaxis()
plt.show()

plt.imshow(np.reshape(dsdsloglike,(100,100)),aspect='auto',extent=[0.19,0.23,5.5,1])
plt.contour(ds1,ds2,np.reshape(dsdsloglike,(100,100)),levels=[np.log(b*np.sum(dsdslike)),np.log(a*np.sum(dsdslike))],colors='black')
plt.gca().invert_yaxis()
plt.show()
"""

