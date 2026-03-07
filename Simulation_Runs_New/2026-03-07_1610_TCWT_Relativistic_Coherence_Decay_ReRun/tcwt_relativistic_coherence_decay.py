import numpy as np
import matplotlib.pyplot as plt

# Fixed internal TCWT values
KAPPA = 1.455
BETA = 1 / 24.6  # ≈ 0.04065, from Ω_transition

beta = np.linspace(0.0, 0.9999, 500)
gamma = 1 / np.sqrt(1 - beta**2)

# Rest mass term (electron for concreteness)
m_c2 = 8.187e-14  # J
K_tc = 1.455

Omega = gamma * (m_c2 + K_tc * beta * 3e8)  # v = beta * c
fidelity = np.exp(-BETA * Omega)
fidelity = np.clip(fidelity, 0.0, 1.0)

fig, ax = plt.subplots(figsize=(11, 6.5))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(beta, fidelity, color='#FF8800', lw=2.8, label='TCWT Coherence')

ax.axhline(0.5, color='red', linestyle='--', label='Classical threshold (~0.5)')
ax.axvspan(0.0, 0.8, color='lime', alpha=0.12, label='Quantum Zone')

ax.set_title('TCWT Stress Test: Relativistic Coherence Decay', color='white', fontsize=15)
ax.set_xlabel('Velocity β = v/c', color='white')
ax.set_ylabel('Quantum Fidelity', color='white')
ax.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white', fontsize=11)
ax.tick_params(colors='white')
ax.grid(alpha=0.15)

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
plt.savefig("$PNG_NAME", dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
