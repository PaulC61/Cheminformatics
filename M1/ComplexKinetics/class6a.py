#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

global k
k= 0.1

def model(y,t):
    dydt = -k*y
    return dydt

y0 = 1

t = np.linspace(0, 20, 1000)

y = odeint(model, y0, t)

plt.figure()
plt.plot(t,y, label="ODE int")
plt.plot(t,(y0*np.exp(-k*t)), 'k--', label="Integrated")
plt.plot(np.log(2)/k, 0.5*y0, 'o', label="half-life")
plt.plot(1/k, y0/np.exp(1), 'o', label="life-time")
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
plt.show()
# %%
