#%%
from matplotlib.markers import MarkerStyle
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

averageRMSD = round(np.mean(bnddata[1:,1]), 5)

print(str(averageRMSD) + ' A ' + 'mol-1 ' + 'kcal-1')

#%%

bound_rmsd50 = bnddata[1:50,1]
bound_rmsd100 = bnddata[1:100,1]
bound_rmsd200 = bnddata[1:200,1]
bound_rmsd500 = bnddata[1:500,1]
bound_rmsd1000 = bnddata[1:1000,1]
bound_rmsd2000 = bnddata[1:2000,1]


#to produce density distributions you need to add 'density=True' in each histogram

bound_data1,bnd_bins1,_=plt.hist(bound_rmsd50, bins=100, edgecolor='black', histtype=u'step')
bound_data2,bnd_bins2,_=plt.hist(bound_rmsd100, bins=100, edgecolor='blue', histtype=u'step')
bound_data3,bnd_bins3,_=plt.hist(bound_rmsd200, bins=100, edgecolor='orange', histtype=u'step')
bound_data4,bnd_bins4,_=plt.hist(bound_rmsd500, bins=100, edgecolor='green', histtype=u'step')
bound_data5,bnd_bins5,_=plt.hist(bound_rmsd1000, bins=100, edgecolor='purple', histtype=u'step')
bound_data6,bnd_bins6,_=plt.hist(bound_rmsd2000, bins=100, edgecolor='red', histtype=u'step')

plt.xlabel("Bound RMSD")
plt.ylabel("Frequency")



#%%
import scipy.stats as stats

bound_density1=stats.gaussian_kde(bound_rmsd50)
bound_density2=stats.gaussian_kde(bound_rmsd100)
bound_density3=stats.gaussian_kde(bound_rmsd200)
bound_density4=stats.gaussian_kde(bound_rmsd500)
bound_density5=stats.gaussian_kde(bound_rmsd1000)
bound_density6=stats.gaussian_kde(bound_rmsd2000)



plt.plot(bnd_bins1, bound_density1(bnd_bins1))
plt.plot(bnd_bins2, bound_density2(bnd_bins2))
plt.plot(bnd_bins3, bound_density3(bnd_bins3))
plt.plot(bnd_bins4, bound_density4(bnd_bins4))
plt.plot(bnd_bins5, bound_density5(bnd_bins5))
plt.plot(bnd_bins6, bound_density6(bnd_bins6))
plt.xlabel('Bound RMSD')
plt.ylabel('Density')
plt.show()

# %%

unbdata = np.genfromtxt('rmsd-unb.txt', delimiter = ' ')

unbound_rmsd50 = unbdata[1:50,1]
unbound_rmsd100 = unbdata[1:100,1]
unbound_rmsd200 = unbdata[1:200,1]
unbound_rmsd500 = unbdata[1:500,1]
unbound_rmsd1000 = unbdata[1:1000,1]
unbound_rmsd2000 = unbdata[1:2000,1]

unbound_data1,unbnd_bins1,_=plt.hist(unbound_rmsd50, bins=100, edgecolor='black', histtype=u'step')
unbound_data2,unbnd_bins2,_=plt.hist(unbound_rmsd100, bins=100, edgecolor='blue', histtype=u'step')
unbound_data3,unbnd_bins3,_=plt.hist(unbound_rmsd200, bins=100, edgecolor='orange', histtype=u'step')
unbound_data4,unbnd_bins4,_=plt.hist(unbound_rmsd500, bins=100, edgecolor='green', histtype=u'step')
unbound_data5,unbnd_bins5,_=plt.hist(unbound_rmsd1000, bins=100, edgecolor='purple', histtype=u'step')
unbound_data6,unbnd_bins6,_=plt.hist(unbound_rmsd2000, bins=100, edgecolor='red', histtype=u'step')

plt.xlabel("Unbound RMSD")
plt.ylabel("Frequency")


#%%

import scipy.stats as stats

unbound_density1=stats.gaussian_kde(unbound_rmsd50)
unbound_density2=stats.gaussian_kde(unbound_rmsd100)
unbound_density3=stats.gaussian_kde(unbound_rmsd200)
unbound_density4=stats.gaussian_kde(unbound_rmsd500)
unbound_density5=stats.gaussian_kde(unbound_rmsd1000)
unbound_density6=stats.gaussian_kde(unbound_rmsd2000)



plt.plot(unbnd_bins1, bound_density1(unbnd_bins1))
plt.plot(unbnd_bins2, bound_density2(unbnd_bins2))
plt.plot(unbnd_bins3, bound_density3(unbnd_bins3))
plt.plot(unbnd_bins4, bound_density4(unbnd_bins4))
plt.plot(unbnd_bins5, bound_density5(unbnd_bins5))
plt.plot(unbnd_bins6, bound_density6(unbnd_bins6))
plt.xlabel('Bound RMSD')
plt.ylabel('Density')
plt.show()



# %%


plt.hist(unbound_rmsd2000, bins=100, edgecolor='blue', histtype=u'step')
plt.hist(bound_rmsd2000, bins=100, edgecolor='maroon', histtype=u'step')



plt.xlabel("RMSD")
plt.ylabel("Frequency")

# %%

plt.plot(bnd_bins6, bound_density6(bnd_bins6))
plt.plot(unbnd_bins6, bound_density6(unbnd_bins6))

plt.xlabel('RMSD')
plt.ylabel('Density')

# %%
