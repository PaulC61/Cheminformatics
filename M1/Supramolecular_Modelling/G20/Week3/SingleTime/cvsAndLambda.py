#%%
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


lstRelevantColumns = [1,3,5,7,9,11]
lstRelevantColumnsStr = ['r', 'theta', 'phi', 'THETA', 'PHI', 'PSI']
lstLambdaDec = [0.0001, 0.001, 0.01, 0.1, 0.2, 0.5, 1.0]
lstLambdaStr = ['0_0001', '0_001', '0_01', '0_1', '0_2','0_5', '1_0']
lstEnergySingle = [0.76390,0.94803,0.50167,2.37691,2.35083,2.36164]
lstEnergyDouble = [0.76729,0.89649,0.54264, 2.54291, 2.97685, 2.26410]
lstEnergyQuadruple = [0.78668,0.93311,0.53046,2.36074,2.82047,2.22528]


x = np.arange(len(lstRelevantColumnsStr))
fig, ax = plt.subplots()

singleRun = ax.bar(x - 0.25, lstEnergySingle, 0.25, label='Default Run Time')
doubleRun = ax.bar(x , lstEnergyDouble, 0.25, label='x2 Run Time')
quadrun = ax.bar(x + 0.25, lstEnergyQuadruple, 0.25, label='x4 Run Time')

ax.set_ylabel("Free Energy (kcal/mol)")
ax.set_xticks(x)
ax.set_xticklabels(lstRelevantColumnsStr)
ax.legend()
********
fig.tight_layout()

print("Default: " + str(round(sum(lstEnergySingle),2)))
print("Double: " + str(round(sum(lstEnergyDouble),2)))
print("Quadruple: " + str(round(sum(lstEnergyQuadruple),2)))


lambda0_0001 = np.genfromtxt('0.0001.vba', delimiter = ' ', autostrip=True)
lambda0_001 = np.genfromtxt('0.001.vba', delimiter = ' ', autostrip=True)
lambda0_01 = np.genfromtxt('0.01.vba', delimiter = ' ', autostrip=True)
lambda0_1 = np.genfromtxt('0.1.vba', delimiter = ' ', autostrip=True)
lambda0_2 = np.genfromtxt('0.2.vba', delimiter = ' ', autostrip=True)
lambda0_5 = np.genfromtxt('0.5.vba', delimiter = ' ', autostrip=True)
lambda1_0 = np.genfromtxt('1.0.vba', delimiter= ' ', autostrip=True)

#%%
# r values for each lambda
# hist
_,binsll0_0001r,_ = plt.hist(lambda0_0001[:,1], bins=100,histtype=u'step')
_,binsll0_001r,_ = plt.hist(lambda0_001[:,1], bins=100,histtype=u'step')
_,binsll0_01r,_ = plt.hist(lambda0_01[:,1], bins=100,histtype=u'step')
_,binsll0_1r,_ = plt.hist(lambda0_1[:,1], bins=100,histtype=u'step')
_,binsll0_2r,_ = plt.hist(lambda0_2[:,1], bins=100,histtype=u'step')
_,binsll0_5r,_ = plt.hist(lambda0_5[:,1], bins=100,histtype=u'step')
_,binsll1_0r,_ = plt.hist(lambda1_0[:,1], bins=100,histtype=u'step')

#%%
# probability distribution 
densityll0_0001r = stats.gaussian_kde(lambda0_0001[1:,1])
densityll0_001r = stats.gaussian_kde(lambda0_001[1:,1])
densityll0_01r = stats.gaussian_kde(lambda0_01[1:,1])
densityll0_1r = stats.gaussian_kde(lambda0_1[1:,1])
densityll0_2r = stats.gaussian_kde(lambda0_2[1:,1])
densityll0_5r = stats.gaussian_kde(lambda0_5[1:,1])
densityll1_0r = stats.gaussian_kde(lambda1_0[1:,1])

