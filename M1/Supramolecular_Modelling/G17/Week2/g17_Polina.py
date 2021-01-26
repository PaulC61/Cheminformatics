#%%
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats

rmsd_02_data = np.genfromtxt('0,2.txt', delimiter=' ')
rmsd_04_data = np.genfromtxt('0,4.txt', delimiter=' ')
rmsd_06_data = np.genfromtxt('0,6.txt', delimiter=' ')
rmsd_08_data = np.genfromtxt('0,8.txt', delimiter=' ')
rmsd_10_data = np.genfromtxt('1,0.txt', delimiter=' ')


rmsd_02 = rmsd_02_data[1:,2]
rmsd_04 = rmsd_04_data[1:,2]
rmsd_06 = rmsd_06_data[1:,2]
rmsd_08 = rmsd_08_data[1:,2]
rmsd_10 = rmsd_10_data[1:,2]

#average
avrg_02=np.mean(rmsd_02/0.2)
avrg_04=np.mean(rmsd_04/0.4)
avrg_06=np.mean(rmsd_06/0.6)
avrg_08=np.mean(rmsd_08/0.8)
avrg_10=np.mean(rmsd_10/1)

'''data_02,bins_02,_=plt.hist(rmsd_02, bins=100, edgecolor='black', histtype=u'step')
data_04,bins_04,_=plt.hist(rmsd_04, bins=100, edgecolor='blue', histtype=u'step')
data_06,bins_06,_=plt.hist(rmsd_06, bins=100, edgecolor='orange', histtype=u'step')
data_08,bins_08,_=plt.hist(rmsd_08, bins=100, edgecolor='green', histtype=u'step')
data_10,bins_10,_=plt.hist(rmsd_10, bins=100, edgecolor='green', histtype=u'step')'''

print(avrg_02,avrg_04,avrg_06,avrg_08,avrg_10)

plt.plot([0.2,0.4,0.6,0.8,1],[avrg_02,avrg_04,avrg_06,avrg_08,avrg_10], 'bs')
plt.ylabel('lambda')
plt.xlabel('U rest')

# %%
density_02=stats.gaussian_kde(rmsd_02)
density_04=stats.gaussian_kde(rmsd_04)
density_06=stats.gaussian_kde(rmsd_06)
density_08=stats.gaussian_kde(rmsd_08)
density_10=stats.gaussian_kde(rmsd_10)

'''plt.plot(bins_02, density_02(bins_02))'''
plt.plot(bins_04, density_04(bins_04))
plt.plot(bins_06, density_06(bins_06))
plt.plot(bins_08, density_08(bins_08))
plt.plot(bins_10, density_10(bins_10))
plt.xlabel('RMSD')
plt.ylabel('Density')
plt.show()
# %%
