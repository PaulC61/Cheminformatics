#%%
import numpy as np

from matplotlib import pyplot as plt
from matplotlib import mlab as mlab



bnddata = np.genfromtxt('rmsd-bnd.txt', delimiter=' ')

bound_rmsd50 = bnddata[:50,1]
bound_rmsd100 = bnddata[:100,1]
bound_rmsd200 = bnddata[:200,1]
bound_rmsd500 = bnddata[:500,1]
bound_rmsd1000 = bnddata[:1000,1]
bound_rmsd2000 = bnddata[:2000,1]


#to produce density distributions you need to add 'density=True' in each histogram

bound_data1,bins1,_=plt.hist(bound_rmsd50, bins=100, edgecolor='black', histtype=u'step')
bound_data2,bins2,_=plt.hist(bound_rmsd100, bins=100, edgecolor='blue', histtype=u'step')
bound_data3,bins3,_=plt.hist(bound_rmsd200, bins=100, edgecolor='orange', histtype=u'step')
bound_data4,bins4,_=plt.hist(bound_rmsd500, bins=100, edgecolor='green', histtype=u'step')
bound_data5,bins5,_=plt.hist(bound_rmsd1000, bins=100, edgecolor='purple', histtype=u'step')
bound_data6,bins6,_=plt.hist(bound_rmsd2000, bins=100, edgecolor='red', histtype=u'step')

plt.xlabel("Bound RMSD")
plt.ylabel("Frequency")

# %%

#%%
import scipy.stats as stats

bound_density1=stats.gaussian_kde(bound_rmsd50)
bound_density2=stats.gaussian_kde(bound_rmsd100)
bound_density3=stats.gaussian_kde(bound_rmsd200)
bound_density4=stats.gaussian_kde(bound_rmsd500)
bound_density5=stats.gaussian_kde(bound_rmsd1000)
bound_density6=stats.gaussian_kde(bound_rmsd2000)



plt.plot(bins1, bound_density1(bins1))
plt.plot(bins2, bound_density2(bins2))
plt.plot(bins3, bound_density3(bins3))
plt.plot(bins4, bound_density4(bins4))
plt.plot(bins5, bound_density5(bins5))
plt.plot(bins6, bound_density6(bins6))
plt.xlabel('Bound RMSD')
plt.ylabel('Density')
plt.show()
# %%

unbdata = np.genfromtxt('rmsd-unb.txt', delimiter = ' ')

bound_rmsd50 = bnddata[1:50,1]
bound_rmsd100 = bnddata[1:100,1]
bound_rmsd200 = bnddata[1:200,1]
bound_rmsd500 = bnddata[1:500,1]
bound_rmsd1000 = bnddata[1:1000,1]
bound_rmsd2000 = bnddata[1:2000,1]
