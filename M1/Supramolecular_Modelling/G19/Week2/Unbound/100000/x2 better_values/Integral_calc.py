# -*- coding: utf-8 -*-
"""
Calcul de l'energie libre
"""

import numpy as np
import matplotlib.pyplot as plt

#---------------Functions---------------

def methodeTrapeze(nbVal, borneInf, borneSup, lst_f):
    stp = (borneSup-borneInf)*(1/nbVal) #Step  
    A = 0
    
    for i in range(0,len(lst_f)-1):
        A += (lst_f[i+1]+lst_f[i])*(stp)*(1/2)
        
    return A


def avg(lst):
    somme = 0
    for i in lst:
        somme += i
    
    return somme/len(lst)


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

steps = 9
lstUrest = []
listLbd = [0.001, 0.01, 0.1, 
           0.2, 0.3, 0.5, 0.7, 0.9, 1.0]

for i in range(steps):
    file = np.genfromtxt(str(listLbd[i])+'.rms', delimiter=' ')
    lstUrest.append(file[1:,2])


lst_avg = createAvgList(lstUrest,steps,listLbd)

plt.figure()
plt.plot(listLbd, lst_avg, 'o')
plt.xlabel('Lambda')
plt.ylabel('avg_Urest')
plt.show()

print("Np",np.trapz(lst_avg, listLbd))

#print("Trap",methodeTrapeze(steps, 0, 1, lst_avg))
