import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate as integrate
from scipy.stats import multivariate_normal

dtype = [('objID', np.uint64),('Z','<f4'),
          ('u','<f4'), ('g','<f4'), ('r','<f4'), ('i','<f4'),('z','<f4'),
         ('OIII','<f4'),('NII','<f4'),('Ha','<f4'), ('Hb','<f4'),('subclass','<U20'),
         ('logmass','<f4'),('logmassun','<f4'),('oh2.5','<f4'),('oh16','<f4'),('oh50','<f4')
         ,('oh84','<f4'),('oh97.5','<f4'),('lgm2.5','<f4'),('lgm16','<f4'),('lgm50','<f4')
         ,('lgm84','<f4'),('lgm97.5','<f4'),('sfr2.5','<f4'),('sfr16','<f4'),('sfr50','<f4')
         ,('sfr84','<f4'),('sfr97.5','<f4'),('disp','<f4'),('sn','<f4')
         ,('erOIII','<f4'),('erNII','<f4'),('erHa','<f4'), ('erHb','<f4')
         , ('d4000','<f4'), ('d4000n','<f4'), ('pe50u','<f4'), ('pe50g','<f4')
         , ('pe50r','<f4'), ('pe50i','<f4'), ('pe50z','<f4'), ('pe90u','<f4')
         ,('pe90g','<f4') , ('pe90r','<f4'), ('pe90i','<f4'), ('pe90z','<f4')
         ,('fwhmu','<f4'),('fwhmg','<f4'),('fwhmr','<f4'),('fwhmi','<f4'),('fwhmz','<f4')]


galaxy = np.genfromtxt("/Users/kkang/Downloads/galaxy12_kkang65382.csv",dtype=dtype,
                     delimiter=',', skip_header=1)
galaxy=np.delete(galaxy, np.where(galaxy['sn']<3),axis=0)
galaxy=np.delete(galaxy, np.where(galaxy['lgm50']==-9999),axis=0)
galaxy=np.delete(galaxy, np.where(galaxy['sfr50']==-9999),axis=0)
galaxy=np.delete(galaxy, np.where(galaxy['disp']==0),axis=0)
galaxy=np.delete(galaxy, np.where(galaxy['disp']==850),axis=0)
galaxy=np.delete(galaxy, np.where(galaxy['OIII']/galaxy['erOIII']<3),axis=0)
galaxy=np.delete(galaxy, np.where(galaxy['NII']/galaxy['erNII']<3),axis=0)
galaxy=np.delete(galaxy, np.where(galaxy['Ha']/galaxy['erHa']<3),axis=0)
galaxy=np.delete(galaxy, np.where(galaxy['Hb']/galaxy['erHb']<3),axis=0)

#### Redshift 제한######
#galaxy=np.delete(galaxy, np.where(galaxy['Z']>0.1),axis=0)

############### 우주론 반영한 데이터 전 처리###############################
## volume limit
# c= 3*10**5km/s, H_0*70km/s/Mpc
d_H = (3 * 10 ** 5 )/ 70  ##c=3*10^5 km/s, H_0=70km/s/Mpc
#comoving distance
def func_z(z_0):
    return 1/np.sqrt(0.3*(1+z_0)**3 + 0.7)
def int_z(z_0):
    return integrate.quad(func_z, 0, z_0)[0]
vec_int_z = np.vectorize(int_z)
d_c = d_H*vec_int_z(galaxy['Z']).astype(np.float16)
#luminosity distance
d_L=d_c*(1+galaxy['Z']).astype(np.float16)

#distance
M=galaxy['r']-5*np.log10(d_L)-25
#Absolute magnitude limit
z_max=max(galaxy['Z']).astype(np.float16)
d_max=d_H*vec_int_z(z_max)*(1+z_max)

M_lim=17.77-5*np.log10(d_max)-25
print(M_lim)

galaxy=np.delete(galaxy, np.where(M>M_lim),axis=0)
M=np.delete(M, np.where(M>M_lim),axis=0)
#######################################################################

