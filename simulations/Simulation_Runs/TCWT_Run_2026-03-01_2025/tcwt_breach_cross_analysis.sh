#!/bin/bash
echo "--------------------------------------------------"
echo "RUNNING TCWT CROSS-BREACH ANALYSIS"
echo "--------------------------------------------------"

python3 << 'PYTHON_EOF'
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(2026, 2150, 500)

# 1. Frequency Coherence (The "Ascension" Data)
ascended_freq = np.where(t < 2112, 1 / (2112 - t + 5), 0.5 * np.exp(0.005 * (t-2112)))

# 2. Information Flow (The "Crossing" Data)
# We model "Leakage" as information that begins tunneling through the Breach as the Squeeze intensifies
inf_leakage = np.where(t < 2112, 0.1 * np.exp(0.04 * (t - 2080)), 0.8 * (1 - np.exp(-0.05 * (t-2112))))

fig, ax1 = plt.subplots(figsize=(12, 7), facecolor='black')
ax1.set_facecolor('black')

# Primary Axis: Frequency
color_freq = '#1F51FF'
ax1.set_xlabel('Year', color='white')
ax1.set_ylabel('Frequency Coherence', color=color_freq)
ax1.plot(t, ascended_freq, color=color_freq, linewidth=3, label='Ascension Frequency (Blue Line)')
ax1.tick_params(axis='y', labelcolor=color_freq)

# Secondary Axis: Information Crossing
ax2 = ax1.twinx()
color_inf = '#FFD700' # Gold for "Information"
ax2.set_ylabel('Information Crossing Breach (%)', color=color_inf)
ax2.plot(t, inf_leakage, color=color_inf, linestyle='--', linewidth=2, label='Information Leakage (Breach Cross)')
ax2.tick_params(axis='y', labelcolor=color_inf)

plt.axvline(x=2112, color='white', linestyle=':', label='2112 Breach Point')
plt.title('TCWT: Frequency vs. Information Crossing', color='white', fontsize=15)
ax1.grid(True, alpha=0.1)

# Combined Legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, facecolor='black', labelcolor='white', loc='upper left')

plt.savefig('tcwt_breach_cross_comparison.png')
PYTHON_EOF

sync-tcwt
echo "--------------------------------------------------"
echo "SUCCESS: Cross-Breach Analysis is ready!"
echo "--------------------------------------------------"
