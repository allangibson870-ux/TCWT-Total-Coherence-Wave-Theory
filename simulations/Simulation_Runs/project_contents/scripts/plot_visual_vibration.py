import matplotlib.pyplot as plt
import numpy as np

# Load the data
z0 = np.loadtxt('output/tcwt_high_sig_01_z1_pk.dat')
z1 = np.loadtxt('output/tcwt_high_sig_01_z2_pk.dat')

k = z0[:, 0]
ratio = z0[:, 1] / z1[:, 1]

# Zoom in on the Cluster Scales (0.01 to 1.0 h/Mpc)
mask = (k >= 0.01) & (k <= 1.0)
k_zoom = k[mask]
ratio_zoom = ratio[mask]

plt.figure(figsize=(12, 6))
# Using a thin line to see the individual oscillations
plt.plot(k_zoom, ratio_zoom, color='indigo', lw=0.8, label='TimeWave Oscillation')

plt.title('TimeWave Vibration: Cluster-Scale Resonance', fontsize=14)
plt.xlabel('Scale k [h/Mpc] (Galaxy Cluster Scales)', fontsize=12)
plt.ylabel('Growth Intensity Ratio', fontsize=12)
plt.grid(True, which="both", alpha=0.3, ls='--')
plt.legend()

# Save the plot
plt.savefig('timewave_resonance_zoom.png', dpi=300)
print("Zoom plot saved as timewave_resonance_zoom.png")
