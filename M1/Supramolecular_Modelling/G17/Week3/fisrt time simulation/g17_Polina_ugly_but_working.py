# %%
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats

# import data
data_0_0001 = np.genfromtxt('0.0001.txt', delimiter=' ')
data_0_001 = np.genfromtxt('0.001.txt', delimiter=' ')
data_0_01 = np.genfromtxt('0.01.txt', delimiter=' ')
data_0_1 = np.genfromtxt('0.1.txt', delimiter=' ')
data_0_2 = np.genfromtxt('0.2.txt', delimiter=' ')
data_0_5 = np.genfromtxt('0.5.txt', delimiter=' ')
data_1_0 = np.genfromtxt('1.0.txt', delimiter=' ')
# %%
# for r histo
lstUrest_r_0_0001 = data_0_0001[7:,2]
lstUrest_r_0_001 = data_0_001[7:,2]
lstUrest_r_0_01 = data_0_01[7:,2]
lstUrest_r_0_1 = data_0_1[7:,2]
lstUrest_r_0_2 = data_0_2[7:,2]
lstUrest_r_0_5 = data_0_5[7:,2]
lstUrest_r_1_0 = data_1_0[7:,2]

data_r_0_0001,bins_r_0_0001,_=plt.hist(lstUrest_r_0_0001, bins=100, edgecolor='yellow', histtype=u'step')
data_r_0_001,bins_r_0_001,_=plt.hist(lstUrest_r_0_001, bins=100, edgecolor='black', histtype=u'step')
data_r_0_01,bins_r_0_01,_=plt.hist(lstUrest_r_0_01, bins=100, edgecolor='blue', histtype=u'step')
data_r_0_1,bins_r_0_1,_=plt.hist(lstUrest_r_0_1, bins=100, edgecolor='orange', histtype=u'step')
data_r_0_2,bins_r_0_2,_=plt.hist(lstUrest_r_0_2, bins=100, edgecolor='green', histtype=u'step')
data_r_0_5,bins_r_0_5,_=plt.hist(lstUrest_r_0_5, bins=100, edgecolor='purple', histtype=u'step')
data_r_1_0,bins_r_1_0,_=plt.hist(lstUrest_r_1_0, bins=100, edgecolor='red', histtype=u'step')

# %%
# for r probability
density_r_0_0001=stats.gaussian_kde(lstUrest_r_0_0001)
density_r_0_001=stats.gaussian_kde(lstUrest_r_0_001)
density_r_0_01=stats.gaussian_kde(lstUrest_r_0_01)
density_r_0_1=stats.gaussian_kde(lstUrest_r_0_1)
density_r_0_2=stats.gaussian_kde(lstUrest_r_0_2)
density_r_0_5=stats.gaussian_kde(lstUrest_r_0_5)
density_r_1_0=stats.gaussian_kde(lstUrest_r_1_0)

plt.plot(bins_r_0_0001, density_r_0_0001(bins_r_0_0001))
plt.plot(bins_r_0_001, density_r_0_001(bins_r_0_001))
plt.plot(bins_r_0_01, density_r_0_01(bins_r_0_01))
plt.plot(bins_r_0_1, density_r_0_1(bins_r_0_1))
plt.plot(bins_r_0_2, density_r_0_2(bins_r_0_2))
plt.plot(bins_r_0_5, density_r_0_5(bins_r_0_5))
plt.plot(bins_r_1_0, density_r_1_0(bins_r_1_0))
plt.xlabel('r')
plt.ylabel('Density')
plt.show()

# %%
# for nu histo
lstUrest_nu_0_0001 = data_0_0001[7:,4]
lstUrest_nu_0_001 = data_0_001[7:,4]
lstUrest_nu_0_01 = data_0_01[7:,4]
lstUrest_nu_0_1 = data_0_1[7:,4]
lstUrest_nu_0_2 = data_0_2[7:,4]
lstUrest_nu_0_5 = data_0_5[7:,4]
lstUrest_nu_1_0 = data_1_0[7:,4]

data_nu_0_0001,bins_nu_0_0001,_=plt.hist(lstUrest_nu_0_0001, bins=100, edgecolor='yellow', histtype=u'step')
data_nu_0_001,bins_nu_0_001,_=plt.hist(lstUrest_nu_0_001, bins=100, edgecolor='black', histtype=u'step')
data_nu_0_01,bins_nu_0_01,_=plt.hist(lstUrest_nu_0_01, bins=100, edgecolor='blue', histtype=u'step')
data_nu_0_1,bins_nu_0_1,_=plt.hist(lstUrest_nu_0_1, bins=100, edgecolor='orange', histtype=u'step')
data_nu_0_2,bins_nu_0_2,_=plt.hist(lstUrest_nu_0_2, bins=100, edgecolor='green', histtype=u'step')
data_nu_0_5,bins_nu_0_5,_=plt.hist(lstUrest_nu_0_5, bins=100, edgecolor='purple', histtype=u'step')
data_nu_1_0,bins_nu_1_0,_=plt.hist(lstUrest_nu_1_0, bins=100, edgecolor='red', histtype=u'step')

