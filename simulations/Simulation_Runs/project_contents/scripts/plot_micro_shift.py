import matplotlib.pyplot as plt
import numpy as np
import os

# Updated to the exact filenames on your screen
std_f = 'output/tcwt_eternal_test_00_z1_pk.dat'
mic_f = 'output/micro_squeeze_00_pk.dat'

if not os.path.exists(std_f):
    print(f"Error: Missing {std_f}")
    exit()
if not os.path.exists(mic_f):
    print(f"Error: Missing {mic_f}")
    exit()

s_data = np.loadtxt(std_f)
m_data = np.loadtxt(mic_f)

k_s, pk_s = s_data[:, 0], s_data[:, 1]
k_m, pk_m = m_data[:, 0], m_data[:, 1]

plt.figure(figsize=(12, 6))
# Normalizing by the first value to see the 'shape' of the growth
plt.loglog(k_s, pk_s / pk_s[0], 'r-', lw=2, label='Standard Density (0.12)')
plt.loglog(k_m, pk_m / pk_m[0], 'g--', lw=2, label='Micro-Squeeze (0.135)')

plt.axvline(0.1, color='k', ls=':', label='Cluster Threshold')
plt.title('TimeWave Resonance: The Micro-Squeeze Shift')
plt.xlabel('Scale k [h/Mpc]')
plt.ylabel('Normalized Growth Intensity')
plt.legend()
plt.grid(True, which="both", alpha=0.2)
plt.savefig('micro_shift_plot.png')
print("Success! Plot saved as micro_shift_plot.png")
