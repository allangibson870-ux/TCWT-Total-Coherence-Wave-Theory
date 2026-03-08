import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

np.random.seed(42)

# Distance range (meters, lab to cosmic scale)
distance_m = np.logspace(0, 12, 80)  # 1 m to 1e12 m (~0.1 light-year)

# Derived κ from hydrogen
KAPPA = 1.454
BETA = 0.75

# Simple model: phase mismatch grows linearly with distance (tiny Ω gradient)
# Fidelity decays as exp(- (KAPPA * distance / coherence_scale))
coherence_scale = 1e8  # base scale in metres (tuned so drop happens at realistic distances)

fidelity = np.exp(-KAPPA * (distance_m / coherence_scale) * BETA)
fidelity = np.clip(fidelity, 0.5, 1.0)  # floor at classical limit

# Find untangling distance (fidelity drops to 0.5)
untangle_idx = np.where(fidelity <= 0.5)[0]
untangle_dist = distance_m[untangle_idx[0]] if len(untangle_idx) > 0 else "beyond range"

fig, ax = plt.subplots(figsize=(11, 6.5))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.semilogx(distance_m, fidelity, color='#00D4FF', lw=2.8, marker='o', markersize=3,
            label='Entanglement Fidelity')
ax.axhline(1.0, color='lime', linestyle=':', label='Perfect Entanglement')
ax.axhline(0.5, color='red', linestyle='--', label='Classical Limit (untangled)')
ax.axvline(untangle_dist, color='white', linestyle='--', alpha=0.6,
           label=f'Untangling distance ≈ {untangle_dist:.1e} m')

ax.set_title('TCWT: Entanglement Untangling Distance', color='white', fontsize=14)
ax.set_xlabel('Separation Distance (metres)', color='white')
ax.set_ylabel('Average Entanglement Fidelity', color='white')
ax.legend(facecolor='#111111', labelcolor='white')
ax.tick_params(colors='white')
ax.grid(alpha=0.15)

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Untangling distance ≈ {untangle_dist:.1e} m")
print(f"Plot saved to: {png_path}")
