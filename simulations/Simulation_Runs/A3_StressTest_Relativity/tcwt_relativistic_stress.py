import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# TCWT Constants
kappa = 1.454
v_over_c = np.linspace(0, 0.99, 200)

def simulate_relativistic_omega():
    # Lorentz Factor: gamma = 1 / sqrt(1 - v^2/c^2)
    gamma = 1 / np.sqrt(1 - v_over_c**2)
    
    # In TCWT, length contraction (r' = r/gamma) 
    # Because of 1/r^4 law: Omega' = Omega * gamma^4
    # We assume a baseline Omega of 0.01 at rest
    base_omega = 0.01
    omega_prime = base_omega * (gamma**4)
    
    # Fidelity F = exp(-kappa * Omega')
    fidelity = np.exp(-kappa * omega_prime)
    return fidelity

feds = simulate_relativistic_omega()

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#080808')
ax.set_facecolor('#080808')

ax.plot(v_over_c, feds, color='#FFCC00', lw=3, label='TCWT Coherence')
ax.axhline(0.5, color='red', ls='--', alpha=0.5, label='Classical Threshold (The Cut)')

# Annotations
ax.annotate('Relativistic Shredding', xy=(0.85, 0.2), xytext=(0.6, 0.4),
            arrowprops=dict(facecolor='white', shrink=0.05), color='white')

# Aesthetics
ax.set_title('TCWT Stress Test: Relativistic Coherence Decay', color='white', fontsize=16)
ax.set_xlabel('Velocity (v/c)', color='white')
ax.set_ylabel('Quantum Fidelity', color='white')
ax.set_ylim(-0.05, 1.05)
ax.grid(alpha=0.1)
ax.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white')
ax.tick_params(colors='white')

plt.tight_layout()
plt.savefig("tcwt_relativistic_decay.png", dpi=200, facecolor=fig.get_facecolor())
plt.close()
