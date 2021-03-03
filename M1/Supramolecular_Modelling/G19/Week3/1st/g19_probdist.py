
#%%
import numpy as np
import scipy.stats as stats

from matplotlib import pyplot as plt


steps = 4
lst_r = []
lst_thetamin = []
lst_phimin = []
lst_thetamaj = []
lst_phimaj = []
lst_psi = []

#listLbd = [0.0001, 0.001, 0.01, 0.1, 0.2, 0.5, 1.0]
listLbd = [0.0001, 0.01, 0.1, 1.0]
for i in range(steps):
    file = np.genfromtxt(str(listLbd[i])+'.vba', delimiter=' ')
    lst_r.append(file[7:,1])
    lst_thetamin.append(file[7:,3])
    lst_phimin.append(file[7:,5])
    lst_thetamaj.append(file[7:,7])
    lst_phimaj.append(file[7:,9])
    lst_psi.append(file[7:,11])



#to produce density distributions you need to add 'density=True' in each histogram
plt.figure()
data1r,bins1r,_=plt.hist(lst_r[0], bins=75, edgecolor='black', histtype='step', label='0.0001')
data2r,bins2r,_=plt.hist(lst_r[1], bins=75, edgecolor='green', histtype='step', label='0.01')
data3r,bins3r,_=plt.hist(lst_r[2], bins=75, edgecolor='red', histtype='step', label='0.1')
data4r,bins4r,_=plt.hist(lst_r[3], bins=75, edgecolor='blue', histtype='step', label='1')
'''data5,bins5,_=plt.hist(lst_r[4], bins=75, edgecolor='purple', histtype='step', label='0.2')
data6,bins6,_=plt.hist(lst_r[5], bins=75, edgecolor='blue', histtype='step', label='0.5')
data7,bins7,_=plt.hist(lst_r[6], bins=75, edgecolor='orange', histtype='step', label='1.0')'''
plt.title('CV : r')
plt.xlabel('nm')
plt.legend()


plt.figure()
data1tmin,bins1tmin,_=plt.hist(lst_thetamin[0], bins=75, edgecolor='black', histtype='step', label='0.0001')
data2tmin,bins2tmin,_=plt.hist(lst_thetamin[1], bins=75, edgecolor='green', histtype='step', label='0.01')
data3tmin,bins3tmin,_=plt.hist(lst_thetamin[2], bins=75, edgecolor='red', histtype='step', label='0.1')
data4tmin,bins4tmin,_=plt.hist(lst_thetamin[3], bins=75, edgecolor='blue', histtype='step', label='1')
'''data5,bins5,_=plt.hist(lst_thetamin[4], bins=75, edgecolor='purple', histtype='step', label='0.2')
data6,bins6,_=plt.hist(lst_thetamin[5], bins=75, edgecolor='blue', histtype='step', label='0.5')
data7,bins7,_=plt.hist(lst_thetamin[6], bins=75, edgecolor='orange', histtype='step', label='1.0')'''
plt.title('CV : theta')
plt.xlabel('rad')
plt.legend()

plt.figure()
data1pmin,bins1pmin,_=plt.hist(lst_phimin[0], bins=75, edgecolor='black', histtype='step', label='0.0001')
data2pmin,bins2pmin,_=plt.hist(lst_phimin[1], bins=75, edgecolor='green', histtype='step', label='0.01')
data3pmin,bins3pmin,_=plt.hist(lst_phimin[2], bins=75, edgecolor='red', histtype='step', label='0.1')
data4pmin,bins4pmin,_=plt.hist(lst_phimin[3], bins=75, edgecolor='blue', histtype='step', label='1')
'''data5,bins5,_=plt.hist(lst_phimin[4], bins=75, edgecolor='purple', histtype='step', label='0.2')
data6,bins6,_=plt.hist(lst_phimin[5], bins=75, edgecolor='blue', histtype='step', label='0.5')
data7,bins7,_=plt.hist(lst_phimin[6], bins=75, edgecolor='orange', histtype='step', label='1.0')'''
plt.title('CV : phi')
plt.xlabel('rad')
plt.legend()

