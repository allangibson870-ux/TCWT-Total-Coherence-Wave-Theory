import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# TCWT Constants
kappa = 1.454
temp_k = np.linspace(0.01, 300, 300) # 0 to 300 Kelvin

def simulate_thermal_coherence():
    # In TCWT, Omega_T increases with temperature.
    # We model this as Omega_T = (k_B * T) / E_coherence
    # where E_coherence is the "stiffness" of the knot.
    omega_t = (0.005 * temp_k) / kappa
    
    # Fidelity F = exp(-kappa * Omega_T)
    # Plus a non-linear "boiling" effect as we hit phase transitions
    boiling_effect = 1.0 / (1.0 + np.exp(0.1 * (temp_k - 150)))
    
    fidelity = np.exp(-omega_t) * boiling_effect
    return fidelity

feds = simulate_thermal_coherence()

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#050505')
ax.set_facecolor('#050505')

ax.plot(temp_k, feds, color='#FF6600', lw=3, label='Knot Stability (TCWT)')
ax.axhline(0.5, color='white', ls='--', alpha=0.3, label='The Heisenberg Cut')

# Zones
ax.axvspan(0, 50, color='cyan', alpha=0.05, label='Supercoherent Zone (Cryo)')
ax.axvspan(270, 300, color='red', alpha=0.05, label='Classical/Thermal Zone')

# Aesthetics
ax.set_title('TCWT Stress Test: Thermal Leakage & Knot Dissolution', color='white', fontsize=16)
ax.set_xlabel('Temperature (Kelvin)', color='white')
ax.set_ylabel('Quantum Fidelity', color='white')
ax.set_ylim(-0.05, 1.05)
ax.grid(alpha=0.1)
ax.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white')
ax.tick_params(colors='white')

plt.tight_layout()
plt.savefig("tcwt_thermal_decay.png", dpi=200, facecolor=fig.get_facecolor())
plt.close()
