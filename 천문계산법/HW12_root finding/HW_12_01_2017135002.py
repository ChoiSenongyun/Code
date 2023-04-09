import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def fun(c):
    return ( c**3/(np.log(1+c)-c/(1+c)))-10



##미분한 함수 구하기
x=sp.symbols('x')
y=x**3/(sp.log(1+x)-x/(1+x))-10
yp=sp.diff(y)
###1차 도함수
def derfun(x):
    return -x**4/((x + 1)**2*(-x/(x + 1) + np.log(x + 1))**2) + 3*x**2/(-x/(x + 1) + np.log(x + 1))
ypp=sp.diff(yp)
####2차 도함수
def der2fun(x):
    return 2*x**5/((x + 1)**4*(-x/(x + 1) + np.log(x + 1))**3) + 2*x**4/((x + 1)**3*(-x/(x + 1) + np.log(x + 1))**2) - 7*x**3/((x + 1)**2*(-x/(x + 1) + np.log(x + 1))**2) + 6*x/(-x/(x + 1) + np.log(x + 1))
def bis(a,b):
    C=[]
    c=(a+b)/2
    N=1 # c=(a+b)/2 으로 이미 한번 bisection 한번 실행한것
    while not fun(c)< 10e-12 or not fun(c)>  -10e-12:
        C.append(abs(fun(c)))
        N+=1
        if fun(a)*fun(c)<0:
            b=c
            c=(a+b)/2
            continue #continue를 넣지 않으면 아래의 if문도 실행될 경우가 있다
        if fun(b)*fun(c)<0:
            a=c
            c=(a+b)/2
            continue
    C.append(abs(fun(c)))
    return c, N,C
c1,N1,C1=bis(1,6)
def secant(a,b):
    C=[]
    c=a-fun(a)*(b-a)/(fun(b)-fun(a))
    N=1
    while not fun(c) < 10e-12 or not fun(c) > -10e-12:
        C.append(abs(fun(c)))
        N+=1
        a=b
        b=c
        c=a-fun(a)*(b-a)/(fun(b)-fun(a))
    C.append(abs(fun(c)))
    return c, N,C
c2,N2,C2=secant(1,6)

def false(a,b):
    C=[]
    c=a-fun(a)*(b-a)/(fun(b)-fun(a))
    N=1
    while not fun(c) < 10e-12 or not fun(c) > -10e-12:
        C.append(abs(fun(c)))
        a=c
        c=a-fun(a)*(b-a)/(fun(b)-fun(a))
        N+=1
    C.append(abs(fun(c)))
    return c, N,C
c3,N3,C3=false(1,6)

def newton(a):
    C=[]
    b=a-fun(a)/derfun(a)
    N=1
    while not fun(b) < 10e-12 or not fun(b) > -10e-12:
        C.append(abs(fun(b)))
        a=b
        b=a-fun(a)/derfun(a)
        N+=1
    C.append(fun(b))
    return b, N,C
c4,N4,C4=newton(6)

print(c1,c2,c3,c4)
print(N1,N2,N3,N4)

########################Convergence rate 비교############################
p=sp.symbols('p')

#############bisectiondml rate#############
"""
plt.plot(C1)
plt.yscale('log')
plt.show()
"""
CC1=[]
for i in range(len(C1)-1):
    CC1.append(C1[i+1]/C1[i])

#############secant#############
"""
plt.plot(C2)
plt.ylim(10e-15,10)
plt.yscale('log')
plt.show()
"""
CC2=[]
for i in range(len(C2)-1):
    CC2.append(C2[i+1]/C2[i])
M2=der2fun(c2)/(2*derfun(c2))
q1=M2-C2[5]/(C2[4]**p)  ### RATE 값#######
#print(sp.solve(q1))
#############false#############
"""
plt.plot(C3)
plt.ylim(10e-15,10)
plt.yscale('log')
plt.show()
"""
CC3=[]
for i in range(len(C3)-1):
    CC3.append(C3[i+1]/C3[i])

#############newton#############
"""
plt.plot(C4)
plt.yscale('log')
plt.show()
"""
CC4=[]
for i in range(len(C4)-1):
    CC4.append(C4[i+1]/C4[i])
M4=der2fun(c4)/(2*derfun(c4))
q2=M4-C4[5]/(C4[4]**p)    ### RATE 값#######
#print(sp.solve(q2))