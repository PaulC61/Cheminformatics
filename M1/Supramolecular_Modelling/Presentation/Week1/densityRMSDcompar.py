## comparison of each bound state RMSD for our group

#%%
import numpy as np
from matplotlib import pyplot as plt

g17_bnddata = np.genfromtxt('g17-rmsd-bnd.txt', delimiter=' ')
g19_bnddata = np.genfromtxt('g19-rmsd-bnd.txt', delimiter=' ')
g20_bnddata = np.genfromtxt('g20-rmsd-bnd.txt', delimiter=' ')

g17_rmsd = g17_bnddata[1:,1]
g19_rmsd = g19_bnddata[1:,1]
g20_rmsd = g20_bnddata[1:,1]


g17_data, g17_bins,_ = plt.hist(g17_rmsd, bins=100, edgecolor='blue',histtype=u'step')
g19_data, g19_bins,_ = plt.hist(g19_rmsd, bins=100, edgecolor='green',histtype=u'step')
g20_data, g20_bins,_ = plt.hist(g20_rmsd, bins=100, edgecolor='purple',histtype=u'step')

plt.xlabel('Bound RMSD')
plt.ylabel('Frequency')

# %%
import scipy.stats as stats

g17_density = stats.gaussian_kde(g17_rmsd)
g19_density = stats.gaussian_kde(g19_rmsd)
g20_density = stats.gaussian_kde(g20_rmsd)

plt.plot(g17_bins,g17_density(g17_bins), label='G-17: Hexane')
plt.plot(g19_bins,g19_density(g19_bins), label='G-19: Cyclohexane')
plt.plot(g20_bins,g20_density(g20_bins), label ='G-20: Benzene')

plt.xlabel('Bound RMSD')
plt.ylabel('Density')
plt.legend()
plt.ylim([0,250])
# %%
