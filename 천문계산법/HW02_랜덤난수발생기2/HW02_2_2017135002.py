from HW02_1_2017135002 import myran #shuffling method를 사용하기 위하여 만들어온 randomnumber 모듈을 불러온다
import sympy as sp #미분 적분 하기 위하여 sympy 모듈 사용
import numpy as np
import matplotlib.pyplot as plt



m=sp.symbols('m')  #m을 변수로 설정
SI=m**-2.35
si=sp.integrate(SI,m) #salpeter's line 적분
C=1/(si.subs(m,100)-si.subs(m,1)) # C(정규화 상수)를 구한다
a=sp.integrate(C*SI,(m,1,m)) #x와 m의 관계를 구한다
x=sp.symbols('x')
M=((1.00199925134584-x)/1.00199925134584)**(-1/1.35) #x를 M으로 변환
ML=[]
for i in myran(100000): #x(i)에 발생한 난수(0~1) 100000개 생성
    ML.append(  ((1.00199925134584-i)/1.00199925134584)**(-1/1.35)   ) #m(질량값)으로 변환한 값




#난수로 만든 salpter's line 분포 를 나타낸다
plt.hist(ML,bins=np.logspace(np.log10(1),np.log10(100),500),histtype='step') #bin도 logscale로 설정
#rn.plt.hist(ML,bins=np.logspace(np.log10(1),np.log10(100),500),histtype='step',density=True)
#난수로 만든 Salpeter's line의 확률분포를 나타낸다(density=True)->Salepter's line 과 비교
plt.title('Salpeter IMF(N=100000)')
plt.xscale('log') #x축 logscale로 변경
plt.yscale('log') #y축 logscale로 변경
plt.xlabel("log(M)[M$\odot$]")
plt.ylabel("log(Number)")

"""
#Salpter's line의 확률 분포를 plot
x1=np.linspace(1,100,10000)
y1=C*x1**(-2.35)
plt.plot(x1,y1)
"""
plt.show()