# %%
# for nu probability
density_nu_0_0001=stats.gaussian_kde(lstUrest_nu_0_0001)
density_nu_0_001=stats.gaussian_kde(lstUrest_nu_0_001)
density_nu_0_01=stats.gaussian_kde(lstUrest_nu_0_01)
density_nu_0_1=stats.gaussian_kde(lstUrest_nu_0_1)
density_nu_0_2=stats.gaussian_kde(lstUrest_nu_0_2)
density_nu_0_5=stats.gaussian_kde(lstUrest_nu_0_5)
density_nu_1_0=stats.gaussian_kde(lstUrest_nu_1_0)

plt.plot(bins_r_0_0001, density_r_0_0001(bins_r_0_0001))
plt.plot(bins_r_0_001, density_r_0_001(bins_r_0_001))
plt.plot(bins_r_0_01, density_r_0_01(bins_r_0_01))
plt.plot(bins_r_0_1, density_r_0_1(bins_r_0_1))
plt.plot(bins_r_0_2, density_r_0_2(bins_r_0_2))
plt.plot(bins_r_0_5, density_r_0_5(bins_r_0_5))
plt.plot(bins_r_1_0, density_r_1_0(bins_r_1_0))
plt.xlabel('nu')
plt.ylabel('Density')
plt.show()

# %%
# for phi histo
lstUrest_phi_0_0001 = data_0_0001[7:,6]
lstUrest_phi_0_001 = data_0_001[7:,6]
lstUrest_phi_0_01 = data_0_01[7:,6]
lstUrest_phi_0_1 = data_0_1[7:,6]
lstUrest_phi_0_2 = data_0_2[7:,6]
lstUrest_phi_0_5 = data_0_5[7:,6]
lstUrest_phi_1_0 = data_1_0[7:,6]

data_phi_0_0001,bins_phi_0_0001,_=plt.hist(lstUrest_phi_0_0001, bins=100, edgecolor='yellow', histtype=u'step')
data_phi_0_001,bins_phi_0_001,_=plt.hist(lstUrest_phi_0_001, bins=100, edgecolor='black', histtype=u'step')
data_phi_0_01,bins_phi_0_01,_=plt.hist(lstUrest_phi_0_01, bins=100, edgecolor='blue', histtype=u'step')
data_phi_0_1,bins_phi_0_1,_=plt.hist(lstUrest_phi_0_1, bins=100, edgecolor='orange', histtype=u'step')
data_phi_0_2,bins_phi_0_2,_=plt.hist(lstUrest_phi_0_2, bins=100, edgecolor='green', histtype=u'step')
data_phi_0_5,bins_phi_0_5,_=plt.hist(lstUrest_phi_0_5, bins=100, edgecolor='purple', histtype=u'step')
data_phi_1_0,bins_phi_1_0,_=plt.hist(lstUrest_phi_1_0, bins=100, edgecolor='red', histtype=u'step')

# %%
# for phi probability
density_phi_0_0001=stats.gaussian_kde(lstUrest_phi_0_0001)
density_phi_0_001=stats.gaussian_kde(lstUrest_phi_0_001)
density_phi_0_01=stats.gaussian_kde(lstUrest_phi_0_01)
density_phi_0_1=stats.gaussian_kde(lstUrest_phi_0_1)
density_phi_0_2=stats.gaussian_kde(lstUrest_phi_0_2)
density_phi_0_5=stats.gaussian_kde(lstUrest_phi_0_5)
density_phi_1_0=stats.gaussian_kde(lstUrest_phi_1_0)

plt.plot(bins_phi_0_0001, density_r_0_0001(bins_phi_0_0001))
plt.plot(bins_phi_0_001, density_r_0_001(bins_phi_0_001))
plt.plot(bins_phi_0_01, density_r_0_01(bins_phi_0_01))
plt.plot(bins_phi_0_1, density_r_0_1(bins_phi_0_1))
plt.plot(bins_phi_0_2, density_r_0_2(bins_phi_0_2))
plt.plot(bins_phi_0_5, density_r_0_5(bins_phi_0_5))
plt.plot(bins_phi_1_0, density_r_1_0(bins_phi_1_0))
plt.xlabel('phi')
plt.ylabel('Density')
plt.show()

