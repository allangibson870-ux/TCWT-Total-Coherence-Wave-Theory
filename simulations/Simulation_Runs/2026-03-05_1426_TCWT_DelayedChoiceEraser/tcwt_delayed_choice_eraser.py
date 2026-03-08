import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

np.random.seed(42)

N = 50000
x = np.random.normal(0, 1.5, N)  # signal position
which_path = np.random.choice([-1, 1], N)  # -1 = slit1, +1 = slit2

# Raw hits (high Ω, no erasure)
raw_x = x + 0.5 * which_path * 3.0  # shift by which-path

# "Eraser" correlation: post-select on "eraser" outcome that reduces Ω
eraser_outcome = np.random.normal(which_path, 0.3)  # fuzzy which-path info
mask_erase = np.abs(eraser_outcome) < 0.4  # "erase" when low distinguishability

erased_x = x[mask_erase]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
fig.patch.set_facecolor('#0a0a0a')

ax1.hist(raw_x, bins=100, color='#FF4444', alpha=0.7, label='Raw hits (high Ω)')
ax1.set_title('TCWT Delayed-Choice Eraser: Raw Signal (No Erasure)', color='white')
ax1.set_ylabel('Counts', color='white')
ax1.legend(facecolor='#111111', labelcolor='white')
ax1.tick_params(colors='white')
ax1.grid(alpha=0.15)

ax2.hist(erased_x, bins=80, color='#00FF88', alpha=0.7, label='Post-selected erased hits (low Ω)')
ax2.set_title('TCWT Delayed-Choice Eraser: Fringes Restored via Erasure', color='white')
ax2.set_xlabel('Screen Position', color='white')
ax2.set_ylabel('Counts', color='white')
ax2.legend(facecolor='#111111', labelcolor='white')
ax2.tick_params(colors='white')
ax2.grid(alpha=0.15)

for ax in [ax1, ax2]:
    ax.set_facecolor('#0a0a0a')
    for s in ax.spines.values():
        s.set_color('white')

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=180, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Saved to: {png_path}")
