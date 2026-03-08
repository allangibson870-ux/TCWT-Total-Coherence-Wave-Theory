import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

np.random.seed(42)

# Measurement frequency (how many per unit time)
freq = np.linspace(0, 80, 100)

# Two cases: weak measurements (Zeno) vs strong measurements (anti-Zeno)
omega_weak_per_meas  = 0.008 * 1.454   # small Ω → Zeno regime
omega_strong_per_meas = 0.08 * 1.454   # larger Ω → anti-Zeno regime

BETA = 0.75
natural_decay_rate = 0.025  # free evolution decay over t=1

# Free evolution fidelity (no measurements)
fidelity_free = np.exp(-natural_decay_rate * 1.0)

fidelity_weak = []
fidelity_strong = []

for f in freq:
    # Weak measurements (Zeno)
    omega_total_weak = f * omega_weak_per_meas
    suppression_weak = np.exp(-BETA * omega_total_weak)
    fid_weak = suppression_weak + (1 - suppression_weak) * fidelity_free
    fidelity_weak.append(np.clip(fid_weak, 0.0, 1.0))
    
    # Strong measurements (anti-Zeno)
    omega_total_strong = f * omega_strong_per_meas
    suppression_strong = np.exp(-BETA * omega_total_strong)
    fid_strong = fidelity_free * np.exp(-omega_total_strong * 1.5)  # extra decay acceleration
    fidelity_strong.append(np.clip(fid_strong, 0.0, 1.0))

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(freq, fidelity_weak, color='#00FF88', lw=2.8, label='Weak measurements (Zeno regime)')
ax.plot(freq, fidelity_strong, color='#FF4444', lw=2.8, label='Strong measurements (Anti-Zeno regime)')
ax.axhline(fidelity_free, color='white', linestyle='--', alpha=0.7, label='No measurements (free evolution)')
ax.axhline(1.0, color='lime', linestyle=':', label='Perfect preservation')

ax.set_title('TCWT: Quantum Zeno + Anti-Zeno Crossover', color='white', fontsize=15)
ax.set_xlabel('Measurement Frequency (per unit time)', color='white', fontsize=13)
ax.set_ylabel('Final State Fidelity', color='white', fontsize=13)
ax.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white', fontsize=11)
ax.tick_params(colors='white')
ax.grid(alpha=0.15)

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=220, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Plot saved to: {png_path}")
