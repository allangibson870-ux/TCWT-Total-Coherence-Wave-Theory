import matplotlib.pyplot as plt
import numpy as np
import os

# Comparing the two TCWT variants
root_05_1 = 'output/tcwt_strong_00_'
root_05_5 = 'output/tcwt_shift_00_'
lcdm_root = 'output/lcdm_ref_00_'

plt.figure(figsize=(10, 6))

def plot_ratio(root, label, color, ls):
    f_t, f_l = f'{root}z1_pk.dat', f'{lcdm_root}z1_pk.dat'
    if os.path.exists(f_t) and os.path.exists(f_l):
        d_t, d_l = np.loadtxt(f_t), np.loadtxt(f_l)
        k_t, pk_t = d_t[:, 0], d_t[:, 1]
        k_l, pk_l = d_l[:, 0], d_l[:, 1]
        pk_l_interp = np.exp(np.interp(np.log(k_t), np.log(k_l), np.log(pk_l)))
        plt.semilogx(k_t, pk_t / pk_l_interp, label=label, color=color, ls=ls, lw=2)

plot_ratio(root_05_1, 'Strong (c3=1.0)', 'blue', '-')
plot_ratio(root_05_5, 'Shifted (c3=5.0)', 'red', '--')

plt.axhline(1.0, color='k', ls=':', alpha=0.5)
plt.title('Effect of tcwt_c3_galileon on Growth Peaks (z=0)')
plt.xlabel('k [h/Mpc]')
plt.ylabel('Ratio to LCDM')
plt.legend()
plt.grid(True, which='both', alpha=0.2)
plt.savefig('tcwt_peak_shift_compare.png')
print('SUCCESS: tcwt_peak_shift_compare.png created')