import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Time axis: dimensionless post-BB time
# t = 0   -> Big Bang
# t = 1.0 -> far future (knot effectively gone)
t_pre  = np.linspace(-2.0, 0.0, 800)
t_post = np.linspace(0.0, 1.0, 1600)
t      = np.concatenate([t_pre, t_post])

# Define "now" in observable, dimensionless time
t_now = 0.7  # today: knot weakened but clearly non-zero

# Background hum (baryonic / visible sector)
bg_amp  = 0.05
bg_freq = 6.0 * np.pi
bg      = bg_amp * np.sin(bg_freq * t)

# Knot mode: tight near 0, loosening after, out of phase (dark sector)
knot_freq  = 20.0 * np.pi
knot_phase = np.pi / 2.0

# Envelope: grows towards 0- (winding up), decays after 0+ (loosening)
env_pre  = np.exp(4.0 * (t_pre - t_pre.max()))
env_pre  /= env_pre.max()

env_post = np.exp(-1.5 * t_post)
env_post /= env_post.max()

env = np.concatenate([env_pre, env_post])

# --- Calibrate knot amplitude to match dark sector fraction at t_now ---

# Target energy fractions today
frac_dark   = 0.95
frac_baryon = 0.05

# Target amplitude ratio at t_now: A_knot / A_bg = sqrt(frac_dark / frac_baryon)
target_ratio = np.sqrt(frac_dark / frac_baryon)

# Find index closest to t_now
idx_now = np.argmin(np.abs(t - t_now))
env_now = env[idx_now]

# We want: (knot_amp * env_now) / bg_amp = target_ratio
# => knot_amp = target_ratio * bg_amp / env_now
knot_amp = target_ratio * bg_amp / env_now

knot = knot_amp * env * np.sin(knot_freq * t + knot_phase)

# Total wave = background + knot
total = bg + knot

# Plotting
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(11, 9), sharex=True)
fig.patch.set_facecolor('#0a0a0a')

# Background
ax1.set_facecolor('#0a0a0a')
ax1.plot(t, bg, color='#00F5FF', lw=1.8, label='Background Hum (Visible)')
ax1.axvline(0.0,  color='#FFAA00', lw=1.0, ls='--')
ax1.axvline(t_now, color='#44FF44', lw=1.0, ls='--')
ax1.set_ylabel('Background', color='white')
ax1.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white')
ax1.tick_params(colors='white')
for s in ax1.spines.values():
    s.set_color('white')

# Knot mode
ax2.set_facecolor('#0a0a0a')
ax2.plot(t, knot, color='#FF44AA', lw=1.8, label='Knot Mode (Dark Sector)')
ax2.axvline(0.0,  color='#FFAA00', lw=1.0, ls='--')
ax2.axvline(t_now, color='#44FF44', lw=1.0, ls='--')
ax2.set_ylabel('Knot Mode', color='white')
ax2.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white')
ax2.tick_params(colors='white')
for s in ax2.spines.values():
    s.set_color('white')

# Total wave
ax3.set_facecolor('#0a0a0a')
ax3.plot(t, total, color='#00FF88', lw=2.0, label='Total Timewave (bg + knot)')
ax3.axvline(0.0,  color='#FFAA00', lw=1.0, ls='--')
ax3.axvline(t_now, color='#44FF44', lw=1.0, ls='--')
ax3.set_xlabel('Dimensionless TCWT Time (0 = BB, 1 = far future)', color='white')
ax3.set_ylabel('Total Wave', color='white')
ax3.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white')
ax3.tick_params(colors='white')
for s in ax3.spines.values():
    s.set_color('white')

plt.suptitle(
    'TCWT Two-Component Timewave (Calibrated)\n'
    'Background = Visible (~5%), Knot = Dark Sector (~95%) at t = now',
    color='white'
)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('forever_timewave_two_component.png', dpi=200)
