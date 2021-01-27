# -*- coding: utf-8 -*-
"""
Calcul de x*log(x) par la methode des trapezes 
"""

import math

'''
First step : Rempli dans un tableau toutes les valeurs
de de la fonction x*log(x) dans un intervale defini
Second step : Calcul la valeur de l'integral en utilisant la methode des trapezes
'''

def methodeTrapeze(nbVal, borneInf, borneSup):
    lst_f = []
    i = borneInf
    stp = (borneSup-borneInf)*(1/nbVal)
    while i <= borneSup:
        lst_f.append(i*math.log(i))
        i += stp
         
    A = 0
    h = borneInf
    
    for i in range(0,len(lst_f)-1):
        A += (lst_f[i+1]+lst_f[i])*(h+stp-h)*(1/2)
        h += stp
        
    return A

print(methodeTrapeze(100,1,2))

