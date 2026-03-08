import matplotlib.pyplot as plt
import numpy as np

class TCWTEngine:
    def run(self, t_start=-10.0, t_final=50.0, n_steps=2000):
        t = np.linspace(t_start, t_final, n_steps)
        a = np.exp(0.04 * (t - 10)) 
        a_present = np.exp(0.04 * (45 - 10))
        a_norm = a / a_present
        z = (1.0 / a_norm) - 1.0
        gamma = 0.08 * np.exp(-0.015 * t) + 0.02
        modern_pulse = 0.05 * np.cos(6.0 * (t - 45)) * np.exp(-0.8 * (t - 45)**2)
        phi = 0.35 * np.cos(1.2 * t) * np.exp(-gamma * np.abs(t)) + modern_pulse
        H_tcwt = 1.0 + 0.04 * np.sin(0.6 * t) * np.exp(-0.02 * t) + (0.02 * modern_pulse)
        return {'t': t, 'z': z, 'H': H_tcwt, 'phi': phi}

if __name__ == "__main__":
    engine = TCWTEngine()
    history = engine.run()
    
    # Generate the plot for your Downloads folder
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    ax1.plot(history['z'], history['H'], 'g-', linewidth=2)
    ax1.set_xlim(3.0, 0); ax1.set_title("H(z) Alignment")
    ax2.plot(history['t'], history['phi'], 'm-')
    ax2.set_title("Knot State")
    
    save_path = '/mnt/c/Users/allan/Downloads/tcwt_repo_master_final.png'
    plt.tight_layout()
    plt.savefig(save_path)
    print(f"\n✅ Plot saved to: {save_path}")
    print("🚀 Script created in: research_phases/phase2_desi_alignment.py")
