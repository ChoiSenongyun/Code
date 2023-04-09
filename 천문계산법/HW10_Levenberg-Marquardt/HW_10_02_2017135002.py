import numpy as np
from scipy.integrate import romberg
from sympy import Integral, Symbol



def snfw(R):
    return  4*np.pi*(R**2)*( 1.5/ (  (R/10)*(1+R/10)**2 ) )

########## 정적분 값 구하기#####################
r=Symbol('r')
f=4*np.pi*(r**2)*( 1.5/ (  (r/10)*(1+r/10)**2 ) )
print(Integral(f,(r,0.0001,100)).doit())


"""
###########Extended Trapezoidal##################
h=4 #h값 변경하면서 변화 확인
r=np.arange(0.0001,100,h)
t=list(r)
t.append(100)
rr=np.array(t)

ET=0
for i in range(len(rr)):
    if i==0:
        ET+= (h*snfw(rr[i]))/2

    elif i==len(rr)-1:
        ET+=(h*snfw(rr[i]))/2

    else:
        ET += (h * snfw(rr[i]))
print( "(h=%s) = %s" % (h, ET))

###########Romberg Algorithm##################
romberg(snfw,0.0001,100,show='True')
"""