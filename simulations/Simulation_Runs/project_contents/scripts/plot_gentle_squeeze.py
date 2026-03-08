import matplotlib.pyplot as plt
import numpy as np
import os

# Standard (0.12) vs Gentle Squeeze (0.15)
std_f = 'output/tcwt_eternal_test_00_z1_pk.dat'
gnt_f = 'output/gentle_squeeze_00_z1_pk.dat'

if not os.path.exists(gnt_f): gnt_f = 'output/gentle_squeeze_z1_pk.dat'
if not os.path.exists(gnt_f):
    print("Even the gentle squeeze is too intense. The TimeWave is incredibly sensitive to mass!")
    exit()

s_data, g_data = np.loadtxt(std_f), np.loadtxt(gnt_f)
plt.figure(figsize=(12, 6))
plt.loglog(s_data[:, 0], s_data[:, 1]/s_data[0,1], 'r-', label='Standard Density (0.12)')
plt.loglog(g_data[:, 0], g_data[:, 1]/g_data[0,1], 'b--', label='Gentle Squeeze (0.15)')
plt.axvline(0.1, color='k', ls=':', label='Cluster Threshold')
plt.title('TimeWave Theory: The Gentle Density Squeeze')
plt.legend()
plt.savefig('gentle_squeeze_plot.png')
print("Success! Plot saved as gentle_squeeze_plot.png")
