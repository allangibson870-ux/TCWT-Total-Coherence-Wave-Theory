import matplotlib.pyplot as plt
import numpy as np

# Load snapshots
z0 = np.loadtxt('output/tcwt_high_sig_01_z1_pk.dat')
z1 = np.loadtxt('output/tcwt_high_sig_01_z2_pk.dat')

plt.figure(figsize=(10, 6))

# Plot the ratio to see how growth "vibrates" over time
# We compare the Power Spectrum at Redshift 0 vs Redshift 1
plt.loglog(z0[:,0], z0[:,1]/z1[:,1], color='purple', lw=2, label='Growth Ratio (z0/z1)')

plt.xlabel('Scale k [h/Mpc]', fontsize=12)
plt.ylabel('Relative Growth Intensity', fontsize=12)
plt.title('TimeWave Perturbations: Galaxy Clumping Vibration', fontsize=14)
plt.grid(True, which="both", alpha=0.2)
plt.legend()

plt.savefig('clumping_vibration.png', dpi=300)
print("Perturbation plot saved as clumping_vibration.png")
