from HW02_1_2017135002 import myran
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sympy as sp #미분 적분 하기 위하여 sympy 모듈 사용
from scipy import stats

def mygauss(m,std,N):
    #난수 N/2개씩 생성하여 총 N개 생성
    # float object cannot be interpreted as an integer 오류 발생
    x1=np.array(myran(int(N/2)))
    x2=np.array(myran(int(N/2)))
    #변환 (표준정규분포의 형태를 가진다. 평균 0 , 표준편차 1)
    y1=np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)
    y2=np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)
    #평균 m, 표준편차 std를 가지는 정규분포 형성
    Y1=std*y1+m
    Y2=std*y2+m
    Y3=[]
    T=[]
    #Y1,Y2를 합친 리스트 만들기
    for i in range(int(N/2)):
        Y3.append(Y1[i])
        Y3.append(Y2[i])
        T.append(i)


    #Y1,Y2,Y3 히스토그램 한번에 표현
    plt.hist(Y1, bins=100,histtype='step',label='Y1')
    plt.hist(Y2, bins=100,histtype='step',label='Y2')
    plt.hist(Y3, bins=100,histtype='step',label='Y1+Y2')
    plt.xlabel("Random Number")
    plt.ylabel("Number")
    plt.legend()


    """
    #3차원 히스토그램 분포
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #x1,x2의 분포
    hist, xedges, yedges = np.histogram2d(x1, x2,bins=(50,50), range=[[0, 1], [0, 1]],density='True')
    #y1,y2의 분포
    hist, xedges, yedges = np.histogram2d(Y1, Y2, bins=(50, 50), density='True')
    xpos, ypos = np.meshgrid(xedges[:-1] + xedges[1:], yedges[:-1] + yedges[1:]) - (xedges[1] - xedges[0])
    xpos = xpos.flatten() * 1. / 2
    ypos = ypos.flatten() * 1. / 2
    zpos = np.zeros_like(xpos)
    dx = xedges[1] - xedges[0]
    dy = yedges[1] - yedges[0]
    dz = hist.flatten()
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
    """
    """
    #발생한 Y1,Y2의 난수를 순서대로 뺌
    plt.figure(figsize=(18,8))
    plt.plot(T,Y1-Y2,linewidth=0.5)
    plt.xlabel('Order') 
    plt.xlabel('Y1-Y2')
    """
    plt.show()
    return Y3


mygauss(100,20,10000)
"""
#curve fit 구현하기
n,bins,patches=plt.hist(mygauss(100,20,10000),bins=100,histtype='step',density='True')
# n은 해당 범위에 속하는 개수를 담고있는 array 개수가 100개
# bins는 범위의 초기값을 담고 있는 array 개수가 101개 ->오류 발생 operands could not be broadcast together with shapes (101,) (100,)
nbins=bins[:100] #개수를 변경해줌
def func(x,h,m,s):
    return h*np.exp(-(x-m)**2/(2*s**2))
popt, pcov=curve_fit(func,nbins,n,p0=[np.max(n),np.median(nbins),np.std(nbins)])
plt.figure()
plt.plot(bins,func(bins,*popt),c='b',label='Gaussian fiiting')

#평균 100, 표준편차 20의 정규분포 plot(범위 0~200)
x3=np.linspace(0,200,10000)
y3=(1/np.sqrt(2*np.pi*20**2)) * np.exp( -(x3-100)**2/(2*20**2)) #Gaussian 함수의 확률 분포를 나타낸다.
plt.plot(x3,y3,color='red',label='Gaussian function')
plt.legend()
plt.show()
"""

"""
#Gaussian function과의 residual 비교
n,bins,patches=plt.hist(mygauss(100,20,10000),bins=100,histtype='step',density='True')
y3=(1/np.sqrt(2*np.pi*20**2)) * np.exp( -(bins[:100]-100)**2/(2*20**2)) #Gaussian 함수의 확률 분포를 나타낸다.
plt.plot(bins[:100],y3,color='red',label='Gaussian function')
N=[]
for i in range(100):
    N.append(i)
plt.figure()
plt.scatter(N,n-y3,s=2)
plt.plot(N,n-y3,label='error value') #오차값 plot
plt.axhline(y=0, color='r', linewidth=1)
#plt.plot(N,(n-y3)*100/y3,label='error rate') #오차율 plot
#plt.ylim(4,180)
plt.legend()
plt.show()
"""

"""
#정규성 검성 (normal test)
stats,p=stats.normaltest(mygauss(100,20,10000))
print(p)
"""

"""
#정규성 검성 (anderson)
statistic,cv,sl=stats.anderson(np.array(mygauss(100,20,10000)))
print(statistic)
print(cv)
"""


"""
#moment 계산
X=np.array(mygauss(100,20,10000))
mean=stats.moment(X,1)/20**1
variance=stats.moment(X,2)/20**2
skewness=stats.moment(X,3)/20**3
kurtosis=stats.moment(X,4)/20**4
print(mean)
print(variance)
print(skewness)
print(kurtosis)
"""
