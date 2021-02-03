#%%
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import angle, extract
import scipy.stats as stats
from mpl_toolkits.mplot3d import Axes3D

#%%

# plotting kf50000
data0_2_kf05 = np.genfromtxt('0_2_05.txt', delimiter = ' ')
data0_4_kf05 = np.genfromtxt('0_4_05.txt', delimiter = ' ')
data0_6_kf05 = np.genfromtxt('0_6_05.txt', delimiter = ' ')
data0_8_kf05 = np.genfromtxt('0_8_05.txt', delimiter = ' ')
data1_0_kf05 = np.genfromtxt('1_0_05.txt', delimiter = ' ')

kf50000_RMSD_matrix = np.transpose(np.array([data0_2_kf05[:,0], data0_2_kf05[:,1] ,data0_4_kf05[:,1], data0_6_kf05[:,1], data0_8_kf05[:,1], data1_0_kf05[:,1]]))

# frequency

_,extrctBins0_2_05,_ = plt.hist(kf50000_RMSD_matrix[:,1], bins=100, histtype=u'step')
_,extrctBins0_4_05,_ = plt.hist(kf50000_RMSD_matrix[:,2], bins=100, histtype=u'step')
_,extrctBins0_6_05,_ = plt.hist(kf50000_RMSD_matrix[:,3], bins=100, histtype=u'step')
_,extrctBins0_8_05,_ = plt.hist(kf50000_RMSD_matrix[:,4], bins=100, histtype=u'step')
_,extrctBins1_0_05,_ = plt.hist(kf50000_RMSD_matrix[:,5], bins=100, histtype=u'step')

dens0_2_05 = stats.gaussian_kde(kf50000_RMSD_matrix[:,1])
dens0_4_05 = stats.gaussian_kde(kf50000_RMSD_matrix[:,2])
dens0_6_05 = stats.gaussian_kde(kf50000_RMSD_matrix[:,3])
dens0_8_05 = stats.gaussian_kde(kf50000_RMSD_matrix[:,4])
dens1_0_05 = stats.gaussian_kde(kf50000_RMSD_matrix[:,5])


#%%

# density
plt.plot(extrctBins0_2_05, dens0_2_05(extrctBins0_2_05))
plt.plot(extrctBins0_4_05, dens0_4_05(extrctBins0_4_05))
plt.plot(extrctBins0_6_05, dens0_6_05(extrctBins0_6_05))
plt.plot(extrctBins0_8_05, dens0_8_05(extrctBins0_8_05))
plt.plot(extrctBins1_0_05, dens1_0_05(extrctBins1_0_05))


#%%

# plotting kf100000
data0_2_kf10 = np.genfromtxt('0_2_10.txt', delimiter = ' ')
data0_4_kf10 = np.genfromtxt('0_4_10.txt', delimiter = ' ')
data0_6_kf10 = np.genfromtxt('0_6_10.txt', delimiter = ' ')
data0_8_kf10 = np.genfromtxt('0_8_10.txt', delimiter = ' ')
data1_0_kf10 = np.genfromtxt('1_0_10.txt', delimiter = ' ')

kf100000_RMSD_matrix = np.transpose(np.array([data0_2_kf10[:,0], data0_2_kf10[:,1] ,data0_4_kf10[:,1], data0_6_kf10[:,1], data0_8_kf10[:,1], data1_0_kf10[:,1]]))

# frequency

_,extrctBins0_2_10,_ = plt.hist(kf100000_RMSD_matrix[:,1], bins=100, histtype=u'step')
_,extrctBins0_4_10,_ = plt.hist(kf100000_RMSD_matrix[:,2], bins=100, histtype=u'step')
_,extrctBins0_6_10,_ = plt.hist(kf100000_RMSD_matrix[:,3], bins=100, histtype=u'step')
_,extrctBins0_8_10,_ = plt.hist(kf100000_RMSD_matrix[:,4], bins=100, histtype=u'step')
_,extrctBins1_0_10,_ = plt.hist(kf100000_RMSD_matrix[:,5], bins=100, histtype=u'step')

