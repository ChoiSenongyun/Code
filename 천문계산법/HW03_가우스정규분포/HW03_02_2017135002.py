from HW02_1_2017135002 import myran
import numpy as np
import matplotlib.pyplot as plt

#변수들 생상
a=np.array(myran(100000))
b=np.array(myran(100000))
c=np.array(myran(100000))
d=np.array(myran(100000))
e=np.array(myran(100000))
f=np.array(myran(100000))
g=np.array(myran(100000))
h=np.array(myran(100000))
i=np.array(myran(100000))
j=np.array(myran(100000))

fig=plt.figure(figsize=(12,8))

ax1=fig.add_axes([0.08,0.6,0.4,0.35])
ax2=fig.add_axes([0.55,0.6,0.4,0.35])
ax3=fig.add_axes([0.08,0.1,0.4,0.35])
ax4=fig.add_axes([0.55,0.1,0.4,0.35])

"""
#난수들의 합
ax1.hist(a,bins=100)
ax2.hist(a+b,bins=100)
ax3.hist(a+b+c,bins=100)
ax4.hist(a+b+c+d+e+f+g+h+i+j,bins=100)
"""
"""
#난수들의 곱
ax1.hist(a,bins=100)
ax2.hist(a*b,bins=100)
ax3.hist(a*b*c,bins=100)
ax4.hist(a*b*c*d*e*f*g*h*i*j,bins=100)
"""
#난수들의 곱의 log
ax1.hist(np.log(a),bins=100)
ax2.hist(np.log(a*b),bins=100)
ax3.hist(np.log(a*b*c),bins=100)
ax4.hist(np.log(a*b*c*d*e*f*g*h*i*j),bins=100)


ax1.set_title('log(Random Number)')
ax2.set_title('log (product of 2 Random Number)')
ax3.set_title('log (product of 3 Random Number)')
ax4.set_title('log (product of 10 Random Number)')
plt.show()



