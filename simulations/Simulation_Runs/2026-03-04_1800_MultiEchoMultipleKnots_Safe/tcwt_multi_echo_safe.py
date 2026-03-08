import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import gc
import os

gc.collect()

t = np.linspace(-5.0, 2.0, 1500)  # fewer points

hum_amp = 0.05
hum_freq = 6.0 * np.pi
hum = hum_amp * np.sin(hum_freq * t)

def damped_knot(t, amp, freq, damping, center):
    phase = freq * (t - center)
    env = np.exp(-damping * np.maximum(t - center, 0))
    return amp * env * np.sin(phase)

knots = [
    damped_knot(t, 0.6, 20*np.pi, 0.8, 0.0),
    damped_knot(t, 0.4, 30*np.pi, 1.0, 0.3),
    damped_knot(t, 0.3, 45*np.pi, 1.2, 0.6)
]

echo_retention = 0.10
echo_delays = [0.25, 0.35, 0.45]

echoes = []
for i, knot in enumerate(knots):
    echo = np.where(t < 0,
                    echo_retention * 0.6 * np.exp(0.8 * (t + echo_delays[i])) * np.sin(20*np.pi * (t + echo_delays[i])),
                    0.0)
    echoes.append(echo)

total = hum + sum(knots) + sum(echoes)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
fig.patch.set_facecolor('#0a0a0a')

colors = ['#FF44AA', '#FF8800', '#FFCC00']

ax1.plot(t, total, color='#00FF88', lw=2.0, label='Total')
ax1.plot(t, hum, color='#00F5FF', lw=1.2, alpha=0.6, label='Hum')
for i, knot in enumerate(knots):
    ax1.plot(t, knot, color=colors[i], lw=1.5, alpha=0.7, label=f'Knot {i+1}')
ax1.axvline(0.0, color='#FFAA00', ls='--', lw=1.2)
ax1.set_title('TimeWave with Multi-Echo', color='white')
ax1.set_ylabel('Amplitude', color='white')
ax1.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white', ncol=2)
ax1.tick_params(colors='white')
ax1.grid(alpha=0.15)

ax2.plot(t, sum(echoes), color='#FFFF44', lw=2.0, label='Combined Echoes')
for i, echo in enumerate(echoes):
    ax2.plot(t, echo, color=colors[i], lw=1.5, alpha=0.7)
ax2.axvline(0.0, color='#FFAA00', ls='--', lw=1.2)
ax2.set_title('Multi-Knot Back-Propagated Echoes', color='white')
ax2.set_xlabel('Time (0 = Snag)', color='white')
ax2.set_ylabel('Amplitude', color='white')
ax2.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white')
ax2.tick_params(colors='white')
ax2.grid(alpha=0.15)

for ax in [ax1, ax2]:
    for s in ax.spines.values():
        s.set_color('white')

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=120, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close('all')
gc.collect()

print(f"Saved to: {png_path}")