plt.plot(binsll0_0001r, densityll0_0001r(binsll0_0001r), label='\u03BB = 0.0001')
plt.plot(binsll0_001r, densityll0_001r(binsll0_001r), label='\u03BB = 0.001')
plt.plot(binsll0_01r, densityll0_01r(binsll0_01r), label='\u03BB = 0.01')
plt.plot(binsll0_1r, densityll0_1r(binsll0_1r), label='\u03BB = 0.1')
plt.plot(binsll0_2r, densityll0_2r(binsll0_2r), label='\u03BB = 0.2')
plt.plot(binsll0_5r, densityll0_5r(binsll0_5r), label='\u03BB = 0.5')
plt.plot(binsll1_0r, densityll1_0r(binsll1_0r), label='\u03BB = 1.0')

plt.ylabel('Probability Density')
plt.xlabel('r')
plt.legend()

#%%
# theta values for each lambda

# hist
_,binsll0_0001theta,_ = plt.hist(lambda0_0001[:,3], bins=100,histtype=u'step')
_,binsll0_001theta,_ = plt.hist(lambda0_001[:,3], bins=100,histtype=u'step')
_,binsll0_01theta,_ = plt.hist(lambda0_01[:,3], bins=100,histtype=u'step')
_,binsll0_1theta,_ = plt.hist(lambda0_1[:,3], bins=100,histtype=u'step')
_,binsll0_2theta,_ = plt.hist(lambda0_2[:,3], bins=100,histtype=u'step')
_,binsll0_5theta,_ = plt.hist(lambda0_5[:,3], bins=100,histtype=u'step')
_,binsll1_0theta,_ = plt.hist(lambda1_0[:,3], bins=100,histtype=u'step')

#%%
# probability distribution 
densityll0_0001theta = stats.gaussian_kde(lambda0_0001[1:,3])
densityll0_001theta = stats.gaussian_kde(lambda0_001[1:,3])
densityll0_01theta = stats.gaussian_kde(lambda0_01[1:,3])
densityll0_1theta = stats.gaussian_kde(lambda0_1[1:,3])
densityll0_2theta = stats.gaussian_kde(lambda0_2[1:,3])
densityll0_5theta = stats.gaussian_kde(lambda0_5[1:,3])
densityll1_0theta = stats.gaussian_kde(lambda1_0[1:,3])

plt.plot(binsll0_0001theta, densityll0_0001theta(binsll0_0001theta), label = '\u03BB = 0.0001')
plt.plot(binsll0_001theta, densityll0_001theta(binsll0_001theta), label = '\u03BB = 0.001')
plt.plot(binsll0_01theta, densityll0_01theta(binsll0_01theta), label = '\u03BB = 0.01')
plt.plot(binsll0_1theta, densityll0_1theta(binsll0_1theta), label = '\u03BB = 0.1')
plt.plot(binsll0_2theta, densityll0_2theta(binsll0_2theta), label = '\u03BB = 0.2')
plt.plot(binsll0_5theta, densityll0_5theta(binsll0_5theta), label = '\u03BB = 0.5')
plt.plot(binsll1_0theta, densityll1_0theta(binsll1_0theta), label = '\u03BB = 1.0')

plt.ylabel('Probability Density')
plt.xlabel('theta')
plt.legend()
# %%
# phi values for each lambda

# hist
_,binsll0_0001phi,_ = plt.hist(lambda0_0001[:,5], bins=100,histtype=u'step')
_,binsll0_001phi,_ = plt.hist(lambda0_001[:,5], bins=100,histtype=u'step')
_,binsll0_01phi,_ = plt.hist(lambda0_01[:,5], bins=100,histtype=u'step')
_,binsll0_1phi,_ = plt.hist(lambda0_1[:,5], bins=100,histtype=u'step')
_,binsll0_2phi,_ = plt.hist(lambda0_2[:,5], bins=100,histtype=u'step')
_,binsll0_5phi,_ = plt.hist(lambda0_5[:,5], bins=100,histtype=u'step')
_,binsll1_0phi,_ = plt.hist(lambda1_0[:,5], bins=100,histtype=u'step')

#%%
# probability distribution 
densityll0_0001phi = stats.gaussian_kde(lambda0_0001[1:,5])
densityll0_001phi = stats.gaussian_kde(lambda0_001[1:,5])
densityll0_01phi = stats.gaussian_kde(lambda0_01[1:,5])
densityll0_1phi = stats.gaussian_kde(lambda0_1[1:,5])
densityll0_2phi = stats.gaussian_kde(lambda0_2[1:,5])
densityll0_5phi = stats.gaussian_kde(lambda0_5[1:,5])
densityll1_0phi = stats.gaussian_kde(lambda1_0[1:,5])

