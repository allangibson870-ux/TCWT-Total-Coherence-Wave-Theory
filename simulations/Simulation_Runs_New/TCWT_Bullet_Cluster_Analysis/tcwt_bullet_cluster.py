import numpy as np
import matplotlib.pyplot as plt

def simulate_bullet_cluster():
    # Grid setup
    x = np.linspace(-5, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)

    # 1. Baryonic Gas (Red): Slowed by Ghost Leakage
    # Position shifted slightly back (-0.5) due to interaction
    gas_pos = [-0.5, 0]
    gas_density = np.exp(-((X - gas_pos[0])**2 + (Y - gas_pos[1])**2) / 1.5)

    # 2. TCWT Lensing Peak (Blue): The Hum Gradient zip-ahead
    # Position moved ahead (+1.0) as it is a coherent phase-wave
    lens_pos = [1.0, 0]
    lens_signal = np.exp(-((X - lens_pos[0])**2 + (Y - lens_pos[1])**2) / 2.0)

    # Visualization
    plt.figure(figsize=(10, 6))
    
    # Plot the Lensing (Blue) - Emergent Gravity
    plt.contour(X, Y, lens_signal, levels=8, colors='cyan', alpha=0.8, label='TCWT Lensing Peak')
    
    # Plot the Gas (Red) - Visible Matter
    plt.contourf(X, Y, gas_density, levels=20, cmap='Reds', alpha=0.6)
    
    plt.title('TCWT Bullet Cluster Simulation: Phase-Lag Separation')
    plt.xlabel('Distance (Mpc)')
    plt.ylabel('Distance (Mpc)')
    
    # Add Legend items manually
    import matplotlib.lines as mlines
    blue_line = mlines.Line2D([], [], color='cyan', label='Lensing (Phase-Gradient Peak)')
    red_patch = mlines.Line2D([], [], color='red', marker='s', markersize=10, ls='', label='Baryonic Gas (Ghost-Leakage Slowdown)')
    plt.legend(handles=[blue_line, red_patch])
    
    plt.grid(True, alpha=0.2)
    plt.savefig('tcwt_bullet_cluster_plot.png')

if __name__ == "__main__":
    simulate_bullet_cluster()
