import matplotlib.pyplot as plt
import numpy as np
import os

# Robust file finder for the slow runs
def get_pk(prefix):
    opts = [f'output/{prefix}z1_pk.dat', f'output/{prefix}00_z1_pk.dat']
    for p in opts:
        if os.path.exists(p): return np.loadtxt(p)
    return None

std, dns = get_pk('slow_std_'), get_pk('slow_dense_')

if std is None or dns is None:
    print("Error: The TimeWave is still too 'stiff'. We may need to lower phi_initial further.")
    exit()

plt.figure(figsize=(12, 6))
# Normalizing both to see the 'shift' in the curve's elbow
plt.loglog(std[:, 0], std[:, 1]/std[0,1], 'r-', label='Standard Density (0.12)')
plt.loglog(dns[:, 0], dns[:, 1]/dns[0,1], 'g--', label='High Density (0.35)')

plt.axvline(0.1, color='k', ls=':', label='Cluster Threshold')
plt.title('TimeWave Vibration: Slow-Wave Density Squeeze')
plt.xlabel('Scale k [h/Mpc]')
plt.ylabel('Normalized Growth Intensity')
plt.legend()
plt.savefig('slow_squeeze_plot.png')
print("Success! Plot saved as slow_squeeze_plot.png")
