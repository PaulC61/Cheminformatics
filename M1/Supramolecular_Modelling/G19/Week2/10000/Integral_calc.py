# -*- coding: utf-8 -*-
"""
Calcul de l'energie libre
"""

import math
import numpy as np

#---------------Functions---------------

def methodeTrapeze(nbVal, borneInf, borneSup, lst_f):
    stp = (borneSup-borneInf)*(1/nbVal) #Step  
    A = 0
    h = borneInf
    
    for i in range(0,len(lst_f)-1):
        A += (lst_f[i+1]+lst_f[i])*(h+stp-h)*(1/2)
        h += stp
        
    return A

def avgList(lst):
    somme = 0
    for i in lst:
        somme += i
    
    return somme/len(lst)


def createAvgList(lst, steps):
    lst_avg = []
    lbd = 1/steps
    for i in lst:
        lst_avg.append(avgList(i)/lbd)
        lbd += 1/steps

    return lst_avg

#---------------Core---------------

steps = 5
decimals = 2
lstUrest = []
lbd = round(1/steps,decimals)
for i in range(steps):
    file = np.genfromtxt(str(round(lbd,decimals))+'.rms', delimiter=' ')
    lstUrest.append(file[1:,2])
    lbd += round(1/steps,decimals)
    

lst_avg = createAvgList(lstUrest,5)

print(methodeTrapeze(5,0,1,lst_avg))

