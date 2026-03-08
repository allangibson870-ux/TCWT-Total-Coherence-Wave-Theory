import matplotlib.pyplot as plt
import numpy as np
import os
import glob

lcdm_ref = 'output/lcdm_ref_00_z1_pk.dat'
c3_list = ['01', '10', '20', '50']
labels = ['c3 = 0.1', 'c3 = 1.0', 'c3 = 2.0', 'c3 = 5.0']

# Load LCDM baseline
d_l = np.loadtxt(lcdm_ref)
k_l, pk_l = d_l[:, 0], d_l[:, 1]

plt.figure(figsize=(10, 6))

for c3, label in zip(c3_list, labels):
    # This tries every possible CLASS naming convention
    patterns = [
        f'output/study_c3_{c3}_*z1_pk.dat',
        f'output/study_c3_{c3}_*pk.dat',
        f'output/study_c3_{c3}*z1_pk.dat'
    ]
    
    found = False
    for p in patterns:
        files = glob.glob(p)
        if files:
            f_t = sorted(files)[-1]
            print(f"MATCH: {label} -> {f_t}")
            d_t = np.loadtxt(f_t)
            k_t, pk_t = d_t[:, 0], d_t[:, 1]
            pk_l_interp = np.exp(np.interp(np.log(k_t), np.log(k_l), np.log(pk_l)))
            plt.semilogx(k_t, pk_t / pk_l_interp, label=label, lw=2)
            found = True
            break
            
    if not found:
        print(f"MISSING: {label} (Checked patterns: {patterns})")

plt.axhline(1.0, color='k', ls='--', alpha=0.5)
plt.title('Final TCWT Sensitivity Study ($z=0$)', fontsize=14)
plt.xlabel('k [h/Mpc]', fontsize=12)
plt.ylabel('Ratio P(k) / P(k)_LCDM', fontsize=12)
plt.legend()
plt.grid(True, which='both', alpha=0.2)
plt.tight_layout()
plt.savefig('tcwt_final_results.png')
print("\nSUCCESS: tcwt_final_results.png created.")