dens0_2_10 = stats.gaussian_kde(kf100000_RMSD_matrix[:,1])
dens0_4_10 = stats.gaussian_kde(kf100000_RMSD_matrix[:,2])
dens0_6_10 = stats.gaussian_kde(kf100000_RMSD_matrix[:,3])
dens0_8_10 = stats.gaussian_kde(kf100000_RMSD_matrix[:,4])
dens1_0_10 = stats.gaussian_kde(kf100000_RMSD_matrix[:,5])


#%%

# density
plt.plot(extrctBins0_2_10, dens0_2_10(extrctBins0_2_10))
plt.plot(extrctBins0_4_10, dens0_4_10(extrctBins0_4_10))
plt.plot(extrctBins0_6_10, dens0_6_10(extrctBins0_6_10))
plt.plot(extrctBins0_8_10, dens0_8_10(extrctBins0_8_10))
plt.plot(extrctBins1_0_10, dens1_0_10(extrctBins1_0_10))


#%%

# plotting kf150000
data0_2_kf15 = np.genfromtxt('0_2_15.txt', delimiter = ' ')
data0_4_kf15 = np.genfromtxt('0_4_15.txt', delimiter = ' ')
data0_6_kf15 = np.genfromtxt('0_6_15.txt', delimiter = ' ')
data0_8_kf15 = np.genfromtxt('0_8_15.txt', delimiter = ' ')
data1_0_kf15 = np.genfromtxt('1_0_15.txt', delimiter = ' ')

kf150000_RMSD_matrix = np.transpose(np.array([data0_2_kf15[:,0], data0_2_kf15[:,1] ,data0_4_kf15[:,1], data0_6_kf15[:,1], data0_8_kf15[:,1], data1_0_kf15[:,1]]))

# frequency

_,extrctBins0_2_15,_ = plt.hist(kf150000_RMSD_matrix[:,1], bins=100, histtype=u'step')
_,extrctBins0_4_15,_ = plt.hist(kf150000_RMSD_matrix[:,2], bins=100, histtype=u'step')
_,extrctBins0_6_15,_ = plt.hist(kf150000_RMSD_matrix[:,3], bins=100, histtype=u'step')
_,extrctBins0_8_15,_ = plt.hist(kf150000_RMSD_matrix[:,4], bins=100, histtype=u'step')
_,extrctBins1_0_15,_ = plt.hist(kf150000_RMSD_matrix[:,5], bins=100, histtype=u'step')

dens0_2_15 = stats.gaussian_kde(kf150000_RMSD_matrix[:,1])
dens0_4_15 = stats.gaussian_kde(kf150000_RMSD_matrix[:,2])
dens0_6_15 = stats.gaussian_kde(kf150000_RMSD_matrix[:,3])
dens0_8_15 = stats.gaussian_kde(kf150000_RMSD_matrix[:,4])
dens1_0_15 = stats.gaussian_kde(kf150000_RMSD_matrix[:,5])


#%%

# density
plt.plot(extrctBins0_2_15, dens0_2_15(extrctBins0_2_15))
plt.plot(extrctBins0_4_15, dens0_4_15(extrctBins0_4_15))
plt.plot(extrctBins0_6_15, dens0_6_15(extrctBins0_6_15))
plt.plot(extrctBins0_8_15, dens0_8_15(extrctBins0_8_15))
plt.plot(extrctBins1_0_15, dens1_0_15(extrctBins1_0_15))

#%%

# plotting kf200000
data0_2_kf20 = np.genfromtxt('0_2_20.txt', delimiter = ' ')
data0_4_kf20 = np.genfromtxt('0_4_20.txt', delimiter = ' ')
data0_6_kf20 = np.genfromtxt('0_6_20.txt', delimiter = ' ')
data0_8_kf20 = np.genfromtxt('0_8_20.txt', delimiter = ' ')
data1_0_kf20 = np.genfromtxt('1_0_20.txt', delimiter = ' ')

kf50000_RMSD_matrix = np.transpose(np.array([data0_2_kf05[:,0], data0_2_kf05[:,1] ,data0_4_kf05[:,1], data0_6_kf05[:,1], data0_8_kf05[:,1], data1_0_kf05[:,1]]))

