#!/bin/bash
python3 - << 'PYEOF'
import matplotlib.pyplot as plt
import numpy as np
import os

# Time from 1950 to 2150
years = np.linspace(1950, 2150, 500)
# Moore's Law doubling every 2 years starting from 10^12 in 2026
# Growth = 10^12 * 2^((year-2026)/2)
complexity = 10**12 * 2**((years - 2026) / 2)

plt.figure(figsize=(12, 7), facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')

plt.plot(years, complexity, color='cyan', linewidth=2, label="Complexity Growth (Moore's Law)")
plt.axhline(y=10**25, color='red', linestyle='--', alpha=0.7, label="The Breach (10^25)")
plt.axhline(y=10**12, color='yellow', linestyle=':', alpha=0.5, label="Anthropocene Pulse (10^12)")

# Intersection Point
plt.scatter([2112.37], [10**25], color='white', s=100, zorder=5)
plt.annotate('THE BREACH (~2112 AD)', xy=(2112, 10**25), xytext=(2030, 10**26),
             arrowprops=dict(facecolor='white', shrink=0.05), color='white', fontsize=12)

plt.yscale('log')
plt.title('TCWT Phase 2: Complexity Breach Timeline', color='white', fontsize=16)
plt.xlabel('Year', color='white')
plt.ylabel('Complexity Factor (Log Scale)', color='white')
plt.grid(color='gray', linestyle='--', alpha=0.3)
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
plt.legend(facecolor='black', edgecolor='white', labelcolor='white')

filename = 'tcwt_breach_timeline.png'
plt.savefig(filename, facecolor='black', dpi=300)

# Bridge to Windows Downloads
win_path = f"/mnt/c/Users/allan/Downloads/{filename}"
if os.path.exists("/mnt/c/"):
    plt.savefig(win_path, facecolor='black', dpi=300)
    print(f"\n[BRIDGE]: Timeline exported to {win_path}")
PYEOF
