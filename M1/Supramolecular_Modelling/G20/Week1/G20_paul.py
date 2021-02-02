#%%
import numpy as np
from matplotlib import pyplot as plt
import math as math

bnddata = np.genfromtxt('rmsd-bnd.txt', delimiter=' ')
bnddata_vmd = np.loadtxt('bound-rmsd-vmd.txt', skiprows=1)

plt.scatter(bnddata[1:,0], bnddata[1:,1], marker='X', label='Plumed')
plt.scatter(bnddata_vmd[:,0],bnddata_vmd[:,1], marker='X', color='green', label='VMD')

plt.ylabel('RMSD')
plt.xlabel('Frame')
plt.legend()

#%%
plt.scatter(bnddata[1:,0], bnddata[1:,1]*10, marker='X', label='Plumed')
plt.scatter(bnddata_vmd[:,0],bnddata_vmd[:,1], marker='X', color='green', alpha=0.2, label='VMD')

plt.ylabel('RMSD')
plt.xlabel('Frame')
plt.legend()


#%%

bound_rmsd50 = bnddata[1:50,1]*10
bound_rmsd100 = bnddata[1:100,1]*10
bound_rmsd200 = bnddata[1:200,1]*10
bound_rmsd500 = bnddata[1:500,1]*10
bound_rmsd1000 = bnddata[1:1000,1]*10
bound_rmsd2000 = bnddata[1:2000,1]*10


#to produce density distributions you need to add 'density=True' in each histogram

bound_data1,bnd_bins1,_=plt.hist(bound_rmsd50, bins=100, edgecolor='black', histtype=u'step', label='n = 50')
bound_data2,bnd_bins2,_=plt.hist(bound_rmsd100, bins=100, edgecolor='blue', histtype=u'step', label='n = 100')
bound_data3,bnd_bins3,_=plt.hist(bound_rmsd200, bins=100, edgecolor='orange', histtype=u'step', label='n = 200')
bound_data4,bnd_bins4,_=plt.hist(bound_rmsd500, bins=100, edgecolor='green', histtype=u'step', label='n = 500')
bound_data5,bnd_bins5,_=plt.hist(bound_rmsd1000, bins=100, edgecolor='purple', histtype=u'step', label='n = 1000')
bound_data6,bnd_bins6,_=plt.hist(bound_rmsd2000, bins=100, edgecolor='red', histtype=u'step', label='n = 2000', linewidth=1.5)

plt.xlabel("Bound RMSD")
plt.ylabel("Frequency")
plt.legend()


#%%
import scipy.stats as stats

bound_density1=stats.gaussian_kde(bound_rmsd50)
bound_density2=stats.gaussian_kde(bound_rmsd100)
bound_density3=stats.gaussian_kde(bound_rmsd200)
bound_density4=stats.gaussian_kde(bound_rmsd500)
bound_density5=stats.gaussian_kde(bound_rmsd1000)
bound_density6=stats.gaussian_kde(bound_rmsd2000)



plt.plot(bnd_bins1, bound_density1(bnd_bins1), label='n = 50')
plt.plot(bnd_bins2, bound_density2(bnd_bins2), label='n = 100')
plt.plot(bnd_bins3, bound_density3(bnd_bins3), label='n = 200')
plt.plot(bnd_bins4, bound_density4(bnd_bins4), label='n = 500', color='brown')
plt.plot(bnd_bins5, bound_density5(bnd_bins5), label='n = 1000', color='purple')
plt.plot(bnd_bins6, bound_density6(bnd_bins6), label='n = 2000', color='red', linewidth='1.5')
plt.xlabel('Bound RMSD')
plt.ylabel('Density')
plt.legend()

# %%

unbdata = np.genfromtxt('rmsd-unb.txt', delimiter = ' ')

plt.scatter(unbdata[1:,0], unbdata[1:,1]*10, marker='X')

plt.ylabel('RMSD')
plt.xlabel('Frame')

bndMeanRMSD = round(np.mean(bnddata[1:,1]*10), 5)
unbMeanRMSD = round(np.mean(unbdata[1:,1]*10), 5)

print('Bound RMSD = '+ str(bndMeanRMSD) + ' A' + '/mol' + '/kcal')
print('Unbound RMSD = '+ str(unbMeanRMSD) + ' A' + '/mol' + '/kcal')

#%%
unbound_rmsd50 = unbdata[1:50,1]*10
unbound_rmsd100 = unbdata[1:100,1]*10
unbound_rmsd200 = unbdata[1:200,1]*10
unbound_rmsd400 = unbdata[1:400,1]*10

unbound_data1,unbnd_bins1,_=plt.hist(unbound_rmsd50, bins=100, edgecolor='black', histtype=u'step', label='n = 50')
unbound_data2,unbnd_bins2,_=plt.hist(unbound_rmsd100, bins=100, edgecolor='blue', histtype=u'step', label='n = 100')
unbound_data3,unbnd_bins3,_=plt.hist(unbound_rmsd200, bins=100, edgecolor='purple', histtype=u'step', label='n = 200')
unbound_data4,unbnd_bins4,_=plt.hist(unbound_rmsd400, bins=100, edgecolor='red', histtype=u'step', label='n = 400', linewidth=1.5)

plt.xlabel("Unbound RMSD")
plt.ylabel("Frequency")
plt.legend()

#%%

import scipy.stats as stats

unbound_density1=stats.gaussian_kde(unbound_rmsd50)
unbound_density2=stats.gaussian_kde(unbound_rmsd100)
unbound_density3=stats.gaussian_kde(unbound_rmsd200)
unbound_density4=stats.gaussian_kde(unbound_rmsd400)




plt.plot(unbnd_bins1, bound_density1(unbnd_bins1), label = 'n = 50')
plt.plot(unbnd_bins2, bound_density2(unbnd_bins2), label = 'n = 100')
plt.plot(unbnd_bins3, bound_density3(unbnd_bins3), label = 'n = 200')
plt.plot(unbnd_bins4, bound_density4(unbnd_bins4), label = 'n = 400', color = 'red', linewidth = 1.5)
plt.xlabel('Unbound RMSD')
plt.ylabel('Density')
plt.legend()



# %%


plt.hist(unbound_rmsd400, bins=100, edgecolor='blue', histtype=u'step', label = "Unbound")
plt.hist(bound_rmsd2000, bins=100, edgecolor='red', histtype=u'step', label = "Bound")



plt.xlabel("RMSD")
plt.ylabel("Frequency")
plt.legend()
# %%

plt.plot(bnd_bins6, bound_density6(bnd_bins6), label="Bound", color='red')
plt.plot(unbnd_bins4, bound_density6(unbnd_bins4), label="Unbound")

plt.xlabel('RMSD')
plt.ylabel('Density')
plt.legend()
# %%
