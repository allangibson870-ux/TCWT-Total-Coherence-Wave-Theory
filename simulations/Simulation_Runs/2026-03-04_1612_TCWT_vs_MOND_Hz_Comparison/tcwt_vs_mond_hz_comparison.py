import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# Redshift range
z = np.linspace(0.0, 20.0, 500)

# TCWT: Resonant late-time modulation
h0_local = 73.1
h0_early = 67.4
decay_scale = 5.0
ripple_amp = 0.8
ripple_freq = 0.8
tcwt_hz = h0_local - (h0_local - h0_early) * (1 - np.exp(-z / decay_scale))
tcwt_hz += ripple_amp * np.sin(ripple_freq * z) * np.exp(-z / 3.0)

# MOND-inspired toy
mond_factor = 1 + 0.02 * np.exp(-z / 2.0)
mond_hz = h0_early * mond_factor

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(z, tcwt_hz, color='#00FF88', lw=2.0, label='TCWT: Resonant Transition H(z)')
ax.axhline(h0_local, color='#FFAA00', ls='--', lw=1.2, label=f'Local H₀ ≈ {h0_local}')
ax.axhline(h0_early, color='#44FF44', ls='--', lw=1.2, label=f'Early H₀ ≈ {h0_early}')
ax.plot(z, mond_hz, color='#FF4444', lw=1.5, alpha=0.7, label='MOND-inspired toy')

ax.set_xlabel('Redshift z', color='white')
ax.set_ylabel('Effective H(z) [km/s/Mpc]', color='white')
ax.set_title('TCWT vs. MOND-inspired H(z) Comparison', color='white')
ax.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white')
ax.tick_params(colors='white')
ax.grid(alpha=0.15, color='gray')

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Saved to: {png_path}")
