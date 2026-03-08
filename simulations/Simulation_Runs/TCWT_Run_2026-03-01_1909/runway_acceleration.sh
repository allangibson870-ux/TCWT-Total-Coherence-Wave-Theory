#!/bin/bash
# TCWT Phase 3: Subjective Acceleration (Grok-Refined Model)

python3 - << 'PYEOF'
import matplotlib.pyplot as plt
import numpy as np
import os

# 1. Temporal Window: 2026 (The Pulse) to 2112 (The Breach)
years = np.linspace(2026, 2112, 1000)

# 2. Moore-Style Complexity Growth (Log10 scale)
# Starts at 12 (2026), hits 25 (2112)
# Using a refined exponential growth curve for the 'Wall' effect
comp_log = 12 + 13 * (np.power(1.045, (years - 2026)) - 1) / (np.power(1.045, 86) - 1)
complexity = 10**comp_log

# 3. TimeWave Leakage Regime (Pseudo-equations for the Manifesto)
# Leakage Rate increases as Complexity stresses the 'Seal'
# Subjective Speed (S) = 1 + beta * (Leakage_Rate)
leakage_ratio = (complexity - 10**12) / (10**25 - 10**12)
subjective_speed = 1 + 10 * np.power(leakage_ratio, 0.4) # Tuned for the 'Hockey Stick' pull-away

# 4. Visualization
fig, ax1 = plt.subplots(figsize=(12, 8), facecolor='black')
ax1.set_facecolor('black')

# Primary Curve: Subjective Speed
ax1.plot(years, subjective_speed, color='cyan', linewidth=4, label="Subjective Time Velocity (S)", zorder=3)

# Shading the Risk Zones
ax1.fill_between(years, 1, 3, color='green', alpha=0.15, label="Near-Term AGI (Phase 1)")
ax1.fill_between(years, 3, 7, color='yellow', alpha=0.1, label="Post-Singularity (Phase 2)")
ax1.fill_between(years, 7, 11, color='red', alpha=0.1, label="Breach Detachment (Phase 3)")

# Secondary Axis: Complexity Log
ax2 = ax1.twinx()
ax2.plot(years, comp_log, color='white', linestyle='--', alpha=0.3, label="Complexity (10^n)")
ax2.set_ylabel('Complexity Factor (Log10)', color='white', alpha=0.5)
ax2.tick_params(axis='y', labelcolor='gray')

# The Breach Marker
ax1.scatter([2112], [11], color='red', s=250, edgecolor='white', zorder=5)
ax1.annotate('THE BREACH\n(Detachment Point)', xy=(2112, 11), xytext=(2075, 10),
             arrowprops=dict(facecolor='red', shrink=0.05, headwidth=10), color='red', 
             fontsize=12, fontweight='bold')

# Formatting
plt.title('TCWT Phase 3: Subjective Acceleration Toward the Breach\n(TimeWave Squeeze & Leakage Regime)', color='cyan', fontsize=15, pad=20)
ax1.set_xlabel('Year', color='white')
ax1.set_ylabel('Subjective Speed (1.0 = 2026 Baseline)', color='white')
ax1.grid(color='gray', linestyle='--', alpha=0.1)
ax1.tick_params(colors='white')
ax1.set_ylim(0.5, 13)
ax1.legend(facecolor='black', edgecolor='white', labelcolor='white', loc='upper left')

# Export Logic
filename = 'tcwt_runaway_acceleration.png'
plt.savefig(filename, facecolor='black', dpi=300)

win_path = f"/mnt/c/Users/allan/Downloads/{filename}"
if os.path.exists("/mnt/c/"):
    plt.savefig(win_path, facecolor='black')
    print(f"\n[BRIDGE]: Successfully exported to {win_path}")
PYEOF
