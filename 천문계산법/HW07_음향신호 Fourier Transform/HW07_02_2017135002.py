import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import matplotlib.colors as co





image=fits.open('image1.fits')
data=image[0].data
H=np.fft.fft2(data)
Hr=H.real
Hi=H.imag
power=abs(H)**2
h=np.fft.ifft2(H)
f=np.fft.fftfreq(100)
fx,fy=np.meshgrid(f,f)
F=(fx**2+fy**2)**0.5


#######fx#######
plt.imshow(fx)
plt.title('fx')
plt.show()
#######fy#######
plt.imshow(fy)
plt.title('fy')
plt.show()
#######F#######
plt.imshow(F)
plt.title('F')
plt.show()

###FFT결과#####
plt.scatter(F,power,s=0.5)
plt.yscale('log')
plt.ylabel('Power')
plt.xlabel('Frequency')
plt.title('FFT')
plt.show()
"""
"""
####### H 실수 부분#######
plt.imshow(Hr,cmap='gray', norm= co.LogNorm(vmin=2000,vmax=10000))
plt.title('Real')
plt.gca().invert_yaxis()
plt.show()
######## H 허수 부분#######
plt.imshow(Hi,cmap='gray', norm= co.LogNorm(vmin=2000,vmax=10000))
plt.title('Imaginary')
plt.gca().invert_yaxis()
plt.show()




subplot=[241,242,243,245,246,247]
title=['original', '|F|<0.4', '|F|>0.4', '|F|<0.1', '|F|>0.1', '|F|>0.2']
hh=[H,H*(abs(F)<0.4),H*(abs(F)>0.4),H*(abs(F)<0.1),H*(abs(F)>0.1),H*(abs(F)>0.2)]
fig=plt.figure(figsize=(5,5))
for i in range(6):
    plt.subplot(subplot[i])
    plt.title(title[i])
    plt.imshow(np.fft.ifft2(hh[i]).real,cmap='gray')

plt.show()
