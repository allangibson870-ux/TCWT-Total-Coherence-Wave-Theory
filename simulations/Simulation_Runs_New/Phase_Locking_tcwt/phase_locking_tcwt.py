import numpy as np
import matplotlib.pyplot as plt
import os

# Ensure output directory exists
os.makedirs("figures", exist_ok=True)

# Grid
N = 400
x = np.linspace(-3, 3, N)
y = np.linspace(-3, 3, N)
X, Y = np.meshgrid(x, y)

# Two knot centres
k1 = (-1.0, 0.0)
k2 = ( 1.0, 0.0)

# Distance fields
r1 = np.sqrt((X - k1[0])**2 + (Y - k1[1])**2)
r2 = np.sqrt((X - k2[0])**2 + (Y - k2[1])**2)

# Phase fields (initially out of sync)
theta1 = np.sin(3*r1) * np.exp(-r1)
theta2 = np.sin(3*r2 + 1.2) * np.exp(-r2)

# Phase-locking blend (simulate synchronisation)
alpha = 0.55
theta_locked = (1-alpha)*theta1 + alpha*theta2

# Plot
plt.figure(figsize=(8,6))
plt.imshow(theta_locked, extent=[-3,3,-3,3], origin='lower', cmap='viridis')
plt.colorbar(label="Phase Amplitude θ")
plt.title("Phase-Locking Between Two TCWT Phase Knots")
plt.xlabel("x")
plt.ylabel("y")

# Save to figures folder
plt.tight_layout()
plt.savefig("figures/phase_locking_tcwt.png", dpi=300)
