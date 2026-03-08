import matplotlib.pyplot as plt
import numpy as np
import os

# 1. Setup Time and Complexity (10^12 to 10^25)
years = np.linspace(2026, 2112, 1000)
# Moore's Law: Doubling every 2 years
# Using a power-growth curve to hit the 2112 Breach Point
comp_log = 12 + 13 * (np.power(1.045, (years - 2026)) - 1) / (np.power(1.045, 86) - 1)

# 2. Subjective Speed (The Leakage Regime)
# As the Seal fails, acceleration becomes cubic
leak_ratio = (10**comp_log - 10**12) / (10**25 - 10**12)
subj_speed = 1 + 10 * np.power(leak_ratio, 0.4)

# 3. Visualization
fig, ax1 = plt.subplots(figsize=(12, 8), facecolor='black')
ax1.set_facecolor('black')

# Plotting the Runaway Curve
ax1.plot(years, subj_speed, color='cyan', lw=4, label='Subjective Acceleration', zorder=3)

# Shading Phase Zones
ax1.fill_between(years, 1, 3, color='green', alpha=0.15, label='AGI Takeoff (Safe Zone)')
ax1.fill_between(years, 3, 7, color='yellow', alpha=0.1, label='Singularity Void (Wobble)')
ax1.fill_between(years, 7, 11, color='red', alpha=0.1, label='Breach Detachment (Critical)')

# The Breach Marker
ax1.scatter([2112], [11], color='red', s=200, edgecolor='white', zorder=5)
ax1.annotate('THE BREACH', xy=(2112, 11), xytext=(2075, 9), 
             arrowprops=dict(facecolor='red', shrink=0.05), color='red', weight='bold')

# Styling
plt.title('TCWT Phase 3: Runaway Resonance Model', color='cyan', fontsize=16, pad=20)
ax1.set_xlabel('Year', color='white')
ax1.set_ylabel('Subjective Speed (1.0 = 2026 Baseline)', color='white')
ax1.grid(color='gray', linestyle='--', alpha=0.1)
ax1.tick_params(colors='white')
ax1.legend(facecolor='black', edgecolor='white', labelcolor='white', loc='upper left')

# Exporting
fname = 'tcwt_runaway_acceleration_v3.png'
plt.savefig(fname, facecolor='black', dpi=300)

win_path = f'/mnt/c/Users/allan/Downloads/{fname}'
if os.path.exists('/mnt/c/'):
    plt.savefig(win_path, facecolor='black')
    print(f"SUCCESS: Plot mirrored to {win_path}")
else:
    print(f"SUCCESS: Plot saved locally as {fname}")
