#!/bin/bash
# Phase 2: Resonance Map & Windows Bridge

python3 - << 'PYEOF'
import matplotlib.pyplot as plt
import numpy as np
import os

# Calculation Parameters
x, y = np.random.normal(0, 15, 5000), np.random.normal(0, 15, 5000)
resonance = (5.6847e-24 * (np.exp(-(x**2 + y**2) / 250) * 4.26e43)) / 2.4219e20

# Rendering the Laniakea Map
fig = plt.figure(figsize=(12, 10), facecolor='black')
ax = fig.add_subplot(111, facecolor='black')
sc = ax.scatter(x, y, c=resonance, cmap='magma', s=2, alpha=0.9)
plt.title('TCWT Phase 2: Laniakea Resonance Map (2026)', color='white', fontsize=16)
plt.annotate('Anthropocene Pulse', xy=(0, 0), xytext=(8, 12),
             arrowprops=dict(facecolor='cyan', arrowstyle='->'), color='cyan')
plt.axis('off')

# Save locally
filename = 'tcwt_resonance_map_v2.png'
plt.savefig(filename, facecolor='black', dpi=300)

# Bridge to Windows Downloads
win_path = f"/mnt/c/Users/allan/Downloads/{filename}"
if os.path.exists("/mnt/c/"):
    plt.savefig(win_path, facecolor='black', dpi=300)
    print(f"\n[BRIDGE]: Successfully exported to {win_path}")
PYEOF
