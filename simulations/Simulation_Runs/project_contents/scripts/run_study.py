import subprocess
import matplotlib.pyplot as plt
import numpy as np
import os
import glob

c3_values = [0.1, 1.0, 2.0, 5.0]
lcdm_ref = 'output/lcdm_ref_00_z1_pk.dat'

plt.figure(figsize=(10, 6))

# Load LCDM baseline
d_l = np.loadtxt(lcdm_ref)
k_l, pk_l = d_l[:, 0], d_l[:, 1]

for c3 in c3_values:
    # We use a unique root for each run
    root = f'output/study_c3_{c3}_'
    ini_file = f'temp_c3_{c3}.ini'
    
    with open(ini_file, 'w') as f:
        f.write(f"h = 0.674\nomega_b = 0.02237\nomega_cdm = 0.1200\ngravity_model = tcwt\n")
        f.write(f"tcwt_upsilon_breaking = 0.5\ntcwt_c3_galileon = {c3}\n")
        f.write(f"output = mPk\nz_pk = 0\nroot = {root}\n")
    
    print(f"Running TCWT with c3 = {c3}...")
    # Using shell=True to ensure it finds the local ./class binary
    result = subprocess.run(f"./class {ini_file}", shell=True, capture_output=True, text=True)
    
    # Check if run actually produced a file
    potential_files = glob.glob(f"{root}*z1_pk.dat")
    
    if potential_files:
        f_t = sorted(potential_files)[-1] # Take the most recent if multiple exist
        d_t = np.loadtxt(f_t)
        k_t, pk_t = d_t[:, 0], d_t[:, 1]
        
        # Log-log interpolation
        pk_l_interp = np.exp(np.interp(np.log(k_t), np.log(k_l), np.log(pk_l)))
        plt.semilogx(k_t, pk_t / pk_l_interp, label=f'c3 = {c3}', lw=2)
        print(f"  -> Success: Found {f_t}")
    else:
        print(f"  -> Error: No output found for c3={c3}")
        if result.stderr: print(f"     CLASS Error: {result.stderr.splitlines()[-1]}")

plt.axhline(1.0, color='k', ls='--', alpha=0.5)
plt.title('TCWT Growth Sensitivity to Galileon Coupling ($z=0$)', fontsize=14)
plt.xlabel('k [h/Mpc]', fontsize=12)
plt.ylabel('Ratio P(k) / P(k)_LCDM', fontsize=12)
plt.legend()
plt.grid(True, which='both', alpha=0.2)
plt.tight_layout()
plt.savefig('tcwt_sensitivity_study.png')
print("\nDONE: Check 'tcwt_sensitivity_study.png'")
