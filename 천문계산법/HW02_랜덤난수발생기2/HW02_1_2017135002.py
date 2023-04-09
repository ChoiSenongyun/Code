import matplotlib.pyplot as plt
import math
import numpy as np
A = 16807
C = 2147483647
Q = 127773
R = 2836
X = 1
M = C+1 # 최대값으로 나누어주기 위하여 Schrage's algorithm을 20000번 반복했을때 최대값을 구한다
T=[]  # 32개의 난수가 들어있는 shuffling 방
N=[]  # Schrage's Algorithm을 위한 임시 리스트
for i in range(32):
    X = A * (X % Q) - R * (X // Q)
    if X < 0:
        X = X + C
    N.append(X)



for i in N:
    T.append(i / (M + 1))  # 32개의 난수가 들어있는 shuffling 방 생성


def myran(n=1,seed=0):
# n은 발생시키는 난수 갯수, shuffling후 X값을 초기화 시키지않고 계속해서 계산,n=1은 myran에 입력값을 주지않으면 n은 1을 갖게된다. seed=0은 seed가 입력되지않을때 seed에 0 반환
    global T,A,C,Q,R,M,N,X
    T1=[] # shuffling method 도중 발생 시킨 2개의 난수를 넣는 배열
    T2=[] # shuffling method로 발생시킨 n개의 난수를 담을 배열
    if seed: #seed에 0이외 값인경우 true로 if문 실행
        X=seed #시드값 대입
        T = []  # shuffling 방을 초기화 시킨다.
        N=[] #임시리스트 초기화
        for i in range(32):
            X = A * (X % Q) - R * (X // Q)
            if X < 0:
                X = X + C
            N.append(X)
        for i in N:
            T.append(i / (M + 1))  # 새로운 시드값으로 shuffling 방 생성
        print("New Seed")
    elif n==-1: # n=-1인경우 shuffling 방 초기화
        T=[] #shuffling 방을 초기화 시킨다.
        for i in range(32):
            X = A * (X % Q) - R * (X // Q)
            if X < 0:
                X = X + C
            N.append(X)
        for i in N:
            T.append(i / (M + 1))  # 32개의 난수가 들어있는 shuffling 방 다시생성
        print("the room is reset")

    #n번 반복하여 난수 n개 생성
    else: # seed=0이고 아무 값도 입력되지않고 n값만 입력되었을때 (n=-1인경우 제외)
        for i in range(n):
                N=[]
                T1=[] #매번 난수발생을 할때 마다 초기화시켜줘야한다. (아니면 계속  축적이 된다)
                for i in range(2):
                     X=A*(X%Q)-R*(X//Q)
                     if X < 0:
                        X = X + C
                     N.append(X)
                for i in N:
                    T1.append(i/(M+1))  # 2개의 난수가 들어있는 shuffling 방  (최대값으로 나누어진 값을 구하면 1에 근접한 값이 하나 무조거 나온다)
                x=T1[0]
                y=math.trunc(T1[1]*32) #0~31의 숫자로 변환 소수부분은 버린다
                T2.append(T[y]) #T2리스트에  발생시킨 32개의 난수중 y번째 난수를 넣어준다
                T[y]=x #y번째 난수를 x를 대입해준다.
        return T2


#히스토그램으로 표현
if __name__=="__main__": #해당 모듈을 import 하였을때 실행되지않기위한 if문문
    plt.hist(myran(10000),bins=100)
    plt.axhline(y=100, color='r', linewidth=1)
    plt.title("Suffling method")
    plt.xlabel("Random Number")
    plt.ylabel("Number")
    plt.xlim(min(T), max(T))  # x축 범위를 T리스트내의 최소값 최대값으로 설정한다
    plt.show()
"""
    #난수들의 상관관계를 보기위한 식
    N=[]
    for i in range(100):
        N.append(i)
    
    plt.plot(N,myran(100)) #100개의 난수 발생
    plt.xlabel("Random Number Order")
    plt.ylabel("Shuffling's Random Number")
    plt.xlim(0, 100)
    plt.ylim(0, 1)
    plt.show()
        
"""





