# -*- coding: utf-8 -*-
"""
Calcul de l'energie libre
"""

import math
import numpy as np
import matplotlib.pyplot as plt

#---------------Functions---------------

def methodeTrapeze(nbVal, borneInf, borneSup, lst_f):
    stp = (borneSup-borneInf)*(1/nbVal) #Step
    A = 0
    
    for i in range(0,len(lst_f)-1):
        A += (lst_f[i+1]+lst_f[i])*(stp)*(1/2)

    return A


def avgList(lst):
    somme = 0
    for i in lst:
        somme += i
    
    return somme/len(lst)


def createAvgList(lstUrest, steps, listLbd):
    lst_avg = []
    comptSteps = 0
    for i in lstUrest:
        lst_avg.append(avgList(i)/listLbd[comptSteps])
        comptSteps += 1
        

    return lst_avg

#---------------Core---------------

steps = 5
lstUrest = []
listLbd = [0.2, 0.4, 0.6, 0.8, 1.0]
for i in range(steps):
    file = np.genfromtxt(str(listLbd[i])+'.rms', delimiter=' ')
    lstUrest.append(file[1:,2])
       

lst_avg = createAvgList(lstUrest, steps, listLbd)

plt.figure()
plt.plot(listLbd, lst_avg, 'o')
plt.xlabel('Lambda')
plt.ylabel('avg_Urest')
plt.show()

err = np.std(lstUrest[0])/math.sqrt(20000) + np.std(lstUrest[1])/math.sqrt(20000) + np.std(lstUrest[2])/math.sqrt(20000) + np.std(lstUrest[3])/math.sqrt(20000) + np.std(lstUrest[4])/math.sqrt(20000)

print("std err",err)

print(methodeTrapeze(steps, 0, 1, lst_avg))
print(np.trapz(lst_avg, listLbd))

