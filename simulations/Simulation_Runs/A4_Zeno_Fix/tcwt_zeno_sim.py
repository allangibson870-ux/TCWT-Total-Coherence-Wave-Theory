import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# TCWT Constants
kappa = 1.454
freqs = np.linspace(0, 80, 200)

def simulate_zeno():
    # Weak measurements preserve state but still "leak" info over time
    zeno = np.exp(-(0.002 * freqs) / kappa)
    # Strong measurements "boil" the temporal curvature, causing rapid collapse
    anti_zeno = np.exp(-(0.008 * freqs**1.5) / kappa)
    return zeno, anti_zeno

zeno_vals, anti_vals = simulate_zeno()

# Plotting
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#050505')
ax.set_facecolor('#050505')

ax.plot(freqs, zeno_vals, color='#00FFCC', lw=3, label='Weak Measurements (Zeno - Stabilized)')
ax.plot(freqs, anti_vals, color='#FF3366', lw=3, label='Strong Measurements (Anti-Zeno - Collapse)')
ax.axhline(0.97, color='white', ls='--', alpha=0.3, label='Free Evolution (No Leakage)')

# Aesthetics
ax.set_title('TCWT: Quantum Zeno vs. Informational Boiling', color='white', fontsize=16)
ax.set_xlabel('Measurement Frequency (Interaction Rate)', color='white')
ax.set_ylabel('System Coherence (Fidelity)', color='white')
ax.set_ylim(0, 1.05)
ax.grid(alpha=0.1)
ax.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white')
ax.tick_params(colors='white')

plt.tight_layout()
plt.savefig("tcwt_zeno_fix.png", dpi=200, facecolor=fig.get_facecolor())
plt.close()
