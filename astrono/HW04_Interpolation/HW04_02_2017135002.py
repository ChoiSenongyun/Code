import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
j,m1=np.loadtxt('sn.dat',usecols=(1,2),skiprows=1,unpack=True)
jd=np.linspace(min(j),max(j),102)
jd=jd[1:101] #JD의 최대값과 최소값 사이를 100 개의 균등한 간격으로 나누었다 (최대값과 최소값은 포함하지않는다)

###############################################Newtons Method 재귀함수 사용하여 구현###############################################
cof=[]
mm=[]
def co(n,m):
   global j
   global m1
   if n==0:
       return m1[m]
   else:
       return ( co(n-1,m)-co(n-1,n-1) )/ (j[m]-j[n-1])
for i in range(16):
    cof.append(co(i,i))
def nw(k,x):
    global j
    global m1
    global cof
    n=len(j)-1
    if k==0: return cof[n]
    else:
        return cof[n-k]+(x-j[n-k])*nw(k-1,x)
for i in jd:
    mm.append(nw(15,i))

plt.scatter(j,m1,s=50,c='r',marker='x')
plt.scatter(jd,mm,s=4)
plt.gca().invert_yaxis()
#plt.ylim(20,15)   ##y축 범위조정
plt.title("Newtons's" )
plt.xlabel('Julian Date')
plt.ylabel('B-mag')
plt.show()

"""
###############################################nevile 재귀함수 사용하여 구현#########################################
def ne(n, m, a):
    global m1
    global j
    if n == m:
        return m1[n - 1]
    else:
        return ((a - j[m - 1]) * ne(n, m - 1, a) + (j[n - 1] - a) * ne(n + 1, m, a)) / (j[n - 1] - j[m - 1])
mm = []
for i in jd:
    mm.append(ne(1, 16, i))

plt.scatter(j, m1, s=50, c='r', marker='x')
plt.scatter(jd, mm, s=4)
plt.gca().invert_yaxis()
plt.title("nevil's")
plt.xlabel('Julian Date')
plt.ylabel('B-mag')
#plt.ylim(20,15)
plt.show()

"""
"""
###############################################Neville 라이브러리 참고###############################################
def neville(xData,yData,x):
    m=len(xData)
    y=yData.copy()
    for k in range(1,m):
        y[0:m-k]=(xData[k:m]-x)*y[0:m-k]+(x-xData[0:m-k])*y[1:m-k+1]
        y[0:m-k]=y[0:m-k]/(xData[k:m]-xData[0:m - k])
    return y[0]
mm=[]
for i in jd:
    mm.append(neville(j,m1,i))

plt.scatter(j,m1,s=50,c='r',marker='x')
plt.scatter(jd,mm,s=4)
plt.gca().invert_yaxis()
#plt.ylim(20,15)
plt.title("Neville's" )
plt.xlabel('Julian Date')
plt.ylabel('B-mag')
plt.show()
"""

"""
###############################################Neville 직접 3차 interpolation 까지 구현###############################################
NA=[]
for a in range(100):
    for b in range(16):
        #하지만 이 if문은 b가 13일때부터는 리스트의 범위를 초과하여 따로 정해준다
        #b<=12인 경우의 if문 j[b] ~ j[b+3] 을 사용하여 Neville's Algorithm 사용
        if j[b]<jd[a]<j[b+1] and b<=12:
            P12=((jd[a]-j[b+1])*m1[b]+(j[b]-jd[a])*m1[b+1] )/(j[b]-j[b+1])
            P23=((jd[a]-j[b+2])*m1[b+1]+(j[b+1]-jd[a])*m1[b+2] )/(j[b+1]-j[b+2])
            P34=((jd[a]-j[b+3])*m1[b+2]+(j[b+2]-jd[a])*m1[b+3] )/(j[b+2]-j[b+3])
            P123=( (jd[a]-j[b+2])*P12+(j[b]-jd[a])*P23 )/(j[b]-j[b+2])
            P234=( (jd[a]-j[b+3])*P23+(j[b+1]-jd[a])*P34 )/(j[b+1]-j[b+3])
            P1234=( (jd[a]-j[b+3])*P123+(j[b]-jd[a])*P234 )/(j[b]-j[b+3])
            NA.append(P1234)
        # b>12인 경우의 if문 j[b-2] ~ j[b+1] 을 사용하여 Neville's Algorithm 사용
        elif j[b] < jd[a] < j[b + 1] and b > 12:
            P12 = ((jd[a] - j[b - 1]) * m1[b - 2] + (j[b - 2] - jd[a]) * m1[b - 1]) / (j[b - 2] - j[b - 1])
            P23 = ((jd[a] - j[b]) * m1[b - 1] + (j[b - 1] - jd[a]) * m1[b]) / (j[b - 1] - j[b])
            P34 = ((jd[a] - j[b+1]) * m1[b] + (j[b] - jd[a]) * m1[b+1]) / (j[b] - j[b+1])
            P123 = ((jd[a] - j[b]) * P12 + (j[b-2] - jd[a]) * P23) / (j[b-2] - j[b])
            P234 = ((jd[a] - j[b+1]) * P23 + (j[b-1] - jd[a]) * P34) / (j[b-1] - j[b+1])
            P1234 = ((jd[a] - j[b+1]) * P123 + (j[b-2] - jd[a]) * P234) / (j[b-2] - j[b+1])
            NA.append(P1234)

plt.scatter(j,m1,s=50,c='r',marker='x')
plt.scatter(jd,NA,s=4)
plt.gca().invert_yaxis()
plt.ylim(20,15)
plt.title("Neville's" )
plt.xlabel('Julian Date')
plt.ylabel('B-mag')
plt.show()

"""

