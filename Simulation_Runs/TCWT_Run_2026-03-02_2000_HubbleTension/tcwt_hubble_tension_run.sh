#!/bin/bash
set -e

BASE="$HOME/projects/TCWT-Temporal-Curvature-Wave-Theory/Simulation_Runs"
ROOT="$HOME/projects/TCWT-Temporal-Curvature-Wave-Theory"
RUN_ID="TCWT_Run_$(date +%Y-%m-%d_%H%M)_HubbleTension"
RUN_DIR="$BASE/$RUN_ID"

mkdir -p "$RUN_DIR"

# Copy all .sh and .py scripts from repo root into the run folder
cp "$ROOT"/*.sh "$RUN_DIR"/ 2>/dev/null || true
cp "$ROOT"/*.py "$RUN_DIR"/ 2>/dev/null || true

cd "$RUN_DIR"

python3 << 'PYTHON_EOF'
import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(0, 3.0, 400)

H0_planck = 67.4
H0_local = 73.1
H0_tcwt_base = 73.0

amp = 1.0
period_z = 2.0
damping_scale = 2.5

trend = H0_planck + (H0_tcwt_base - H0_planck) * np.exp(-z / 3.0)
osc = amp * np.exp(-z / damping_scale) * np.sin(2 * np.pi * z / period_z)
H_tcwt = trend + osc

H_local_line = np.full_like(z, H0_local)
H_planck_line = np.full_like(z, H0_planck)

plt.figure(figsize=(10, 6))
plt.plot(z, H_tcwt, color='limegreen', lw=2.5, label='TCWT: Resonant Transition H(z)')
plt.plot(z, H_local_line, 'm--', lw=1.8, label='Local H₀ (SH0ES/Riess ≈ 73.1)')
plt.plot(z, H_planck_line, 'c--', lw=1.8, label='Early H₀ (Planck/CMB ≈ 67.4)')
plt.xlabel('Redshift z')
plt.ylabel('Effective H(z) [km/s/Mpc]')
plt.title('TCWT vs Hubble Tension: Resonant Late-Time Modulation of H(z)')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('tcwt_hubble_tension.png', dpi=200)
PYTHON_EOF

cat << 'README' > README.md
# TCWT – Hubble Tension Simulation Run

This run models H(z) under TCWT as a damped resonant modulation bridging SH0ES and Planck values.

Output: tcwt_hubble_tension.png
README

WIN_DEST="/mnt/c/Users/allan/Downloads"
cp -r "$RUN_DIR" "$WIN_DEST"/
