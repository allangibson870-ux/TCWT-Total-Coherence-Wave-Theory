import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def create_hopfion_visualization():
    fig = plt.figure(figsize=(16, 10), facecolor='black')
    
    # 1. Mass Wall (Top Left) - Toroidal Topological Domain Wall
    ax1 = fig.add_subplot(2, 3, 1, projection='3d')
    ax1.set_facecolor('black')
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, 2 * np.pi, 100)
    U, V = np.meshgrid(u, v)
    R, r = 3, 1
    X = (R + r * np.cos(V)) * np.cos(U)
    Y = (R + r * np.cos(V)) * np.sin(U)
    Z = r * np.sin(V)
    ax1.plot_surface(X, Y, Z, cmap='gist_heat', alpha=0.8, antialiased=True)
    ax1.set_title("Mass Wall / Topological Domain Wall", color='white')
    ax1.axis('off')

    # 2. Chiral Twist Operator (Top Center) - Spiral Gradient Flow
    ax2 = fig.add_subplot(2, 3, 2, projection='3d')
    ax2.set_facecolor('black')
    z = np.linspace(-2, 2, 100)
    r_spiral = 1.0
    theta_spiral = np.linspace(0, 4 * np.pi, 100)
    x_spiral = r_spiral * np.cos(theta_spiral)
    y_spiral = r_spiral * np.sin(theta_spiral)
    ax2.plot(x_spiral, y_spiral, z, color='orange', lw=3)
    ax2.plot(-x_spiral, -y_spiral, z, color='deepskyblue', lw=3)
    ax2.set_title("Chiral Twist Operator: Spiral Gradient Flow", color='white')
    ax2.axis('off')

    # 3. Two-Component Spinor (Top Right) - Spin-Up / Spin-Down States
    ax3 = fig.add_subplot(2, 3, 3, projection='3d')
    ax3.set_facecolor('black')
    u_disk = np.linspace(0, 2*np.pi, 50)
    r_disk = np.linspace(0, 2, 20)
    U_d, R_d = np.meshgrid(u_disk, r_disk)
    X_d = R_d * np.cos(U_d)
    Y_d = R_d * np.sin(U_d)
    ax3.plot_surface(X_d, Y_d, np.ones_like(X_d), color='cyan', alpha=0.3)
    ax3.plot_surface(X_d, Y_d, -np.ones_like(X_d), color='orange', alpha=0.3)
    ax3.set_title("Two-Component Spinor: Up/Down Components", color='white')
    ax3.axis('off')

    # 4. Zero-Mode Density (Bottom Center) - Unified Phase-Knotted Core
    ax4 = fig.add_subplot(2, 1, 2, projection='3d')
    ax4.set_facecolor('black')
    t = np.linspace(0, 2*np.pi, 200)
    x_k = np.sin(t) + 2*np.sin(2*t)
    y_k = np.cos(t) - 2*np.cos(2*t)
    z_k = -np.sin(3*t)
    ax4.plot(x_k, y_k, z_k, color='white', lw=4, alpha=0.9)
    # Adding background star-like field particles
    pts = np.random.uniform(-5, 5, (500, 3))
    ax4.scatter(pts[:,0], pts[:,1], pts[:,2], c='orange', s=1, alpha=0.5)
    ax4.set_title("Zero-Mode Density: Bound Hopfion State", color='white', fontsize=15)
    ax4.axis('off')

    plt.tight_layout()
    plt.show()

create_hopfion_visualization()
