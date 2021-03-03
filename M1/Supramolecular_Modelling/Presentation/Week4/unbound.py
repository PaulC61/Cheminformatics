#%%
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


lstRelevantColumns = [1,3,5,7,9,11]
lstRelevantColumnsStr = ['VdW', 'Coulomb', 'Total']
lstg17 = [9,686, 0,023, 9,709]
lstg19 = [11.657, 0.300, 11.957]
lstg20 = []


x = np.arange(len(lstRelevantColumnsStr))
fig, ax = plt.subplots()

singleRun = ax.bar(x - 0.25, lstg17, 0.25, label='Hexane')
doubleRun = ax.bar(x , lstg19, 0.25, label='Cyclohexane')
quadrun = ax.bar(x + 0.25, lstg20, 0.25, label='Benzene')

ax.set_ylabel("Contribution (kcal/mol)")
ax.set_xticks(x)
ax.set_xticklabels(lstRelevantColumnsStr)
ax.legend()
fig.tight_layout()