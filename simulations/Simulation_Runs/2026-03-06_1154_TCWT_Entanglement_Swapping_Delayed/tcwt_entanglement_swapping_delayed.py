import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

np.random.seed(42)

# Delay time (units of coherence time)
delay_times = np.linspace(0, 10, 80)

# Which-path ambiguity strength (0 = no info, 1 = full which-path)
which_path_strength = 0.6  # partial ambiguity

KAPPA = 1.454
BETA = 0.75

fidelities = []

for delay in delay_times:
    # Phase mismatch from delay (accumulated Ω gradient)
    phase_mismatch = KAPPA * delay * 0.1  # small per unit delay
    
    # Which-path measurement on pair A adds Ω → de-phases
    omega_which = which_path_strength * BETA * 2.0
    vis_which = np.exp(-omega_which)
    
    # Swapping fidelity: reduced by phase mismatch + which-path loss
    base_fid = (1 + np.cos(phase_mismatch)) / 2  # interference term
    swapping_fid = vis_which * base_fid + (1 - vis_which) * 0.5  # classical mixing
    
    # Delay also adds decoherence to pair B before swap
    delay_decoh = np.exp(-BETA * delay * 0.05)
    final_fid = swapping_fid * delay_decoh
    
    fidelities.append(np.clip(final_fid, 0.5, 1.0))

fig, ax = plt.subplots(figsize=(11, 6.5))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(delay_times, fidelities, color='#00D4FF', lw=2.8, marker='o', markersize=3,
        label=f'Swapped Fidelity (which-path strength = {which_path_strength})')
ax.axhline(1.0, color='lime', linestyle=':', label='Perfect Swapping')
ax.axhline(0.5, color='red', linestyle='--', label='Classical Limit')

ax.set_title('TCWT: Delayed Entanglement Swapping with Which-Path Ambiguity', color='white', fontsize=14)
ax.set_xlabel('Delay Time (coherence units)', color='white')
ax.set_ylabel('Swapped Entanglement Fidelity', color='white')
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
