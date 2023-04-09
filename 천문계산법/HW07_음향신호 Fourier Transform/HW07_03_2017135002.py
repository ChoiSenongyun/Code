import numpy as np
import matplotlib.pyplot as plt
#가우시안 커널 만들기

#kernel 설정
def cg(sigma,type):
    x = np.linspace(0, 999, 1000)
    G=(np.exp(-((x-500)**2)/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma))
    CG=np.array(list(G[500:])+list(G[:500]))
    if type==1:
        return CG
    elif type==0:
        return G

data=np.loadtxt('noisy_sn.dat')
d=data[:,0]
m=data[:,1]


mirror1=list(m[0:500])
mirror2=list(m[500:])

zerom=np.array(list(np.zeros(500))+list(m)+list(np.zeros(500)))
endm=np.array(list(np.tile(m[0],500))+list(m)+list(np.tile(m[-1],500)))
periodicm=np.array(mirror2+list(m)+mirror1)
mirror1.reverse()
mirror2.reverse()
mirrorm=np.array(mirror1+list(m)+mirror2)


#####zero padding 에서 direct convolution sigma의 변화############
dca=[]
dcb=[]
dcc=[]
dcd=[]
for i in range(1000):
    dca.append(np.sum(zerom[i:i+1000]*cg(1,0)))
    dcb.append(np.sum(zerom[i:i + 1000] * cg(2, 0)))
    dcc.append(np.sum(zerom[i:i + 1000] * cg(5, 0)))
    dcd.append(np.sum(zerom[i:i + 1000] * cg(10, 0)))

subplot=[241,242,245,246]
title=['sigma=1', 'sigma=2', 'sigma=5', 'sigma=10']
dc=[dca,dcb,dcc,dcd]
fig=plt.figure()
fig.suptitle('Direct Convolution')
#direct convoulution
for i in range(4):
    plt.subplot(subplot[i])
    plt.title(title[i])
    plt.gca().invert_yaxis()
    plt.plot(d,dc[i])
    plt.plot(d,m,linewidth=0.2)
plt.show()

##############FFT를 통한 CONVOLUTION
fta=np.fft.ifft(np.fft.fft(m)*np.fft.fft(cg(1,1)))
ftb=np.fft.ifft(np.fft.fft(m)*np.fft.fft(cg(2,1)))
ftc=np.fft.ifft(np.fft.fft(m)*np.fft.fft(cg(5,1)))
ftd=np.fft.ifft(np.fft.fft(m)*np.fft.fft(cg(10,1)))

subplot=[241,242,245,246]
title=['sigma=1', 'sigma=2', 'sigma=5', 'sigma=10']
fft=[fta,ftb,ftc,ftd]
fig=plt.figure()
fig.suptitle('FFT')
for i in range(4):
    plt.subplot(subplot[i])
    plt.title(title[i])
    plt.plot(d,fft[i])
    plt.plot(d,m,linewidth=0.2)
    plt.gca().invert_yaxis()
plt.show()

#####boundary padding##########
index=np.linspace(0,1999,2000)
plt.plot(index,zerom,label='zero')
plt.plot(index,endm,label='end')
plt.plot(index,periodicm,label='periodic')
plt.plot(index,mirrorm,label='mirror')
plt.gca().invert_yaxis()
plt.ylim(20,13)
plt.title('boundary padding')
plt.legend()
plt.show()



#effect of boundary conditions#
zero=[]
end=[]
per=[]
mir=[]
for i in range(1000):
    zero.append(np.sum(zerom[i:i+1000]*cg(10,0)))
    end.append(np.sum(endm[i:i + 1000] * cg(10, 0)))
    per.append(np.sum(periodicm[i:i + 1000] * cg(10, 0)))
    mir.append(np.sum(mirrorm[i:i + 1000] * cg(10, 0)))
plt.plot(d,zero,label='zero')
plt.plot(d,end,label='end')
plt.plot(d,per,label='periodic')
plt.plot(d,mir,label='mirror')
plt.plot(d,m,linewidth=0.2)
plt.gca().invert_yaxis()
plt.title('boundary condition')
plt.legend()
plt.xlabel('date')
plt.ylabel('magnitude')
plt.ylim(20,15)
plt.show()



#####periodic 에서 direct convolution sigma의 변화############
pea=[]
peb=[]
pec=[]
ped=[]
for i in range(1000):
    pea.append(np.sum(periodicm[i:i+1000]*cg(1,0)))
    peb.append(np.sum(periodicm[i:i + 1000] * cg(2, 0)))
    pec.append(np.sum(periodicm[i:i + 1000] * cg(5, 0)))
    ped.append(np.sum(periodicm[i:i + 1000] * cg(10, 0)))

subplot=[241,242,245,246]
title=['sigma=1', 'sigma=2', 'sigma=5', 'sigma=10']
pe=[pea,peb,pec,ped]
fig=plt.figure()
for i in range(4):
    plt.subplot(subplot[i])
    plt.title(title[i])
    plt.gca().invert_yaxis()
    plt.plot(d,pe[i])
    plt.plot(d,m,linewidth=0.2)
plt.show()
