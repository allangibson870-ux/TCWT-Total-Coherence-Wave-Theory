# ============================================================
# Compute phase and its gradient
# ============================================================
psi_total = psi_up + psi_dn
theta = np.angle(psi_total)

# Finite differences for ∇θ
dtheta_dx = (np.roll(theta, -1, axis=0) - np.roll(theta, 1, axis=0)) / (2*dx)
dtheta_dy = (np.roll(theta, -1, axis=1) - np.roll(theta, 1, axis=1)) / (2*dx)
dtheta_dz = (np.roll(theta, -1, axis=2) - np.roll(theta, 1, axis=2)) / (2*dx)

# Phase gradient magnitude
lambda_grad = np.sqrt(dtheta_dx**2 + dtheta_dy**2 + dtheta_dz**2)

# ============================================================
# Compare λ to the cap
# ============================================================
lambda_cap = np.max(lambda_grad)   # or your theoretical cap value

# Normalized for plotting
lambda_norm = lambda_grad / lambda_cap
rho_norm = rho / rho.max()

# ============================================================
# 1D slice for visualization
# ============================================================
iz = grid_size // 2
iy = grid_size // 2

rho_1d = rho_norm[:, iy, iz]
lam_1d = lambda_norm[:, iy, iz]

import matplotlib.pyplot as plt

plt.figure(figsize=(10,4))
plt.plot(rho_1d, label="Density ρ(x)")
plt.plot(lam_1d, label="Phase Gradient λ(x)")
plt.axhline(1.0, color='red', linestyle='--', label="λ_cap")
plt.legend()
plt.title("Phase Gradient Reaches Cap Where Density Peaks")
plt.xlabel("x")
plt.ylabel("Normalized Value")
plt.tight_layout()
plt.show()
