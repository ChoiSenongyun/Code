import numpy as np
import matplotlib.pyplot as plt

def der(x,y):
    return 2*x*y

def exact(x):
    return np.exp(x**2)/(10*np.exp(1))

def rk2(initial,target,h):
    X = initial[0]
    Y = initial[1]
    N = int((target - X) / h)
    error=[]
    for i in range(N):
        k1=h*der(X, Y)
        k2=h*der(X+h/2,Y+k1/2)
        X+=h
        Y+=k2
        error.append(exact(X)-Y)
    return Y, error,N


def rk4(initial,target,h):
    X=initial[0]
    Y=initial[1]
    N=int((target-X)/h)
    error=[]
    for i in range(N):
        k1=h*der(X,Y)
        k2=h*der(X+h/2,Y+k1/2)
        k3=h*der(X+h/2,Y+k2/2)
        k4=h*der(X+h,Y+k3)
        X+=h
        Y+=k1/6+k2/3+k3/3+k4/6
        error.append(exact(X)-Y)
    return Y, error,N


def anotherrunge(initial,target,h):
    X=initial[0]
    Y=initial[1]
    N=int((target-X)/h)
    error=[]
    for i in range(N):
        k1=h*der(X,Y)
        k2=h*der(X+h/3,Y+k1/3)
        k3=h*der(X+h*2/3,Y+k2-k1/3)
        k4=h*der(X+h,Y+k3-k2+k1)
        X+=h
        Y+=k1/8+k2*3/8+k3*3/8+k4/8
        error.append(exact(X)-Y)
    return Y, error,N

def rk5(initial,target,h):
    X=initial[0]
    Y=initial[1]
    N=int((target-X)/h)
    error=[]
    for i in range(N):
        k1=h*der(X,Y)
        k2=h*der(X+h*0.0869565,Y+k1*0.0869565)
        k3=h*der(X+h*0.324324,Y+k2*0.604821-k1*0.280496)
        k4=h*der(X+h*0.931034,Y+k3*4.8-k2*12.9184+k1*9.049492)
        k5=h*der(X+h*0.995,Y-k4*0.05558+k3*7.02827-k2*19.9258+k1*13.948144)
        k6=h*der(X+h,Y-k5*0.005572-k4*0.052479+k3*7.1923-k2*20.4497+k1*14.315445)
        X+=h
        Y+=k1*0.097345+k2*0+k3*0.49226+k4*2.472-k5*20.08661+k6*18.025
        error.append(exact(X)-Y)
    return Y, error,N


###### 자유낙하 운동 runge 를 통하여 분석##############

def fallder(t,y):
    return -9.8*t+15
def fallexact(t):
    return -4.9*(t**2)+15*t

def fallrk4(initial,target,h):
    X=initial[0]
    Y=initial[1]
    N=int((target-X)/h)
    list=[]
    for i in range(N):
        list.append(Y)
        k1=h*fallder(X,Y)
        k2=h*fallder(X+h/2,Y+k1/2)
        k3=h*fallder(X+h/2,Y+k2/2)
        k4=h*fallder(X+h,Y+k3)
        X+=h
        Y+=k1/6+k2/3+k3/3+k4/6
    return Y,list

##second order runge########
Y2,error2,N2=rk2((1,0.1),1.8,0.05)
##fourth order runge########
Y4,error4,N4=rk4((1,0.1),1.8,0.05)
##fifth order runge#########
Y5,error5,N5=rk5((1,0.1),1.8,0.05)
#####point 지점을 달리한 runge #####
Y,error,N=anotherrunge((1,0.1),1.8,0.05)
##낙하운동 추정하는 runge####
Yfall,Ylist=fallrk4((0,0),3,0.1)
Ylist.append(Yfall)



"""
####운동 그래프 그리기 ############
time=np.arange(0,3.1,0.1)
##### 예측한 운동은 scatter#########
plt.scatter(time,Ylist,color='red')
#### 실제 운동은 plot ########
plt.plot(time,fallexact(time))
plt.xlabel('Time')
plt.ylabel('Position')
plt.show()
"""