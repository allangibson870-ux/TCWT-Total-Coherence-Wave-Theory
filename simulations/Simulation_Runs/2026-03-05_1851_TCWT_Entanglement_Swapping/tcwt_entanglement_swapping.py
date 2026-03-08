import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

np.random.seed(42)

omega_values = np.linspace(0.0, 5.0, 80)
fidelity_results = []

# Derived κ from hydrogen squeeze (as before)
KAPPA = 1.454
BETA = 0.75  # damping

for omega in omega_values:
    # Visibility / coherence suppression
    vis = np.exp(-BETA * omega)
    
    # Entanglement swapping fidelity
    # Low Ω: near-perfect swapping (quantum)
    # High Ω: classical limit (no swapping)
    # Model: fidelity = vis * (1 + cos(phase_diff)) / 2 + noise term
    phase_diff = KAPPA * omega * np.random.normal(0, 0.5)
    base_fid = (1 + np.cos(phase_diff)) / 2
    noise = (1 - vis) * 0.5  # classical mixing
    
    fidelity = vis * base_fid + noise
    # Cap at 1.0 and floor at 0.5 (max classical correlation)
    fidelity = np.clip(fidelity, 0.5, 1.0)
    
    fidelity_results.append(fidelity)

fig, ax = plt.subplots(figsize=(11, 6.5))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(omega_values, fidelity_results, color='#00D4FF', lw=2.8, marker='o', markersize=4,
        label='Swapping Fidelity (κ=1.454 from H squeeze)')
ax.axhline(1.0, color='lime', linestyle=':', label='Perfect Quantum Swapping')
ax.axhline(0.5, color='red', linestyle='--', label='Classical Limit (no entanglement)')
ax.fill_between(omega_values, 0.5, 1.0, color='lime', alpha=0.12, label='Quantum Regime')

ax.set_title('TCWT: Entanglement Swapping Fidelity vs Ω Distortion', color='white', fontsize=14)
ax.set_xlabel('Distortion Strength Ω', color='white', fontsize=12)
ax.set_ylabel('Average Swapping Fidelity', color='white', fontsize=12)
ax.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white', fontsize=10)
ax.tick_params(colors='white')
ax.grid(alpha=0.15)

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Saved to: {png_path}")
