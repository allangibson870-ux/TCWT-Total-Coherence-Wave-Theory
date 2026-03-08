import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from tcwt_engine import TCWTParameters, TCWTEngine

def run_simulation():
    params = TCWTParameters()
    # Ensuring we use your stable 'Residual Hum' settings
    params.H_baseline = 0.05
    params.residual_hum = 0.04
    params.expansion_push = 0.12
    
    engine = TCWTEngine(params)
    return engine.run(t_final=50.0, n_steps=1000)

def plot_grok_style(hist):
    t = hist['t']
    a = hist['a']
    phi = hist['phi']
    H = hist['H']
    
    win_user = "allan"
    save_path = f"/mnt/c/Users/{win_user}/Downloads/grok_timewave_comparison.png"
    
    # --- GROK'S TWEAKED PLOTTING BLOCK ---
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. Scale Factor (The Gentle Bend)
    axs[0,0].plot(t, a, 'b-', label='Timewave', linewidth=2)
    axs[0,0].plot(t, 1 + 0.05*t, 'k--', label='Linear Reference')
    axs[0,0].set_title("Scale Factor (The Gentle Bend)")
    
    # 2. Knot State (Untangling)
    axs[0,1].plot(t, phi, 'm-', label='Knot State')
    axs[0,1].set_title("Knot State (Untangling)")
    
    # 3. Expansion Rate (H)
    axs[1,0].plot(t, H, 'g-', label='H(t)')
    axs[1,0].set_title("Expansion Rate (H)")
    
    # 4. Dark Sector Density (Comparison)
    axs[1,1].plot(t, np.full_like(t, 0.70), 'k-', label='Dark Sector Baseline')
    axs[1,1].set_title("Dark Sector Density")
    
    for ax in axs.flat: 
        ax.legend()
        ax.grid(True, alpha=0.3)
        
    plt.tight_layout()
    # -------------------------------------
    
    plt.savefig('grok_comparison.png')
    try:
        plt.savefig(save_path)
        print(f"\n🚀 SUCCESS! Grok-styled plots saved to Downloads.")
    except:
        print(f"\n⚠️ Saved locally as grok_comparison.png")

if __name__ == "__main__":
    history = run_simulation()
    plot_grok_style(history)
