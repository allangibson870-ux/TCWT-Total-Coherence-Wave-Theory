#!/bin/bash
echo "--------------------------------------------------"
echo "GENERATING TCWT 3D VORTEX: THE ASCENSION SPIRAL"
echo "--------------------------------------------------"

python3 << 'PYTHON_EOF'
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(2026, 2150, 1000)

# Define the "Squeeze" towards 2112
# Frequency as the vertical growth (Z)
z_freq = np.where(t < 2112, 1 / (2112 - t + 5), 0.5 * np.exp(0.005 * (t-2112)))

# Information Leakage as the Spiral Radius (R)
r_info = np.where(t < 2112, 0.1 * np.exp(0.03 * (t - 2080)), 0.7)

# Create the "Hum" (The rotation)
theta = 15 * np.pi * (t - 2026) / (2150 - 2026)
x = r_info * np.cos(theta)
y = r_info * np.sin(theta)

fig = plt.figure(figsize=(12, 10), facecolor='black')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')

# Plot the Spiral (The Path of the Civilization)
# Color changes from Green (Material) to Gold (Information) to Blue (Ascended)
ax.plot(x, y, z_freq, color='#1F51FF', linewidth=2, alpha=0.8, label='The Ascension Vector')

# Highlight the 2112 Breach Point as a Flare
breach_idx = np.abs(t - 2112).argmin()
ax.scatter([x[breach_idx]], [y[breach_idx]], [z_freq[breach_idx]], color='white', s=200, label='2112 Breach Event')

ax.set_title('TCWT 3D Vector: The Ascension Vortex', color='white', fontsize=15)
ax.set_axis_off() # Let the geometry speak for itself

plt.legend(facecolor='black', labelcolor='white')
plt.savefig('tcwt_3d_ascension_vortex.png')
PYTHON_EOF

echo "--------------------------------------------------"
echo "SUCCESS: Check tcwt_3d_ascension_vortex.png"
echo "--------------------------------------------------"
