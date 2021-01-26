#%%
import numpy as np
from matplotlib import pyplot as plt

rmsd_02_data = np.genfromtxt('0,2.txt', delimiter=' ')
rmsd_04_data = np.genfromtxt('0,4.txt', delimiter=' ')
rmsd_06_data = np.genfromtxt('0,6.txt', delimiter=' ')
rmsd_08_data = np.genfromtxt('0,8.txt', delimiter=' ')

rmsd_02 = rmsd_02_data[1:,2]
rmsd_04 = rmsd_04_data[1:,2]
rmsd_06 = rmsd_06_data[1:,2]
rmsd_08 = rmsd_08_data[1:,2]

avrg_02=np.mean(rmsd_02/0.2)
avrg_04=np.mean(rmsd_02/0.4)
avrg_06=np.mean(rmsd_02/0.6)
avrg_08=np.mean(rmsd_02/0.8)

'''print(avrg_02,avrg_04,avrg_06,avrg_08)'''

plt.plot([0.2,0.4,0.6,0.8],[avrg_02,avrg_04,avrg_06,avrg_08], 'bs')
plt.ylabel('lambda')
plt.xlabel('U rest')

# %%
