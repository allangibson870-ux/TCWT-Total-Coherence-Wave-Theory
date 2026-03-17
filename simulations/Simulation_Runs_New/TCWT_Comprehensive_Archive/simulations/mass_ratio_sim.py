import numpy as np
import matplotlib.pyplot as plt

def run_mass_ratio():
    a0 = 1e-4; GM_b = 1.0
    r = np.logspace(1, 5, 500)
    a_n = GM_b / r**2
    a_tcwt = np.sqrt(a_n**2 + (a_n * a0))
    ratio = (a_tcwt * r**2 - GM_b) / GM_b
    
    plt.figure(figsize=(10, 6))
    plt.loglog(r, ratio, color='magenta', lw=2)
    plt.title('TCWT Emergent Dark Matter: Mass Ratio vs. Distance')
    plt.ylabel('Mp / Mb'); plt.xlabel('Distance r')
    plt.grid(True, which="both", alpha=0.3)
    plt.savefig('mass_ratio_plot.png')

if __name__ == "__main__":
    run_mass_ratio()
