import matplotlib.pyplot as plt
import numpy as np
import os

# Standard baseline we know works
std_path = 'output/tcwt_eternal_test_00_z1_pk.dat'
# Our new stable high-density run
dense_path = 'output/stable_dense_z1_pk.dat'

if not os.path.exists(dense_path):
    # Check for the common '00' suffix
    dense_path = 'output/stable_dense_00_z1_pk.dat'

if not os.path.exists(dense_path):
    print("Error: Simulation did not produce a .dat file. Check terminal for 'Error' messages.")
    exit()

s_data = np.loadtxt(std_path)
d_data = np.loadtxt(dense_path)

plt.figure(figsize=(12, 6))
plt.loglog(s_data[:, 0], s_data[:, 1]/s_data[0,1], 'r-', label='Standard Density')
plt.loglog(d_data[:, 0], d_data[:, 1]/d_data[0,1], 'g--', label='Stable High Density')
plt.axvline(0.1, color='k', ls=':', label='Cluster Threshold')
plt.title('TimeWave Vibration: Stable Density Squeeze')
plt.xlabel('Scale k [h/Mpc]')
plt.ylabel('Relative Growth Intensity')
plt.legend()
plt.savefig('stable_squeeze_plot.png')
print("Plot saved as stable_squeeze_plot.png")
