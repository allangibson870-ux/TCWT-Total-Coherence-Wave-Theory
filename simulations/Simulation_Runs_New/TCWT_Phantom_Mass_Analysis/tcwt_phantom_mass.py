import numpy as np
import matplotlib.pyplot as plt

def calculate_phantom_mass():
    # Constants
    a0 = 1e-4  # MOND Threshold from previous plot
    GM_baryonic = 1.0
    r = np.logspace(1, 5, 500)
    
    # Accelerations
    a_newton = GM_baryonic / r**2
    a_tcwt = np.sqrt(a_newton**2 + (a_newton * a0))
    
    # Effective 'Observed' Mass: M_obs = a * r^2 / G
    # Since G=1 in our normalized units:
    m_obs = a_tcwt * r**2
    m_phantom = m_obs - GM_baryonic
    
    # Ratio of Dark Matter to Baryonic Matter
    ratio = m_phantom / GM_baryonic

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(r, ratio, color='magenta', lw=2.5, label='Phantom Mass Ratio ($M_p / M_b$)')
    
    plt.xscale('log')
    plt.yscale('log')
    plt.title('TCWT Emergent Dark Matter: Mass Ratio vs. Distance')
    plt.xlabel('Distance $r$ (Log Scale)')
    plt.ylabel('Mass Ratio ($M_{phantom} / M_{baryonic}$)')
    plt.grid(True, which="both", alpha=0.3)
    plt.axvline(x=100, color='red', ls=':', label='MOND Transition Point')
    plt.legend()
    plt.savefig('tcwt_phantom_mass_ratio.png')

if __name__ == "__main__":
    calculate_phantom_mass()
