
import numpy as np
import scipy.stats  as ss
import matplotlib.pyplot as plt
import math as mp

data=np.array([70.3, 72.6, 65.7, 68.9, 75.7, 73.0, 69.4, 71.0, 72.6, 67.3 ])
data.sort()
n=len(data)
v=n-1
X=np.average(data)
S=np.sqrt(np.sum( (data-X)**2)/(n-1))
tvalue=(X-5)/ (S/np.sqrt(n))

########## t distribution ############
f=mp.gamma( (v+1)/2)/ ( mp.sqrt(v*mp.pi) * mp.gamma(v/2)) * (1+((data-X)**2)/v )**(-(v+1)/2)
plt.plot(data-X,f)
plt.show()



y=ss.ttest_1samp(data,65,alternative='two-sided')
print(y)
