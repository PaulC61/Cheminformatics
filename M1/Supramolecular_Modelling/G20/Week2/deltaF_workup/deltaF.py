#%%
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import extract
import scipy.stats as stats
import math as math

# kf 110000

lambda0_0025 = np.genfromtxt('0.0025.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_005 = np.genfromtxt('0.005.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_0075 = np.genfromtxt('0.0075.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_01 = np.genfromtxt('0.01.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_1 = np.genfromtxt('0.1.rms', delimiter=' ', skip_header=0, autostrip=True) 
lambda0_15 = np.genfromtxt('0.15.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_2 = np.genfromtxt('0.2.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_3 = np.genfromtxt('0.3.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_4 = np.genfromtxt('0.4.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_5 = np.genfromtxt('0.5.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_6 = np.genfromtxt('0.6.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_7 = np.genfromtxt('0.7.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda1_0 = np.genfromtxt('1.0.rms', delimiter=' ', skip_header=0, autostrip=True)

lstLbd = [0.0025, 0.005, 0.0075, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0]
lstUrest = [np.mean(lambda0_0025[:,2])/0.0025, np.mean(lambda0_005[:,2])/0.005, np.mean(lambda0_0075[:,2])/0.0075, np.mean(lambda0_1[:,2])/0.1, np.mean(lambda0_15[:,2])/0.15,np.mean(lambda0_2[:,2])/0.2,
            np.mean(lambda0_3[:,2])/0.3,np.mean(lambda0_4[:,2])/0.4,np.mean(lambda0_5[:,2])/0.5, np.mean(lambda0_6[:,2])/0.6, 
            np.mean(lambda0_7[:,2])/0.7, np.mean(lambda1_0[:,2])/1.0]

plt.plot(lstLbd, lstUrest)
plt.xlim(0, 1)
plt.xlabel('\u03BB')
plt.ylabel('Urest/\u03BB (kJ/mol)')

print(lstUrest)


#%%
x = np.linspace(1,2,1000)
xlogx = []

for i in range(len(x)):
    xlogx.append(x[i]*(math.log(x[i])))

plt.plot(x, xlogx)
plt.xlabel('x')
plt.ylabel('x log (x)')

def trapzIntegration(x, y):
    sumArea = 0
    for i in range(1, len(x)):
        sumArea += 0.5*(y[i]+y[i-1])*(x[i]-x[i-1])
    return sumArea

print(trapzIntegration(x, xlogx))

# for deltaF

print(round(trapzIntegration(lstLbd,lstUrest)*0.239006,3))
print(round(np.trapz(lstUrest,lstLbd),3))
# %%

_,extrctBins0_0025,_ = plt.hist(lambda0_0025[:,1], bins=100, histtype=u'step')
_,extrctBins0_005,_ = plt.hist(lambda0_005[:,1], bins=100, histtype=u'step')
_,extrctBins0_0075,_ = plt.hist(lambda0_0075[:,1], bins=100, histtype=u'step')
_,extrctBins0_01,_ = plt.hist(lambda0_01[:,1], bins=100, histtype=u'step')
_,extrctBins0_1,_ = plt.hist(lambda0_1[:,1], bins=100, histtype=u'step')
_,extrctBins0_15,_ = plt.hist(lambda0_15[:,1], bins=100, histtype=u'step')
_,extrctBins0_2,_ = plt.hist(lambda0_2[:,1], bins=100, histtype=u'step')
_,extrctBins0_3,_ = plt.hist(lambda0_3[:,1], bins=100, histtype=u'step')
_,extrctBins0_4,_ = plt.hist(lambda0_4[:,1], bins=100, histtype=u'step')
_,extrctBins0_5,_ = plt.hist(lambda0_5[:,1], bins=100, histtype=u'step')
_,extrctBins0_6,_ = plt.hist(lambda0_6[:,1], bins=100, histtype=u'step')
_,extrctBins0_7,_ = plt.hist(lambda0_7[:,1], bins=100, histtype=u'step')
_,extrctBins1_0,_ = plt.hist(lambda1_0[:,1], bins=100, histtype=u'step')




#%%

dens0_0025 = stats.gaussian_kde(lambda0_0025[:,1])
dens0_005 = stats.gaussian_kde(lambda0_005[:,1])
dens0_0075 = stats.gaussian_kde(lambda0_0075[:,1])
dens0_01 = stats.gaussian_kde(lambda0_01[:,1])
dens0_1 =  stats.gaussian_kde(lambda0_1[:,1])
dens0_15 = stats.gaussian_kde(lambda0_15[:,1])
dens0_2 = stats.gaussian_kde(lambda0_2[:,1])
dens0_3 = stats.gaussian_kde(lambda0_3[:,1])
dens0_4 = stats.gaussian_kde(lambda0_4[:,1])
dens0_5 = stats.gaussian_kde(lambda0_5[:,1])
dens0_6 = stats.gaussian_kde(lambda0_6[:,1])
dens0_7 = stats.gaussian_kde(lambda0_7[:,1])
dens1_0 = stats.gaussian_kde(lambda1_0[:,1])


plt.plot(extrctBins0_0025, dens0_0025(extrctBins0_0025))
plt.plot(extrctBins0_005, dens0_005(extrctBins0_005))
plt.plot(extrctBins0_0075, dens0_0075(extrctBins0_0075))
plt.plot(extrctBins0_01, dens0_01(extrctBins0_01))
plt.plot(extrctBins0_1, dens0_1(extrctBins0_1))
plt.plot(extrctBins0_15, dens0_15(extrctBins0_15))
plt.plot(extrctBins0_2, dens0_2(extrctBins0_2))
plt.plot(extrctBins0_3, dens0_3(extrctBins0_3))
plt.plot(extrctBins0_4, dens0_4(extrctBins0_4))
plt.plot(extrctBins0_5, dens0_5(extrctBins0_5))
plt.plot(extrctBins0_6, dens0_6(extrctBins0_6))
plt.plot(extrctBins0_7, dens0_7(extrctBins0_7))
plt.plot(extrctBins1_0, dens1_0(extrctBins1_0))


plt.xlabel('RMSD')
plt.ylabel('Probability Density')
plt.ylim(bottom=0)

# %%