# frequency

_,extrctBins0_2_20,_ = plt.hist(kf50000_RMSD_matrix[:,1], bins=100, histtype=u'step')
_,extrctBins0_4_20,_ = plt.hist(kf50000_RMSD_matrix[:,2], bins=100, histtype=u'step')
_,extrctBins0_6_20,_ = plt.hist(kf50000_RMSD_matrix[:,3], bins=100, histtype=u'step')
_,extrctBins0_8_20,_ = plt.hist(kf50000_RMSD_matrix[:,4], bins=100, histtype=u'step')
_,extrctBins1_0_20,_ = plt.hist(kf50000_RMSD_matrix[:,5], bins=100, histtype=u'step')

dens0_2_20 = stats.gaussian_kde(kf50000_RMSD_matrix[:,1])
dens0_4_20 = stats.gaussian_kde(kf50000_RMSD_matrix[:,2])
dens0_6_20 = stats.gaussian_kde(kf50000_RMSD_matrix[:,3])
dens0_8_20 = stats.gaussian_kde(kf50000_RMSD_matrix[:,4])
dens1_0_20 = stats.gaussian_kde(kf50000_RMSD_matrix[:,5])


#%%

# density
plt.plot(extrctBins0_2_20, dens0_2_20(extrctBins0_2_20))
plt.plot(extrctBins0_4_20, dens0_4_20(extrctBins0_4_20))
plt.plot(extrctBins0_6_20, dens0_6_20(extrctBins0_6_20))
plt.plot(extrctBins0_8_20, dens0_8_20(extrctBins0_8_20))
plt.plot(extrctBins1_0_20, dens1_0_20(extrctBins1_0_20))

#%%

# plotting kf250000
data0_2_kf25 = np.genfromtxt('0_2_25.txt', delimiter = ' ')
data0_4_kf25 = np.genfromtxt('0_4_25.txt', delimiter = ' ')
data0_6_kf25 = np.genfromtxt('0_6_25.txt', delimiter = ' ')
data0_8_kf25 = np.genfromtxt('0_8_25.txt', delimiter = ' ')
data1_0_kf25 = np.genfromtxt('1_0_25.txt', delimiter = ' ')

kf250000_RMSD_matrix = np.transpose(np.array([data0_2_kf25[:,0], data0_2_kf25[:,1] ,data0_4_kf25[:,1], data0_6_kf25[:,1], data0_8_kf25[:,1], data1_0_kf25[:,1]]))

# frequency

_,extrctBins0_2_25,_ = plt.hist(kf250000_RMSD_matrix[:,1], bins=100, histtype=u'step')
_,extrctBins0_4_25,_ = plt.hist(kf250000_RMSD_matrix[:,2], bins=100, histtype=u'step')
_,extrctBins0_6_25,_ = plt.hist(kf250000_RMSD_matrix[:,3], bins=100, histtype=u'step')
_,extrctBins0_8_25,_ = plt.hist(kf250000_RMSD_matrix[:,4], bins=100, histtype=u'step')
_,extrctBins1_0_25,_ = plt.hist(kf250000_RMSD_matrix[:,5], bins=100, histtype=u'step')

dens0_2_25 = stats.gaussian_kde(kf250000_RMSD_matrix[:,1])
dens0_4_25 = stats.gaussian_kde(kf250000_RMSD_matrix[:,2])
dens0_6_25 = stats.gaussian_kde(kf250000_RMSD_matrix[:,3])
dens0_8_25 = stats.gaussian_kde(kf250000_RMSD_matrix[:,4])
dens1_0_25 = stats.gaussian_kde(kf250000_RMSD_matrix[:,5])


#%%

# density
plt.plot(extrctBins0_2_25, dens0_2_25(extrctBins0_2_25))
plt.plot(extrctBins0_4_25, dens0_4_25(extrctBins0_4_25))
plt.plot(extrctBins0_6_25, dens0_6_25(extrctBins0_6_25))
plt.plot(extrctBins0_8_25, dens0_8_25(extrctBins0_8_25))
plt.plot(extrctBins1_0_25, dens1_0_25(extrctBins1_0_25))


