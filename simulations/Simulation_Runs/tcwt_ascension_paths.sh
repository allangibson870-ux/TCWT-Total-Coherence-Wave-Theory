#!/bin/bash
echo "--------------------------------------------------"
echo "INITIATING TCWT ASCENSION SIMULATION..."
echo "--------------------------------------------------"

python3 << 'PYTHON_EOF'
import numpy as np
import matplotlib.pyplot as plt

# Time scale: 2026 to 2150
t = np.linspace(2026, 2150, 500)

# Path 1: The "Runaway" (Chaos/Extinction)
runaway = np.where(t < 2112, 1 / (2112 - t + 5), 0.25)

# Path 2: The "Luddite" (The Low-Freq Anchor)
luddite = np.ones_like(t) * (1 / (2112 - 2026 + 5))

# Path 3: The "Ascended" (The Stargate Shift)
ascended = np.where(t < 2112, 1 / (2112 - t + 5), 0.5 * np.exp(0.005 * (t-2112)))

plt.figure(figsize=(12, 7), facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')

plt.plot(t, runaway, color='#FF3131', linestyle='--', alpha=0.6, label='Path 1: The Runaway (Red Line)')
plt.plot(t, luddite, color='#39FF14', linewidth=3, label='Path 2: The Luddite (Green Line)')
plt.plot(t, ascended, color='#1F51FF', linewidth=3, label='Path 3: The Ascended (Blue Line)')

plt.axvline(x=2112, color='white', linestyle=':', label='2112 Breach Point')
plt.title('TCWT Ascension: Frequency Coherence (2026-2150)', color='white', fontsize=15)
plt.xlabel('Year', color='white')
plt.ylabel('Complexity Density / Coherence', color='white')
plt.tick_params(colors='white')
plt.legend(facecolor='black', labelcolor='white')
plt.grid(True, alpha=0.1)
plt.savefig('tcwt_ascension_paths_comparison.png')
PYTHON_EOF

echo "--------------------------------------------------"
echo "DONE: Check tcwt_ascension_paths_comparison.png"
echo "--------------------------------------------------"