"""
###############################################Neville의 단점 보완하기 위하여 합체###############################################
def neville(xData,yData,x):
    m=len(xData)
    y=yData.copy()
    for k in range(1,m):
        y[0:m-k]=(xData[k:m]-x)*y[0:m-k]+(x-xData[0:m-k])*y[1:m-k+1]
        y[0:m-k]=y[0:m-k]/(xData[k:m]-xData[0:m - k])
    return y[0]
mm=[]
for i in jd:
    mm.append(neville(j,m1,i))

tj=[]
NA=[]
for a in range(100):
    for b in range(16):
        if j[b] < jd[a] < j[b + 1] and b == 12:
            P12 = ((jd[a] - j[b + 1]) * m1[b] + (j[b] - jd[a]) * m1[b + 1]) / (j[b] - j[b + 1])
            P23 = ((jd[a] - j[b + 2]) * m1[b + 1] + (j[b + 1] - jd[a]) * m1[b + 2]) / (j[b + 1] - j[b + 2])
            P34 = ((jd[a] - j[b + 3]) * m1[b + 2] + (j[b + 2] - jd[a]) * m1[b + 3]) / (j[b + 2] - j[b + 3])
            P123 = ((jd[a] - j[b + 2]) * P12 + (j[b] - jd[a]) * P23) / (j[b] - j[b + 2])
            P234 = ((jd[a] - j[b + 3]) * P23 + (j[b + 1] - jd[a]) * P34) / (j[b + 1] - j[b + 3])
            P1234 = ((jd[a] - j[b + 3]) * P123 + (j[b] - jd[a]) * P234) / (j[b] - j[b + 3])
            NA.append(P1234)
            tj.append(jd[a])
        elif j[b] < jd[a] < j[b + 1] and b > 12:
            P12 = ((jd[a] - j[b - 1]) * m1[b - 2] + (j[b - 2] - jd[a]) * m1[b - 1]) / (j[b - 2] - j[b - 1])
            P23 = ((jd[a] - j[b]) * m1[b - 1] + (j[b - 1] - jd[a]) * m1[b]) / (j[b - 1] - j[b])
            P34 = ((jd[a] - j[b+1]) * m1[b] + (j[b] - jd[a]) * m1[b+1]) / (j[b] - j[b+1])
            P123 = ((jd[a] - j[b]) * P12 + (j[b-2] - jd[a]) * P23) / (j[b-2] - j[b])
            P234 = ((jd[a] - j[b+1]) * P23 + (j[b-1] - jd[a]) * P34) / (j[b-1] - j[b+1])
            P1234 = ((jd[a] - j[b+1]) * P123 + (j[b-2] - jd[a]) * P234) / (j[b-2] - j[b+1])
            NA.append(P1234)
            tj.append(jd[a])

plt.scatter(j,m1,s=50,c='r',marker='x')
plt.scatter(tj,NA,s=4)
plt.scatter(jd,mm,s=4)
plt.gca().invert_yaxis()
plt.ylim(20,15)
plt.title("Neville's" )
plt.xlabel('Julian Date')
plt.ylabel('B-mag')
plt.show()
"""
