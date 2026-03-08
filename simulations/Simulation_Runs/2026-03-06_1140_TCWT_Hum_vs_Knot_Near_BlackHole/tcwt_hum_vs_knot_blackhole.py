import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

np.random.seed(42)

# Radial distance in units of Schwarzschild radius (just outside to far away)
r_over_rs = np.linspace(1.01, 20, 150)

# Extreme Ω gradient near horizon
omega = 15.0 / (r_over_rs - 1.0)  # tuned for sharp transition

# Background Hum: exponentially suppressed by Ω
hum_amplitude = np.exp(-1.0 * omega)

# Knot mode: rises as background is suppressed (conservation of total wave energy)
# Knot amplitude ≈ 1 - hum_amplitude, with sharp peak near horizon
knot_amplitude = 1.0 - hum_amplitude
knot_amplitude = np.clip(knot_amplitude * (1 + 8 * np.exp(-12 * (r_over_rs - 1.0))), 0, 1.2)

fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.semilogy(r_over_rs, hum_amplitude, color='#00FFAA', lw=3.0, label='Background Hum (suppressed)')
ax.semilogy(r_over_rs, knot_amplitude, color='#FF4400', lw=3.0, label='Knot Mode (black hole itself)')

ax.axvline(1.0, color='red', linestyle='--', lw=2.0, label='Event Horizon (Rs)')
ax.axhline(1e-4, color='white', linestyle=':', alpha=0.6, label='Hum effectively gone')

ax.set_title('TCWT: Background Hum vs Knot Mode Near Black Hole', color='white', fontsize=16)
ax.set_xlabel('Radial Distance (in Rs)', color='white', fontsize=13)
ax.set_ylabel('Normalised Amplitude (log scale)', color='white', fontsize=13)
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
