import matplotlib.pyplot as plt
import numpy as np
import os

# Finding the latest strong run (likely index 00)
tcwt_root = 'output/tcwt_strong_00_'
lcdm_root = 'output/lcdm_ref_00_'
redshifts = ['0', '1.0', '2.0', '5.0', '10.0']
colors = plt.cm.plasma(np.linspace(0, 0.8, len(redshifts)))

plt.figure(figsize=(10, 6))
for i, z in enumerate(redshifts):
    f_t, f_l = f'{tcwt_root}z{i+1}_pk.dat', f'{lcdm_root}z{i+1}_pk.dat'
    if os.path.exists(f_t) and os.path.exists(f_l):
        d_t, d_l = np.loadtxt(f_t), np.loadtxt(f_l)
        k_t, pk_t = d_t[:, 0], d_t[:, 1]
        k_l, pk_l = d_l[:, 0], d_l[:, 1]
        pk_l_interp = np.exp(np.interp(np.log(k_t), np.log(k_l), np.log(pk_l)))
        plt.semilogx(k_t, pk_t / pk_l_interp, label=f'z = {z}', color=colors[i], lw=2)

plt.axhline(1.0, color='black', ls='--', alpha=0.5)
plt.title('Ratio: P(k) Strong TCWT (0.5) / P(k) LCDM', fontsize=14)
plt.xlabel('k [h/Mpc]', fontsize=12)
plt.ylabel('Ratio', fontsize=12)
plt.legend()
plt.grid(True, which='both', ls='-', alpha=0.2)
plt.tight_layout()
plt.savefig('tcwt_strong_ratio.png')
print('SUCCESS: tcwt_strong_ratio.png created')