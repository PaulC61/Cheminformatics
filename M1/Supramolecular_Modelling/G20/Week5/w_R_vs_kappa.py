
import matplotlib.pyplot as plt

kappa = [10, 100, 1000, 10000, 1000000]
w_R = [3.63266, 7.72334, 11.81402, 15.90470, 19.99538]
w_tot = [0.59831, 4.68899, 8.77967, 12.87035, 16.96103]

plt.figure()
plt.plot(kappa, w_R, label= r'$W_{rest}$', marker='o')
# plt.plot(kappa, w_tot, label=r'$W_{tot}$', marker='o')
plt.xlabel(r'$k_{f}$')
plt.ylabel('Energy (kcal/mol)')
plt.legend(loc='lower right')
plt.show()