#%%

# plotting kf300000
data0_2_kf30 = np.genfromtxt('0_2_30.txt', delimiter = ' ')
data0_4_kf30 = np.genfromtxt('0_4_30.txt', delimiter = ' ')
data0_6_kf30 = np.genfromtxt('0_6_30.txt', delimiter = ' ')
data0_8_kf30 = np.genfromtxt('0_8_30.txt', delimiter = ' ')
data1_0_kf30 = np.genfromtxt('1_0_30.txt', delimiter = ' ')

kf300000_RMSD_matrix = np.transpose(np.array([data0_2_kf30[:,0], data0_2_kf30[:,1] ,data0_4_kf30[:,1], data0_6_kf30[:,1], data0_8_kf30[:,1], data1_0_kf30[:,1]]))

# frequency

_,extrctBins0_2_30,_ = plt.hist(kf300000_RMSD_matrix[:,1], bins=100, histtype=u'step')
_,extrctBins0_4_30,_ = plt.hist(kf300000_RMSD_matrix[:,2], bins=100, histtype=u'step')
_,extrctBins0_6_30,_ = plt.hist(kf300000_RMSD_matrix[:,3], bins=100, histtype=u'step')
_,extrctBins0_8_30,_ = plt.hist(kf300000_RMSD_matrix[:,4], bins=100, histtype=u'step')
_,extrctBins1_0_30,_ = plt.hist(kf300000_RMSD_matrix[:,5], bins=100, histtype=u'step')

dens0_2_30 = stats.gaussian_kde(kf300000_RMSD_matrix[:,1])
dens0_4_30 = stats.gaussian_kde(kf300000_RMSD_matrix[:,2])
dens0_6_30 = stats.gaussian_kde(kf300000_RMSD_matrix[:,3])
dens0_8_30 = stats.gaussian_kde(kf300000_RMSD_matrix[:,4])
dens1_0_30 = stats.gaussian_kde(kf300000_RMSD_matrix[:,5])


#%%

# density
plt.plot(extrctBins0_2_30, dens0_2_30(extrctBins0_2_30))
plt.plot(extrctBins0_4_30, dens0_4_30(extrctBins0_4_30))
plt.plot(extrctBins0_6_30, dens0_6_30(extrctBins0_6_30))
plt.plot(extrctBins0_8_30, dens0_8_30(extrctBins0_8_30))
plt.plot(extrctBins1_0_30, dens1_0_30(extrctBins1_0_30))

#%%

# plotting kf350000
data0_2_kf35 = np.genfromtxt('0_2_35.txt', delimiter = ' ')
data0_4_kf35 = np.genfromtxt('0_4_35.txt', delimiter = ' ')
data0_6_kf35 = np.genfromtxt('0_6_35.txt', delimiter = ' ')
data0_8_kf35 = np.genfromtxt('0_8_35.txt', delimiter = ' ')
data1_0_kf35 = np.genfromtxt('1_0_35.txt', delimiter = ' ')

kf350000_RMSD_matrix = np.transpose(np.array([data0_2_kf35[:,0], data0_2_kf35[:,1] ,data0_4_kf35[:,1], data0_6_kf35[:,1], data0_8_kf35[:,1], data1_0_kf35[:,1]]))

# frequency

_,extrctBins0_2_35,_ = plt.hist(kf350000_RMSD_matrix[:,1], bins=100, histtype=u'step')
_,extrctBins0_4_35,_ = plt.hist(kf350000_RMSD_matrix[:,2], bins=100, histtype=u'step')
_,extrctBins0_6_35,_ = plt.hist(kf350000_RMSD_matrix[:,3], bins=100, histtype=u'step')
_,extrctBins0_8_35,_ = plt.hist(kf350000_RMSD_matrix[:,4], bins=100, histtype=u'step')
_,extrctBins1_0_35,_ = plt.hist(kf350000_RMSD_matrix[:,5], bins=100, histtype=u'step')

