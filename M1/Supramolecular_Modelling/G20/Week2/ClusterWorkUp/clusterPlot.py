#%%
import numpy as np
import matplotlib.pyplot as plt

cutoffRMSD = [0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]
numberOfClusters = [200, 118, 43, 28, 20, 17, 17]

plt.scatter(cutoffRMSD, numberOfClusters, facecolors='none', edgecolors='r')
plt.xlabel('RMSD Cut-Off')
plt.ylabel('# of Clusters')
