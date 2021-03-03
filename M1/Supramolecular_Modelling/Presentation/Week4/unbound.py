#%%
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


lstRelevantColumns = [1,3,5,7,9,11]
lstRelevantColumnsStr = ['VdW', 'Coulomb', 'Total']
lstg17 = [-2.561, 0.016, -2.483]
lstg19 = [-2.336, -0.001,-2.336]
lstg20 = [-2.635, 1.798, -0.837]


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