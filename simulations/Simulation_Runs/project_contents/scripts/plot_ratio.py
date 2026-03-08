import matplotlib.pyplot as plt
import numpy as np
import os

tcwt_root = 'output/tcwt_deep_03_'
lcdm_root = 'output/lcdm_ref_'
redshifts = ['0', '1.0', '2.0', '5.0', '10.0']
colors = plt.cm.plasma(np.linspace(0, 0.8, len(redshifts)))

plt.figure(figsize=(10, 6))

for i, z in enumerate(redshifts):
    f_tcwt = f'{tcwt_root}z{i+1}_pk.dat'
    f_lcdm = f'{lcdm_root}z{i+1}_pk.dat'
    
    if os.path.exists(f_tcwt) and os.path.exists(f_lcdm):
        d_tcwt = np.loadtxt(f_tcwt)
        d_lcdm = np.loadtxt(f_lcdm)
        # Plot ratio: TCWT / LCDM
        plt.semilogx(d_tcwt[:, 0], d_tcwt[:, 1]/d_lcdm[:, 1], label=f'z = {z}', color=colors[i], lw=2)

plt.axhline(1.0, color='black', ls='--', alpha=0.5)
plt.title('Ratio: P(k) TCWT / P(k) LCDM', fontsize=14)
plt.xlabel('k [h/Mpc]', fontsize=12)
plt.ylabel('Ratio', fontsize=12)
plt.legend()
plt.grid(True, which='both', ls='-', alpha=0.2)
plt.tight_layout()
plt.savefig('tcwt_vs_lcdm_ratio.png')
print('SUCCESS: tcwt_vs_lcdm_ratio.png created')