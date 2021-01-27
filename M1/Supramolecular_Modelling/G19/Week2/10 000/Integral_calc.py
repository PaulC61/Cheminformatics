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

def avgList(lst):
    somme = 0
    for i in lst:
        somme += i
    
    return somme/len(lst)


file02 = np.genfromtxt('0,2.txt', delimiter=' ')
file04 = np.genfromtxt('0,4.txt', delimiter=' ')
file06 = np.genfromtxt('0,6.txt', delimiter=' ')
file08 = np.genfromtxt('0,8.txt', delimiter=' ')
file10 = np.genfromtxt('1,0.txt', delimiter=' ')

Urest02 = file02[1:,2]
Urest04 = file04[1:,2]
Urest06 = file06[1:,2]
Urest08 = file06[1:,2]
Urest10 = file10[1:,2]


lst_avg = [avgList(Urest02),avgList(Urest04),avgList(Urest06),avgList(Urest08),avgList(Urest10)]


print(methodeTrapeze(5,0,1,lst_avg))

