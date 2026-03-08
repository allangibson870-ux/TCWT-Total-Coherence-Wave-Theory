import matplotlib.pyplot as plt
import numpy as np
import os

tcwt_strong = 'output/tcwt_strong_00_z1_pk.dat'
tcwt_stable = 'output/tcwt_stable_00_z1_pk.dat'
tcwt_goldi = 'output/tcwt_goldilocks_00_z1_pk.dat'
lcdm_ref = 'output/lcdm_ref_00_z1_pk.dat'

plt.figure(figsize=(10, 6))

def get_ratio(f_t, f_l):
    if os.path.exists(f_t) and os.path.exists(f_l):
        d_t, d_l = np.loadtxt(f_t), np.loadtxt(f_l)
        pk_l_interp = np.exp(np.interp(np.log(d_t[:,0]), np.log(d_l[:,0]), np.log(d_l[:,1])))
        return d_t[:,0], d_t[:,1]/pk_l_interp
    return None, None

k1, r1 = get_ratio(tcwt_strong, lcdm_ref)
if r1 is not None: plt.semilogx(k1, r1, label='Strong (0.5)', alpha=0.3)

k2, r2 = get_ratio(tcwt_stable, lcdm_ref)
if r2 is not None: plt.semilogx(k2, r2, label='Stable (0.05)', alpha=0.5)

k3, r3 = get_ratio(tcwt_goldi, lcdm_ref)
if r3 is not None: plt.semilogx(k3, r3, label='Goldilocks (0.18)', color='red', lw=2)

plt.axhline(1.0, color='k', ls='--')
plt.title('TCWT Growth: Finding the Goldilocks Zone (0.18)')
plt.xlabel('k [h/Mpc]')
plt.ylabel('Ratio to LCDM')
plt.legend()
plt.grid(True, which='both', alpha=0.2)
plt.savefig('tcwt_goldilocks_check.png')
print('SUCCESS: tcwt_goldilocks_check.png created')