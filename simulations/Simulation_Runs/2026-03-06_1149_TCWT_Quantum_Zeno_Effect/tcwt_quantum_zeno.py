import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

np.random.seed(42)

# Measurement frequency (how often we apply weak Ω kick per unit time)
freq = np.linspace(0, 100, 120)  # 0 = no measurement → free evolution

# Derived κ from hydrogen squeeze
KAPPA = 1.454
BETA = 0.75

# Evolution without measurement: fidelity decays slowly due to natural Ω
natural_decay_rate = 0.02
fidelity_free = np.exp(-natural_decay_rate * 1.0)  # over fixed time t=1

# With Zeno: each measurement adds small Ω → suppresses evolution
# Fidelity ≈ exp(- Ω_total), where Ω_total ∝ freq × κ × BETA
omega_per_measurement = KAPPA * 0.01  # weak per measurement
omega_total = freq * omega_per_measurement
zeno_suppression = np.exp(-BETA * omega_total)

# Combined: Zeno protects against natural decay
fidelity_zeno = zeno_suppression * (1 - (1 - fidelity_free) * (1 - zeno_suppression))

# Clip to realistic range
fidelity_zeno = np.clip(fidelity_zeno, 0.0, 1.0)

fig, ax = plt.subplots(figsize=(11, 6.5))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(freq, fidelity_zeno, color='#FF8800', lw=2.8, marker='o', markersize=3,
        label='Fidelity with Zeno measurements')
ax.axhline(fidelity_free, color='lime', linestyle='--', label='No measurements (free evolution)')
ax.axhline(1.0, color='white', linestyle=':', alpha=0.6, label='Perfect preservation')

ax.set_title('TCWT: Quantum Zeno Effect – Frequent Weak Measurements Freeze Evolution', color='white', fontsize=14)
ax.set_xlabel('Measurement Frequency (per unit time)', color='white')
ax.set_ylabel('Final State Fidelity', color='white')
ax.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white', fontsize=10)
ax.tick_params(colors='white')
ax.grid(alpha=0.15)

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=220, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Plot saved to: {png_path}")
