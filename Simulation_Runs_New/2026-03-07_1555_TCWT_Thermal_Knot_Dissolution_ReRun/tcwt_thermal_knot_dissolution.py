import numpy as np
import matplotlib.pyplot as plt

# Fixed internal TCWT values
KAPPA = 1.455
BETA = 1 / 24.6  # ≈ 0.04065, derived from transition scale

# Temperature range (Kelvin)
T = np.linspace(0, 300, 200)

# Thermal energy per degree of freedom (k_B T)
kB = 1.380649e-23  # Boltzmann constant
E_thermal = kB * T

# Knot binding energy scale (from squeeze pressure, hydrogen reference)
E_knot = 3.509e12 * (1e-30)  # rough scale from P_bind * volume ~10^{-30} m³

# Effective Ω from thermal leakage (competes with knot squeeze)
Omega_thermal = KAPPA * (E_thermal / E_knot)

# Fidelity suppression (visibility)
fidelity = np.exp(-BETA * Omega_thermal)
fidelity = np.clip(fidelity, 0.0, 1.0)

fig, ax = plt.subplots(figsize=(11, 6.5))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(T, fidelity, color='#FF8800', lw=2.8, label='Knot Stability (TCWT)')

ax.axvspan(0, 50, color='#006400', alpha=0.12, label='Supercoherent Zone (Cryo)')
ax.axvspan(150, 300, color='#8B0000', alpha=0.3, label='Classical/Thermal Zone')

ax.axhline(0.5, color='gray', linestyle='--', label='Classical threshold (~0.5)')

ax.set_title('TCWT Stress Test: Thermal Leakage & Knot Dissolution', color='white', fontsize=15)
ax.set_xlabel('Temperature (Kelvin)', color='white')
ax.set_ylabel('Quantum Fidelity', color='white')
ax.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white', fontsize=11)
ax.tick_params(colors='white')
ax.grid(alpha=0.15)

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
plt.savefig("$PNG_NAME", dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
