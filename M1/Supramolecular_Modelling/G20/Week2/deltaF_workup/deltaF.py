#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import math as math
# kf 110000

lambda0_0025 = np.genfromtxt('0.0025.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_005 = np.genfromtxt('0.005.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_0075 = np.genfromtxt('0.0075.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_01 = np.genfromtxt('0.01.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_1 = np.genfromtxt('0.1.rms', delimiter=' ', skip_header=0, autostrip=True) 
lambda0_15 = np.genfromtxt('0.15.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_2 = np.genfromtxt('0.2.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_3 = np.genfromtxt('0.3.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_4 = np.genfromtxt('0.4.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_5 = np.genfromtxt('0.5.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_6 = np.genfromtxt('0.6.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda0_7 = np.genfromtxt('0.7.rms', delimiter=' ', skip_header=0, autostrip=True)
lambda1_0 = np.genfromtxt('1.0.rms', delimiter=' ', skip_header=0, autostrip=True)

lstLbd = [0.0025, 0.005, 0.0075, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0]
lstUrest = [np.mean(lambda0_0025[:,2])/0.0025, np.mean(lambda0_005[:,2])/0.005, np.mean(lambda0_0075[:,2])/0.0075, np.mean(lambda0_1[:,2])/0.1, np.mean(lambda0_15[:,2])/0.15,np.mean(lambda0_2[:,2])/0.2,
            np.mean(lambda0_3[:,2])/0.3,np.mean(lambda0_4[:,2])/0.4,np.mean(lambda0_5[:,2])/0.5, np.mean(lambda0_6[:,2])/0.6, 
            np.mean(lambda0_7[:,2])/0.7, np.mean(lambda1_0[:,2])/1.0]

plt.plot(lstLbd, lstUrest)

plt.xlabel('\u03BB')
plt.ylabel('Urest')

print(lstUrest)


#%%
x = np.linspace(1,2,1000)
xlogx = []

for i in range(len(x)):
    xlogx.append(x[i]*(math.log(x[i])))

plt.plot(x, xlogx)
plt.xlabel('x')
plt.ylabel('x log (x)')

def trapzIntegration(x, y):
    sumArea = 0
    for i in range(1, len(x)):
        sumArea += 0.5*(y[i]+y[i-1])*(x[i]-x[i-1])
    return sumArea

print(trapzIntegration(x, xlogx))

# for deltaF

print(trapzIntegration(lstLbd,lstUrest))

# %%
