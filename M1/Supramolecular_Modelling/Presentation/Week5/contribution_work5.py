#%%
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


lstRelevantColumns = [1,3,5,7,9,11]
lstRelevantColumnsStr = ['']
lstg17 = [-1.97329]
lstg19 = [-2.62]
lstg20 = [-3.034]


x = np.arange(len(lstRelevantColumnsStr))
fig, ax = plt.subplots()

singleRun = ax.bar(x - 0.25, lstg17, 0.25, label='Hexane')
doubleRun = ax.bar(x , lstg19, 0.25, label='Cyclohexane')
quadrun = ax.bar(x + 0.25, lstg20, 0.25, label='Benzene')

ax.set_ylabel("Symmetry contribution (kcal/mol)")
ax.set_xticks(x)
ax.set_xticklabels(lstRelevantColumnsStr)
ax.legend()
fig.tight_layout()