import numpy as np
import matplotlib.pyplot as pl

x=np.linspace(0,99,100) #xarray 생성 (0~99)
####x=100*np.sin(x) #sinx를 가지는 h에 대하여 DFT 하면 어떻게 될까아

a=len(x) #x의 개수 (N)이 변화 하더라도 DFT가 가능하게 주파수,k 등을 설정해준다)
f1=np.linspace(0,1-1/a,a)
f2=f1*(f1>0.5)-1
#주파수 생성
f=np.array(list(f1)[:51]+list(f2)[51:])
f.sort()

k=np.linspace(1,a,a) #k 생성 (1~N-1)

# 주파수의 범위 설정하기
#f=0
fa=0
#f절대값<0.02
ft=abs(f)<0.02
fb=f[ft]
#f절대값>0.02
ft=abs(f)>0.02
fc=f[ft]
#f절대값<0.1
ft=abs(f)<0.1
fd=f[ft]
#f절대값>0.1
ft=abs(f)>0.1
fe=f[ft]
#f=0.5
ff=0.5
#f 10개
fg=f[-11:-1]



# 100*100 행렬 생성후 계산하면 only size-1 arrays can be converted to Python scalars 에러가 발생하여 1*10000로 생성후 다시 100*100으로 바꾸어준다
def DFT(f,x,k):
    a = len(k)
    if type(f) == int or type(f)==float:
        b = 1
    else:
        b = len(f)
    xt = x.repeat(b)  # X값 원소 ab개수
    ft = np.tile(f, (1, a))[0]  # f값 원소 ab개수
    kt = k.repeat(b)  # k값 원소 ab개수
    FT=xt*np.exp(-2j*np.pi*kt*ft) #DFT값 원소 ab개수
    dft =FT.reshape(a, b) #a*b 출력
    return np.sum(dft,0)#합으로 b개수 만큼 출력


###역변환 만들어주기###
def DIFT(f,H,k):
    a = len(k)
    if type(f) == int or type(f)==float:
        b = 1
    else:
        b = len(f)
    ft = np.tile(f, (1, a))[0]
    kt = k.repeat(b)
    Ht=np.tile(H,(1,a))[0]
    FIT= Ht*np.exp(2j*np.pi*kt*ft)
    dift=FIT.reshape(a,b)
    return np.sum(dift,1)/a




#DFT의 Power Spectrum PLOT
pl.scatter(f,abs(DFT(f,x,k))**2,s=2)
pl.yscale('log')
pl.xlim(-0.5,0.5)
pl.ylim(10**3,10**8)
pl.title("DFT's Power Spectrum")
pl.xlabel('Frequency')
pl.ylabel('Power Spectrum')
pl.show()
#DIFT PLOT
pl.scatter(k,DIFT(f,DFT(f,x,k),k),s=2)
pl.title("Discrete Inverse Fourier Transform")
pl.xlabel('Array')
pl.ylabel('Original')
pl.xlim(0,100)
pl.ylim(-105,105)
pl.show()


#앞의 10개의 주파수만 남기고 DIFT PLOT
pl.scatter(k,DIFT(fg,DFT(fg,x,k),k),s=2)
pl.plot(k,DIFT(fg,DFT(fg,x,k),k))
pl.xlabel('Array')
pl.ylabel('Original')
pl.title("Discrete Inverse Fourier Transform")
pl.show()


"""
subplt=[231,232,233,234,235,236,241]
titles=['All','f=0','abs(f)<0.02','abs(f)>0.02','abs(f)<0.1','abs(f)>0.1','f=0.5']
fs=[f,fa,fb,fc,fd,fe,ff]

#DIFT SUBPLOT 사용하여 한번에 출력
pl.figure()
for i in range(7):
    pl.subplot(subplt[i])
    pl.scatter(k,DIFT(fs[i],DFT(fs[i],x,k),k),s=2)
    pl.title(titles[i])
    pl.xlabel('array number')
    pl.ylabel("Original")
    pl.xlim(0, 100)
    pl.ylim(-105, 105)
pl.show()
#DFT SUBPLOT 사용하여 한번에 출력
for i in range(7):
    pl.subplot(subplt[i])
    pl.scatter(fs[i],abs(DFT(fs[i],x,k))**2,s=2)
    pl.title(titles[i])
    pl.xlabel('frequency')
    pl.ylabel("Power")
    pl.yscale('log')
    pl.xlim(-0.5, 0.5)
    pl.ylim(10 ** 3, 10 ** 8)
pl.show()
"""
"""
#주파수 0.5일때 DIFT  확대해서 보기
pl.scatter(k,DIFT(ff,DFT(ff,x,k),k),s=2)
pl.plot(k,DIFT(ff,DFT(ff,x,k),k))
pl.title("Discrete Inverse Fourier Transform")
pl.xlabel('Array')
pl.ylabel('Original')
pl.xlim(0,100)
pl.ylim(-5,5)
pl.show()
"""