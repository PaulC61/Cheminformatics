
#%%
import numpy as np

from matplotlib import pyplot as plt

bnddata = np.genfromtxt('rmsd-bnd.txt', delimiter=' ')

rmsd = bnddata[1:50,1]

plt.hist(rmsd, bins=100, edgecolor='black')

plt.xlabel('rmsd')


# %%
