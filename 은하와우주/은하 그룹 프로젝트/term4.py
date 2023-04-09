import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate as integrate
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
#galaxy=np.delete(galaxy, np.where(galaxy['Z']<0.098),axis=0)

#######################################################################

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

agnst=agn[np.where(agnpar>0.8)]
Magnst=Magn[np.where(agnpar>0.8)]

starformst=starform[np.where(starformpar<0.1)]
Mstarformst=Mstarform[np.where(starformpar<0.1)]
agnc=agnst['pe90r']/agnst['pe50r']
starformc=starformst['pe90r']/starformst['pe50r']


###########################################################
agn56=np.delete(agnst, np.where( np.logical_or((agnst['g']-agnst['r'])<0.5 , (agnst['g']-agnst['r'])>=0.6)),axis=0)

agn67=np.delete(agnst, np.where((agnst['g']-agnst['r'])<0.6),axis=0)
agn67=np.delete(agn67, np.where((agn67['g']-agn67['r'])>=0.7),axis=0)

agn78=np.delete(agnst, np.where((agnst['g']-agnst['r'])<0.7),axis=0)
agn78=np.delete(agn78, np.where((agn78['g']-agn78['r'])>=0.8),axis=0)

agn89=np.delete(agnst, np.where((agnst['g']-agnst['r'])<0.8),axis=0)
agn89=np.delete(agn89, np.where((agn89['g']-agn89['r'])>=0.9),axis=0)

agn91=np.delete(agnst, np.where((agnst['g']-agnst['r'])<0.9),axis=0)
agn91=np.delete(agn91, np.where((agn91['g']-agn91['r'])>=1.0),axis=0)

######################################################################
agn561004=np.delete(agn56, np.where(agn56['lgm50']<10.0),axis=0)
agn561004=np.delete(agn561004, np.where(agn561004['lgm50']>=10.4),axis=0)

agn671004=np.delete(agn67, np.where(agn67['lgm50']<10.0),axis=0)
agn671004=np.delete(agn671004, np.where(agn671004['lgm50']>=10.4),axis=0)

agn781004=np.delete(agn78, np.where(agn78['lgm50']<10.0),axis=0)
agn781004=np.delete(agn781004, np.where(agn781004['lgm50']>=10.4),axis=0)

agn891004=np.delete(agn89, np.where(agn89['lgm50']<10.0),axis=0)
agn891004=np.delete(agn891004, np.where(agn891004['lgm50']>=10.4),axis=0)

agn911004=np.delete(agn91, np.where(agn91['lgm50']<10.0),axis=0)
agn911004=np.delete(agn911004, np.where(agn911004['lgm50']>=10.4),axis=0)
######################################################################

agn671048=np.delete(agn67, np.where(agn67['lgm50']<10.4),axis=0)
agn671048=np.delete(agn671048, np.where(agn671048['lgm50']>=10.8),axis=0)

agn781048=np.delete(agn78, np.where(agn78['lgm50']<10.4),axis=0)
agn781048=np.delete(agn781048, np.where(agn781048['lgm50']>=10.8),axis=0)

agn891048=np.delete(agn89, np.where(agn89['lgm50']<10.4),axis=0)
agn891048=np.delete(agn891048, np.where(agn891048['lgm50']>=10.8),axis=0)

agn911048=np.delete(agn91, np.where(agn91['lgm50']<10.4),axis=0)
agn911048=np.delete(agn911048, np.where(agn911048['lgm50']>=10.8),axis=0)
######################################################################
agn781082=np.delete(agn78, np.where(agn78['lgm50']<10.8),axis=0)
agn781082=np.delete(agn781082, np.where(agn781082['lgm50']>=11.2),axis=0)

agn891082=np.delete(agn89, np.where(agn89['lgm50']<10.8),axis=0)
agn891082=np.delete(agn891082, np.where(agn891082['lgm50']>=11.2),axis=0)

agn911082=np.delete(agn91, np.where(agn91['lgm50']<10.8),axis=0)
agn911082=np.delete(agn911082, np.where(agn911082['lgm50']>=11.2),axis=0)
######################################################################
agn891126=np.delete(agn89, np.where(agn89['lgm50']<11.2),axis=0)
agn891126=np.delete(agn891126, np.where(agn891126['lgm50']>=11.6),axis=0)

