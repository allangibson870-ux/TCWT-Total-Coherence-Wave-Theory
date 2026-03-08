import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(0, 20.0, 800)

H0_planck = 67.4
H0_local = 73.1
H0_tcwt_base = 73.0

amp = 1.0
period_z = 4.0
damping_scale = 6.0

trend = H0_planck + (H0_tcwt_base - H0_planck) * np.exp(-z / 5.0)
osc = amp * np.exp(-z / damping_scale) * np.sin(2 * np.pi * z / period_z)
H_tcwt = trend + osc

H_local_line = np.full_like(z, H0_local)
H_planck_line = np.full_like(z, H0_planck)

plt.figure(figsize=(10, 6))
plt.plot(z, H_tcwt, color='limegreen', lw=2.5, label='TCWT: Resonant Transition H(z), High-z')
plt.plot(z, H_local_line, 'm--', lw=1.8, label='Local H₀ (SH0ES/Riess ≈ 73.1)')
plt.plot(z, H_planck_line, 'c--', lw=1.8, label='Early H₀ (Planck/CMB ≈ 67.4)')
plt.xlabel('Redshift z')
plt.ylabel('Effective H(z) [km/s/Mpc]')
plt.title('TCWT vs Hubble Tension (High-z): Resonant Late-Time Modulation of H(z)')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('tcwt_hubble_tension_highz.png', dpi=200)
