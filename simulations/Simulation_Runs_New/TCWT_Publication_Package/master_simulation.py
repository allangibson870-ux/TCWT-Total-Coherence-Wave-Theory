import numpy as np
import matplotlib.pyplot as plt

def run_master_sim():
    # Parameters
    a0 = 1e-4
    GM_b = 1.0
    r = np.logspace(1, 5, 1000)
    
    # 1. Deep Space Scaling
    a_n = GM_b / r**2
    a_tcwt = np.sqrt(a_n**2 + (a_n * a0))
    
    # 2. Phantom Mass Ratio
    m_obs = a_tcwt * r**2
    ratio = (m_obs - GM_b) / GM_b

    # Plot 1: Acceleration
    plt.figure(figsize=(10, 5))
    plt.loglog(r, a_tcwt, color='cyan', label='TCWT Phase-Bleed')
    plt.loglog(r, a_n, color='orange', ls='--', label='Newtonian')
    plt.title('TCWT Deep Space Scaling')
    plt.legend(); plt.grid(True, which="both", alpha=0.3)
    plt.savefig('plots/scaling_analysis.png')
    plt.close()

    # Plot 2: Mass Ratio
    plt.figure(figsize=(10, 5))
    plt.loglog(r, ratio, color='magenta', lw=2)
    plt.axvline(x=100, color='red', ls=':', label='MOND Threshold')
    plt.title('TCWT Emergent Dark Matter: Mass Ratio vs. Distance')
    plt.ylabel('Mp / Mb'); plt.xlabel('Distance r')
    plt.legend(); plt.grid(True, which="both", alpha=0.3)
    plt.savefig('plots/mass_ratio_final.png')

if __name__ == "__main__":
    run_master_sim()
