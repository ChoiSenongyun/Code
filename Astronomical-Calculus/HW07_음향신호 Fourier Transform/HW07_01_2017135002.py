import wavio
import numpy as np
import matplotlib.pyplot as plt


#피아노 도 추출
sound=wavio.read('Do262.wav')
duration=sound.data.shape[0]*1.0/sound.rate
x=sound.data.flatten()*1.0
y=np.fft.fft(x)
p=np.abs(y)**2
freq=np.fft.fftfreq(sound.data.shape[0])*sound.data.shape[0]/duration
time=np.linspace(0,duration,sound.data.shape[0])

#REAL SPACE
plt.plot(time,sound.data,linewidth=0.1,color='blue')
plt.title('Real Space')
plt.xlabel('Time')
plt.ylabel('Data')
plt.show()
#FFT시
plt.plot(freq,p)
plt.xlim(1,5000)
plt.ylim(10e6,10e17)
plt.yscale('log')
plt.title('FFT')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.show()

#####################Power가 최대( 일정 이상 지점의) 주파수를 구하기##########################
cord=p>10e13




##########내가 도음을 내기
mysound=wavio.read('mydo.wav')
duration1=mysound.data.shape[0]*1.0/mysound.rate
x1=mysound.data.flatten()*1.0
y1=np.fft.fft(x1)
p1=np.abs(y1)**2
freq1=np.fft.fftfreq(mysound.data.shape[0]*2)*mysound.data.shape[0]/duration1
time1=np.linspace(0,duration1,mysound.data.shape[0])
#REAL SPACE
plt.plot(time1,mysound.data,linewidth=0.1,color='blue')
plt.title('Real Space')
plt.xlabel('Time')
plt.ylabel('Data')
plt.show()

#FFT시
plt.plot(freq1,p1,linewidth=0.2)
plt.xlim(1,5000)
plt.ylim(10e3,10e17)
plt.yscale('log')
plt.title('FFT')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.show()



#피아노 파 추출
fsound=wavio.read('pianoF.wav')
duration2=fsound.data.shape[0]*1.0/fsound.rate
x2=fsound.data.flatten()*1.0
y2=np.fft.fft(x2)
p2=np.abs(y2)**2
freq2=np.fft.fftfreq(fsound.data.shape[0]*2)*fsound.data.shape[0]/duration2
time2=np.linspace(0,duration2,fsound.data.shape[0])
#REAL SPACE
plt.plot(time2,fsound.data,linewidth=0.05,color='blue')
plt.title('Real Space')
plt.xlabel('Time')
plt.ylabel('Data')
plt.show()


#FFT시
plt.plot(freq2,p2,linewidth=0.2)
plt.xlim(1,5000)
plt.ylim(10e3,10e17)
plt.yscale('log')
plt.title('FFT')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.show()



#피아노 시 추출
bsound=wavio.read('pianoB.wav')
duration3=bsound.data.shape[0]*1.0/bsound.rate
x3=bsound.data.flatten()*1.0
y3=np.fft.fft(x3)
p3=np.abs(y3)**2
freq3=np.fft.fftfreq(bsound.data.shape[0]*2)*bsound.data.shape[0]/duration3
time3=np.linspace(0,duration3,bsound.data.shape[0])
#REAL SPACE
plt.plot(time3,bsound.data,linewidth=0.05,color='blue')
plt.title('Real Space')
plt.xlabel('Time')
plt.ylabel('Data')
plt.show()


#FFT시
plt.plot(freq3,p3,linewidth=0.2)
plt.xlim(1,5000)
plt.ylim(10e3,10e17)
plt.yscale('log')
plt.title('FFT')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.show()