plt.plot(binsll0_0001phi, densityll0_0001phi(binsll0_0001phi), label = '\u03BB = 0.0001')
plt.plot(binsll0_001phi, densityll0_001phi(binsll0_001phi),label = '\u03BB = 0.001')
plt.plot(binsll0_01phi, densityll0_01phi(binsll0_01phi), label = '\u03BB = 0.01')
plt.plot(binsll0_1phi, densityll0_1phi(binsll0_1phi), label = '\u03BB = 0.1')
plt.plot(binsll0_2phi, densityll0_2phi(binsll0_2phi), label = '\u03BB = 0.2')
plt.plot(binsll0_5phi, densityll0_5phi(binsll0_5phi), label = '\u03BB = 0.5')
plt.plot(binsll1_0phi, densityll1_0phi(binsll1_0phi), label = '\u03BB = 1.0')

plt.xlabel('phi')
plt.ylabel('Probability Density')
plt.legend()

#%%
# THETA values for each lambda

# hist
_,binsll0_0001THETA,_ = plt.hist(lambda0_0001[:,7], bins=100,histtype=u'step')
_,binsll0_001THETA,_ = plt.hist(lambda0_001[:,7], bins=100,histtype=u'step')
_,binsll0_01THETA,_ = plt.hist(lambda0_01[:,7], bins=100,histtype=u'step')
_,binsll0_1THETA,_ = plt.hist(lambda0_1[:,7], bins=100,histtype=u'step')
_,binsll0_2THETA,_ = plt.hist(lambda0_2[:,7], bins=100,histtype=u'step')
_,binsll0_5THETA,_ = plt.hist(lambda0_5[:,7], bins=100,histtype=u'step')
_,binsll1_0THETA,_ = plt.hist(lambda1_0[:,7], bins=100,histtype=u'step')
# probability distribution 

#%%
densityll0_0001THETA = stats.gaussian_kde(lambda0_0001[1:,7])
densityll0_001THETA = stats.gaussian_kde(lambda0_001[1:,7])
densityll0_01THETA = stats.gaussian_kde(lambda0_01[1:,7])
densityll0_1THETA = stats.gaussian_kde(lambda0_1[1:,7])
densityll0_2THETA = stats.gaussian_kde(lambda0_2[1:,7])
densityll0_5THETA = stats.gaussian_kde(lambda0_5[1:,7])
densityll1_0THETA = stats.gaussian_kde(lambda1_0[1:,7])

plt.plot(binsll0_0001THETA, densityll0_0001THETA(binsll0_0001THETA), label = '\u03BB = 0.0001')
plt.plot(binsll0_001THETA, densityll0_001THETA(binsll0_001THETA), label = '\u03BB = 0.001')
plt.plot(binsll0_01THETA, densityll0_01THETA(binsll0_01THETA), label = '\u03BB = 0.01')
plt.plot(binsll0_1THETA, densityll0_1THETA(binsll0_1THETA), label = '\u03BB = 0.1')
plt.plot(binsll0_2THETA, densityll0_2THETA(binsll0_2THETA), label = '\u03BB = 0.2')
plt.plot(binsll0_5THETA, densityll0_5THETA(binsll0_5THETA), label = '\u03BB = 0.5')
plt.plot(binsll1_0THETA, densityll1_0THETA(binsll1_0THETA), label = '\u03BB = 1.0')

plt.xlabel('THETA')
plt.ylabel('Probability Density')
plt.legend()

#%%
# PHI values for each lambda

# hist
_,binsll0_0001PHI,_ = plt.hist(lambda0_0001[:,9], bins=100,histtype=u'step')
_,binsll0_001PHI,_ = plt.hist(lambda0_001[:,9], bins=100,histtype=u'step')
_,binsll0_01PHI,_ = plt.hist(lambda0_01[:,9], bins=100,histtype=u'step')
_,binsll0_1PHI,_ = plt.hist(lambda0_1[:,9], bins=100,histtype=u'step')
_,binsll0_2PHI,_ = plt.hist(lambda0_2[:,9], bins=100,histtype=u'step')
_,binsll0_5PHI,_ = plt.hist(lambda0_5[:,9], bins=100,histtype=u'step')
_,binsll1_0PHI,_ = plt.hist(lambda1_0[:,9], bins=100,histtype=u'step')


