import numpy as np
import matplotlib.pyplot as plt

# Fixed internal TCWT values
KAPPA = 1.455
BETA = 1 / 24.6  # ≈ 0.04065

# Measurement frequency range (interactions per second)
nu = np.linspace(0, 80, 200)

# Weak measurements (Zeno): small Ω per interaction
Omega_weak = KAPPA * nu * 1e-12  # small Δt per weak measurement
fidelity_weak = np.exp(-BETA * Omega_weak)
fidelity_weak = np.clip(fidelity_weak, 0.0, 1.0)

# Strong measurements (Anti-Zeno): large Ω per interaction
Omega_strong = KAPPA * nu * 1e-9  # larger Δt per strong measurement
fidelity_strong = np.exp(-BETA * Omega_strong)
fidelity_strong = np.clip(fidelity_strong, 0.0, 1.0)

# Free evolution (no measurements)
fidelity_free = np.ones_like(nu)

fig, ax = plt.subplots(figsize=(11, 6.5))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(nu, fidelity_weak, color='#00FF88', lw=2.8, label='Weak Measurements (Zeno - Stabilized)')
ax.plot(nu, fidelity_strong, color='#FF4444', lw=2.8, label='Strong Measurements (Anti-Zeno - Collapse)')
ax.plot(nu, fidelity_free, color='white', linestyle='--', lw=1.5, label='Free Evolution (No Leakage)')

ax.axhline(0.5, color='gray', linestyle='--', label='Classical threshold (~0.5)')

ax.set_title('TCWT: Quantum Zeno vs. Informational Boiling', color='white', fontsize=15)
ax.set_xlabel('Measurement Frequency (Interaction Rate)', color='white')
ax.set_ylabel('System Coherence (Fidelity)', color='white')
ax.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white', fontsize=11)
ax.tick_params(colors='white')
ax.grid(alpha=0.15)

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
plt.savefig("$PNG_NAME", dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