########## 은하군 분류##################################################
null=galaxy[np.where(galaxy['subclass']=='null')]
agn=galaxy[np.where(galaxy['subclass']=='AGN')]
starform=galaxy[np.where(galaxy['subclass']=='STARFORMING')]
starburst=galaxy[np.where(galaxy['subclass']=='STARBURST')]

Mnull=M[np.where(galaxy['subclass']=='null')]
Magn=M[np.where(galaxy['subclass']=='AGN')]
Mstarform=M[np.where(galaxy['subclass']=='STARFORMING')]
Mstarburst=M[np.where(galaxy['subclass']=='STARBURST')]


agnpar=1.2*(np.log10(agn['NII']/agn['Ha'])+0.4)+np.log10(agn['OIII']/agn['Hb'])
starformpar=1.2*(np.log10(starform['NII']/starform['Ha'])+0.4)+np.log10(starform['OIII']/starform['Hb'])

agnst=agn[np.where(agnpar>0.7)]
Magnst=Magn[np.where(agnpar>0.7)]

starformst=starform[np.where(starformpar<0.1)]
Mstarformst=Mstarform[np.where(starformpar<0.1)]

#######################################################################
agnc=agnst['pe90r']/agnst['pe50r']
starformc=starformst['pe90r']/starformst['pe50r']


################# 아래는 데이터를 시각화 하며 그릅과 데이터간의 상관관계 찾기 ############################
"""
plt.scatter(np.logstarformst['disp'],starformst['sfr50'],color='blue',s=1,label='STARFORMING',alpha=0.5)
plt.scatter(agnst['disp'],agnst['sfr50'],color='red',s=1,label='AGN')

plt.legend(fontsize=15)

plt.ylim(-4,4)
plt.xlabel('Mr',fontsize=15)
plt.ylabel('SFR Log Msun/yr',fontsize=15)
plt.title('Mr - SFR',fontsize=15)
plt.show()

"""

"""
## redshift ssfr                                       
plt.scatter(starformst['Z'],starformst['sfr50']-starformst['lgm50'],color='r',label='AGN')
plt.show()
"""
                                         
                                         
                                         
##redshift에 따른 비율
"""

bins=np.arange(0.03,0.1,0.002)
agnhist,agnbins=np.histogram(agn['Z'],bins)
starformhist,starformbins=np.histogram(starform['Z'],bins)

agnhistn=np.array(agnhist)/len(agn['Z'])
starformhistn=np.array(starformhist)/len(starform['Z'])



plt.step(bins[:-1],agnhistn,where='mid',color='r',label='AGN')
plt.step(bins[:-1],starformhistn,where='mid',color='b',label='STARFORMING')
plt.legend(fontsize=15)
plt.xlabel('Z redshift',fontsize=15)
plt.ylabel('N density',fontsize=15)
plt.show()
"""

## mass 분포 비율
bins=np.arange(7,12,0.05)
agnhist,agnbins=np.histogram(agnst['lgm50'],bins)
starformhist,starformbins=np.histogram(starformst['lgm50'],bins)

agnhistn=np.array(agnhist)/len(agnst['lgm50'])
starformhistn=np.array(starformhist)/len(starformst['lgm50'])

plt.step(agnbins[:-1],agnhistn,where='mid',color='r',label='AGN')
plt.step(starformbins[:-1],starformhistn,where='mid',color='b',label='STARFORMING')
plt.legend(fontsize=15,loc='upper left')
plt.xlabel('logM/$M_{\odot}$',fontsize=15)
plt.ylabel('N density',fontsize=15)
plt.xlim(9.5,11.5)
plt.show()







