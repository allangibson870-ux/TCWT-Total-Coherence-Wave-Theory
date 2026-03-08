import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, random, getpass
from datetime import datetime

# Capture source code
try:
    with open(__file__, 'r') as f:
        SCRIPT_CODE = f.read()
except:
    SCRIPT_CODE = "Source capture failed."

# --- PARAMETERS ---
K_TC = 1.91          # Our Universal Constant
THRESHOLD = 1.5      # The edge of the "Quantum Island"
SCREEN_RES = 500     # Number of pixels on the screen
x = np.linspace(-10, 10, SCREEN_RES)

def simulate_pattern(mass, velocity):
    """Calculates the screen pattern based on TCWT Resonance"""
    # 1. Calculate Total Temporal Distortion (Omega)
    omega = mass + (K_TC * velocity)
    
    # 2. Determine Resonance (Coherence)
    # If Omega is low, resonance is high (Quantum Wave)
    # If Omega is high, resonance is low (Classical Particle)
    coherence = np.exp(-(omega / THRESHOLD)**4) # Sharp transition at the threshold
    
    # 3. Wave Pattern (Interference)
    # Standard double-slit interference: cos^2(x) * envelope
    interference = (np.cos(1.5 * x)**2) * np.exp(-0.1 * x**2)
    
    # 4. Classical Pattern (Two Blobs)
    # Sum of two Gaussians behind the slits
    classical = np.exp(-0.5 * (x-2)**2) + np.exp(-0.5 * (x+2)**2)
    
    # 5. The TCWT Result: A mix based on manifold resonance
    return (coherence * interference) + ((1 - coherence) * classical)

# --- EXECUTION: THREE SCENARIOS ---
# 1. Quantum Electron (Low Mass, Low Speed)
pattern_a = simulate_pattern(0.1, 0.2) 

# 2. Classical Molecule (High Mass, Low Speed)
pattern_b = simulate_pattern(1.8, 0.1)

# 3. Relativistic Particle (Low Mass, High Speed)
pattern_c = simulate_pattern(0.1, 0.8)

# --- FILE MANAGEMENT ---
win_user = os.popen("powershell.exe '$env:UserName'").read().strip() or getpass.getuser()
ts = datetime.now().strftime('%Y-%m-%d_%H%M')
outdir = f"/mnt/c/Users/{win_user}/Downloads/{ts}_TCWT_Double_Slit"
os.makedirs(outdir, exist_ok=True)

# --- GRAPHING ---
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(x, pattern_a, color='blue', label='Quantum (Low M, Low V)')
plt.title("TCWT Double Slit: Resonant Wave Pattern")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(x, pattern_b, color='red', label='Classical (High Mass)')
plt.title("TCWT Double Slit: Mass-Induced Decoherence")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(x, pattern_c, color='darkorange', label='Classical (Relativistic Speed)')
plt.title("TCWT Double Slit: Velocity-Induced Decoherence")
plt.legend()

plt.tight_layout()
plt.savefig(f"{outdir}/double_slit_results.png")

# --- README ---
readme_content = f"""# TCWT Double Slit Simulation

## The Hypothesis:
In Temporal Curvature Wave Theory, wave-particle duality is a function of manifold resonance. 
Interference patterns are only visible when the particle is "In Tune" with the eternal wave.

## The Formula:
**Total Distortion ($\Omega$) = Mass + ({K_TC} * Velocity)**

- If $\Omega$ < {THRESHOLD}: The manifold is resonant. The particle behaves as a **Wave**.
- If $\Omega$ > {THRESHOLD}: The manifold is distorted. The particle behaves as a **Classical Object**.

## Results in this Run:
1. **Top Graph (Blue)**: Low Mass/Velocity. $\Omega$ is low. You see the fringes of the "Small World."
2. **Middle Graph (Red)**: High Mass. $\Omega$ is high. The "Temporal Curvature" (Gravity) breaks the resonance.
3. **Bottom Graph (Orange)**: High Velocity. $\Omega$ is high. The "Doppler Shift" tunes the observer out of resonance.
"""

with open(f"{outdir}/README.md", "w") as f:
    f.write(readme_content)

with open(f"{outdir}/tcwt_double_slit.py", "w") as f:
    f.write(SCRIPT_CODE)

print(f"Double Slit Simulation Complete. Check Downloads/{ts}_TCWT_Double_Slit")
