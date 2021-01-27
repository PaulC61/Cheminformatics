# -*- coding: utf-8 -*-
"""
Calcul de x*log(x) par la methode des trapezes 
"""

import math

'''
Fonction remplissannt dans un tableau toutes les valeurs
de l'integrale entre les deux bornes
'''

def methodeTrapeze(nbVal, borneInf, borneSup):
    lst_f = []
    i = borneInf
    while i <= borneSup:
        lst_f.append(i*math.log(i))
        i += (borneSup-borneInf)*(1/nbVal)
        
    A = 0
    h = borneInf
    for i in range(0,len(lst_f)-1):
        A += (lst_f[i+1]+lst_f[i])*(h+0.01-h)*(1/2)
        h += (borneSup-borneInf)*(1/nbVal)
        
    return A

print(methodeTrapeze(100,1,2))