dens0_2_35 = stats.gaussian_kde(kf350000_RMSD_matrix[:,1])
dens0_4_35 = stats.gaussian_kde(kf350000_RMSD_matrix[:,2])
dens0_6_35 = stats.gaussian_kde(kf350000_RMSD_matrix[:,3])
dens0_8_35 = stats.gaussian_kde(kf350000_RMSD_matrix[:,4])
dens1_0_35 = stats.gaussian_kde(kf350000_RMSD_matrix[:,5])


#%%

# density
plt.plot(extrctBins0_2_35, dens0_2_35(extrctBins0_2_35))
plt.plot(extrctBins0_4_35, dens0_4_35(extrctBins0_4_35))
plt.plot(extrctBins0_6_35, dens0_6_35(extrctBins0_6_35))
plt.plot(extrctBins0_8_35, dens0_8_35(extrctBins0_8_35))
plt.plot(extrctBins1_0_35, dens1_0_35(extrctBins1_0_35))

#%%

# plotting kf400000
data0_2_kf40 = np.genfromtxt('0_2_40.txt', delimiter = ' ')
data0_4_kf40 = np.genfromtxt('0_4_40.txt', delimiter = ' ')
data0_6_kf40 = np.genfromtxt('0_6_40.txt', delimiter = ' ')
data0_8_kf40 = np.genfromtxt('0_8_40.txt', delimiter = ' ')
data1_0_kf40 = np.genfromtxt('1_0_40.txt', delimiter = ' ')

kf400000_RMSD_matrix = np.transpose(np.array([data0_2_kf40[:,0], data0_2_kf40[:,1] ,data0_4_kf40[:,1], data0_6_kf40[:,1], data0_8_kf40[:,1], data1_0_kf40[:,1]]))

# frequency

_,extrctBins0_2_40,_ = plt.hist(kf400000_RMSD_matrix[:,1], bins=100, histtype=u'step')
_,extrctBins0_4_40,_ = plt.hist(kf400000_RMSD_matrix[:,2], bins=100, histtype=u'step')
_,extrctBins0_6_40,_ = plt.hist(kf400000_RMSD_matrix[:,3], bins=100, histtype=u'step')
_,extrctBins0_8_40,_ = plt.hist(kf400000_RMSD_matrix[:,4], bins=100, histtype=u'step')
_,extrctBins1_0_40,_ = plt.hist(kf400000_RMSD_matrix[:,5], bins=100, histtype=u'step')

dens0_2_40 = stats.gaussian_kde(kf400000_RMSD_matrix[:,1])
dens0_4_40 = stats.gaussian_kde(kf400000_RMSD_matrix[:,2])
dens0_6_40 = stats.gaussian_kde(kf400000_RMSD_matrix[:,3])
dens0_8_40 = stats.gaussian_kde(kf400000_RMSD_matrix[:,4])
dens1_0_40 = stats.gaussian_kde(kf400000_RMSD_matrix[:,5])


#%%

# density
plt.plot(extrctBins0_2_40, dens0_2_40(extrctBins0_2_40))
plt.plot(extrctBins0_4_40, dens0_4_40(extrctBins0_4_40))
plt.plot(extrctBins0_6_40, dens0_6_40(extrctBins0_6_40))
plt.plot(extrctBins0_8_40, dens0_8_40(extrctBins0_8_40))
plt.plot(extrctBins1_0_40, dens1_0_40(extrctBins1_0_40))

#%%

# plotting kf50000
data0_2_kf45 = np.genfromtxt('0_2_45.txt', delimiter = ' ')
data0_4_kf45 = np.genfromtxt('0_4_45.txt', delimiter = ' ')
data0_6_kf45 = np.genfromtxt('0_6_45.txt', delimiter = ' ')
data0_8_kf45 = np.genfromtxt('0_8_45.txt', delimiter = ' ')
data1_0_kf45 = np.genfromtxt('1_0_45.txt', delimiter = ' ')

kf450000_RMSD_matrix = np.transpose(np.array([data0_2_kf45[:,0], data0_2_kf45[:,1] ,data0_4_kf45[:,1], data0_6_kf45[:,1], data0_8_kf45[:,1], data1_0_kf45[:,1]]))