plt.figure()
data1tmaj,bins1tmaj,_=plt.hist(lst_thetamaj[0], bins=75, edgecolor='black', histtype='step', label='0.0001')
data2tmaj,bins2tmaj,_=plt.hist(lst_thetamaj[1], bins=75, edgecolor='green', histtype='step', label='0.01')
data3tmaj,bins3tmaj,_=plt.hist(lst_thetamaj[2], bins=75, edgecolor='red', histtype='step', label='0.1')
data4tmaj,bins4tmaj,_=plt.hist(lst_thetamaj[3], bins=75, edgecolor='blue', histtype='step', label='1')
'''data5,bins5,_=plt.hist(lst_thetamaj[4], bins=75, edgecolor='purple', histtype='step', label='0.2')
data6,bins6,_=plt.hist(lst_thetamaj[5], bins=75, edgecolor='blue', histtype='step', label='0.5')
data7,bins7,_=plt.hist(lst_thetamaj[6], bins=75, edgecolor='orange', histtype='step', label='1.0')'''
plt.title('CV : THETA')
plt.xlabel('rad')
plt.legend()

plt.figure()
data1pmaj,bins1pmaj,_=plt.hist(lst_phimaj[0], bins=75, edgecolor='black', histtype='step', label='0.0001')
data2pmaj,bins2pmaj,_=plt.hist(lst_phimaj[1], bins=75, edgecolor='green', histtype='step', label='0.01')
data3pmaj,bins3pmaj,_=plt.hist(lst_phimaj[2], bins=75, edgecolor='red', histtype='step', label='0.1')
data4pmaj,bins4pmaj,_=plt.hist(lst_phimaj[3], bins=75, edgecolor='blue', histtype='step', label='1')
'''data5,bins5,_=plt.hist(lst_phimaj[4], bins=75, edgecolor='purple', histtype='step', label='0.2')
data6,bins6,_=plt.hist(lst_phimaj[5], bins=75, edgecolor='blue', histtype='step', label='0.5')
data7,bins7,_=plt.hist(lst_phimaj[6], bins=75, edgecolor='orange', histtype='step', label='1.0')'''
plt.title('CV : PHI')
plt.xlabel('rad')
plt.legend()

plt.figure()
data1psi,bins1psi,_=plt.hist(lst_psi[0], bins=75, edgecolor='black', histtype='step', label='0.0001')
data2psi,bins2psi,_=plt.hist(lst_psi[1], bins=75, edgecolor='green', histtype='step', label='0.01')
data3psi,bins3psi,_=plt.hist(lst_psi[2], bins=75, edgecolor='red', histtype='step', label='0.1')
data4psi,bins4psi,_=plt.hist(lst_psi[3], bins=75, edgecolor='blue', histtype='step', label='1')
'''data5,bins5,_=plt.hist(lst_psi[4], bins=75, edgecolor='purple', histtype='step', label='0.2')
data6,bins6,_=plt.hist(lst_psi[5], bins=75, edgecolor='blue', histtype='step', label='0.5')
data7,bins7,_=plt.hist(lst_psi[6], bins=75, edgecolor='orange', histtype='step', label='1.0')'''
plt.title('CV : PSI')
plt.xlabel('rad')
plt.legend()

# %%

#%%

plt.figure()
density1r=stats.gaussian_kde(lst_r[0])
density2r=stats.gaussian_kde(lst_r[1])
density3r=stats.gaussian_kde(lst_r[2])
density4r=stats.gaussian_kde(lst_r[3])


plt.plot(bins1r, density1r(bins1r), label='0.0001')
plt.plot(bins2r, density2r(bins2r), label='0.01')
plt.plot(bins3r, density3r(bins3r), label='0.1')
plt.plot(bins4r, density4r(bins4r), label='1')
plt.title('CV : r')
plt.xlabel('Urest')
plt.ylabel('Density')
plt.legend()
plt.show()

