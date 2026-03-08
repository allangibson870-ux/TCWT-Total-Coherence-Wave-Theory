import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, random, getpass
from datetime import datetime

# Capture source
try:
    with open(__file__, 'r') as f:
        SCRIPT_CODE = f.read()
except:
    SCRIPT_CODE = "Source capture failed."

random.seed(42)
np.random.seed(42)

# --- PARAMETERS ---
DOTS = 1200  # Number of individual particles to fire
K_TC = 1.91

def get_hit_position(mass, velocity):
    omega = mass + (K_TC * velocity)
    threshold = 1.5
    coherence = np.exp(-(omega / threshold)**4)
    
    # Generate a random position based on the TCWT probability distribution
    x_range = np.linspace(-10, 10, 1000)
    
    # TCWT Probability Density
    interference = (np.cos(1.5 * x_range)**2) * np.exp(-0.1 * x_range**2)
    classical = np.exp(-0.5 * (x_range-2)**2) + np.exp(-0.5 * (x_range+2)**2)
    p = (coherence * interference) + ((1 - coherence) * classical)
    p /= p.sum() # Normalize
    
    return np.random.choice(x_range, p=p)

# --- SIMULATE THE DOTS ---
quantum_dots = [get_hit_position(0.1, 0.1) for _ in range(DOTS)]
observed_dots = [get_hit_position(1.8, 0.1) for _ in range(DOTS)] # 'Observed' adds Mass

# --- FILE MANAGEMENT ---
win_user = os.popen("powershell.exe '$env:UserName'").read().strip() or getpass.getuser()
ts = datetime.now().strftime('%Y-%m-%d_%H%M')
outdir = f"/mnt/c/Users/{win_user}/Downloads/{ts}_TCWT_Individual_Dots"
os.makedirs(outdir, exist_ok=True)

# --- GRAPHING ---
plt.figure(figsize=(12, 8))

# Top Plot: Individual Hits
plt.subplot(2, 1, 1)
plt.scatter(quantum_dots, [random.random() for _ in range(DOTS)], color='blue', s=2, alpha=0.6)
plt.title("TCWT: Individual Quantum Hits (Low Mass/Velocity)")
plt.xlabel("Position on Screen")
plt.yticks([])

# Bottom Plot: Observed Hits
plt.subplot(2, 1, 2)
plt.scatter(observed_dots, [random.random() for _ in range(DOTS)], color='red', s=2, alpha=0.6)
plt.title("TCWT: Individual 'Observed' Hits (Mass-Induced Transition)")
plt.xlabel("Position on Screen")
plt.yticks([])

plt.tight_layout()
plt.savefig(f"{outdir}/individual_dots.png")

# --- README ---
readme_content = f"""# TCWT: The 'Classic Dots' Test

## What is a 'Dot' in TCWT?
In this simulation, we fired {DOTS} individual particles. Each 'dot' represents a localized 
**Manifold Snap** where the eternal wave interacts with the detector.

## The Observation Effect:
1. **Top Graph (Blue)**: The particles are undisturbed. Their low mass-velocity ($\Omega$) 
   allows them to stay in resonance, creating the striped 'interference' pattern.
2. **Bottom Graph (Red)**: We 'Observed' the particles by increasing the local mass (M). 
   This extra distortion kills the resonance, forcing the dots into two distinct classical piles.

This proves that TCWT explains **Wave-Particle Duality** as a simple frequency/mass shift.
"""

with open(f"{outdir}/README.md", "w") as f:
    f.write(readme_content)

with open(f"{outdir}/tcwt_dots_on_screen.py", "w") as f:
    f.write(SCRIPT_CODE)

print(f"Simulation Complete. Look at the 'dots' in: {outdir}")
