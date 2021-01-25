
#%%
import numpy as np
import scipy.stats as stats

from matplotlib import pyplot as plt
from matplotlib import mlab as mlab




bnddata = np.genfromtxt('rmsd-bnd.txt', delimiter=' ')

rmsd50 = bnddata[1:50,1]
rmsd100 = bnddata[1:100,1]
rmsd200 = bnddata[1:200,1]
rmsd500 = bnddata[1:500,1]
rmsd1000 = bnddata[1:1000,1]
rmsd2000 = bnddata[1:2000,1]


#to produce density distributions you need to add 'density=True' in each histogram

data1,bins1,_=plt.hist(rmsd50, bins=100, edgecolor='black', histtype=u'step')
data2,bins2,_=plt.hist(rmsd100, bins=100, edgecolor='blue', histtype=u'step')
data3,bins3,_=plt.hist(rmsd200, bins=100, edgecolor='orange', histtype=u'step')
data4,bins4,_=plt.hist(rmsd500, bins=100, edgecolor='green', histtype=u'step')
data5,bins5,_=plt.hist(rmsd1000, bins=100, edgecolor='purple', histtype=u'step')
data6,bins6,_=plt.hist(rmsd2000, bins=100, edgecolor='red', histtype=u'step')



# %%

#%%


density1=stats.gaussian_kde(rmsd50)
density2=stats.gaussian_kde(rmsd100)
density3=stats.gaussian_kde(rmsd200)
density4=stats.gaussian_kde(rmsd500)
density5=stats.gaussian_kde(rmsd1000)
density6=stats.gaussian_kde(rmsd2000)


plt.xlabel('rmsd')
plt.plot(bins1, density1(bins1))
plt.plot(bins2, density2(bins2))
plt.plot(bins3, density3(bins3))
plt.plot(bins4, density4(bins4))
plt.plot(bins5, density5(bins5))
plt.plot(bins6, density6(bins6))
plt.show()
# %%

