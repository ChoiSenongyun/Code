import matplotlib.pyplot as plt
import numpy as np # 산점도 및 추세선을 그리기 위하여 numpy 모듈 추가
import time # 시간 관련 함수를 사용하기 위하여 time 모듈 추가



A=16807
C=2147483647
Q=127773
R=2836
X=1
"""
X=time.time()  # X초기값을 현재 시간의 실수값으로 설정한다-이로서 x값을 랜덤한 값으로 지정한다
"""
N=[]
T=[]
for i in range(10000): # 10000번 반복하는 for문
    X=A*(X%Q)-R*(X//Q)  # %은 나머지를 반환하는 연산자, //은 몫을 반환하는 연산자
    if X<0:    # X값이 음수인경우 C를 더하여 양수를 만들어준다
        X=X+C
    """ 
        if X==0: # X값이 0이 되었을때 다른수로 바꾸어주는 식
        X=1
    """
    N.append(X)  # N리스트에 X값 추가
M=max(N) # 0과 1사이의 난수값을 발생시키위하여 N리스트에 있는 값을 (최대값+1)로 나누어준다
for i in N:
    T.append(i/(M+1))  # N리스트를 0과 1사이의 변수로 만들어 새로운 리스트에 넣어준다



plt.hist(T,bins=100) #누적확률밀도함수 만들시 plt.hist(T,bins=100,density=True, cumulative=True)을 사용한다
plt.title("Pseudo-Random Number Generator(bins=100)")
plt.xlabel("Random Number")
plt.ylabel("Number")
plt.xlim(min(T), max(T))  # x축 범위를 T리스트내의 최소값 최대값으로 설정한다
plt.show()

"""   
산점도를 그리기 위하여 T1리스트에 1~10000까지 넣어준다
T1=[]
for i in range(10000):  
    T1.append(i)
T리스트를 크기 순서대로 정렬 
T.sort() 


산점도를 그리면서 추세선을 나타내는 식
z=np.polyfit(T1,T,1)
p=np.poly1d(z)
pylab.plot(T1,T,'o')
pylab.plot(T1,p(T1),"r--")
pylab.show()
print("y=%.6fx+(%.6f)" %(z[0], z[1]))
"""


"""
발생한 랜덤 난수들의 평균을 구하는 식
A=0
for i in T:
    A=A+i
print(A/10000)
"""

