import numpy as np
import matplotlib.pyplot as plt
def fun1(a,b):
    return b*np.exp(a)-2*b

def f1dera(a,b):
    return b*np.exp(a)

def f1derb(a,b):
    return np.exp(a)-2

def fun2(a,b):
    return a*b-b**3

def f2dera(a,b):
    return b

def f2derb(a,b):
    return a-3*b**2

def invjac(a,b):
    J=np.array([ [f1dera(a,b),f1derb(a,b)],[f2dera(a,b),f2derb(a,b)]],dtype='float')
    return np.linalg.inv(J)

def jac(a,b):
    J=np.array([ [f1dera(a,b),f1derb(a,b)],[f2dera(a,b),f2derb(a,b)]],dtype='float')
    return J
##########################Newton Raphson#########################
x1=np.random.uniform(-5,5,1000)
x2=np.random.uniform(-5,5,1000)


def nr(a,b):
    X1=[]
    X2=[]
    N=[]
    for i in range(1000):
        T=[[a[i]],[b[i]]]
        n=0
        try:
            while n<100:
                np.seterr(over='raise')
                n+=1
                if abs(fun1(T[0][0], T[1][0])) < 10e-12 and abs(fun2(T[0][0], T[1][0])) < 10e-12:
                    N.append(n)
                    X1.append(T[0][0])
                    X2.append(T[1][0])
                    break
                else:
                    T=T-np.dot(invjac(T[0][0],T[1][0]),[[fun1(T[0][0],T[1][0])],[fun2(T[0][0],T[1][0])]])

        except:
            pass
    return np.array(X1),np.array(X2),N
"""
T[1][0] 즉 b 값이 0에 가까워지면 a가 어떤 값을 가져도 식이 성립하기 때문에 a값이 무한으로 커질경우 np.exp(a)으로 인하여 overflow가 발생할수 있다.
이를 방지하기 위하여 np.seterr(over='raise') 로 overflow가 발생하면 error 가 발생하게 하고 except 문을 사용하여
error 발생시 pass 하여 그냥 넘어가도록 한다
"""


X1,X2,N=nr(x1,x2)
#평균 횟수 구하기
print(np.average(N))
#분포 그리기
"""

plt.scatter(X1,X2,s=1)
plt.xlim(-5,5)
plt.show()
"""
#Solution 찾기
"""
print(X1[X1>0.6])
print(X2[X2<-0.8])
"""

#############Broyden Method#################################
x1=np.random.uniform(-5,5,1000)
x2=np.random.uniform(-5,5,1000)

def bro(a,b):
    X1=[]
    X2=[]
    N=[]
    for i in range(1000):
        T =[[a[i]],[b[i]]]
        J=jac(T[0][0],T[1][0])  # 첫 자코비안 저장
        Tn=T-np.dot(np.linalg.inv(J),[[fun1(T[0][0], T[1][0])],[fun2(T[0][0], T[1][0])]]) #그다음 X2 생성
        n=1
        try:
            while n<100:
                np.seterr(over='raise')
                n+=1
                if abs(fun1(Tn[0][0], Tn[1][0])) < 10e-12 and abs(fun2(Tn[0][0], Tn[1][0])) < 10e-12:
                    N.append(n)
                    X1.append(Tn[0][0])
                    X2.append(Tn[1][0])
                    break
                else:
                    df=[fun1(Tn[0][0], Tn[1][0])-fun1(T[0][0], T[1][0]), fun2(Tn[0][0], Tn[1][0])-fun2(T[0][0], T[1][0])] #함수값의 변화량
                    dx=[Tn[0][0]-T[0][0],Tn[1][0]-T[1][0]] # a,b의 변화량
                    sizedx=(Tn[0][0]-T[0][0])**2+(Tn[1][0]-T[1][0])**2  # 변화량 크기의 제곱
                    J=J+ np.outer((df-np.dot(J, dx)),dx)/sizedx   # 새로운 자코비안 저장
                    T=Tn
                    Tn=T-np.dot(np.linalg.inv(J),[[fun1(T[0][0], T[1][0])],[fun2(T[0][0], T[1][0])]])
        except:
            pass
    return np.array(X1),np.array(X2),N

XX1,XX2,NN=bro(x1,x2)
#평균 횟수 구하기
print(np.average(NN))
#분포그리기###
"""

plt.scatter(XX1,XX2,s=1)
plt.xlim(-5,5)
plt.show()
"""
"""
#Solution 찾기
print(XX1[XX1>0.6])
print(XX2[XX2<-0.8])
"""