plt.figure()
density1tmin=stats.gaussian_kde(lst_thetamin[0])
density2tmin=stats.gaussian_kde(lst_thetamin[1])
density3tmin=stats.gaussian_kde(lst_thetamin[2])
density4tmin=stats.gaussian_kde(lst_thetamin[3])


plt.plot(bins1tmin, density1tmin(bins1tmin), label='0.0001')
plt.plot(bins2tmin, density2tmin(bins2tmin), label='0.01')
plt.plot(bins3tmin, density3tmin(bins3tmin), label='0.1')
plt.plot(bins4tmin, density4tmin(bins4tmin), label='1')
plt.title('CV : theta')
plt.xlabel('Urest')
plt.ylabel('Density')
plt.legend()
plt.show()

plt.figure()
density1pmin=stats.gaussian_kde(lst_phimin[0])
density2pmin=stats.gaussian_kde(lst_phimin[1])
density3pmin=stats.gaussian_kde(lst_phimin[2])
density4pmin=stats.gaussian_kde(lst_phimin[3])


plt.plot(bins1pmin, density1pmin(bins1pmin), label='0.0001')
plt.plot(bins2pmin, density2pmin(bins2pmin), label='0.01')
plt.plot(bins3pmin, density3pmin(bins3pmin), label='0.1')
plt.plot(bins4pmin, density4pmin(bins4pmin), label='1')
plt.title('CV : phi')
plt.xlabel('Urest')
plt.ylabel('Density')
plt.legend()
plt.show()


plt.figure()
density1tmaj=stats.gaussian_kde(lst_thetamaj[0])
density2tmaj=stats.gaussian_kde(lst_thetamaj[1])
density3tmaj=stats.gaussian_kde(lst_thetamaj[2])
density4tmaj=stats.gaussian_kde(lst_thetamaj[3])


plt.plot(bins1tmaj, density1pmin(bins1tmaj), label='0.0001')
plt.plot(bins2tmaj, density2pmin(bins2tmaj), label='0.01')
plt.plot(bins3tmaj, density3pmin(bins3tmaj), label='0.1')
plt.plot(bins4tmaj, density4pmin(bins4tmaj), label='1')
plt.title('CV : THETA')
plt.xlabel('Urest')
plt.ylabel('Density')
plt.legend()
plt.show()

plt.figure()
density1pmaj=stats.gaussian_kde(lst_phimaj[0])
density2pmaj=stats.gaussian_kde(lst_phimaj[1])
density3pmaj=stats.gaussian_kde(lst_phimaj[2])
density4pmaj=stats.gaussian_kde(lst_phimaj[3])


plt.plot(bins1pmaj, density1pmin(bins1pmaj), label='0.0001')
plt.plot(bins2pmaj, density2pmin(bins2pmaj), label='0.01')
plt.plot(bins3pmaj, density3pmin(bins3pmaj), label='0.1')
plt.plot(bins4pmaj, density4pmin(bins4pmaj), label='1')
plt.title('CV : PHI')
plt.xlabel('Urest')
plt.ylabel('Density')
plt.legend()
plt.show()


plt.figure()
density1psi=stats.gaussian_kde(lst_psi[0])
density2psi=stats.gaussian_kde(lst_psi[1])
density3psi=stats.gaussian_kde(lst_psi[2])
density4psi=stats.gaussian_kde(lst_psi[3])


plt.plot(bins1psi, density1pmin(bins1psi), label='0.0001')
plt.plot(bins2psi, density2pmin(bins2psi), label='0.01')
plt.plot(bins3psi, density3pmin(bins3psi), label='0.1')
plt.plot(bins4psi, density4pmin(bins4psi), label='1')
plt.title('CV : PSI')
plt.xlabel('Urest')
plt.ylabel('Density')
plt.legend()
plt.show()