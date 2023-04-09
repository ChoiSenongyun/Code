import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, solve
from scipy.interpolate import CubicSpline as cs
from scipy.interpolate import UnivariateSpline

j,m=np.loadtxt('sn.dat',usecols=(1,2),skiprows=1,unpack=True)
jd=np.linspace(min(j),max(j),102)
jd=jd[1:101] #JD의 최대값과 최소값 사이를 100 개의 균등한 간격으로 나누었다 (최대값과 최소값은 포함하지않는다)

###############################################직접 구현##################################################
y0=Symbol('y0')
y1=Symbol('y1')
y2=Symbol('y2')
y3=Symbol('y3')
y4=Symbol('y4')
y5=Symbol('y5')
y6=Symbol('y6')
y7=Symbol('y7')
y8=Symbol('y8')
y9=Symbol('y9')
y10=Symbol('y10')
y11=Symbol('y11')
y12=Symbol('y12')
y13=Symbol('y13')
y14=Symbol('y14')
y15=Symbol('y15')
y0=0
y15=0

Y=[y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15]
e=[]
for i in range(14):
    e.append((j[i+1]-j[i])*Y[i]/6+(j[i+2]-j[i])*Y[i+1]/3+(j[i+2]-j[i+1])*Y[i+2]/6-(m[i+2]-m[i+1])/(j[i+2]-j[i+1])+(m[i+1]-m[i])/(j[i+1]-j[i]))
result=solve(e)
k=list(result.values())
for i in range(1,6):
    k.append(k[i])
del k[1:6]
k.insert(0,0)
k.insert(15,0)
bm=[]
mm=0
for a in range(100):
    mm=0
    for b in range(16):
        if j[b]<jd[a]<j[b+1]:
            e=str('y')+str(b)
            f =str('y') + str(b+1)
            A=(j[b+1]-jd[a])/(j[b+1]-j[b])
            B=(jd[a]-j[b])/(j[b+1]-j[b])
            C=(A**3-A) * ((j[b+1]-j[b])**2) / 6
            D = (B ** 3 - B) * ((j[b + 1] - j[b]) ** 2) / 6
            mm=A*m[b]+B*m[b+1]+C*k[b]+D*k[b+1]
            bm.append(mm)

plt.scatter(j,m,s=50,c='r',marker='x')
plt.scatter(jd,bm,s=4)
plt.gca().invert_yaxis()
plt.title("Cubic's" )
plt.xlabel('Julian Date')
plt.ylabel('B-mag')
plt.show()


"""
###############################################라이브러리로 구현##################################################
cb=cs(j,m)
plt.scatter(j,m,s=50,c='r',marker='x')
plt.scatter(jd,cb(jd),s=4)
plt.gca().invert_yaxis()
plt.title('Cubic')
plt.xlabel('Julian Date')
plt.ylabel('B-mag')
plt.show()
"""


###############################################3개 방법 비교##################################################


"""
###############################################Linear 의 first derivates 구하기###############################################
bm=[]
mm=0
for a in range(100):
    mm=0
    for b in range(16):
        if j[b]<jd[a]<j[b+1]:
            mm=m[b]+(m[b+1]-m[b])/(j[b+1]-j[b])*(jd[a]-j[b])
            bm.append(mm)
fdm = np.diff(bm) / np.diff(jd)
fdjd = (np.array(jd)[:-1] + np.array(jd)[1:]) / 2

plt.scatter(fdjd,fdm)
plt.ylim(-0.3,0.3)
plt.title('Linear first derivates')
plt.show()
"""

"""
###############################################nevile first derivates 구하기###############################################
def neville(xData,yData,x):
    m=len(xData)
    y=yData.copy()
    for k in range(1,m):
        y[0:m-k]=(xData[k:m]-x)*y[0:m-k]+(x-xData[0:m-k])*y[1:m-k+1]
        y[0:m-k]=y[0:m-k]/(xData[k:m]-xData[0:m - k])
    return y[0]
mm=[]
for i in jd:
    mm.append(neville(j,m,i))

fdm = np.diff(mm) / np.diff(jd)
fdjd = (np.array(jd)[:-1] + np.array(jd)[1:]) / 2
plt.scatter(fdjd,fdm)
plt.ylim(-0.3,0.3)
plt.title('neville first derivates')
plt.show()
"""

"""
###############################################cubic first derivates 구하기###############################################
cb=cs(j,m)
fdm = np.diff(cb(jd)) / np.diff(jd)
fdjd = (np.array(jd)[:-1] + np.array(jd)[1:]) / 2
plt.scatter(fdjd,fdm)
plt.ylim(-0.3,0.3)
plt.ylim(-0.3,0.3)
plt.title('spline first derivates')
plt.show()
"""


"""
###############################################Linear 의 second derivates 구하기###############################################
bm=[]
mm=0
for a in range(100):
    mm=0
    for b in range(16):
        if j[b]<jd[a]<j[b+1]:
            mm=m[b]+(m[b+1]-m[b])/(j[b+1]-j[b])*(jd[a]-j[b])
            bm.append(mm)

j_spl = UnivariateSpline(jd,bm,s=0,k=4)
j_spl_2d = j_spl.derivative(n=2)
plt.scatter(jd,j_spl_2d(jd))
plt.title('Linear second derivates')
plt.ylim(-0.2,0.2)
plt.show()
"""

"""
###############################################nevile second derivates 구하기###############################################
def neville(xData,yData,x):
    m=len(xData)
    y=yData.copy()
    for k in range(1,m):
        y[0:m-k]=(xData[k:m]-x)*y[0:m-k]+(x-xData[0:m-k])*y[1:m-k+1]
        y[0:m-k]=y[0:m-k]/(xData[k:m]-xData[0:m - k])
    return y[0]
mm=[]
for i in jd:
    mm.append(neville(j,m,i))

j_spl = UnivariateSpline(jd,mm,s=0,k=4)
j_spl_2d = j_spl.derivative(n=2)
plt.scatter(jd,j_spl_2d(jd))
plt.title('nevile second derivates')
plt.ylim(-0.2,0.2)
plt.show()
"""

"""
###############################################cubic second derivates 구하기###############################################
cb=cs(j,m)
j_spl = UnivariateSpline(jd,cb(jd),s=0,k=4)
j_spl_2d = j_spl.derivative(n=2)
plt.scatter(jd,j_spl_2d(jd))
plt.ylim(-0.2,0.2)
plt.title('spline second derivates')
plt.show()
"""