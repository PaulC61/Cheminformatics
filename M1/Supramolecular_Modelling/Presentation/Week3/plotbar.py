#%%
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


lstRelevantColumns = [1,3,5,7,9,11]
lstRelevantColumnsStr = ['r', 'theta', 'phi', 'THETA', 'PHI', 'PSI']
lstLambdaDec = [0.0001, 0.001, 0.01, 0.1, 0.2, 0.5, 1.0]
lstLambdaStr = ['0_0001', '0_001', '0_01', '0_1', '0_2','0_5', '1_0']
lstg17 = [2.08982, 0.92826, 0.76986, 1.91439, 2.95518, 2.94152]
lstg19 = [0.498, 1.001, 1.349, 3.052, 3.983, 4.267]
lstg20 = [0.76729,0.89649,0.54264, 2.54291, 2.97685, 2.26410]


x = np.arange(len(lstRelevantColumnsStr))
fig, ax = plt.subplots()

singleRun = ax.bar(x - 0.25, lstg17, 0.25, label='Hexane')
doubleRun = ax.bar(x , lstg19, 0.25, label='Cyclohexane')
quadrun = ax.bar(x + 0.25, lstg20, 0.25, label='Benzene')

ax.set_ylabel("Free Energy (kcal/mol)")
ax.set_xticks(x)
ax.set_xticklabels(lstRelevantColumnsStr)
ax.legend()
fig.tight_layout()
