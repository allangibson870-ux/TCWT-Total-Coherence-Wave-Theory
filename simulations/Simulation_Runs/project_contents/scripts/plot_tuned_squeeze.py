import matplotlib.pyplot as plt
import numpy as np
import os

# Paths to our baseline and new tuned run
std_path = 'output/tcwt_eternal_test_00_z1_pk.dat'
dns_path = 'output/tuned_dense_z1_pk.dat'

# Fallback for hi_class indexing
if not os.path.exists(dns_path): dns_path = 'output/tuned_dense_00_z1_pk.dat'

if not os.path.exists(dns_path):
    print("Error: Files still missing. The TimeWave is still too 'stiff' for the solver.")
    exit()

s_data = np.loadtxt(std_path)
d_data = np.loadtxt(dns_path)

plt.figure(figsize=(12, 6))
# Normalize both to their first point to see the 'Squeeze' shift
plt.loglog(s_data[:, 0], s_data[:, 1]/s_data[0,1], 'r-', label='Standard Density')
plt.loglog(d_data[:, 0], d_data[:, 1]/d_data[0,1], 'g--', label='Tuned High Density')
plt.axvline(0.1, color='k', ls=':', label='Cluster Threshold')
plt.title('TimeWave Vibration: Tuned Density Squeeze')
plt.xlabel('Scale k [h/Mpc]')
plt.ylabel('Normalized Growth Intensity')
plt.legend()
plt.savefig('tuned_squeeze_plot.png')
print("Plot saved as tuned_squeeze_plot.png")