#%%
# probability distribution 
densityll0_0001PHI = stats.gaussian_kde(lambda0_0001[1:,9])
densityll0_001PHI = stats.gaussian_kde(lambda0_001[1:,9])
densityll0_01PHI = stats.gaussian_kde(lambda0_01[1:,9])
densityll0_1PHI = stats.gaussian_kde(lambda0_1[1:,9])
densityll0_2PHI = stats.gaussian_kde(lambda0_2[1:,9])
densityll0_5PHI = stats.gaussian_kde(lambda0_5[1:,9])
densityll1_0PHI = stats.gaussian_kde(lambda1_0[1:,9])

plt.plot(binsll0_0001PHI, densityll0_0001PHI(binsll0_0001PHI), label = '\u03BB = 0.0001' )
plt.plot(binsll0_001PHI, densityll0_001PHI(binsll0_001PHI), label = '\u03BB = 0.001' )
plt.plot(binsll0_01PHI, densityll0_01PHI(binsll0_01PHI), label = '\u03BB = 0.01' )
plt.plot(binsll0_1PHI, densityll0_1PHI(binsll0_1PHI), label = '\u03BB = 0.1' )
plt.plot(binsll0_2PHI, densityll0_2PHI(binsll0_2PHI), label = '\u03BB = 0.2' )
plt.plot(binsll0_5PHI, densityll0_5PHI(binsll0_5PHI), label = '\u03BB = 0.5' )
plt.plot(binsll1_0PHI, densityll1_0PHI(binsll1_0PHI), label = '\u03BB = 1.0' )

plt.xlabel('PHI')
plt.ylabel('Probability Density')
plt.legend()

#%%
# PSI values for each lambda
# hist
_,binsll0_0001PSI,_ = plt.hist(lambda0_0001[:,11], bins=100,histtype=u'step')
_,binsll0_001PSI,_ = plt.hist(lambda0_001[:,11], bins=100,histtype=u'step')
_,binsll0_01PSI,_ = plt.hist(lambda0_01[:,11], bins=100,histtype=u'step')
_,binsll0_1PSI,_ = plt.hist(lambda0_1[:,11], bins=100,histtype=u'step')
_,binsll0_2PSI,_ = plt.hist(lambda0_2[:,11], bins=100,histtype=u'step')
_,binsll0_5PSI,_ = plt.hist(lambda0_5[:,11], bins=100,histtype=u'step')
_,binsll1_0PSI,_ = plt.hist(lambda1_0[:,11], bins=100,histtype=u'step')

# probability distribution 
#%%
densityll0_0001PSI = stats.gaussian_kde(lambda0_0001[1:,11])
densityll0_001PSI = stats.gaussian_kde(lambda0_001[1:,11])
densityll0_01PSI = stats.gaussian_kde(lambda0_01[1:,11])
densityll0_1PSI = stats.gaussian_kde(lambda0_1[1:,11])
densityll0_2PSI = stats.gaussian_kde(lambda0_2[1:,11])
densityll0_5PSI = stats.gaussian_kde(lambda0_5[1:,11])
densityll1_0PSI = stats.gaussian_kde(lambda1_0[1:,11])

plt.plot(binsll0_0001PSI, densityll0_0001PSI(binsll0_0001PSI),label = '\u03BB = 0.0001')
plt.plot(binsll0_001PSI, densityll0_001PSI(binsll0_001PSI),label = '\u03BB = 0.001')
plt.plot(binsll0_01PSI, densityll0_01PSI(binsll0_01PSI),label = '\u03BB = 0.01')
plt.plot(binsll0_1PSI, densityll0_1PSI(binsll0_1PSI),label = '\u03BB = 0.1')
plt.plot(binsll0_2PSI, densityll0_2PSI(binsll0_2PSI),label = '\u03BB = 0.2')
plt.plot(binsll0_5PSI, densityll0_5PSI(binsll0_5PSI),label = '\u03BB = 0.5')
plt.plot(binsll1_0PSI, densityll1_0PSI(binsll1_0PSI),label = '\u03BB = 1.0')

plt.xlabel('PSI')
plt.ylabel('Probability Density')
plt.legend()
# %%