# %%
# for THETA histo
lstUrest_THETA_0_0001 = data_0_0001[7:,8]
lstUrest_THETA_0_001 = data_0_001[7:,8]
lstUrest_THETA_0_01 = data_0_01[7:,8]
lstUrest_THETA_0_1 = data_0_1[7:,8]
lstUrest_THETA_0_2 = data_0_2[7:,8]
lstUrest_THETA_0_5 = data_0_5[7:,8]
lstUrest_THETA_1_0 = data_1_0[7:,8]

data_THETA_0_0001,bins_phi_0_0001,_=plt.hist(lstUrest_THETA_0_0001, bins=100, edgecolor='yellow', histtype=u'step')
data_THETA_0_001,bins_phi_0_001,_=plt.hist(lstUrest_THETA_0_001, bins=100, edgecolor='black', histtype=u'step')
data_THETA_0_01,bins_phi_0_01,_=plt.hist(lstUrest_THETA_0_01, bins=100, edgecolor='blue', histtype=u'step')
data_THETA_0_1,bins_phi_0_1,_=plt.hist(lstUrest_THETA_0_1, bins=100, edgecolor='orange', histtype=u'step')
data_THETA_0_2,bins_phi_0_2,_=plt.hist(lstUrest_THETA_0_2, bins=100, edgecolor='green', histtype=u'step')
data_THETA_0_5,bins_phi_0_5,_=plt.hist(lstUrest_THETA_0_5, bins=100, edgecolor='purple', histtype=u'step')
data_THETA_1_0,bins_phi_1_0,_=plt.hist(lstUrest_THETA_1_0, bins=100, edgecolor='red', histtype=u'step')

# %%
# for THETA probability
density_THETA_0_0001=stats.gaussian_kde(lstUrest_THETA_0_0001)
density_THETA_0_001=stats.gaussian_kde(lstUrest_THETA_0_001)
density_THETA_0_01=stats.gaussian_kde(lstUrest_THETA_0_01)
density_THETA_0_1=stats.gaussian_kde(lstUrest_THETA_0_1)
density_THETA_0_2=stats.gaussian_kde(lstUrest_THETA_0_2)
density_THETA_0_5=stats.gaussian_kde(lstUrest_THETA_0_5)
density_THETA_1_0=stats.gaussian_kde(lstUrest_THETA_1_0)

plt.plot(bins_phi_0_0001, density_r_0_0001(bins_phi_0_0001))
plt.plot(bins_phi_0_001, density_r_0_001(bins_phi_0_001))
plt.plot(bins_phi_0_01, density_r_0_01(bins_phi_0_01))
plt.plot(bins_phi_0_1, density_r_0_1(bins_phi_0_1))
plt.plot(bins_phi_0_2, density_r_0_2(bins_phi_0_2))
plt.plot(bins_phi_0_5, density_r_0_5(bins_phi_0_5))
plt.plot(bins_phi_1_0, density_r_1_0(bins_phi_1_0))
plt.xlabel('THETA')
plt.ylabel('Density')
plt.show()

# %%
# for PHI histo
lstUrest_PHI_0_0001 = data_0_0001[7:,10]
lstUrest_PHI_0_001 = data_0_001[7:,10]
lstUrest_PHI_0_01 = data_0_01[7:,10]
lstUrest_PHI_0_1 = data_0_1[7:,10]
lstUrest_PHI_0_2 = data_0_2[7:,10]
lstUrest_PHI_0_5 = data_0_5[7:,10]
lstUrest_PHI_1_0 = data_1_0[7:,10]

data_PHI_0_0001,bins_PHI_0_0001,_=plt.hist(lstUrest_PHI_0_0001, bins=100, edgecolor='yellow', histtype=u'step')
data_PHI_0_001,bins_PHI_0_001,_=plt.hist(lstUrest_PHI_0_001, bins=100, edgecolor='black', histtype=u'step')
data_PHI_0_01,bins_PHI_0_01,_=plt.hist(lstUrest_PHI_0_01, bins=100, edgecolor='blue', histtype=u'step')
data_PHI_0_1,bins_PHI_0_1,_=plt.hist(lstUrest_PHI_0_1, bins=100, edgecolor='orange', histtype=u'step')
data_PHI_0_2,bins_PHI_0_2,_=plt.hist(lstUrest_PHI_0_2, bins=100, edgecolor='green', histtype=u'step')
data_PHI_0_5,bins_PHI_0_5,_=plt.hist(lstUrest_PHI_0_5, bins=100, edgecolor='purple', histtype=u'step')
data_PHI_1_0,bins_PHI_1_0,_=plt.hist(lstUrest_PHI_1_0, bins=100, edgecolor='red', histtype=u'step')

