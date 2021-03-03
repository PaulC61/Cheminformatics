# Urest plots for default lambda schedule

# %%
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats


lstUrest_g17 = [0.60506, 0.92349, 1.22291, 1.48476, 1.71415, 1.93006, 2.13796, 2.34800, 2.56222, 2.76744, 2.95910, 3.02912]
lstUrest_g19 = [0.06224, 0.65081, 1.22467, 1.72317, 2.55617, 3.24288, 3.85860, 4.14854]
lstUrest_g20 = [0.60565, 0.89151, 1.16864, 1.66526, 2.11759, 2.57528, 3.03234, 3.45601, 4.52562]
#lstUrest_g20 = [0.01835, 0.03611, 0.05263, 0.60565, 0.89151, 1.16864, 1.66526, 2.11759, 2.57528, 3.03234, 3.45601, 4.52562]
lstLbd_g17 = [0.2, 0.27, 0.34, 0.41, 0.48, 0.55, 0.62, 0.69, 0.76, 0.83, 0.90, 0.97]
lstLbd_g19 = [0.001, 0.01, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0]
lstLbd_g20 = [0.01, 0.015, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
#lstLbd_g20 = [0.0025, 0.0050, 0.0075, 0.01, 0.015, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]



plt.figure()
plt.plot(lstLbd_g17, lstUrest_g17, 'xb-', label='G-17, Hexane')
plt.plot(lstLbd_g19, lstUrest_g19, 'xr-', label='G-19, Cyclohexane')
plt.plot(lstLbd_g20, lstUrest_g20, 'xg-', label='G-20, Benzene')
plt.xlabel('Lambda')
plt.ylabel('Free Energy (kcal/mol)')
plt.legend()
plt.show()

lstUrestunb_g17 = [1.70345, 3.20608, 4.70188, 6.09530, 7.40139, 8.32797, 8.66958, 8.74097, 8.80568, 8.86609, 8.92549, 8.95058]
lstUrestunb_g19 = [0.06255, 0.63740, 1.18517, 1.66736, 2.11136, 2.51006, 2.86749, 3.20309, 3.52183, 4.10699]
lstUrestunb_g20 = [0.23033, 0.45127, 0.59752, 0.74214, 0.88036, 1.01237,  1.38886]
#lstUrestunb_g20 = [0.00408, 0.00807, 0.01200, 0.15243, 0.23033, 0.30565, 0.45127, 0.59752, 0.74214, 0.88036, 1.01237,  1.38886]
lstLbdunb_g17 = [0.2, 0.27, 0.34, 0.41, 0.48, 0.55, 0.62, 0.69, 0.76, 0.83, 0.90, 0.97]
lstLbdunb_g19 = [0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.8, 1.0]
lstLbdunb_g20 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
#lstLbdunb_g20 = [0.0025, 0.0050, 0.0075, 0.01, 0.1, 0.015, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

plt.figure()
plt.plot(lstLbdunb_g17, lstUrestunb_g17, 'xb-', label='G-17, Hexane')
plt.plot(lstLbdunb_g19, lstUrestunb_g19, 'xr-', label='G-19, Cyclohexane')
plt.plot(lstLbdunb_g20, lstUrestunb_g20, 'xg-', label='G-20, Benzene')
plt.xlabel('Lambda')
plt.ylabel('Free Energy (kcal/mol)')
plt.legend()
plt.show()
# %%



# %%
