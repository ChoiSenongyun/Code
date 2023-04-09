from HW02_1_2017135002 import myran #shuffling method를 사용하기 위하여 만들어온 randomnumber 모듈을 불러온다
import math as mp
import numpy as np
import matplotlib.pyplot as plt

X1=[]
X2=[]
G=[]
T=[]
while 1: #break문이 나올때까지 무한 반복
    T=myran(2) #난수 2개 발생
    x1=10*T[0]-5 #-5~5의 범위를 가지는 난수로 변경
    x2=T[1]


    if x2< (1/mp.sqrt(2*mp.pi)) * mp.exp( (-x1**2)/2 ):
        G.append(x1)
        X2.append(x2)
    if len(G)>10000:
        break #발생한 난수 값이 10000개 넘을경우 while 반복문 중지


plt.hist(G,bins=100,density=True) #발생한 난수의 분포를 나타낸다.
# density=True 를 사용하여 확률분포를 나타낸다.


plt.scatter(G,X2,s=1) #x1,x2분포를 scatter
x3=np.linspace(-5,5,100)
y3=(1/np.sqrt(2*mp.pi)) * np.exp( (-x3**2)/2 ) #Gaussian 함수의 확률 분포를 나타낸다.
plt.plot(x3,y3,color='red')

plt.title('Gaussian Distribution')
plt.show()


#========================================================================================
#Salepter's line을 Return Method를 사용하여 난수 분포를 만들어낸다
"""
X1=[]
X2=[]
G=[]
T=[]
while 1: #break문이 나올때까지 무한 반복
    T=myran(2) #난수 2개 발생
    x1=T[0]
    x2=99*T[1]+1 #1~100까지의 난수로 변경(별의 질량)
    if x1<1.35269898931688*x2**(-2.35): #Salpeter라인의 확률분포
        G.append(x1)
        X2.append(x2)
    if len(X2)>50000:
        break #발생한 난수 값이 50000개 넘을경우 while 반복문 중지
#과제2에서 한 plot 그대로 사용
#Return Method를 사용하여 만들어안 Salepter's line 난수 분포
plt.hist(X2,bins=np.logspace(np.log10(1),np.log10(100),300),histtype='step',density=True)#발생한 난수의 분포를 나타낸다.
#Salpeter's line
x5=np.linspace(1,100,10000)
y5=1.35269898931688*x5**(-2.35)
plt.plot(x5,y5)
plt.xscale('log') #x축 logscale로 변경
plt.yscale('log') #y축 logscale로 변경
plt.xlabel("log(M)[M$\odot$]")
plt.ylabel("log(Number)")
plt.show()
"""