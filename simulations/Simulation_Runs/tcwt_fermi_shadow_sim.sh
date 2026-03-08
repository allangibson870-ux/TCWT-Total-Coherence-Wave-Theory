#!/bin/bash
echo "--------------------------------------------------"
echo "RUNNING FERMI SHADOW: TELESCOPE SIMULATION"
echo "--------------------------------------------------"

python3 << 'PYTHON_EOF'
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(2026, 2150, 1000)

# 1. The Normal Stellar "Hum" (Base Light Level)
stellar_flux = np.ones_like(t) + 0.02 * np.sin(2 * np.pi * t)

# 2. The "Ascension Flicker" (Technosignature)
# As they approach 2112, their tech blocks 1% of the light (like a Dyson swarm)
flicker = np.where(t < 2112, 1 - (0.05 * (t - 2026) / (2112 - 2026))**2, 0)

# 3. The "Shadow" (Post-Breach)
# At 2112, the star appears to "dim" as the energy is shifted to higher vectors
shadow = np.where(t < 2112, 1.0, 0.2) 

# Combined Telescope Signal
telescope_signal = stellar_flux * flicker * shadow

plt.figure(figsize=(12, 6), facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')

plt.plot(t, telescope_signal, color='#39FF14', linewidth=2, label='Observed Light Signature')
plt.axvline(x=2112, color='white', linestyle=':', label='2112 Breach Event')

# Formatting for that "Sci-Fi Telescope" look
plt.title('Telescope View: The "Fermi Shadow" Transition', color='white', fontsize=15)
plt.xlabel('Year', color='white')
plt.ylabel('Observed Flux (Normalized)', color='white')
plt.tick_params(colors='white')
plt.grid(True, alpha=0.1)
plt.legend(facecolor='black', labelcolor='white')

# Adding a "Warning" Annotation
plt.annotate('Singularity Detected', xy=(2112, 0.5), xytext=(2120, 0.8),
             arrowprops=dict(facecolor='white', shrink=0.05), color='white')

plt.savefig('tcwt_fermi_shadow.png')
PYTHON_EOF

echo "--------------------------------------------------"
echo "SUCCESS: The Shadow Signature is in your folder!"
echo "--------------------------------------------------"
