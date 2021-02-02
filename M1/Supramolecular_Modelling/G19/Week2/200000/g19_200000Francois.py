
#%%
import numpy as np
import scipy.stats as stats

from matplotlib import pyplot as plt




steps = 5
lstUrest = []
listLbd = [0.2, 0.4, 0.6, 0.8, 1.0]

for i in range(steps):
    file = np.genfromtxt(str(listLbd[i])+'.rms', delimiter=' ')
    lstUrest.append(file[1:,2])



#to produce density distributions you need to add 'density=True' in each histogram

data1,bins1,_=plt.hist(lstUrest[0], bins=75, edgecolor='black', histtype='step', label='0.2')
data2,bins2,_=plt.hist(lstUrest[1], bins=75, edgecolor='blue', histtype='step', label='0.4')
data3,bins3,_=plt.hist(lstUrest[2], bins=75, edgecolor='red', histtype='step', label='0.6')
data4,bins4,_=plt.hist(lstUrest[3], bins=75, edgecolor='green', histtype='step', label='0.8')
data5,bins5,_=plt.hist(lstUrest[4], bins=75, edgecolor='purple', histtype='step', label='1.0')
plt.xlabel('Urest')
plt.legend()


# %%

#%%

density1=stats.gaussian_kde(lstUrest[0])
density2=stats.gaussian_kde(lstUrest[1])
density3=stats.gaussian_kde(lstUrest[2])
density4=stats.gaussian_kde(lstUrest[3])
density5=stats.gaussian_kde(lstUrest[4])

plt.plot(bins1, density1(bins1))
plt.plot(bins2, density2(bins2))
plt.plot(bins3, density3(bins3))
plt.plot(bins4, density4(bins4))
plt.plot(bins5, density5(bins5))
plt.show()
# %%

