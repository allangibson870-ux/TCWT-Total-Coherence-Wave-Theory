import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# Constants
G = 6.67430e-11
P_squeeze = 2.4219e20  # Pa from hydrogen knot

# Masses and typical radii (surface for extended objects, Schwarzschild for BH)
objects = [
    {"name": "Proton",      "mass": 1.67e-27,   "radius": 8.8e-16,   "color": "red",     "marker": "o"},
    {"name": "Human",       "mass": 70,         "radius": 0.5,       "color": "orange",  "marker": "s"},
    {"name": "Earth",       "mass": 5.97e24,    "radius": 6.37e6,    "color": "blue",    "marker": "^"},
    {"name": "Sun",         "mass": 1.99e30,    "radius": 6.96e8,    "color": "yellow",  "marker": "D"},
    {"name": "Black Hole",  "mass": 1.99e30,    "radius": 2.95e3,    "color": "purple",  "marker": "*"},  # solar-mass BH
]

# Distortion Ω at surface = G M² / (4π r⁴ P_squeeze)
distortions = []
for obj in objects:
    M = obj["mass"]
    r = obj["radius"]
    omega = (G * M**2) / (4 * np.pi * r**4 * P_squeeze)
    distortions.append(omega)

# Hum amplitude = exp(-Ω)
hum_amplitudes = [np.exp(-omega) for omega in distortions]

# Plot
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

masses = [obj["mass"] for obj in objects]
names = [obj["name"] for obj in objects]
colors = [obj["color"] for obj in objects]
markers = [obj["marker"] for obj in objects]

ax.semilogx(masses, hum_amplitudes, color='white', lw=2.5, linestyle='-', alpha=0.6)
for m, a, name, col, mk in zip(masses, hum_amplitudes, names, colors, markers):
    ax.scatter(m, a, s=180, color=col, marker=mk, edgecolor='white', linewidth=1.5, label=name)

ax.axhline(1.0, color='lime', linestyle=':', label='No distortion (Hum intact)')
ax.axhline(1e-4, color='red', linestyle='--', label='Hum effectively gone')

ax.set_title('TCWT: Background Hum Distortion Around Varying Masses', color='white', fontsize=16)
ax.set_xlabel('Mass (kg) – log scale', color='white')
ax.set_ylabel('Normalised Hum Amplitude at Surface', color='white')
ax.set_xscale('log')
ax.legend(facecolor='#111111', edgecolor='#444444', labelcolor='white', fontsize=11, loc='lower left')
ax.tick_params(colors='white')
ax.grid(alpha=0.15)

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=220, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Plot saved to: {png_path}")
print("Hum amplitudes at surface:")
for name, a in zip(names, hum_amplitudes):
    print(f"  {name:12}: {a:.3e}")