"""
## g-r and dispersion
plt.scatter(starformst['g']-starformst['r'],starformst['disp'],color='blue',s=1,label='STARFORMING')
plt.scatter(agnst['g']-agnst['r'],agnst['disp'],color='red',s=1,label='AGN')
plt.legend()
plt.xlabel('g-r')
plt.xlim(0,1.25)
plt.ylabel('Dispersion')
plt.show()
"""
"""
## g-r and Mass
plt.scatter(starformst['g']-starformst['r'],starformst['lgm50'],color='blue',s=1,label='STARFORMING')
plt.scatter(agnst['g']-agnst['r'],agnst['lgm50'],color='red',s=1,label='AGN')
plt.legend()
plt.xlabel('g-r')
plt.xlim(0.5,1)
plt.ylim(10,11.6)
plt.ylabel('logM/$M_{\odot}$')
plt.show()

"""







"""
# mass and d4000
plt.scatter(starformst['lgm50'],starformst['d4000'],color='blue',s=1,label='STARFORMING')
plt.scatter(agnst['lgm50'],agnst['d4000'],color='red',s=1,label='AGN')
plt.legend()
plt.xlim(6,14)
plt.xlabel('logM/$M_{\odot}$')
plt.ylabel('D4000')
plt.show()
"""

"""
#concetration 비율
plt.hist(starformc,bins=20,color='blue',density=True,label='STARFORMING',alpha=0.75)
plt.hist(agnc,bins=20,color='red',density=True,label='AGN',alpha=0.75)
plt.xlabel('Concentration')
plt.legend()
plt.show()
"""
"""
# mass and concetration
plt.scatter(starformst['lgm50'],starformc,color='blue',s=1,label='STARFORMING')
plt.scatter(agnst['lgm50'],agnc,color='red',s=1,label='AGN')
plt.legend()
plt.xlim(6,14)
plt.xlabel('logM/$M_{\odot}$')
plt.ylabel('Concetration')
plt.show()
"""
"""
#d4000 비율
plt.hist(starformst['d4000'],bins=20,color='blue',density=True,label='STARFORMING',alpha=0.75)
plt.hist(agnst['d4000'],bins=20,color='red',density=True,label='AGN',alpha=0.75)
plt.xlabel('D4000')
plt.legend()
plt.show()
"""
"""
plt.scatter(starformst['Z'],starformst['disp'],color='blue',s=1,label='STARFORMING')
plt.scatter(agnst['Z'],agnst['disp'],color='red',s=1,label='AGN')
plt.legend()

plt.show()
"""

"""
## mass and o3
plt.scatter(starformst['lgm50'],starformst['OIII'],color='blue',s=1,label='STARFORMING')
plt.scatter(agnst['lgm50'],agnst['OIII'],color='red',s=1,label='AGN')
plt.legend()
plt.xlim(6,14)
plt.ylim(0,5000)
plt.xlabel('logM/$M_{\odot}$')
plt.ylabel('OIII flux [10-17 ergs/cm2/s/A]')
plt.show()

"""
"""
#green valley
plt.scatter(Mnull,null['u']-null['r'],color='RED',s=1,label='Passive',alpha=0.2)
plt.scatter(Mstarformst,starformst['u']-starformst['r'],color='blue',s=1,label='STARFORMING',alpha=0.2)
plt.scatter(Magnst,agnst['u']-agnst['r'],color='black',s=2,label='AGN')
plt.legend()
plt.xlabel('Absolute Magnitude r')
plt.ylabel('u-r')
plt.gca().invert_xaxis()
"""




"""
plt.scatter(Mnull,null['u']-null['r'],color='RED',s=1,label='Passive')
plt.show()
"""
"""
plt.contour(Mnull, null['u']-null['r'], rv.pdf(pos))
plt.show()
"""


## h and sfr
"""
plt.scatter(np.log10(starformst['Ha']),starformst['sfr50'],color='blue',s=1,label='STARFORMING')
plt.scatter(np.log10(agnst['Ha']),agnst['sfr50'],color='red',s=1,label='AGN')
plt.scatter(np.log10(null['Ha']),null['sfr50'],color='green',s=1,label='null')
plt.legend()
plt.xlim(0,5)
plt.ylim(-4,4)
plt.show()
"""

