import numpy as np
import matplotlib.pyplot as plt

def analyze_mond_transition():
    # TCWT & MOND Constants
    a0 = 1.2e-10  # MOND acceleration scale (m/s^2)
    GM = 1.0      # Normalized Mass
    r = np.logspace(0, 3, 500) # Distance from 1 to 1000 units
    
    # 1. Pure Newtonian Acceleration (1/r^2)
    a_newton = GM / r**2
    
    # 2. TCWT Phase-Bleed (MOND-Transition)
    # Using the TCWT interpolation: a = sqrt(a_newton * a0) in the weak field
    # We use a smooth transition function
    a_tcwt = np.sqrt(a_newton**2 + (a_newton * a0))

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(r, a_tcwt, label='TCWT Phase-Bleed (with MOND)', color='cyan', lw=2.5)
    plt.plot(r, a_newton, label='Newtonian Limit ($1/r^2$)', color='orange', ls='--')
    plt.axhline(y=a0, color='red', linestyle=':', label='MOND Threshold ($a_0$)')
    
    plt.yscale('log')
    plt.xscale('log')
    plt.title('TCWT Corrected Scaling: Transition to Flat Rotation')
    plt.xlabel('Distance $r$ (log scale)')
    plt.ylabel('Acceleration $a$ (log scale)')
    plt.legend()
    plt.grid(True, which="both", alpha=0.3)
    plt.savefig('tcwt_corrected_scaling.png')

if __name__ == "__main__":
    analyze_mond_transition()
