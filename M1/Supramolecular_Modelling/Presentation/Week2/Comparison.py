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
plt.plot(listLbd, lst_avg_g17, 'xb-', label='G-17, Hexane')
plt.plot(listLbd, lst_avg_g19, 'xr-', label='G-19, Cyclohexane')
plt.plot(listLbd, lst_avg_g20, 'xg-', label='G-20, Benzene')
plt.xlabel('Lambda')
plt.ylabel('Energy')
plt.legend()
plt.show()
# %%
g17deltaF = np.trapz(lst_avg_g17, listLbd)*0.239006
g19deltaF = np.trapz(lst_avg_g19, listLbd)*0.239006
g20deltaF = np.trapz(lst_avg_g20, listLbd)*0.239006


print('G-17 \u0394F = ' + str(round(g17deltaF, 2)))
print('G-19 \u0394F = ' + str(round(g19deltaF, 2)))
print('G-20 \u0394F = ' + str(round(g20deltaF,3)))
# %%
