from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
x = [0.5, 0.6, 0.7,0.8,
           0.6, 0.7,0.8,0.9,
                  0.7,0.8,0.9,
                      0.8,0.9]
y = [10 ,10 ,10 ,10 ,
            10.4,10.4,10.4,10.4,
               10.8,10.8,10.8,
                11.2,11.2]

dx =[0.1,0.1, 0.1,0.1,
           0.1, 0.1,0.1,0.1,
                  0.1,0.1,0.1,
                    0.1,0.1]
dy =[0.4,0.4, 0.4,0.4,
           0.4, 0.4,0.4,0.4,
                  0.4,0.4,0.4,
                    0.4,0.4]

agnsfr=np.array([-10.273985, -10.340201, -10.938989, -11.289973,
                 -10.277444, -10.686158, -11.184431, -11.460366,
                 -10.703556, -11.180832, -11.573596,
                 -11.44062, -12.028493])

starformsft=np.array([-9.888726, -10.054034, -10.302167, -10.600964,
                      -10.05661, -10.262769, -10.5789795, -10.879129,
                      -10.31187, -10.58854, -10.840707,
                      -10.698455, -10.897933])

z=starformsft-agnsfr
print(agnsfr)
print(starformsft)
print(z)
fig = plt.figure()
ax = fig.add_subplot()
minv, maxv = 0,  1.13056
cmap = plt.cm.jet
norm = plt.Normalize(minv, maxv)
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm, ax=ax ,location='right').ax.set_title(label='log($\\frac{SSFR(Starforming)}{SSFR(Agn)}$ ) ',size=15,rotation=-360)

ax.set_xlim(0.5,1)
ax.set_ylim(10,11.6)
for x, y, c, h,hh in zip(x, y, z, dx,dy):
    ax.add_artist(Rectangle(xy=(x, y),
                  color=cmap(c),        # I did c**2 to get nice colors from your numbers
                  width=h, height=hh))      # Gives a square of area h*h

plt.xlabel('g-r',fontsize=15)
plt.ylabel('logM/$M_{\odot}$',fontsize=15)

plt.show()


