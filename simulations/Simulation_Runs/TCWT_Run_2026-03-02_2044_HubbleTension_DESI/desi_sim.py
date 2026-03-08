import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load DESI-style data
df = pd.read_csv("../../hubble_tension_data.csv")

z_data = df["redshift"].values
H_data = df["H_z_predicted"].values

# Assume a simple symmetric error for illustration (DESI-like)
H_err = np.full_like(H_data, 1.5)

# TCWT model curve
z = np.linspace(0, 3.0, 600)

H0_planck = 67.4
H0_local = 73.1
H0_tcwt_base = 73.0

amp = 1.0
period_z = 2.0
damping_scale = 3.0

trend = H0_planck + (H0_tcwt_base - H0_planck) * np.exp(-z / 4.0)
osc = amp * np.exp(-z / damping_scale) * np.sin(2 * np.pi * z / period_z)
H_tcwt = trend + osc

H_local_line = np.full_like(z, H0_local)
H_planck_line = np.full_like(z, H0_planck)

plt.figure(figsize=(10, 6))

plt.errorbar(z_data, H_data, yerr=H_err, fmt='o', color='black',
             ecolor='gray', elinewidth=1.2, capsize=3,
             label='DESI-style H(z) points')

plt.plot(z, H_tcwt, color='limegreen', lw=2.5,
         label='TCWT: Resonant Transition H(z)')

plt.plot(z, H_local_line, 'm--', lw=1.8,
         label='Local H₀ (SH0ES/Riess ≈ 73.1)')

plt.plot(z, H_planck_line, 'c--', lw=1.8,
         label='Early H₀ (Planck/CMB ≈ 67.4)')

plt.xlabel('Redshift z')
plt.ylabel('H(z) [km/s/Mpc]')
plt.title('TCWT vs DESI-style H(z): Resonant Late-Time Modulation')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('tcwt_hubble_tension_desi.png', dpi=200)
