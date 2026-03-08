import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

t = np.linspace(-5.0, 2.0, 2000)

hum_amp = 0.05
hum_freq = 6.0 * np.pi
hum = hum_amp * np.sin(hum_freq * t)

main_knot_amp = 0.6
main_knot_freq = 20.0 * np.pi
main_damping = 0.8
main_knot = np.where(t >= 0, main_knot_amp * np.exp(-main_damping * t) * np.sin(main_knot_freq * t), 0.0)

sub_knot_amp = 1.2
sub_knot_freq = 40.0 * np.pi
sub_damping = 1.2
sub_center = 0.2
sub_width = 0.4
envelope = np.exp(-0.5 * ((t - sub_center) / sub_width) ** 2)
sub_knot = sub_knot_amp * envelope * np.exp(-sub_damping * np.maximum(t, 0)) * np.sin(sub_knot_freq * t)

echo_retention = 0.12
echo_delay = 0.25
sub_echo = np.where(t < 0, echo_retention * sub_knot_amp * np.exp(sub_damping * (t + echo_delay)) * np.sin(sub_knot_freq * (t + echo_delay)), 0.0)

total = hum + main_knot + sub_knot + sub_echo

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
fig.patch.set_facecolor('#0a0a0a')

ax1.plot(t, total, color='#00FF88', lw=2.0, label='Total (with sub-echo)')
ax1.plot(t, hum, color='#00F5FF', lw=1.2, alpha=0.6, label='Background Hum')
ax1.plot(t, main_knot, color='#FF44AA', lw=1.5, alpha=0.7, label='Main knot')
ax1.plot(t, sub_knot, color='#FF8800', lw=1.5, alpha=0.7, label='Sub-knot (BH-like)')
ax1.axvline(0.0, color='#FFAA00', ls='--', lw=1.2, label='Main Snag / t=0')
ax1.set_title('TimeWave with Sub-Knot Echo Back-Propagation', color='white')
ax1.set_ylabel('Amplitude', color='white')
ax1.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white')
ax1.tick_params(colors='white')
ax1.grid(alpha=0.15)

ax2.plot(t, sub_echo, color='#FFFF44', lw=2.0, label='Sub-knot Echo (back-propagated)')
ax2.axvline(0.0, color='#FFAA00', ls='--', lw=1.2)
ax2.set_title('Echo from Sub-Knot Only (pre-Snag imprint)', color='white')
ax2.set_xlabel('Dimensionless Time (0 = Snag/BB)', color='white')
ax2.set_ylabel('Amplitude', color='white')
ax2.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white')
ax2.tick_params(colors='white')
ax2.grid(alpha=0.15)

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Saved to: {png_path}")