agn911126=np.delete(agn91, np.where(agn91['lgm50']<11.2),axis=0)
agn911126=np.delete(agn911126, np.where(agn911126['lgm50']>=11.6),axis=0)

###########################################################
sf56=np.delete(starformst, np.where((starformst['g']-starformst['r'])<0.5),axis=0)
sf56=np.delete(sf56, np.where((sf56['g']-sf56['r'])>=0.6),axis=0)

sf67=np.delete(starformst, np.where((starformst['g']-starformst['r'])<0.6),axis=0)
sf67=np.delete(sf67, np.where((sf67['g']-sf67['r'])>=0.7),axis=0)

sf78=np.delete(starformst, np.where((starformst['g']-starformst['r'])<0.7),axis=0)
sf78=np.delete(sf78, np.where((sf78['g']-sf78['r'])>=0.8),axis=0)

sf89=np.delete(starformst, np.where((starformst['g']-starformst['r'])<0.8),axis=0)
sf89=np.delete(sf89, np.where((sf89['g']-sf89['r'])>=0.9),axis=0)

sf91=np.delete(starformst, np.where((starformst['g']-starformst['r'])<0.9),axis=0)
sf91=np.delete(sf91, np.where((sf91['g']-sf91['r'])>=1.0),axis=0)


######################################################################
sf561004=np.delete(sf56, np.where(sf56['lgm50']<10.0),axis=0)
sf561004=np.delete(sf561004, np.where(sf561004['lgm50']>=10.4),axis=0)

sf671004=np.delete(sf67, np.where(sf67['lgm50']<10.0),axis=0)
sf671004=np.delete(sf671004, np.where(sf671004['lgm50']>=10.4),axis=0)

sf781004=np.delete(sf78, np.where(sf78['lgm50']<10.0),axis=0)
sf781004=np.delete(sf781004, np.where(sf781004['lgm50']>=10.4),axis=0)

sf891004=np.delete(sf89, np.where(sf89['lgm50']<10.0),axis=0)
sf891004=np.delete(sf891004, np.where(sf891004['lgm50']>=10.4),axis=0)

sf911004=np.delete(sf91, np.where(sf91['lgm50']<10.0),axis=0)
sf911004=np.delete(sf911004, np.where(sf911004['lgm50']>=10.4),axis=0)
######################################################################

sf671048=np.delete(sf67, np.where(sf67['lgm50']<10.4),axis=0)
sf671048=np.delete(sf671048, np.where(sf671048['lgm50']>=10.8),axis=0)

sf781048=np.delete(sf78, np.where(sf78['lgm50']<10.4),axis=0)
sf781048=np.delete(sf781048, np.where(sf781048['lgm50']>=10.8),axis=0)

sf891048=np.delete(sf89, np.where(sf89['lgm50']<10.4),axis=0)
sf891048=np.delete(sf891048, np.where(sf891048['lgm50']>=10.8),axis=0)

sf911048=np.delete(sf91, np.where(sf91['lgm50']<10.4),axis=0)
sf911048=np.delete(sf911048, np.where(sf911048['lgm50']>=10.8),axis=0)
######################################################################
sf781082=np.delete(sf78, np.where(sf78['lgm50']<10.8),axis=0)
sf781082=np.delete(sf781082, np.where(sf781082['lgm50']>=11.2),axis=0)

sf891082=np.delete(sf89, np.where(sf89['lgm50']<10.8),axis=0)
sf891082=np.delete(sf891082, np.where(sf891082['lgm50']>=11.2),axis=0)

sf911082=np.delete(sf91, np.where(sf91['lgm50']<10.8),axis=0)
sf911082=np.delete(sf911082, np.where(sf911082['lgm50']>=11.2),axis=0)
######################################################################
sf891126=np.delete(sf89, np.where(sf89['lgm50']<11.2),axis=0)
sf891126=np.delete(sf891126, np.where(sf891126['lgm50']>=11.6),axis=0)

sf911126=np.delete(sf91, np.where(sf91['lgm50']<11.2),axis=0)
sf911126=np.delete(sf911126, np.where(sf911126['lgm50']>=11.6),axis=0)


