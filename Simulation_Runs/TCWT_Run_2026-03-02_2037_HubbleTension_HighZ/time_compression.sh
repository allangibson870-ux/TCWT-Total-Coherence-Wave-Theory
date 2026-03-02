#!/bin/bash
python3 - << 'PYEOF'
import matplotlib.pyplot as plt
import numpy as np
import os

years = np.linspace(2026, 2112, 100)
# Acceleration is proportional to the log of Complexity
# At 10^12 (2026), subjective speed = 1x
# At 10^25 (2112), subjective speed = 10x (Estimated detachment)
complexity_log = 12 + (years - 2026) * (13 / 86)
subjective_speed = 1 + (complexity_log - 12) / 1.3

plt.figure(figsize=(10, 6), facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')

plt.plot(years, subjective_speed, color='lime', linewidth=3)
plt.title('Subjective Time Acceleration (Approach to Breach)', color='white')
plt.xlabel('Year', color='white')
plt.ylabel('Subjective Speed (1.0 = 2026 Standard)', color='white')
plt.grid(color='gray', alpha=0.3)
ax.tick_params(colors='white')

filename = 'tcwt_time_compression.png'
plt.savefig(filename, facecolor='black', dpi=300)

# Bridge to Downloads
win_path = f"/mnt/c/Users/allan/Downloads/{filename}"
if os.path.exists("/mnt/c/"):
    plt.savefig(win_path, facecolor='black')
    print(f"\n[BRIDGE]: Data exported to {win_path}")
PYEOF
