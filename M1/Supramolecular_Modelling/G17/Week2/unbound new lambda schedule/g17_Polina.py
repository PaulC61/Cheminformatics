# %%
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats

def createAvgList(lstUrest, steps, listLbd):
    lst_avg = []
    comptSteps = 0
    for i in lstUrest:
        lst_avg.append(np.mean(i)/listLbd[comptSteps])
        comptSteps += 1
    return lst_avg

steps = 13
lstUrest_unb = []
lstUrest_bnd = []
listLbd = [0.2, 0.27, 0.34, 0.41, 0.48, 0.55, 0.62, 0.69, 0.76, 0.83, 0.9, 0.97, 1.0]
for i in range(steps):
    file = np.genfromtxt(str(listLbd[i]) + '.txt', delimiter=' ')
    lstUrest_unb.append(file[1:,2])
for i in range(steps):
    file = np.genfromtxt('bnd' + str(listLbd[i]) + '.txt', delimiter=' ')
    lstUrest_bnd.append(file[1:,2])
       
lst_avg_unb = createAvgList(lstUrest_unb, steps, listLbd)
lst_avg_bnd = createAvgList(lstUrest_bnd, steps, listLbd)

plt.figure()
plt.plot(listLbd, lst_avg_unb, 'xb-', label="unbound")
plt.plot(listLbd, lst_avg_bnd, 'xr-', label="bound")
plt.xlabel('Lambda')
plt.ylabel('Energy')
plt.legend()
plt.show()
# %%
