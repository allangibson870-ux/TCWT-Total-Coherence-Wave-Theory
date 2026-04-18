import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def generate_tau_hopfion():
    fig = plt.figure(figsize=(14, 8), facecolor='black')
    
    # 1. Mass Wall (Top Left) - Complex Q=3 Toroid
    ax1 = fig.add_subplot(2, 3, 1, projection='3d')
    ax1.set_facecolor('black')
    u, v = np.meshgrid(np.linspace(0, 2*np.pi, 80), np.linspace(0, 2*np.pi, 80))
    R, r = 3, 1
    # Adding Q=3 topological deformation
    X = (R + r * np.cos(v)) * np.cos(u)
    Y = (R + r * np.cos(v)) * np.sin(u)
    Z = r * np.sin(v + 2*np.sin(3*u)) # Triple twist 
    ax1.plot_surface(X, Y, Z, cmap='inferno', alpha=0.7, linewidth=0, antialiased=True)
    ax1.set_title("Q=3 Tau Mass Wall", color='white')
    ax1.axis('off')

    # 2. Chiral Twist (Top Center) - Extreme Spiral Flow
    ax2 = fig.add_subplot(2, 3, 2, projection='3d')
    ax2.set_facecolor('black')
    z_s = np.linspace(-2, 2, 300)
    theta_s = np.linspace(0, 12 * np.pi, 300) # 6 Full rotations for Tau energy
    ax2.plot(np.cos(theta_s), np.sin(theta_s), z_s, color='orange', lw=1.5)
    ax2.plot(-np.cos(theta_s), -np.sin(theta_s), z_s, color='deepskyblue', lw=1.5)
    ax2.set_title("High-Energy Phase Spiral", color='white')
    ax2.axis('off')

    # 3. Energy Levels (Top Right) - Dense Spinor Stack
    ax3 = fig.add_subplot(2, 3, 3, projection='3d')
    ax3.set_facecolor('black')
    u_d, r_d = np.meshgrid(np.linspace(0, 2*np.pi, 40), np.linspace(0, 2, 15))
    X_d, Y_d = r_d * np.cos(u_d), r_d * np.sin(u_d)
    # 6 Levels representing the Tau's deep energy well
    for h in [2, 1.2, 0.4, -0.4, -1.2, -2]:
        ax3.plot_surface(X_d, Y_d, h * np.ones_like(X_d), color='cyan' if h > 0 else 'orange', alpha=0.1)
    ax3.set_title("Tau Multi-Branch States", color='white')
    ax3.axis('off')

    # 4. Zero-Mode Braid (Bottom) - The Hyper-Knot
    ax4 = fig.add_subplot(2, 1, 2, projection='3d')
    ax4.set_facecolor('black')
    t = np.linspace(0, 2*np.pi, 600)
    # Q=3 Cinquefoil-style knot
    xk = (3 + np.cos(5*t)) * np.cos(2*t)
    yk = (3 + np.cos(5*t)) * np.sin(2*t)
    zk = np.sin(5*t)
    ax4.plot(xk, yk, zk, color='white', lw=6, alpha=0.9)
    
    # Hum fluctuation background
    pts = np.random.uniform(-7, 7, (1000, 3))
    ax4.scatter(pts[:,0], pts[:,1], pts[:,2], c='violet', s=0.5, alpha=0.15)
    ax4.set_title("Tau Zero-Mode: Q=3 Hyper-Braided State", color='white', fontsize=16)
    ax4.axis('off')

    plt.tight_layout()
    plt.show()

generate_tau_hopfion()
