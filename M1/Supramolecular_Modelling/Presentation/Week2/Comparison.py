# Urest plots for default lambda schedule

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

steps = 5
lstUrest_g17 = []
lstUrest_g19 = []
lstUrest_g20 = []
listLbd = [0.2, 0.4, 0.6, 0.8, 1.0]
for i in range(steps):
    file = np.genfromtxt('g17_' + str(listLbd[i]) + '.txt', delimiter=' ')
    lstUrest_g17.append(file[1:,2])

for i in range(steps):
    file = np.genfromtxt('g19_' + str(listLbd[i]) + '.txt', delimiter=' ')
    lstUrest_g19.append(file[1:,2])

for i in range(steps):
    file = np.genfromtxt('g20_' + str(listLbd[i]) + '.txt', delimiter=' ')
    lstUrest_g20.append(file[1:,2])
       
lst_avg_g17 = createAvgList(lstUrest_g17, steps, listLbd)
lst_avg_g19 = createAvgList(lstUrest_g19, steps, listLbd)
lst_avg_g20 = createAvgList(lstUrest_g20, steps, listLbd)

plt.figure()
plt.plot(listLbd, lst_avg_g17, 'xb-')
plt.plot(listLbd, lst_avg_g19, 'xr-')
plt.plot(listLbd, lst_avg_g17, 'xg-')
plt.xlabel('Lambda')
plt.ylabel('Energy')
plt.legend()
plt.show()
# %%
