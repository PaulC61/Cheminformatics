
#%%
import numpy as np
import scipy.stats as stats

from matplotlib import pyplot as plt
from matplotlib import mlab as mlab




file02 = np.genfromtxt('0,2.txt', delimiter=' ')
file04 = np.genfromtxt('0,4.txt', delimiter=' ')
file06 = np.genfromtxt('0,6.txt', delimiter=' ')
file08 = np.genfromtxt('0,8.txt', delimiter=' ')
file10 = np.genfromtxt('1,0.txt', delimiter=' ')


Urest02 = file02[1:,2]
Urest04 = file04[1:,2]
Urest06 = file06[1:,2]
Urest08 = file08[1:,2]
Urest10 = file10[1:,2]



#to produce density distributions you need to add 'density=True' in each histogram

data1,bins1,_=plt.hist(Urest02, bins=100, edgecolor='black', histtype=u'step')
data2,bins2,_=plt.hist(Urest04, bins=100, edgecolor='blue', histtype=u'step')
data3,bins3,_=plt.hist(Urest06, bins=100, edgecolor='red', histtype=u'step')
data4,bins4,_=plt.hist(Urest08, bins=100, edgecolor='green', histtype=u'step')
data5,bins5,_=plt.hist(Urest10, bins=100, edgecolor='purple', histtype=u'step')



# %%

#%%


density1=stats.gaussian_kde(Urest02)
density2=stats.gaussian_kde(Urest04)
density3=stats.gaussian_kde(Urest06)
density4=stats.gaussian_kde(Urest08)
density5=stats.gaussian_kde(Urest10)

plt.xlabel('Urest')
plt.plot(bins1, density1(bins1))
plt.plot(bins2, density2(bins2))
plt.plot(bins3, density3(bins3))
plt.plot(bins4, density4(bins4))
plt.plot(bins5, density5(bins5))
plt.show()
# %%