# %%
# for PHI probability
density_PHI_0_0001=stats.gaussian_kde(lstUrest_PHI_0_0001)
density_PHI_0_001=stats.gaussian_kde(lstUrest_PHI_0_001)
density_PHI_0_01=stats.gaussian_kde(lstUrest_PHI_0_01)
density_PHI_0_1=stats.gaussian_kde(lstUrest_PHI_0_1)
density_PHI_0_2=stats.gaussian_kde(lstUrest_PHI_0_2)
density_PHI_0_5=stats.gaussian_kde(lstUrest_PHI_0_5)
density_PHI_1_0=stats.gaussian_kde(lstUrest_PHI_1_0)

plt.plot(bins_PHI_0_0001, density_r_0_0001(bins_PHI_0_0001))
plt.plot(bins_PHI_0_001, density_r_0_001(bins_PHI_0_001))
plt.plot(bins_PHI_0_01, density_r_0_01(bins_PHI_0_01))
plt.plot(bins_PHI_0_1, density_r_0_1(bins_PHI_0_1))
plt.plot(bins_PHI_0_2, density_r_0_2(bins_PHI_0_2))
plt.plot(bins_PHI_0_5, density_r_0_5(bins_PHI_0_5))
plt.plot(bins_PHI_1_0, density_r_1_0(bins_PHI_1_0))
plt.xlabel('PHI')
plt.ylabel('Density')
plt.show()

# %%
# for PSI histo
lstUrest_PSI_0_0001 = data_0_0001[7:,12]
lstUrest_PSI_0_001 = data_0_001[7:,12]
lstUrest_PSI_0_01 = data_0_01[7:,12]
lstUrest_PSI_0_1 = data_0_1[7:,12]
lstUrest_PSI_0_2 = data_0_2[7:,12]
lstUrest_PSI_0_5 = data_0_5[7:,12]
lstUrest_PSI_1_0 = data_1_0[7:,12]

data_PSI_0_0001,bins_psi_0_0001,_=plt.hist(lstUrest_PSI_0_0001, bins=100, edgecolor='yellow', histtype=u'step')
data_PSI_0_001,bins_psi_0_001,_=plt.hist(lstUrest_PSI_0_001, bins=100, edgecolor='black', histtype=u'step')
data_PSI_0_01,bins_psi_0_01,_=plt.hist(lstUrest_PSI_0_01, bins=100, edgecolor='blue', histtype=u'step')
data_PSI_0_1,bins_psi_0_1,_=plt.hist(lstUrest_PSI_0_1, bins=100, edgecolor='orange', histtype=u'step')
data_PSI_0_2,bins_psi_0_2,_=plt.hist(lstUrest_PSI_0_2, bins=100, edgecolor='green', histtype=u'step')
data_PSI_0_5,bins_psi_0_5,_=plt.hist(lstUrest_PSI_0_5, bins=100, edgecolor='purple', histtype=u'step')
data_PSI_1_0,bins_psi_1_0,_=plt.hist(lstUrest_PSI_1_0, bins=100, edgecolor='red', histtype=u'step')

# %%
# for PSI probability
density_PSI_0_0001=stats.gaussian_kde(lstUrest_PSI_0_0001)
density_PSI_0_001=stats.gaussian_kde(lstUrest_PSI_0_001)
density_PSI_0_01=stats.gaussian_kde(lstUrest_PSI_0_01)
density_PSI_0_1=stats.gaussian_kde(lstUrest_PSI_0_1)
density_PSI_0_2=stats.gaussian_kde(lstUrest_PSI_0_2)
density_PSI_0_5=stats.gaussian_kde(lstUrest_PSI_0_5)
density_PSI_1_0=stats.gaussian_kde(lstUrest_PSI_1_0)

plt.plot(bins_phi_0_0001, density_r_0_0001(bins_phi_0_0001))
plt.plot(bins_phi_0_001, density_r_0_001(bins_phi_0_001))
plt.plot(bins_phi_0_01, density_r_0_01(bins_phi_0_01))
plt.plot(bins_phi_0_1, density_r_0_1(bins_phi_0_1))
plt.plot(bins_phi_0_2, density_r_0_2(bins_phi_0_2))
plt.plot(bins_phi_0_5, density_r_0_5(bins_phi_0_5))
plt.plot(bins_phi_1_0, density_r_1_0(bins_phi_1_0))
plt.xlabel('PSI')
plt.ylabel('Density')
plt.show()