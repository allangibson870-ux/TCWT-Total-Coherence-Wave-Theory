import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

t = np.linspace(0, 1e-6, 500)  # short time scale

# Ω spike for macroscopic object (~10^27 degrees of freedom)
omega_macro = 1e10 * t**2  # rapid rise
visibility = np.exp(-omega_macro)

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(t*1e6, visibility, color='#FF8800', lw=2.5, label='Superposition Visibility')
ax.set_title('TCWT: Macroscopic Superposition Decoherence (Schrödinger Cat)', color='white')
ax.set_xlabel('Time (microseconds)', color='white')
ax.set_ylabel('Visibility of Superposition', color='white')
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
