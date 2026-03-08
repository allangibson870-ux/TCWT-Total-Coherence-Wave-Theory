import matplotlib.pyplot as plt
import numpy as np

class TCWTParameters:
    def __init__(self):
        self.H_baseline = 0.09 
        self.radiation_freq = 1.2
        self.vls_freq = 0.3
        self.transition_point = 18.0 

class TCWTEngine:
    def __init__(self, params):
        self.p = params

    def run(self, t_final=50.0, n_steps=1000):
        t = np.linspace(0, t_final, n_steps)
        a = np.exp(0.09 * t) 
        w_rad = np.exp(-t / self.p.transition_point)
        w_vls = 1 - w_rad
        phi = (0.5 * np.cos(self.p.radiation_freq * t) * w_rad) + (0.1 * np.sin(self.p.vls_freq * t) * w_vls)
        H = self.p.H_baseline + 0.015 * np.cos(0.8 * t) * np.exp(-0.1 * t)
        return {'t': t, 'a': a, 'phi': phi, 'H': H}

def plot_rad_to_vls(hist):
    t, a, phi, H = hist['t'], hist['a'], hist['phi'], hist['H']
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    
    axs[0,0].plot(t, a, 'b-', label='Timewave')
    axs[0,0].set_title("Scale Factor (The Gentle Bend)")
    
    axs[0,1].plot(t, phi, 'm-', label='Knot State')
    axs[0,1].axvspan(10, 25, color='gray', alpha=0.1, label='Rad-VLS Handover')
    axs[0,1].set_title("Knot State (Transition to VLS)")
    
    axs[1,0].plot(t, H, 'g-', label='H(t)')
    axs[1,0].set_ylim(0.03, 0.11)
    axs[1,0].set_title("Expansion Rate (H)")
    
    axs[1,1].plot(t, np.full_like(t, 0.70), 'k-', label='Dark Sector Baseline')
    axs[1,1].set_ylim(0.67, 0.73)
    axs[1,1].set_title("Dark Sector Density")
    
    for ax in axs.flat: 
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('rad_vls_transition.png')
    print("🚀 Plot saved as 'rad_vls_transition.png'")

if __name__ == "__main__":
    params = TCWTParameters()
    engine = TCWTEngine(params)
    history = engine.run()
    plot_rad_to_vls(history)
