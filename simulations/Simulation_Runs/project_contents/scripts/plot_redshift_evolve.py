import matplotlib.pyplot as plt
import numpy as np
import os

tcwt_root = 'output/tcwt_evolve_00_'
lcdm_root = 'output/lcdm_ref_00_'
redshifts = ['0', '1.0', '2.0', '5.0', '10.0']
colors = plt.cm.viridis(np.linspace(0, 1, len(redshifts)))

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
plt.title('Redshift Evolution of TCWT Growth Ratio (0.05 Breaking)', fontsize=14)
plt.xlabel('k [h/Mpc]', fontsize=12)
plt.ylabel('Ratio P(k)_TCWT / P(k)_LCDM', fontsize=12)
plt.legend()
plt.grid(True, which='both', alpha=0.2)
plt.tight_layout()
plt.savefig('tcwt_redshift_evolution.png')
print('SUCCESS: tcwt_redshift_evolution.png created')