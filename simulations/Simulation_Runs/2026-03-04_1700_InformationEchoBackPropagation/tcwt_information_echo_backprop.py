import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# Time axis (dimensionless)
t = np.linspace(-5.0, 2.0, 2000)

# Background Hum (eternal, low amplitude)
hum_amp = 0.05
hum_freq = 6.0 * np.pi
hum = hum_amp * np.sin(hum_freq * t)

# Forward knot (post-BB damping, untangling)
knot_amp = 0.6
knot_freq = 20.0 * np.pi
knot_damping = 0.8  # fast damping post-t=0
knot = np.where(t >= 0, knot_amp * np.exp(-knot_damping * t) * np.sin(knot_freq * t), 0.0)

# Information echo: small fraction of knot's final state fed back pre-t=0
echo_retention = 0.08  # 8% of knot amplitude echoes back
echo_delay = 0.3       # slight time shift
echo = np.where(t < 0, echo_retention * knot_amp * np.exp(knot_damping * (t + echo_delay)) * np.sin(knot_freq * (t + echo_delay)), 0.0)

# Total with echo
total_with_echo = hum + knot + echo
total_no_echo = hum + knot

# Plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
fig.patch.set_facecolor('#0a0a0a')

# Top: without echo
ax1.set_facecolor('#0a0a0a')
ax1.plot(t, total_no_echo, color='#00FF88', lw=2.0, label='Total (no echo)')
ax1.plot(t, hum, color='#00F5FF', lw=1.2, alpha=0.6, label='Background Hum')
ax1.plot(t, knot, color='#FF44AA', lw=1.5, alpha=0.7, label='Forward Knot')
ax1.axvline(0.0, color='#FFAA00', ls='--', lw=1.2, label='Snag / t=0')
ax1.set_title('TimeWave without Echo', color='white')
ax1.set_ylabel('Amplitude', color='white')
ax1.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white')
ax1.tick_params(colors='white')
ax1.grid(alpha=0.15, color='gray')
for s in ax1.spines.values():
    s.set_color('white')

# Bottom: with echo
ax2.set_facecolor('#0a0a0a')
ax2.plot(t, total_with_echo, color='#00FF88', lw=2.0, label='Total (with echo)')
ax2.plot(t, hum, color='#00F5FF', lw=1.2, alpha=0.6, label='Background Hum')
ax2.plot(t, knot, color='#FF44AA', lw=1.5, alpha=0.7, label='Forward Knot')
ax2.plot(t, echo, color='#FFFF44', lw=1.8, alpha=0.8, label='Back-Propagated Echo')
ax2.axvline(0.0, color='#FFAA00', ls='--', lw=1.2, label='Snag / t=0')
ax2.set_title('TimeWave with Information Echo Back-Propagation', color='white')
ax2.set_xlabel('Dimensionless Time (0 = Snag/BB)', color='white')
ax2.set_ylabel('Amplitude', color='white')
ax2.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white')
ax2.tick_params(colors='white')
ax2.grid(alpha=0.15, color='gray')
for s in ax2.spines.values():
    s.set_color('white')

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Saved to: {png_path}")
