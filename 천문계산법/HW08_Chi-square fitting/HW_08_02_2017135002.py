import numpy as np
import matplotlib.pyplot as plt
import random as rd
mo=np.loadtxt('xy.dat')
x=mo[:,0]
y=mo[:,1]
yer=mo[:,2]


def ch(a,b):
    return np.sum(((y-a-b*x)/yer)**2)


def determine(x1,x2,x3,y1,y2,y3):
    ch1=ch(x1,y1)
    ch2=ch(x2,y2)
    ch3=ch(x3,y3)
    CH=[[ch1,x1,y1],[ch2,x2,y2],[ch3,x3,y3]]
    CH.sort() #정렬에서 왼쪽에 ch값 작은거 오른쪽에 ch값 큰걸로 정렬
    # CH[2] 부분을 reflection 한 값
    rex=CH[0][1]+CH[1][1]-CH[2][1]
    rey=CH[0][2]+CH[1][2]-CH[2][2]
    chre=ch(rex,rey)
    if chre<=CH[0][0]:  #최저값이면 EXTENSION
        exx=2*rex-(CH[0][1]+CH[1][1])/2
        exy = 2 * rey - (CH[0][2] + CH[1][2]) / 2
        chex=ch(exx,exy)
        if chex<=chre: #extension이 reflection 보다 작으면
            return CH[0][1], CH[1][1],exx, CH[0][2], CH[1][2], exy
        elif  chex>chre:  #extension이 reflection보다 크면
            return CH[0][1], CH[1][1],rex, CH[0][2], CH[1][2], rey
    elif chre>CH[0][0] and chre<=CH[1][0]: #reflection 값이 중간값이면
        return CH[0][1], CH[1][1],rex, CH[0][2], CH[1][2], rey

    elif  chre>CH[1][0]:  #reflection 한 값이 최고값이면 contraction
        cox=(CH[0][1]+CH[1][1]+CH[2][1])/2
        coy =(CH[0][2] + CH[1][2] + CH[2][2]) / 2
        chco=ch(cox,coy)
        if chco>CH[1][0]: #여전히 최고갑이면 shrink 함
            return CH[0][1],(CH[1][1]+CH[0][1])/2, (CH[2][1]+CH[0][1])/2, CH[0][2],  (CH[1][2]+CH[0][2])/2, (CH[2][2]+CH[0][2])/2
        else: #아니면 contraction 반환
            return CH[0][1],CH[1][1], cox, CH[0][2], CH[1][2],  coy

def downhill(x1,x2,x3,y1,y2,y3):
    p=[x1,x2,x3,y1,y2,y3]
    px=[]
    py=[]
    maxx=0
    mix=0
    may=0
    miy=0
    N=0
    while 1:
        N+=1
        #삼각형이 움직인 경로 저장
        px.append([p[0],p[1],p[2]])
        py.append([p[3],p[4],p[5]])
        #움직인 경로를 나타낼 평면의 경계 지정
        if max([p[0],p[1],p[2]])>maxx: maxx=max([p[0],p[1],p[2]])
        if max([p[3],p[4],p[5]]) > may: may = max([p[3],p[4],p[5]])
        if min([p[0],p[1],p[2]])<mix: mix=min([p[0],p[1],p[2]])
        if min([p[3],p[4],p[5]]) <miy: miy = min([p[3],p[4],p[5]])
        """
        # 삼각형의 변의 길이 기준으로 수렴조건
        if np.sqrt(  ((p[0]-p[1])**2 + (p[3]-p[4])**2  )+ ((p[1]-p[2])**2 + (p[4]-p[5])**2 ) +( (p[0]-p[2])**2 + (p[3]-p[5])**2) ) <0.00001:
            return p, px, py, maxx, mix, may, miy,N
            break
        """
        """
         # 3 지점에서 reduced chi squre가 1이하일때
        if ch(p[0],p[3])/12 < 1 and ch(p[1],[4]) < 1 and ch(p[2],p[5]) <1 :
            return p, px, py, maxx, mix, may, miy,N
            break
        """

        """
        # 삼각형 넓이 기준으로  수렴조건
        if np.abs(p[0] * p[4] + p[3] * p[2] + p[5] * p[1] - p[4] * p[2] - p[3] * p[1] - p[0] * p[5]) / 2 < 0.0001:
            return p, px, py, maxx, mix, may, miy,N
            break
        """
        if np.sqrt(((p[0] - p[1]) ** 2 + (p[3] - p[4]) ** 2) + ((p[1] - p[2]) ** 2 + (p[4] - p[5]) ** 2) + (
                (p[0] - p[2]) ** 2 + (p[3] - p[5]) ** 2)) < 0.00001:
            return p, px, py, maxx, mix, may, miy, N
            break
        else: p=determine(p[0],p[1],p[2],p[3],p[4],p[5])

#초기 삼각형은 무작위로 지정 gif의 경우(5,0,-3,4,-4,2)

p,px,py,maxx,minx,maxy,miny,N=downhill(5,0,-3,4,-4,2)
#random 으로 좌표 설정
#p,px,py,maxx,minx,maxy,miny,N=downhill(rd.randrange(-100,100),rd.randrange(-100,100),rd.randrange(-100,100),rd.randrange(-100,100),rd.randrange(-100,100),rd.randrange(-100,100))
print(p[0],p[3])
print(p[1],p[4])
print(p[2],p[5])
"""
#reduced chi square
print(ch(p[0],p[3])/12)
print(ch(p[1],p[4])/12)
print(ch(p[2],p[5])/12)
"""


#downhill 과정의  나온 최대, 최소값으로 경계지정
a=np.linspace(minx,maxx,100)
b=np.linspace(miny,maxy,100)
chi=np.zeros((100,100))

for i in range(len(a)):
    for j in range(len(b)):
        chi[i][j]=ch(a[j],b[i])

"""
# 삼각형 경로이미지 plot
for i in range(len(px)):
    plt.contourf(a, b, chi)
    plt.colorbar()
    line=plt.Polygon([(px[i][0],py[i][0]),(px[i][1],py[i][1]),(px[i][2],py[i][2])],closed=True,fill=None,edgecolor='r')
    plt.gca().add_line(line)
    plt.title('downhill %s' % str(i + 1))
    plt.xlabel('a')
    plt.ylabel('b')
    #plt.savefig('downhill %s'% str(i+1))
    plt.show()
"""



"""
##오차 구하기
h=0.000001
am=(p[0]+p[1]+p[2])/3
bm=(p[3]+p[4]+p[5])/3

aerr=1/np.sqrt(  (ch(am+h,bm)- 2*ch(am,bm)  +ch(am-h,bm) )/h**2 )
berr=1/np.sqrt(  (ch(am,bm+h)- 2*ch(am,bm)  +ch(am,bm-h) )/h**2 )

print(aerr)
print(berr)
"""





