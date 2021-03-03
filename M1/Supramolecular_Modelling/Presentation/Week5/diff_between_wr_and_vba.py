#%%
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


lstRelevantColumns = [1,3,5,7,9,11]
lstRelevantColumnsStr = ['Hexane', 'Cyclohexane', 'Benzene']
lstgWr = [11.82032, 12.30, 12.5]
lstVBA = [11.59903, 14.15, 9.66]
lstDiff = [0.22129, -1.85, 2.84]


x = np.arange(len(lstRelevantColumnsStr))
fig, ax = plt.subplots()

singleRun = ax.bar(x - 0.25, lstgWr, 0.25, label='W_r')
doubleRun = ax.bar(x , lstVBA, 0.25, label='Free energy VBA')
quadrun = ax.bar(x + 0.25, lstDiff, 0.25, label='Difference')

ax.set_ylabel("Contribution (kcal/mol)")
ax.set_xticks(x)
ax.set_xticklabels(lstRelevantColumnsStr)
ax.legend()
fig.tight_layout()