# frequency

_,extrctBins0_2_45,_ = plt.hist(kf450000_RMSD_matrix[:,1], bins=100, histtype=u'step')
_,extrctBins0_4_45,_ = plt.hist(kf450000_RMSD_matrix[:,2], bins=100, histtype=u'step')
_,extrctBins0_6_45,_ = plt.hist(kf450000_RMSD_matrix[:,3], bins=100, histtype=u'step')
_,extrctBins0_8_45,_ = plt.hist(kf450000_RMSD_matrix[:,4], bins=100, histtype=u'step')
_,extrctBins1_0_45,_ = plt.hist(kf450000_RMSD_matrix[:,5], bins=100, histtype=u'step')

dens0_2_45 = stats.gaussian_kde(kf50000_RMSD_matrix[:,1])
dens0_4_45 = stats.gaussian_kde(kf50000_RMSD_matrix[:,2])
dens0_6_45 = stats.gaussian_kde(kf50000_RMSD_matrix[:,3])
dens0_8_45 = stats.gaussian_kde(kf50000_RMSD_matrix[:,4])
dens1_0_45 = stats.gaussian_kde(kf50000_RMSD_matrix[:,5])


#%%

# density
plt.plot(extrctBins0_2_45, dens0_2_45(extrctBins0_2_45))
plt.plot(extrctBins0_4_45, dens0_4_45(extrctBins0_4_45))
plt.plot(extrctBins0_6_45, dens0_6_45(extrctBins0_6_45))
plt.plot(extrctBins0_8_45, dens0_8_45(extrctBins0_8_45))
plt.plot(extrctBins1_0_45, dens1_0_45(extrctBins1_0_45))

#%%
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

kf_array = [50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000]
ax.plot3D(extrctBins0_2_05, [50000]*101, dens0_2_05(extrctBins0_2_05), 'C0', label='\u03BB = 0.2')
ax.plot3D(extrctBins0_4_05, [50000]*101, dens0_4_05(extrctBins0_4_05), 'C1', label='\u03BB = 0.4')
ax.plot3D(extrctBins0_6_05, [50000]*101, dens0_6_05(extrctBins0_6_05), 'C2', label='\u03BB = 0.6')
ax.plot3D(extrctBins0_8_05, [50000]*101, dens0_8_05(extrctBins0_8_05), 'C3', label='\u03BB = 0.8')
ax.plot3D(extrctBins1_0_05, [50000]*101, dens1_0_05(extrctBins1_0_05), 'C4', label='\u03BB = 1.0')

ax.plot3D(extrctBins0_2_10, [100000]*101, dens0_2_10(extrctBins0_2_10), 'C0')
ax.plot3D(extrctBins0_4_10, [100000]*101, dens0_4_10(extrctBins0_4_10), 'C1')
ax.plot3D(extrctBins0_6_10, [100000]*101, dens0_6_10(extrctBins0_6_10), 'C2')
ax.plot3D(extrctBins0_8_10, [100000]*101, dens0_8_10(extrctBins0_8_10), 'C3')
ax.plot3D(extrctBins1_0_10, [100000]*101, dens1_0_10(extrctBins1_0_10), 'C4')

ax.plot3D(extrctBins0_2_15, [150000]*101, dens0_2_15(extrctBins0_2_15), 'C0')
ax.plot3D(extrctBins0_4_15, [150000]*101, dens0_4_15(extrctBins0_4_15), 'C1')
ax.plot3D(extrctBins0_6_15, [150000]*101, dens0_6_15(extrctBins0_6_15), 'C2')
ax.plot3D(extrctBins0_8_15, [150000]*101, dens0_8_15(extrctBins0_8_15), 'C3')
ax.plot3D(extrctBins1_0_15, [150000]*101, dens1_0_15(extrctBins1_0_15), 'C4')

