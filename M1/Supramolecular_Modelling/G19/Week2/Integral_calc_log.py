#%%
"""
Calcul de x*log(x) par la methode des trapezes 
"""

import math
import numpy as np

'''
First fonction : Rempli dans un tableau toutes les valeurs
de de la fonction x*log(x) dans un intervale defini
Second fonction : Calcul la valeur de l'integral en utilisant la methode des trapezes
'''

def lstValF(nbVal, borneInf, borneSup):
    stp = (borneSup-borneInf)*(1/nbVal) #Step, dx
    lst_f = []
    i = borneInf
    while i <= borneSup:
        lst_f.append(i*math.log(i))
        i += stp
    return lst_f

def methodeTrapeze(nbVal, borneInf, borneSup, lst_f):
    stp = (borneSup-borneInf)*(1/nbVal) #Step    
    A = 0
    
    for i in range(0,len(lst_f)-1):
        A += (lst_f[i+1]+lst_f[i])*(stp)*(1/2)
        
    return A

nbstep = 1000000
lst_f = lstValF(nbstep,1,2)

print(methodeTrapeze(nbstep,1,2, lst_f))
print(np.trapz(lst_f, dx = 1/nbstep))


# %%
