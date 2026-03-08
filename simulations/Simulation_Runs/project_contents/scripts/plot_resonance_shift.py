import matplotlib.pyplot as plt
import numpy as np
import os

# Define possible indices hi_class might have used
for idx in ['00', '01', '02']:
    path1 = f'output/tcwt_eternal_test_{idx}_z1_pk.dat'
    path2 = f'output/tcwt_eternal_test_{idx}_z2_pk.dat'
    if os.path.exists(path1):
        print(f"Loading data from index {idx}...")
        z0 = np.loadtxt(path1)
        z5 = np.loadtxt(path2)
        break
else:
    print("Could not find the output files. Please check 'ls output/tcwt_eternal_test_*'")
    exit()

k = z0[:, 0]
# Calculate the Growth Intensity Ratio for both
# (Power at k / Power at k_min) to see the 'Resonance' shape
ratio_today = z0[:, 1] / z0[0, 1]
ratio_early = z5[:, 1] / z5[0, 1]

plt.figure(figsize=(12, 6))
plt.loglog(k, ratio_today, color='crimson', lw=2, label='Today (z=0)')
plt.loglog(k, ratio_early, color='navy', lw=2, ls='--', label='Early Universe (z=5)')
plt.axhline(2.711, color='black', ls=':', label='2.711 Resonance (e)')

plt.xlabel('Scale k [h/Mpc]', fontsize=12)
plt.ylabel('Normalized Growth Intensity', fontsize=12)
plt.title('TimeWave Resonance: Today vs. High-Density Past', fontsize=14)
plt.grid(True, which="both", alpha=0.2)
plt.legend()
plt.savefig('resonance_shift_comparison.png', dpi=300)
print("Comparison plot saved as resonance_shift_comparison.png")
