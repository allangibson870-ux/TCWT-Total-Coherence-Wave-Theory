import numpy as np
import matplotlib.pyplot as plt

def analyze_force():
    # TCWT Parameters
    kappa = 1.455
    a0 = 1.2e-10 # MOND scale for reference
    R_crit = 0.086
    Theta0 = 1.65
    
    # 1D Slice across the Hum field
    r = np.linspace(0.1, 2.0, 500) # Distance from center of a knot
    
    # TCWT Gradient (Acceleration)
    # Derivative of Gaussian: a \propto r * exp(-r^2)
    accel_tcwt = (r / R_crit**2) * Theta0 * np.exp(-r**2 / (2 * R_crit**2))
    
    # Newtonian Reference (1/r^2) scaled for comparison
    newtonian = 0.05 / r**2

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(r, accel_tcwt, label='TCWT Phase-Bleed ($a$)', color='cyan', lw=2)
    plt.plot(r, newtonian, label='Newtonian Limit ($1/r^2$)', color='orange', ls='--')
    
    plt.yscale('log')
    plt.xscale('log')
    plt.title('TCWT Acceleration Scaling: Newtonian vs. Phase-Bleed')
    plt.xlabel('Distance $r$ (log scale)')
    plt.ylabel('Acceleration $a$ (log scale)')
    plt.axhline(y=0.001, color='red', linestyle=':', label='MOND Threshold ($a_0$)')
    plt.legend()
    plt.grid(True, which="both", alpha=0.3)
    plt.savefig('tcwt_force_scaling.png')

if __name__ == "__main__":
    analyze_force()