"""
## mass 분포 비율
plt.hist(starformst['lgm50'],bins=20,color='blue',density=True,label='STARFORMING',alpha=0.75)
plt.hist(agnst['lgm50'],bins=20,color='red',density=True,label='AGN',alpha=0.75)
plt.xlabel('logM/$M_{\odot}$')
plt.legend()
plt.show()
"""


"""
#mass and h alpha flux
plt.scatter(starformst['lgm50'],starformst['Ha'],color='blue',s=1,label='STARFORMING')
plt.scatter(agnst['lgm50'],agnst['Ha'],color='red',s=1,label='AGN')
plt.legend()
plt.xlim(6,14)
plt.ylim(0,5000)
plt.xlabel('logM/$M_{\odot}$')
plt.ylabel('H alpha flux [10-17 ergs/cm2/s/A]')
plt.show()

"""

"""
# mass and dispersion
plt.scatter(starformst['lgm50'],starformst['disp'],color='blue',s=1,label='STARFORMING')
plt.scatter(agnst['lgm50'],agnst['disp'],color='red',s=1,label='AGN')
plt.legend()
plt.xlim(6,14)
plt.xlabel('logM/$M_{\odot}$')
plt.ylabel('Velocity Dispersion [km/s]')
plt.show()
"""

"""
# mass and sfr
plt.scatter(starformst['lgm50'],starformst['sfr50'],color='blue',s=1,label='STARFORMING',alpha=0.5)
plt.scatter(agnst['lgm50'],agnst['sfr50'],color='red',s=1,label='AGN')

plt.legend(fontsize=15)
plt.xlim(9,12)
plt.ylim(-4,4)
plt.xlabel('logM/$M_{\odot}$',fontsize=15)
plt.ylabel('SFR Log Msun/yr',fontsize=15)
plt.title('Mass - SFR',fontsize=15)
plt.show()


# magnitude and sfr
plt.scatter(Mstarformst,starformst['sfr50'],color='blue',s=1,label='STARFORMING',alpha=0.5)
plt.scatter(Magnst,agnst['sfr50'],color='red',s=1,label='AGN')

plt.legend(fontsize=15)
plt.xlim(-23,-20.75)
plt.ylim(-4,4)
plt.xlabel('Mr',fontsize=15)
plt.ylabel('SFR Log Msun/yr',fontsize=15)
plt.title('Mr - SFR',fontsize=15)
plt.show()

plt.scatter(starformst['Z'],starformst['sfr50'],color='blue',s=1,label='STARFORMING',alpha=0.5)
plt.scatter(agnst['Z'],agnst['sfr50'],color='red',s=1,label='AGN')

plt.legend(fontsize=15)

plt.ylim(-4,4)
plt.xlabel('Z redshift',fontsize=15)
plt.ylabel('SFR Log Msun/yr',fontsize=15)
plt.title('Z - SFR',fontsize=15)
plt.show()

"""
"""
# bpt 
plt.scatter(np.log10(agn['NII']/agn['Ha']),np.log10(agn['OIII']/agn['Hb']),color='red',s=1,label='AGN',alpha=0.2)
plt.scatter(np.log10(starform['NII']/starform['Ha']),np.log10(starform['OIII']/starform['Hb']),color='blue',s=1,label='STARFORMING',alpha=0.2)
plt.scatter(np.log10(agnst['NII']/agnst['Ha']),np.log10(agnst['OIII']/agnst['Hb']),color='red',s=1,label='High AGN')
plt.scatter(np.log10(starformst['NII']/starformst['Ha']),np.log10(starformst['OIII']/starformst['Hb']),color='blue',s=1,label='High STARFORMING')

plt.legend(fontsize=15)
plt.xlim(-2,2)
plt.ylim(-2.5,2.5)
plt.xlabel('log10(NII/Ha)',fontsize=15)
plt.ylabel('log10(OIII/Hb)',fontsize=15)
plt.show()
"""