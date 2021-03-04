# -*- coding: utf-8 -*-
"""
Calcul de l'energie libre
"""

import math
import numpy as np
import matplotlib.pyplot as plt

#---------------Functions---------------


def createAvgList(lstUrest, steps, listLbdn):
    lst_avg = []
    comptSteps = 0
    for i in lstUrest:
        lst_avg.append(np.mean(i)/listLbd[comptSteps])
        comptSteps += 1
        

    return lst_avg

#---------------Core---------------

steps = 7
lst_r = []
lst_thetamin = []
lst_phimin = []
lst_thetamaj = []
lst_phimaj = []
lst_psi = []

listLbd = [0.0001, 0.001, 0.01, 0.1, 0.2, 0.5, 1.0]
for i in range(steps):
    file = np.genfromtxt(str(listLbd[i])+'.vba', delimiter=' ')
    lst_r.append(file[7:,2])
    lst_thetamin.append(file[7:,4])
    lst_phimin.append(file[7:,6])
    lst_thetamaj.append(file[7:,8])
    lst_phimaj.append(file[7:,10])
    lst_psi.append(file[7:,12])
    
       

lst_avg_r = createAvgList(lst_r, steps, listLbd)
lst_avg_thetamin = createAvgList(lst_thetamin, steps, listLbd)
lst_avg_phimin = createAvgList(lst_phimin, steps, listLbd)
lst_avg_thetamaj = createAvgList(lst_thetamaj, steps, listLbd)
lst_avg_phimaj = createAvgList(lst_phimaj, steps, listLbd)
lst_avg_psi = createAvgList(lst_psi, steps, listLbd)

lst_1st = [1130.8265294269713, 400.1583099504421, 115.2096038993135, 15.680399123039162, 8.197040363950794, 3.268367579678458, 1.6725151559043727]
lst_2nd = [1025.5572445591538, 771.3821798226134, 110.07614565550652, 16.55102227681145, 8.993661773219772, 3.4454631386927694, 1.7214720589149548]
lst_3rd = [1000.2026062246267, 639.1688402643981, 110.57971564661001, 16.243948951387242, 8.679219351999599, 3.386953098529768, 1.7108170719111573]


contribR = np.trapz(lst_avg_r, listLbd)
print("Contribution r = ", contribR*0.2388, "KCal/mol")

contribThetaMin = np.trapz(lst_avg_thetamin, listLbd)
print("Contribution theta = ", contribThetaMin*0.2388, "KCal/mol")

contribPhiMin = np.trapz(lst_avg_phimin, listLbd)
print("Contribution phi = ", contribPhiMin*0.2388, "KCal/mol")

contribThetaMaj = np.trapz(lst_avg_thetamaj, listLbd)
print("Contribution THETA = ", contribThetaMaj*0.2388, "KCal/mol")

contribPhiMaj = np.trapz(lst_avg_phimaj, listLbd)
print("Contribution PHI = ", contribPhiMaj*0.2388, "KCal/mol")

contribPsi = np.trapz(lst_avg_psi, listLbd)
print("Contribution PSI = ", contribPsi*0.2388, "KCal/mol")

Total = contribR + contribThetaMin + contribPhiMin + contribThetaMaj + contribPhiMaj + contribPsi

print("Total free energy = ", Total*0.2388, "KCal/mol")



