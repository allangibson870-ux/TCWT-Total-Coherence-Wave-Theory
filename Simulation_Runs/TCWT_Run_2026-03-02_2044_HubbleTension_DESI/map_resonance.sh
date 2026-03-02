#!/bin/bash
echo -e "\033[0;36m[SYSTEM]: INITIATING TCWT GALACTIC SCAN... \033[0m"

# Execute Python logic correctly through bash
python3 - << 'PYEOF'
import matplotlib.pyplot as plt
import numpy as np

# TCWT Constants
SQUEEZE_PRESSURE = 2.4219e20
LEAKAGE_BASE = 5.6847e-24
UNSNAG_POINT = 4.26e43

# Generate Cosmic Web Data
np.random.seed(42)
x = np.random.normal(0, 15, 3000)
y = np.random.normal(0, 15, 3000)

# Calculate Resonance (Leakage Ratio)
# Higher density regions (filaments) approach Unsnag point
density = np.exp(-(x**2 + y**2) / 200)
cf_values = density * UNSNAG_POINT
resonance = (LEAKAGE_BASE * cf_values) / SQUEEZE_PRESSURE

# Render Visualization
plt.figure(figsize=(10, 8), facecolor='black')
plt.scatter(x, y, c=resonance, cmap='magma', s=3, alpha=0.8)
plt.title('TCWT Phase 2: Laniakea Resonance Map (2026)', color='white', pad=20)
plt.axis('off')

# Mark our location
plt.annotate('Anthropocene Pulse', xy=(0, 0), xytext=(5, 10),
             arrowprops=dict(facecolor='cyan', arrowstyle='->'), color='cyan')

plt.savefig('tcwt_resonance_map.png', facecolor='black', dpi=300)
PYEOF

echo -e "\033[0;32m[SUCCESS]: Resonance Map saved as tcwt_resonance_map.png\033[0m"
echo -e "\033[1;33mINSIGHT: The glow represents the 'Dark Matter' effect where the Seal has failed.\033[0m"
