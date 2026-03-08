import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# Time in Billions of Years (Gyr)
time_gyr = np.linspace(0.5, 30, 300) 
kappa_initial = 1.454

def simulate_cosmic_coherence():
    # Scale factor a(t) for an expanding universe
    # Simple expansion model: a(t) grows over time
    scale_factor = (time_gyr / 13.8)**(2/3) # Matter-dominated approximation
    
    # In TCWT, the "Hum Density" is inversely proportional to the scale factor
    # This causes Kappa to "soften" as the universe thins
    kappa_drift = kappa_initial / (scale_factor**0.5)
    
    # Maximum Coherent Volume (V_max) 
    # V_max is limited by the local Omega saturation threshold
    v_max = 1.0 / (kappa_drift**2)
    return v_max, kappa_drift

v_max_vals, k_drift_vals = simulate_cosmic_coherence()

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#050505')
ax1.set_facecolor('#050505')

# Plot 1: Maximum Coherent Volume
ax1.plot(time_gyr, v_max_vals, color='#00FFCC', lw=3, label='Max Coherent Volume')
ax1.set_xlabel('Time Since Big Bang (Billions of Years)', color='white')
ax1.set_ylabel('Quantum Stability Limit', color='#00FFCC')
ax1.tick_params(axis='y', labelcolor='#00FFCC')

# Plot 2: Kappa Drift (The "Universal Stiffness")
ax2 = ax1.twinx()
ax2.plot(time_gyr, k_drift_vals, color='#FFCC00', lw=2, ls='--', label='Kappa Drift (κ)')
ax2.set_ylabel('Universal Coupling Constant (κ)', color='#FFCC00')
ax2.tick_params(axis='y', labelcolor='#FFCC00')

# Marker for "Now" (13.8 Gyr)
ax1.axvline(13.8, color='white', ls=':', alpha=0.5)
ax1.text(14, 0.5, 'PRESENT DAY', color='white', alpha=0.5)

# Aesthetics
ax1.set_title('TCWT Stress Test: The Evolution of Universal Coherence', color='white', fontsize=16)
ax1.grid(alpha=0.05)
ax1.tick_params(colors='white')

plt.tight_layout()
plt.savefig("tcwt_cosmic_evolution.png", dpi=200, facecolor=fig.get_facecolor())
plt.close()
