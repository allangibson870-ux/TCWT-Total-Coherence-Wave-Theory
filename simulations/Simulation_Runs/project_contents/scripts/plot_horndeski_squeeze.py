import matplotlib.pyplot as plt
import numpy as np
import os

# Find the Horndeski run and our standard baseline
std_path = 'output/tcwt_eternal_test_00_z1_pk.dat'
dns_path = 'output/horndeski_squeeze_z1_pk.dat'

if not os.path.exists(dns_path): dns_path = 'output/horndeski_squeeze_00_z1_pk.dat'

if not os.path.exists(dns_path):
    print("Error: Even the Horndeski proxy is too stiff. We may need to use a simpler MDE model.")
    exit()

s_data, d_data = np.loadtxt(std_path), np.loadtxt(dns_path)
plt.figure(figsize=(12, 6))
plt.loglog(s_data[:, 0], s_data[:, 1]/s_data, 'r-', label='TimeWave Standard')
plt.loglog(d_data[:, 0], d_data[:, 1]/d_data, 'g--', label='Horndeski Vibration (Squeeze)')
plt.axvline(0.1, color='k', ls=':', label='Cluster Threshold')
plt.title('TimeWave Theory: Horndeski Vibration Squeeze')
plt.legend()
plt.savefig('horndeski_squeeze_plot.png')
print("Plot saved as horndeski_squeeze_plot.png")
