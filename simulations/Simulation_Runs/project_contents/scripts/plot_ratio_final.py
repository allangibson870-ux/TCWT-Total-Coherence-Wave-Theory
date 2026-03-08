import matplotlib.pyplot as plt
import numpy as np
import os

# Hard-coding the exact paths we see in your terminal
tcwt_root = 'output/tcwt_deep_03_'
lcdm_root = 'output/lcdm_ref_00_'
redshifts = ['0', '1.0', '2.0', '5.0', '10.0']
colors = plt.cm.plasma(np.linspace(0, 0.8, len(redshifts)))

plt.figure(figsize=(10, 6))

for i, z in enumerate(redshifts):
    f_t = f'{tcwt_root}z{i+1}_pk.dat'
    f_l = f'{lcdm_root}z{i+1}_pk.dat'
    
    if os.path.exists(f_t) and os.path.exists(f_l):
        d_t = np.loadtxt(f_t)
        d_l = np.loadtxt(f_l)
        # Plot ratio: TCWT / LCDM
        plt.semilogx(d_t[:, 0], d_t[:, 1]/d_l[:, 1], label=f'z = {z}', color=colors[i], lw=2)
    else:
        print(f'Missing one of: {f_t} or {f_l}')

plt.axhline(1.0, color='black', ls='--', alpha=0.5)
plt.title('Ratio: P(k) TCWT / P(k) LCDM', fontsize=14)
plt.xlabel('k [h/Mpc]', fontsize=12)
plt.ylabel('Ratio', fontsize=12)
plt.legend()
plt.grid(True, which='both', ls='-', alpha=0.2)
plt.tight_layout()
plt.savefig('tcwt_vs_lcdm_ratio_final.png')
print('SUCCESS: tcwt_vs_lcdm_ratio_final.png created')