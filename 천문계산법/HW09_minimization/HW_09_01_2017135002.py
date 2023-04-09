import numpy as np
import matplotlib.pyplot as plt

#첫번째 함수생성
def f1(x):
    y1=( np.sin(x)**2 ) * np.cos(x/4) + 4*(x**4) - 6*(x**3) - 2*x + 6
    return y1
def f2(x):
    y2=-( (np.cos(x/2)**2)/(x**2+5) )-2*np.exp( - ( ( (x-3)**2)/100))
    return y2
#황금비율 리스트 출력
def  opt(x1,x2):
    if x1>x2:
        return [x2,x2*0.61803+x1*0.38197,x2*0.38197+x1*0.61803,x1]
    else:
        return [x1,x2*0.38197+x1*0.61803,x2*0.61803+x1*0.38197, x2]
#linear minimization 재귀 함수를 사용한다.
def lm1(x1,x2):
    X=opt(x1,x2)
    #base 조건을 양끝점 간격이 0.000001 이하일때 종료되도록
    if abs(x1-x2)<0.000001:
        return [x1,x2]
    if f1(X[1]) < f1(X[2]):
        return lm1(x1,X[2])
    else:
        return lm1(X[1],x2)
def lm2(x1,x2):
    X=opt(x1,x2)
    if abs(x1-x2)<0.000001:
        return [x1,x2]
    if f2(X[1]) < f2(X[2]):
        return lm2(x1,X[2])
    else:
        return lm2(X[1],x2)


################# Linear Miniminzation################
print(lm1(-5,5))
print(lm2(-5,5))

#2개점의 평균값을 사용
av1=(lm1(-5,5)[0]+lm1(-5,5)[1])/2
av2=(lm2(-5,5)[0]+lm2(-5,5)[1])/2

t=np.linspace(-5,5,100)


plt.plot(t,f1(t))
plt.scatter(av1,f1(av1),s=25)
plt.xlim(-2,3)
plt.ylim(0,100)
plt.text(0.8,15,'x=1.18705')
plt.text(0.8,10,'f1(x)=2.35431')
plt.title('Line Minimization')
plt.show()


plt.plot(t,f2(t))
plt.scatter(av2,f2(av2),s=25)
plt.xlim(-2,4)
plt.ylim(-2.1,-1.5)
plt.text(0.3,-1.99,'x=0.59875')
plt.text(0.3,-2.02,'f2(x)=-2.05833')
plt.title('Line Minimization')
plt.show()





###설정한 양끝점 내부에 최소값이 없을경우?? 외분 사용?##########



#점 내부의 황금비율 뿐만 아니라 외부에서의 황금비율 점도 고려하여 출력한다.
def  exopt(x1,x2):
    if x1>x2:
        return [ x2*(1/0.61803)-(x1*0.38197)/0.61803,x2,x2*0.61803+x1*0.38197,
                 x2*0.38197+x1*0.61803,x1,x1*(1/0.61803)-(x2*0.38197)/0.61803]
    else:
        return [x1*(1/0.61803)-(x2*0.38197)/0.61803,x1,x2*0.38197+x1*0.61803,
                x2*0.61803+x1*0.38197, x2, x2*(1/0.61803)-(x1*0.38197)/0.61803]

##linear miniminzation 도중 내분, 외분 한점이 이외에 x1,x2에서 최소를 가진다면??
def lm3(x1,x2):
    X=exopt(x1,x2)
    c=[f1(X[0]),f1(X[1]),f1(X[2]),f1(X[3]),f1(X[4]),f1(X[5])]
    if abs(x1-x2)<0.000001:
        return [x1,x2]
    if min(c)==f1(X[0]):
        return lm3(X[0],X[1])
    elif min(c)==f1(X[1]):
        return lm3(X[0],X[1])
    elif min(c)==f1(X[2]):
        return lm3(X[1],X[2])
    elif min(c)==f1(X[3]):
        return lm3(X[3],X[4])
    elif min(c)==f1(X[4]):
        return lm3(X[4],X[5])
    elif min(c)==f1(X[5]):
        return lm3(X[4],X[5])

def lm4(x1,x2):
    X=exopt(x1,x2)
    c=[f2(X[0]),f2(X[1]),f2(X[2]),f2(X[3]),f2(X[4]),f2(X[5])]
    if abs(x1-x2)<0.000001:
        return [x1,x2]
    if min(c)==f2(X[0]):
        return lm4(X[0],X[1])
    elif min(c)==f2(X[1]):
        return lm4(X[0],X[1])
    elif min(c)==f2(X[2]):
        return lm4(X[1],X[2])
    elif min(c)==f2(X[3]):
        return lm4(X[3],X[4])
    elif min(c)==f2(X[4]):
        return lm4(X[4],X[5])
    elif min(c)==f2(X[5]):
        return lm4(X[4],X[5])
"""
print(lm3(3,5))
print(lm4(3,5))

av3=(lm3(3,5)[0]+lm3(3,5)[1])/2
av4=(lm4(3,5)[0]+lm4(3,5)[1])/2

t=np.linspace(-5,5,100)

######## 내부에 global miniminum이 없을때    외분도 고려  ##################

plt.plot(t,f1(t))
plt.scatter(3,f1(3),s=25)
plt.scatter(av3,f1(av3),s=25)
plt.scatter(5,f1(5),s=25)
plt.xlim(0,5.5)
plt.ylim(-50,2000)
plt.text(0.8,150,'x=1.18705')
plt.text(0.8,50,'f1(x)=2.35431')
plt.title('Line Minimization')
plt.show()


plt.plot(t,f2(t))
plt.scatter(3,f2(3),s=25)
plt.scatter(av4,f2(av4),s=25)
plt.scatter(5,f2(5),s=25)
plt.xlim(0,5.5)
plt.text(0.3,-1.97,'x=0.59875')
plt.text(0.3,-2.02,'f2(x)=-2.05833')
plt.title('Line Minimization')
plt.show()
"""



"""
##################################  local minimum이 여러곳  ##########################
t=np.linspace(-4,5,100)

def f3(x):
    return (x-2)*(3*x+1)*(x-4)*(x+3)



def lm5(x1,x2):
    X=exopt(x1,x2)
    c=[f3(X[0]),f3(X[1]),f3(X[2]),f3(X[3]),f3(X[4]),f3(X[5])]
    if abs(x1-x2)<0.000001:
        return [x1,x2]
    if min(c)==f3(X[0]):
        return lm5(X[0],X[1])
    elif min(c)==f3(X[1]):
        return lm5(X[0],X[1])
    elif min(c)==f3(X[2]):
        return lm5(X[1],X[2])
    elif min(c)==f3(X[3]):
        return lm5(X[3],X[4])
    elif min(c)==f3(X[4]):
        return lm5(X[4],X[5])
    elif min(c)==f3(X[5]):
        return lm5(X[4],X[5])
print(lm5(-3,4))
print(lm5(2,4))

av5=(lm5(-2,4)[0]+lm5(-2,4)[1])/2
av6=(lm5(2,4)[0]+lm5(2,4)[1])/2

plt.plot(t,f3(t))
plt.scatter(-3,f3(-3),s=25)
plt.scatter(av5,f3(av5),s=25)
plt.scatter(4,f3(4),s=25)
plt.title('Line Minimization')
plt.show()

plt.plot(t,f3(t))
plt.scatter(2,f3(2),s=25)
plt.scatter(av6,f3(av6),s=25)
plt.scatter(4,f3(4),s=25)
plt.title('Line Minimization')
plt.show()
"""