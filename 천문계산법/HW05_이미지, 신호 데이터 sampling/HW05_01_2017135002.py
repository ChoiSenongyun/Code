from astropy.io import fits
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

import math as ma

data1=fits.open('image1.fits')
image1=data1[0].data
a=np.linspace(0,100,100)
b=np.linspace(0,100,100)
x=np.linspace(0,100,500)
y=np.linspace(0,100,500)
nearest=np.zeros((500,500))

##neighbor####
for i in range(500):
     for j in range(500):
          nearest[int(i)][int(j)]=image1[int(i/5)][int(j/5)]
##linear##
bilnear1=interpolate.interp2d(a,b,image1,kind='linear')
bilnear2=bilnear1(x,y)
##cubic##
cubic1=interpolate.interp2d(a,b,image1,kind='cubic')
cubic2=cubic1(x,y)
###############################neighbor#############################
"""
plt.imshow(nearest,cmap='gray')     
plt.gca().invert_yaxis()
plt.title('nearest')
plt.show()
"""
#########neighbor의 data 리스트에 모두 담기(비교를 위하여)#########

nh=[]
for i in range(len(nearest)):
    for j in range(len(nearest[0])):
        nh.append(nearest[i][j])

########################bilnear###########################
""" 
plt.imshow(bilnear2,cmap='gray')
plt.gca().invert_yaxis()
plt.title('linear')
plt.show()
"""
#########linear의 data 리스트에 모두 담기(비교를 위하여)#########

lh=[]
for i in range(len(bilnear2)):
    for j in range(len(bilnear2[0])):
        lh.append(bilnear2[i][j])

#######################cubic#########################
""" 
plt.imshow(cubic2,cmap='gray')
plt.gca().invert_yaxis()
plt.title('cubic')
plt.show()
"""
#########cubic의 data 리스트에 모두 담기(비교를 위하여)#########

ch=[]
for i in range(len(cubic2)):
    for j in range(len(cubic2[0])):
        ch.append(cubic2[i][j])

#########원본 image의 data 리스트에 모두 담기(비교를 위하여)#########
oh=[]
for i in range(len(image1)):
    for j in range(len(image1[0])):
        oh.append(image1[i][j])

"""
plt.hist(oh,bins=100)
plt.title('original')
plt.show()
"""
"""
plt.hist(nh,bins=100)
plt.title('nearest')
plt.show()
"""
"""
plt.hist(lh,bins=100)
plt.title('linear')
plt.show()
"""
"""
plt.hist(ch,bins=100)
plt.title('cubic')
plt.show()
"""

#########psnr을 통한 비교#########
"""
original=cv.imread('original.png')
contrast=cv.imread('cubic.png')

def psnr(img1,img2):
     mse = np.mean((img1 - img2) ** 2)
     print("mse:",mse)
     if mse == 0:
          return 100
     PIXEL_MAX = 255.0
     return 20 * ma.log10(PIXEL_MAX / ma.sqrt(mse))
d = psnr(original, contrast)
print(d)
"""


