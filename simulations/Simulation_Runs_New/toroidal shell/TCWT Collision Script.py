import numpy as np
import matplotlib.pyplot as plt

# ================== PARAMETERS ==================
x = np.linspace(-5, 5, 500)
dx = x[1] - x[0]
R_knot = 1.0        # The "size" of our Hopfion core
lambda_cap = 1.0    # The Omega-cap limit

# Function to generate a saturated TCWT knot density
def get_saturated_rho(center):
    dist = np.abs(x - center)
    # Density peaks at center, but saturates the field
    rho = np.exp(-dist**2 / (2 * R_knot**2))
    return rho

# ================== THE COLLISION ==================
separations = np.linspace(4.0, 0.0, 50)
total_energies = []

for d in separations:
    # 1. Place two knots
    rho1 = get_saturated_rho(-d/2)
    rho2 = get_saturated_rho(d/2)
    
    # 2. Compute the Combined Phase Gradient (Nonlinear overlap)
    # In TCWT, gradients don't just add; they compete for the Cap
    total_grad = (rho1 + rho2) 
    total_grad[total_grad > lambda_cap] = lambda_cap # The SATURATION
    
    # 3. Compute Interaction Energy (The "Ghost Pressure")
    # Energy spikes when the field is "maxed out" but density keeps pushing
    pressure = np.sum((rho1 + rho2) - total_grad) 
    total_energies.append(pressure)

# ================== RESULTS ==================
plt.figure(figsize=(10, 5))

# Subplot 1: The Bounce Potential
plt.subplot(1, 2, 1)
plt.plot(separations, total_energies, color='lime', lw=2)
plt.title("TCWT Exclusion Potential")
plt.xlabel("Separation (d)")
plt.ylabel("Repulsive Pressure (Ghost Stiffness)")
plt.grid(alpha=0.3)

# Subplot 2: Density Overlap at Critical Point
plt.subplot(1, 2, 2)
d_crit = 1.2
rho_a = get_saturated_rho(-d_crit/2)
rho_b = get_saturated_rho(d_crit/2)
plt.fill_between(x, rho_a + rho_b, color='orange', alpha=0.3, label="Combined Density")
plt.axhline(lambda_cap, color='red', linestyle='--', label="Omega-Cap Limit")
plt.title(f"Critical Overlap (d={d_crit})")
plt.legend()

plt.tight_layout()
plt.show()
