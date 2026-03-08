import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# TCWT Constants
kappa = 1.454
# G-Force (multiples of Earth Gravity)
g_force = np.linspace(1, 100000, 500) 

def predict_decoherence():
    # Standard QM: Coherence is independent of G-force (Flat line at 1.0)
    standard_qm = np.ones_like(g_force)
    
    # TCWT: Gravity induces Omega. As G increases, Omega rises by power of 4.
    # We normalize such that 1G is negligible.
    omega_g = (g_force / 50000)**4 
    tcwt_fidelity = np.exp(-kappa * omega_g)
    
    return standard_qm, tcwt_fidelity

sqm, tcwt = predict_decoherence()

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#050505')
ax.set_facecolor('#050505')

ax.plot(g_force, sqm, color='white', ls='--', alpha=0.5, label='Standard QM (No Effect)')
ax.plot(g_force, tcwt, color='#00FFCC', lw=3, label='TCWT Prediction (Gravitational Collapse)')

# The Conflict Point
ax.fill_between(g_force, tcwt, sqm, color='red', alpha=0.1, label='The Conflict Zone')

# Aesthetics
ax.set_title('TCWT Blind Prediction: Spontaneous Collapse via Acceleration', color='white', fontsize=16)
ax.set_xlabel('Acceleration (G-Force)', color='white')
ax.set_ylabel('Quantum Coherence (Fidelity)', color='white')
ax.set_xscale('log')
ax.grid(alpha=0.1)
ax.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white')
ax.tick_params(colors='white')

plt.tight_layout()
plt.savefig("tcwt_blind_prediction.png", dpi=200, facecolor=fig.get_facecolor())
plt.close()
