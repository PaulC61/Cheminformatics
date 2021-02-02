#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# kf = 100,000 RMSD for ll

all_0_2 = np.genfromtxt('0_2.txt', delimiter=' ')
all_0_4 = np.genfromtxt('0_4.txt', delimiter=' ')
all_0_6 = np.genfromtxt('0_6.txt', delimiter=' ')
all_0_8 = np.genfromtxt('0_8.txt', delimiter=' ')
all_1_0 = np.genfromtxt('1_0.txt', delimiter=' ')

kf350000_RMSD_matrix = np.transpose(np.array([all_0_2[:,0],all_0_2[:,1], all_0_4[:,1], all_0_6[:,1], all_0_8[:,1], all_1_0[:,1]]))

_,extractBins0_2_org,_ = plt.hist(kf350000_RMSD_matrix[:,1], bins=100, histtype=u'step')
_,extractBins0_4_org,_ = plt.hist(kf350000_RMSD_matrix[:,2], bins=100, histtype=u'step')
_,extractBins0_6_org,_ = plt.hist(kf350000_RMSD_matrix[:,3], bins=100, histtype=u'step')
_,extractBins0_8_org,_ = plt.hist(kf350000_RMSD_matrix[:,4], bins=100, histtype=u'step')
_,extractBins1_0_org,_ = plt.hist(kf350000_RMSD_matrix[:,5], bins=100, histtype=u'step')



# %%
density_ll_0_2_kf_35 = stats.gaussian_kde(kf350000_RMSD_matrix[:,1])
density_ll_0_4_kf_35 = stats.gaussian_kde(kf350000_RMSD_matrix[:,2])
density_ll_0_6_kf_35 = stats.gaussian_kde(kf350000_RMSD_matrix[:,3])
density_ll_0_8_kf_35 = stats.gaussian_kde(kf350000_RMSD_matrix[:,4])
density_ll_1_0_kf_35 = stats.gaussian_kde(kf350000_RMSD_matrix[:,5])

plt.plot(extractBins0_2_org, density_ll_0_2_kf_35(extractBins0_2_org))
plt.plot(extractBins0_4_org, density_ll_0_4_kf_35(extractBins0_4_org))
plt.plot(extractBins0_6_org, density_ll_0_6_kf_35(extractBins0_6_org))
plt.plot(extractBins0_8_org, density_ll_0_8_kf_35(extractBins0_8_org))
plt.plot(extractBins1_0_org, density_ll_1_0_kf_35(extractBins1_0_org))

# %%
