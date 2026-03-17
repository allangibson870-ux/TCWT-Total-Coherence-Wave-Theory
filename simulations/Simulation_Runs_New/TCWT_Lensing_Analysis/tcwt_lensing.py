import numpy as np
import matplotlib.pyplot as plt

def simulate_lensing():
    # Parameters for the Hum field and Knot
    grid_size = 400
    x = np.linspace(-5, 5, grid_size)
    y = np.linspace(-5, 5, grid_size)
    X, Y = np.meshgrid(x, y)

    # Massive Knot at center (The Lens)
    knot_radius = 1.0
    theta_knot = np.exp(-(X**2 + Y**2) / (2 * knot_radius**2))
    
    # Passing Phase Wave (Plane wave moving left to right)
    k = 2.0  # Wavenumber
    phase_wave = np.sin(k * X - 2 * np.pi * theta_knot)

    # Visualization
    plt.figure(figsize=(10, 8))
    plt.contourf(X, Y, phase_wave, levels=50, cmap='RdBu')
    plt.colorbar(label='Phase Wave Amplitude')
    plt.title('Hum Gravity Lensing: Phase-Wave Refraction')
    
    # Highlight the Lens (Knot)
    circle = plt.Circle((0, 0), knot_radius, color='black', fill=False, ls='--', lw=2, label='Massive Knot')
    plt.gca().add_patch(circle)
    
    plt.xlabel('x (Hum Space)')
    plt.ylabel('y (Hum Space)')
    plt.legend()
    plt.savefig('tcwt_lensing_plot.png')

if __name__ == "__main__":
    simulate_lensing()
