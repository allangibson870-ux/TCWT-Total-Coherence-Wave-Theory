import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# Time in years
years = np.linspace(2020, 2150, 1000)

# Staggered breach times
breach_times = [2112, 2125, 2135, 2145]
breach_colors = ['#FF4444', '#FF8800', '#FFCC00', '#44FF88']

# Baseline flux
flux = np.ones_like(years)

# Apply successive drops
for i, t_breach in enumerate(breach_times):
    mask = years >= t_breach
    drop_factor = 0.2 ** (i + 1)
    flux[mask] *= (1 - drop_factor)

# Pre-Breach small oscillations
flux += 0.02 * np.sin(2 * np.pi * (years - 2020) / 11.0)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(years, flux, color='#00FF88', lw=2.5, label='Observed Flux (normalized)')

for i, t in enumerate(breach_times):
    ax.axvline(t, color=breach_colors[i], ls='--', lw=1.5, alpha=0.7,
               label=f'Stage {i+1} Breach ({t})' if i == 0 else f'Stage {i+1} ({t})')

ax.set_xlabel('Year', color='white')
ax.set_ylabel('Normalized Observed Flux', color='white')
ax.set_title('TCWT Fermi Shadow: Multi-Stage Cascade', color='white')
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
