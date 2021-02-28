#%%
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

k1 = 1.8
k2 = 1
k3 = 1
k4 = 1
k5 = 1

def model(C, t):
    X = C[0]
    Y = C[1]
    Z = C[2]
    A = C[3]
    dXdt = X*(k1*A - k4) - k2*X*Y
    dYdt = -k3*Y + k5*Z
    dZdt = k4*X - k5*Z
    dAdt = 0
    Cout = [dXdt,dYdt,dZdt, dAdt]
    return Cout

C0 = [5,5,5,4]

t = np.linspace(0, 25, 5000)

Cint = odeint(model, C0, t)

# 2D
plt.figure()
plt.plot(t, Cint[:,0], 'b-', label=r'X')
plt.plot(t, Cint[:,1], 'r-', label=r'Y')
plt.plot(t, Cint[:,2], 'k--', label=r'Z')
plt.plot(t, Cint[:,3], 'g--', label=r'A')
plt.ylabel('conc.')
plt.xlabel('time')
plt.legend()
plt.show()

#3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Cint[:,0], Cint[:,1], Cint[:,2], c='r', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# %%
