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
lstUrest = []
listLbd = [0.2, 0.27, 0.34, 0.41, 0.48, 0.55, 0.62, 0.69, 0.76, 0.83, 0.9, 0.97, 1.0]
for i in range(steps):
    file = np.genfromtxt(str(listLbd[i]) + '.txt', delimiter=' ')
    lstUrest.append(file[1:,2])
       
lst_avg = createAvgList(lstUrest, steps, listLbd)

plt.figure()
plt.plot(listLbd, lst_avg, 'xb-')
plt.xlabel('Lambda')
plt.ylabel('Energy')
plt.show()
# %%
