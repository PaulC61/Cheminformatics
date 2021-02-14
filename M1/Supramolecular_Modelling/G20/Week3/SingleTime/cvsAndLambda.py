#%%
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


lstRelevantColumns = [1,3,5,7,9,11]
lstRelevantColumnsStr = ['r', 'theta', 'phi', 'THETA', 'PHI', 'PSI']
lstLambdaDec = [0.0001, 0.001, 0.01, 0.1, 0.2, 0.5, 1.0]
lstLambdaStr = ['0_0001', '0_001', '0_01', '0_1', '0_2','0_5', '1_0']



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

plt.plot(binsll0_0001r, densityll0_0001r(binsll0_0001r))
plt.plot(binsll0_001r, densityll0_001r(binsll0_001r))
plt.plot(binsll0_01r, densityll0_01r(binsll0_01r))
plt.plot(binsll0_1r, densityll0_1r(binsll0_1r))
plt.plot(binsll0_2r, densityll0_2r(binsll0_2r))
plt.plot(binsll0_5r, densityll0_5r(binsll0_5r))
plt.plot(binsll1_0r, densityll1_0r(binsll1_0r))

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
# probability distribution 

# %%
# phi values for each lambda

# hist

# probability distribution 


#%%
# THETA values for each lambda

# hist

# probability distribution 


#%%
# PHI values for each lambda

# hist

# probability distribution 


#%%
# PSI values for each lambda


# hist

# probability distribution 
