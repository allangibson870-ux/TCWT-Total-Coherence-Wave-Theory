import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. Compute total wavefunction and phase
# ============================================================
psi_total = psi_up + psi_dn
theta = np.angle(psi_total)

# ============================================================
# 2. Compute ∇θ using centered finite differences
# ============================================================
dtheta_dx = (np.roll(theta, -1, axis=0) - np.roll(theta, 1, axis=0)) / (2*dx)
dtheta_dy = (np.roll(theta, -1, axis=1) - np.roll(theta, 1, axis=1)) / (2*dx)
dtheta_dz = (np.roll(theta, -1, axis=2) - np.roll(theta, 1, axis=2)) / (2*dx)

lambda_grad = np.sqrt(dtheta_dx**2 + dtheta_dy**2 + dtheta_dz**2)

# ============================================================
# 3. Density
# ============================================================
rho = np.abs(psi_up)**2 + np.abs(psi_dn)**2

# Normalize for plotting
rho_norm = rho / rho.max()
lambda_norm = lambda_grad / lambda_grad.max()   # λ_cap = max value

# ============================================================
# 4. Extract 1D slice (center line)
# ============================================================
iz = grid_size // 2
iy = grid_size // 2

rho_1d = rho_norm[:, iy, iz]
lam_1d = lambda_norm[:, iy, iz]

x = np.arange(grid_size) * dx

# ============================================================
# 5. Extract 2D λ-map slice
# ============================================================
lambda_2d = lambda_norm[:, :, iz]

# ============================================================
# 6. Plot the 4-panel diagnostic
# ============================================================
fig, axs = plt.subplots(1, 4, figsize=(18, 4))

# ---------------- Panel 1: Density ----------------
axs[0].plot(x, rho_1d, color='orange')
axs[0].set_title("1. Density Profile ρ(x)")
axs[0].set_xlabel("x")
axs[0].set_ylabel("Normalized ρ")
axs[0].grid(alpha=0.3)

# ---------------- Panel 2: Phase Gradient ----------------
axs[1].plot(x, lam_1d, color='cyan')
axs[1].set_title("2. Phase Gradient λ(x) = |∇θ|")
axs[1].set_xlabel("x")
axs[1].set_ylabel("Normalized λ")
axs[1].grid(alpha=0.3)

# ---------------- Panel 3: Overlay + Cap ----------------
axs[2].plot(x, rho_1d, color='orange', label="ρ(x)")
axs[2].plot(x, lam_1d, color='cyan', label="λ(x)")
axs[2].axhline(1.0, color='red', linestyle='--', label="λ_cap")
axs[2].set_title("3. Cap Saturation at Density Peak")
axs[2].set_xlabel("x")
axs[2].set_ylabel("Normalized Values")
axs[2].legend()
axs[2].grid(alpha=0.3)

# ---------------- Panel 4: 2D λ-map ----------------
im = axs[3].imshow(lambda_2d, cmap='viridis', origin='lower',
                   extent=[x.min(), x.max(), x.min(), x.max()])
axs[3].set_title("4. 2D Phase Gradient Map λ(x,y)")
axs[3].set_xlabel("x")
axs[3].set_ylabel("y")
plt.colorbar(im, ax=axs[3], fraction=0.046, pad=0.04)

plt.suptitle("Phase-Gradient Saturation Diagnostic (4-Panel)", fontsize=14)
plt.tight_layout()
plt.show()
