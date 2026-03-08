import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# Physical constants (SI units)
G = 6.67430e-11           # m³ kg⁻¹ s⁻²
hbar = 1.0545718e-34      # J s
m_e = 9.1093837e-31       # kg (electron mass)
e_charge = 1.60217662e-19 # C
epsilon_0 = 8.854187817e-12  # F/m
a0 = 5.29177210903e-11    # Bohr radius (m)

# 1. Squeeze pressure inside the Snag knot
# (from your earlier Phase-2 calculation - typical value used)
SQUEEZE_PRESSURE = 2.4219e20  # J/m³ (Pa)

# 2. Gravitational leakage pressure at Bohr radius
# Effective "gravity" from leakage: p_leakage = (G * m_e²) / (4π a0⁴)
# This is the pressure scale of the residual gravitational field at atomic distance
p_leakage = (G * m_e**2) / (4 * np.pi * a0**4)

# 3. Leakage ratio r = p_leakage / SQUEEZE_PRESSURE
r = p_leakage / SQUEEZE_PRESSURE

# 4. Derived κ = log10(1/r) / 30
kappa = np.log10(1 / r) / 30

# Print key results
print(f"Squeeze pressure inside knot: {SQUEEZE_PRESSURE:.4e} Pa")
print(f"Gravitational leakage pressure at Bohr radius: {p_leakage:.4e} Pa")
print(f"Leakage ratio r: {r:.4e}")
print(f"1/r (order): {1/r:.2e}")
print(f"Derived κ from hydrogen squeeze: {kappa:.3f}")

# Simple plot: leakage suppression vs distance (for visual)
r_dist = np.linspace(0.1 * a0, 10 * a0, 200)
suppression = (a0 / r_dist)**4  # 1/r⁴ fall-off of gravitational pressure
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.semilogy(r_dist / a0, suppression, color='#FF8800', lw=2.5, label='Leakage suppression ~1/r⁴')
ax.axvline(1, color='lime', linestyle='--', label='Bohr radius')
ax.set_title('TCWT: Gravitational Leakage Suppression vs Distance', color='white')
ax.set_xlabel('Distance (Bohr radii)', color='white')
ax.set_ylabel('Relative leakage pressure', color='white')
ax.legend(facecolor='#111111', labelcolor='white')
ax.tick_params(colors='white')
ax.grid(alpha=0.15)

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=180, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Plot saved to: {png_path}")
print(f"Derived κ = {kappa:.3f} (used in non-commuting phase term)")
