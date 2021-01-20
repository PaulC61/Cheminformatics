
#%%
import numpy as np

from matplotlib import pyplot as plt
from matplotlib import mlab as mlab

bnddata = np.genfromtxt('rmsd-bnd.txt', delimiter=' ')

rmsd50 = bnddata[1:50,1]
rmsd100 = bnddata[1:100,1]
rmsd200 = bnddata[1:200,1]
rmsd500 = bnddata[1:500,1]
rmsd1000 = bnddata[1:1000,1]
rmsd2000 = bnddata[1:2000,1]

plt.hist(rmsd50, bins=100, edgecolor='black', histtype=u'step')
plt.hist(rmsd100, bins=100, edgecolor='blue', histtype=u'step')
plt.hist(rmsd200, bins=100, edgecolor='orange', histtype=u'step')
plt.hist(rmsd500, bins=100, edgecolor='green', histtype=u'step')
plt.hist(rmsd1000, bins=100, edgecolor='purple', histtype=u'step')
plt.hist(rmsd2000, bins=100, edgecolor='red', histtype=u'step')


plt.xlabel('rmsd')

# %%
