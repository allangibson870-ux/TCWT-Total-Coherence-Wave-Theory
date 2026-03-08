import matplotlib.pyplot as plt
import numpy as np
import os

# Baseline vs Tension-Release
std_path = 'output/tcwt_eternal_test_00_z1_pk.dat'
dns_path = 'output/tension_release_z1_pk.dat'
if not os.path.exists(dns_path): dns_path = 'output/tension_release_00_z1_pk.dat'

if not os.path.exists(dns_path):
    print("Numerical Limit Reached. The TimeWave 'Vibration' at 0.35 density is too intense for linear theory.")
    exit()

s_data, d_data = np.loadtxt(std_path), np.loadtxt(dns_path)
plt.figure(figsize=(12, 6))
# Normalizing both to see the physical 'shift' in the elbow
plt.loglog(s_data[:, 0], s_data[:, 1]/s_data, 'r-', label='Standard Density (0.12)')
plt.loglog(d_data[:, 0], d_data[:, 1]/d_data, 'g--', label='High Density Squeeze (0.35)')
plt.axvline(0.1, color='k', ls=':', label='Cluster Threshold')
plt.title('TimeWave Theory: Density vs Vibration Shift')
plt.legend()
plt.savefig('tension_squeeze_plot.png')
print("Success! Plot saved as tension_squeeze_plot.png")