print([np.average(agn561004['sfr50']),np.average(agn671004['sfr50']),np.average(agn781004['sfr50'])
,np.average(agn891004['sfr50']),
np.average(agn671048['sfr50']),np.average([agn781048['sfr50']]),np.average([agn891048['sfr50']]),np.average([agn911048['sfr50']]),
np.average([agn781082['sfr50']]), np.average([agn891082['sfr50']]), np.average([agn911082['sfr50']]),
       np.average([agn891126['sfr50']]), np.average([agn911126['sfr50']])   ])

print([len(agn561004['sfr50']),len(agn671004['sfr50']),len(agn781004['sfr50'])
,len(agn891004['sfr50']),
len(agn671048['sfr50']),len(agn781048['sfr50']),len(agn891048['sfr50']),len(agn911048['sfr50']),
len(agn781082['sfr50']), len(agn891082['sfr50']), len(agn911082['sfr50']),
       len(agn891126['sfr50']), len(agn911126['sfr50'])   ])

print([np.average(sf561004['sfr50']),np.average(sf671004['sfr50']),np.average(sf781004['sfr50'])
,np.average(sf891004['sfr50']),
np.average(sf671048['sfr50']),np.average(sf781048['sfr50']),np.average(sf891048['sfr50']),np.average(sf911048['sfr50']),
np.average(sf781082['sfr50']), np.average(sf891082['sfr50']), np.average(sf911082['sfr50']),
       np.average(sf891126['sfr50']), np.average(sf911126['sfr50'])   ])

print([len(sf561004['sfr50']),len(sf671004['sfr50']),len(sf781004['sfr50'])
,len(sf891004['sfr50']),
len(sf671048['sfr50']),len(sf781048['sfr50']),len(sf891048['sfr50']),len(sf911048['sfr50']),
len(sf781082['sfr50']), len(sf891082['sfr50']), len(sf911082['sfr50']),
       len(sf891126['sfr50']), len(sf911126['sfr50'])   ])
"""
print([np.average(agn561004['sfr50']-agn561004['lgm50']),np.average(agn671004['sfr50']-agn671004['lgm50']),np.average(agn781004['sfr50']-agn781004['lgm50'])
,np.average(agn891004['sfr50']-agn891004['lgm50']),np.average(agn911004['sfr50']-agn911004['lgm50']),
np.average(agn671048['sfr50']-agn671048['lgm50']),np.average(agn781048['sfr50']-agn781048['lgm50']),np.average(agn891048['sfr50']-agn891048['lgm50']),np.average(agn911048['sfr50']-agn911048['lgm50']),
np.average(agn781082['sfr50']-agn781082['lgm50']), np.average(agn891082['sfr50']-agn891082['lgm50']), np.average(agn911082['sfr50']-agn911082['lgm50']),
       np.average(agn891126['sfr50']-agn891126['lgm50']), np.average(agn911126['sfr50']-agn911126['lgm50'])   ])


print([np.average(sf561004['sfr50']-sf561004['lgm50']),np.average(sf671004['sfr50']-sf671004['lgm50']),np.average(sf781004['sfr50']-sf781004['lgm50'])
,np.average(sf891004['sfr50']-sf891004['lgm50']),np.average(sf911004['sfr50']-sf911004['lgm50']),
np.average(sf671048['sfr50']-sf671048['lgm50']),np.average(sf781048['sfr50']-sf781048['lgm50']),np.average(sf891048['sfr50']-sf891048['lgm50']),np.average(sf911048['sfr50']-sf911048['lgm50']),
np.average(sf781082['sfr50']-sf781082['lgm50']), np.average(sf891082['sfr50']-sf891082['lgm50']), np.average(sf911082['sfr50']-sf911082['lgm50']),
       np.average(sf891126['sfr50']-sf891126['lgm50']), np.average(sf911126['sfr50']-sf911126['lgm50'])   ])
"""
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

## g-r and Mass
plt.scatter(starformst['g']-starformst['r'],starformst['lgm50'],color='blue',s=1,label='STARFORMING',alpha=0.6)
plt.scatter(agnst['g']-agnst['r'],agnst['lgm50'],color='red',s=1,label='AGN')
plt.legend(fontsize=15)
plt.xlabel('g-r',fontsize=15)
plt.xlim(0.5,1)
plt.ylim(10,11.5)
plt.ylabel('logM/$M_{\odot}$',fontsize=15)
plt.show()
