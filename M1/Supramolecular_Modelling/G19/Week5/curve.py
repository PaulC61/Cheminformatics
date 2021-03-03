# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:15:52 2021

@author: worldwidetorquedmicr
"""

import matplotlib.pyplot as plt

lst_k = [10, 100, 1000, 10000, 100000, 1000000]
lst_w_r = [3.43862, 7.52930, 11.61998, 15.71066, 19.80134, 23.89202]

plt.figure()
plt.plot(lst_w_r, lst_k, 'o')
plt.xlabel('W_r')
plt.ylabel('K')
plt.title("Variation of the work of the restraint by increasing the force constant")
plt.show()