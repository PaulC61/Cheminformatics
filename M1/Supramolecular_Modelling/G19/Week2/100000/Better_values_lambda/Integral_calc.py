# -*- coding: utf-8 -*-
"""
Calcul de l'energie libre
"""

import math
import numpy as np




def methodeTrapeze(nbVal, borneInf, borneSup, lst_f):
    stp = (borneSup-borneInf)*(1/nbVal) #Step  
    A = 0
    h = borneInf
    
    for i in range(0,len(lst_f)-1):
        A += (lst_f[i+1]+lst_f[i])*(h+stp-h)*(1/2)
        h += stp
        
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

def createAvgList(lst, steps):
    lst_avg = []
    lbd = 1/steps
    for i in lst:
        lst_avg.append(avgList(i)/lbd)
        lbd += 1/steps

    return lst_avg
    

steps = 10
decimals = 1
lstUrest = []
lbd = round(1/steps,decimals)

for i in range(steps):
    file = np.genfromtxt(str(round(lbd,decimals))+'.txt', delimiter=' ')
    lstUrest.append(file[1:,2])
    lbd += round(1/steps,decimals)


lst_avg = createAvgList(lstUrest,10)


print(methodeTrapeze(steps,0,1,lst_avg))

