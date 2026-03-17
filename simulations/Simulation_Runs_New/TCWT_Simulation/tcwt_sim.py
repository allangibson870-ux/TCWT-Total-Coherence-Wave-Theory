import numpy as np
import matplotlib.pyplot as plt

def simulate_knot():
    # TCWT Parameters
    kappa = 1.455
    Omega_max = 16.91
    R_crit = 0.086
    Theta0 = 1.65
    r = np.linspace(0, 0.5, 200)

    # Phase Knot Profile theta(r)
    theta = Theta0 * np.exp(-r**2 / (2 * R_crit**2))
    
    # Phase Gradient |nabla theta|
    grad_theta = np.abs(- (r / R_crit**2) * theta)

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(r, theta, label='Phase Field $\\theta(r)$', color='blue', lw=2)
    plt.plot(r, grad_theta, label='Phase Gradient $|\\nabla \\theta|$', color='red', ls='--')
    plt.axvline(x=R_crit, color='green', linestyle=':', label='Critical Radius $R_{crit}$')
    plt.title('TCWT Phase-Knot (Matter) Structure')
    plt.xlabel('Radius $r$ (Theory Units)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('tcwt_knot_profile.png')

if __name__ == "__main__":
    simulate_knot()