ax.plot3D(extrctBins0_2_20, [200000]*101, dens0_2_20(extrctBins0_2_20), 'C0')
ax.plot3D(extrctBins0_4_20, [200000]*101, dens0_4_20(extrctBins0_4_20), 'C1')
ax.plot3D(extrctBins0_6_20, [200000]*101, dens0_6_20(extrctBins0_6_20), 'C2')
ax.plot3D(extrctBins0_8_20, [200000]*101, dens0_8_20(extrctBins0_8_20), 'C3')
ax.plot3D(extrctBins1_0_20, [200000]*101, dens1_0_20(extrctBins1_0_20), 'C4')

ax.plot3D(extrctBins0_2_25, [250000]*101, dens0_2_25(extrctBins0_2_25), 'C0')
ax.plot3D(extrctBins0_4_25, [250000]*101, dens0_4_25(extrctBins0_4_25), 'C1')
ax.plot3D(extrctBins0_6_25, [250000]*101, dens0_6_25(extrctBins0_6_25), 'C2')
ax.plot3D(extrctBins0_8_25, [250000]*101, dens0_8_25(extrctBins0_8_25), 'C3')
ax.plot3D(extrctBins1_0_25, [250000]*101, dens1_0_25(extrctBins1_0_25), 'C4')

ax.plot3D(extrctBins0_2_30, [300000]*101, dens0_2_30(extrctBins0_2_30), 'C0')
ax.plot3D(extrctBins0_4_30, [300000]*101, dens0_4_30(extrctBins0_4_30), 'C1')
ax.plot3D(extrctBins0_6_30, [300000]*101, dens0_6_30(extrctBins0_6_30), 'C2')
ax.plot3D(extrctBins0_8_30, [300000]*101, dens0_8_30(extrctBins0_8_30), 'C3')
ax.plot3D(extrctBins1_0_30, [300000]*101, dens1_0_30(extrctBins1_0_30), 'C4')

ax.plot3D(extrctBins0_2_35, [350000]*101, dens0_2_35(extrctBins0_2_35), 'C0')
ax.plot3D(extrctBins0_4_35, [350000]*101, dens0_4_35(extrctBins0_4_35), 'C1')
ax.plot3D(extrctBins0_6_35, [350000]*101, dens0_6_35(extrctBins0_6_35), 'C2')
ax.plot3D(extrctBins0_8_35, [350000]*101, dens0_8_35(extrctBins0_8_35), 'C3')
ax.plot3D(extrctBins1_0_35, [350000]*101, dens1_0_35(extrctBins1_0_35), 'C4')

ax.plot3D(extrctBins0_2_40, [400000]*101, dens0_2_40(extrctBins0_2_40), 'C0')
ax.plot3D(extrctBins0_4_40, [400000]*101, dens0_4_40(extrctBins0_4_40), 'C1')
ax.plot3D(extrctBins0_6_40, [400000]*101, dens0_6_40(extrctBins0_6_40), 'C2')
ax.plot3D(extrctBins0_8_40, [400000]*101, dens0_8_40(extrctBins0_8_40), 'C3')
ax.plot3D(extrctBins1_0_40, [400000]*101, dens1_0_40(extrctBins1_0_40), 'C4')

ax.plot3D(extrctBins0_2_45, [450000]*101, dens0_2_45(extrctBins0_2_45), 'C0')
ax.plot3D(extrctBins0_4_45, [450000]*101, dens0_4_45(extrctBins0_4_45), 'C1')
ax.plot3D(extrctBins0_6_45, [450000]*101, dens0_6_45(extrctBins0_6_45), 'C2')
ax.plot3D(extrctBins0_8_45, [450000]*101, dens0_8_45(extrctBins0_8_45), 'C3')
ax.plot3D(extrctBins1_0_45, [450000]*101, dens1_0_45(extrctBins1_0_45), 'C4')

ax.legend()
ax.set_xlabel('RMSD', fontweight='bold', fontstyle='italic')
ax.set_ylabel('Kf', fontweight='bold', fontstyle='italic')
ax.set_zlabel('Density', fontweight='bold', fontstyle='italic')
# ax.xaxis.set_pane_color((1.0,1.0,1.0,0.0))
# ax.yaxis.set_pane_color((1.0,1.0,1.0,0.0))
# ax.zaxis.set_pane_color((1.0,1.0,1.0,0.0))
# ax.grid(False)

# %%
