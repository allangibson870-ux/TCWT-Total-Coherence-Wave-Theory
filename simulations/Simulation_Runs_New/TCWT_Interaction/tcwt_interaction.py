import numpy as np
import matplotlib.pyplot as plt

def simulate_interaction():
    # TCWT Parameters
    kappa = 1.455
    R_crit = 0.086
    Theta0 = 1.65
    
    # Grid setup (2D space)
    x = np.linspace(-0.5, 0.5, 300)
    y = np.linspace(-0.5, 0.5, 300)
    X, Y = np.meshgrid(x, y)

    # Positions of two knots (separated by distance D)
    pos1 = [-0.15, 0]
    pos2 = [0.15, 0]

    # Individual Knot Profiles
    theta1 = Theta0 * np.exp(-((X - pos1[0])**2 + (Y - pos1[1])**2) / (2 * R_crit**2))
    theta2 = Theta0 * np.exp(-((X - pos2[0])**2 + (Y - pos2[1])**2) / (2 * R_crit**2))
    
    # Total Phase Field (Superposition)
    theta_total = theta1 + theta2
    
    # Calculate Phase Gradient (Force Field)
    grad_x, grad_y = np.gradient(theta_total)
    grad_mag = np.sqrt(grad_x**2 + grad_y**2)

    # Visualization
    plt.figure(figsize=(12, 5))

    # Plot 1: Phase Field Superposition
    plt.subplot(1, 2, 1)
    plt.contourf(X, Y, theta_total, levels=50, cmap='viridis')
    plt.colorbar(label='Phase Amplitude $\\theta$')
    plt.title('Hum Phase Superposition (Two Knots)')
    plt.scatter([pos1[0], pos2[0]], [pos1[1], pos2[1]], color='white', s=10, label='Knot Centers')
    
    # Plot 2: Gradient Intensity (Gravitational Potential Wells)
    plt.subplot(1, 2, 2)
    plt.contourf(X, Y, grad_mag, levels=50, cmap='magma')
    plt.colorbar(label='Gradient Magnitude $|\nabla \\theta|$')
    plt.title('Phase-Bleed Acceleration Field')
    
    plt.tight_layout()
    plt.savefig('tcwt_interaction_map.png')

if __name__ == "__main__":
    simulate_interaction()
