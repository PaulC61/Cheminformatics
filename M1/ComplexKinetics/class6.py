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

plt.plot(t,y, label="ODE int")
plt.plot(t,(y0*np.exp(-k*t)), 'k--', label="Integrated")
plt.xlabel('time')
plt.ylabel('y(t)')
# %%
