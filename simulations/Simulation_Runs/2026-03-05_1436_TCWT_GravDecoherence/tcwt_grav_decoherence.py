import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

path_diff = np.linspace(0, 1e-6, 200)  # proper time difference (seconds)
decoh_rate = 1e12 * path_diff**2  # quadratic in GR time dilation
visibility = np.exp(-decoh_rate)

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(path_diff*1e6, visibility, color='#44FF88', lw=2.5, label='Interference Visibility')
ax.set_title('TCWT: Gravitational Decoherence (Path-Dependent Time Dilation)', color='white')
ax.set_xlabel('Proper Time Difference (microseconds)', color='white')
ax.set_ylabel('Visibility', color='white')
ax.legend(facecolor='#111111', labelcolor='white')
ax.tick_params(colors='white')
ax.grid(alpha=0.15)

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=180, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Saved to: {png_path}")
