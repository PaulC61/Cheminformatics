
#%%
import numpy as np

from matplotlib import pyplot as plt
from matplotlib import mlab as mlab

import scipy.stats as stats

bnddata = np.genfromtxt('rmsd-bnd.txt', delimiter=' ')

rmsd50 = bnddata[1:50,1]
rmsd100 = bnddata[1:100,1]
rmsd200 = bnddata[1:200,1]
rmsd500 = bnddata[1:500,1]
rmsd1000 = bnddata[1:1000,1]
rmsd2000 = bnddata[1:2000,1]


#to produce density distributions you need to add 'density=True' in each histogram
'''data1,bins,_=plt.hist(rmsd50, bins=100, edgecolor='black', histtype=u'step')
data2,bins,_=plt.hist(rmsd100, bins=100, edgecolor='blue', histtype=u'step')
data3,bins,_=plt.hist(rmsd200, bins=100, edgecolor='orange', histtype=u'step')
data4,bins,_=plt.hist(rmsd500, bins=100, edgecolor='green', histtype=u'step')
data5,bins,_=plt.hist(rmsd1000, bins=100, edgecolor='purple', histtype=u'step')'''
data6,bins,_=plt.hist(rmsd2000, bins=100, edgecolor='red', histtype=u'step',density=True)

density=stats.gaussian_kde(rmsd100)
density=stats.gaussian_kde(rmsd200)
density=stats.gaussian_kde(rmsd500)
density=stats.gaussian_kde(rmsd1000)
density=stats.gaussian_kde(rmsd2000)

plt.xlabel('rmsd')
plt.plot(bins, density(bins))
plt.show()

# %%
