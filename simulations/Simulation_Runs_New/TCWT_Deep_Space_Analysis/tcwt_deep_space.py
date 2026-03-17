import numpy as np
import matplotlib.pyplot as plt

def analyze_deep_space():
    # TCWT & MOND Constants
    a0 = 1e-4  # Scaled up for visibility in the plot window
    GM = 1.0   
    # Extend distance significantly to cross the a0 threshold
    r = np.logspace(0, 5, 1000) 
    
    # 1. Newtonian Limit (1/r^2)
    a_newton = GM / r**2
    
    # 2. TCWT Transition (interpolating to 1/r)
    # This is the "Deep MOND" limit where a -> sqrt(a_newton * a0)
    a_tcwt = np.sqrt(a_newton**2 + (a_newton * a0))

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(r, a_tcwt, label='TCWT Phase-Bleed (Deep Space)', color='cyan', lw=2.5)
    plt.plot(r, a_newton, label='Newtonian Limit ($1/r^2$)', color='orange', ls='--')
    plt.axhline(y=a0, color='red', linestyle=':', label='MOND Threshold ($a_0$)')
    
    plt.yscale('log')
    plt.xscale('log')
    plt.title('TCWT Deep Space Scaling: The MOND Divergence')
    plt.xlabel('Distance $r$ (Log Scale)')
    plt.ylabel('Acceleration $a$ (Log Scale)')
    
    # Annotate the Slopes
    plt.text(10, 1e-3, 'Slope = -2 (Newtonian)', color='orange', rotation=-30)
    plt.text(10**4, 1e-5, 'Slope = -1 (Flat Rotation)', color='cyan', rotation=-15)
    
    plt.legend()
    plt.grid(True, which="both", alpha=0.3)
    plt.savefig('tcwt_deep_scaling.png')

if __name__ == "__main__":
    analyze_deep_space()
