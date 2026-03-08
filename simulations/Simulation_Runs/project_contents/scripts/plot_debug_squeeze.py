import matplotlib.pyplot as plt
import numpy as np
import os

# Load the new Debug Dense run and your previous Eternal Standard run
std_path = 'output/tcwt_eternal_test_00_z1_pk.dat'
dense_path = 'output/debug_dense_z1_pk.dat'

if not os.path.exists(std_path) or not os.path.exists(dense_path):
    print("Files missing. Please check your output/ folder.")
    exit()

s_data, d_data = np.loadtxt(std_path), np.loadtxt(dense_path)
k = s_data[:, 0]

# Normalized Growth to see the TimeWave resonance shape
y_std = s_data[:, 1] / s_data[0, 1]
y_dense = d_data[:, 1] / d_data[0, 1]

plt.figure(figsize=(12, 6))
plt.loglog(k, y_std, 'r-', lw=2, label='Standard Density (Massive)')
plt.loglog(k, y_dense, 'g--', lw=2, label='High Density (The Squeeze)')
plt.axvline(0.1, color='k', ls=':', label='Cluster Threshold')
plt.title('TimeWave Vibration: Debug Density Test')
plt.xlabel('Scale k [h/Mpc]')
plt.ylabel('Relative Growth Intensity')
plt.legend()
plt.grid(True, which="both", alpha=0.2)
plt.savefig('debug_squeeze_plot.png')
print("Plot saved as debug_squeeze_plot.png")
