
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import curve_fit

# dCAdt = -k * CA

tspan = [0, 0.1, 0.2, 0.4, 0.8, 1]
Ca_data = [2.0081, 1.5512, 1.1903, 0.7160, 0.2562, 0.1495]
k = 2.6

# def dCAdt(Ca, t):
#     return - k * Ca

## Manual Fit Part ##
# plt.figure()
# plt.plot(tspan, Ca_data, 'o')
# plt.ylabel('[A]')
# plt.xlabel('time')
# Ctemp = odeint(dCAdt, Ca_data[0], np.linspace(0,1,1000))
# plt.plot(np.linspace(0,1,1000), Ctemp, label = "manual")
# plt.show()

#################################

def fitfunc(t, k):
    def dCAdt(Ca,t):
        return -k * Ca
    Ca0 = Ca_data[0]
    CaSol = odeint(dCAdt, Ca0, t)
    return CaSol[: , 0]

##################################
plt.figure()
k_fit, kcov = curve_fit(fitfunc, tspan, Ca_data, p0 = 2.6)

tfit = np.linspace(0,1)
fit = fitfunc(tfit, k_fit)

plt.plot(tfit, fit, 'b', label='fit')
plt.show()
