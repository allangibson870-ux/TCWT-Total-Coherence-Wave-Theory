import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

np.random.seed(42)

# Radial distance from black hole centre (in units of Schwarzschild radius Rs)
r_over_rs = np.linspace(1.01, 20, 100)  # just outside horizon to far away

# Ω spikes dramatically near horizon (1 / (1 - Rs/r))
omega = 10.0 / (r_over_rs - 1.0)

# Hum amplitude damping + phase scrambling
hum_amplitude = np.exp(-0.8 * omega)
phase_coherence = np.exp(-1.2 * omega)  # stronger scrambling near horizon

fig, ax = plt.subplots(figsize=(11, 6.5))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(r_over_rs, hum_amplitude, color='#00FFAA', lw=2.5, label='Hum Amplitude')
ax.plot(r_over_rs, phase_coherence, color='#FFAA00', lw=2.5, label='Phase Coherence')
ax.axvline(1.0, color='red', linestyle='--', label='Event Horizon (Rs)')
ax.axhline(0.01, color='white', linestyle=':', alpha=0.6, label='Hum effectively gone')

ax.set_title('TCWT: Eternal Hum Reaction Near Black Hole', color='white', fontsize=14)
ax.set_xlabel('Radial Distance (in Rs)', color='white')
ax.set_ylabel('Normalised Hum Strength', color='white')
ax.legend(facecolor='#111111', labelcolor='white')
ax.tick_params(colors='white')
ax.grid(alpha=0.15)
ax.set_yscale('log')

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Plot saved to: {png_path}")
