import matplotlib.pyplot as plt
import numpy as np
import os

def load_res(root):
    paths = [f'output/{root}z1_pk.dat', f'output/{root}00_z1_pk.dat']
    for p in paths:
        if os.path.exists(p): return np.loadtxt(p)
    return None

std = load_res('sq_std_')
dns = load_res('sq_dense_')

if std is None or dns is None:
    print(f"Error: Files still missing. Check your 'output/' folder.")
    exit()

k = std[:, 0]
y_std = (std[:, 1] / std[0, 1]) * 2.711
y_dns = (dns[:, 1] / dns[0, 1]) * 2.711

plt.figure(figsize=(12, 6))
plt.loglog(k, y_std, 'r-', lw=2, label='Standard Density (z=0)')
plt.loglog(k, y_dns, 'g--', lw=2, label='High Density (The Squeeze)')
plt.axhline(2.711, color='k', ls=':', label='2.711 Resonance (e)')
plt.title('TimeWave Compression: Density vs Vibration')
plt.xlabel('Scale k [h/Mpc]')
plt.ylabel('Normalized Growth Intensity')
plt.legend()
plt.savefig('timewave_compression_test.png')
print("Plot saved as timewave_compression_test.png")
