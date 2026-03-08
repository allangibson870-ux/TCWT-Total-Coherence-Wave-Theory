import matplotlib.pyplot as plt
import numpy as np

# Load snapshots
z0 = np.loadtxt('output/tcwt_high_sig_01_z1_pk.dat')
z1 = np.loadtxt('output/tcwt_high_sig_01_z2_pk.dat')

k = z0[:, 0]
ratio = z0[:, 1] / z1[:, 1]

# Filter for the Jitter region: 0.01 < k < 1.0
mask = (k >= 0.01) & (k <= 1.0)
k_zoom = k[mask]
ratio_zoom = ratio[mask]

plt.figure(figsize=(10, 6))
plt.plot(k_zoom, ratio_zoom, color='darkmagenta', lw=1.5, label='Jitter Signal')

plt.xscale('log')
plt.xlabel('Scale k [h/Mpc] (Cluster Scales)', fontsize=12)
plt.ylabel('Growth Ratio', fontsize=12)
plt.title('TimeWave Vibration: Zoom on Cluster-Scale Jitter', fontsize=14)
plt.grid(True, which="both", alpha=0.3)
plt.legend()

# Perform a basic FFT to find the "Vibration Frequency"
from scipy.fft import fft, fftfreq
N = len(ratio_zoom)
T = np.mean(np.diff(np.log10(k_zoom)))
yf = fft(ratio_zoom - np.mean(ratio_zoom))
xf = fftfreq(N, T)[:N//2]
peak_freq = xf[np.argmax(2.0/N * np.abs(yf[0:N//2]))]

print(f"Detected TimeWave Frequency in scale-space: {peak_freq:.4f}")

plt.savefig('timewave_jitter_zoom.png', dpi=300)
