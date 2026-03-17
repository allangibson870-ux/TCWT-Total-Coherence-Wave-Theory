import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def simulate_s2_orbit():
    # Constants for Sgr A* and S2 (Normalized Units)
    GM = 1.0
    c = 50.0  # Scaled down speed of light for visualization of precession
    ecc = 0.88
    a = 1.0
    
    # TCWT Correction (Hum-Drag / Saturation Deviation)
    f_sp_gr = 1.0
    f_sp_tcwt = 1.15  # Predicted 'Hum-Drag' deviation

    def equations(w, t, f_sp):
        x, y, vx, vy = w
        r = np.sqrt(x**2 + y**2)
        # Relativistic acceleration (Schwarzschild Precession term)
        # a = -GM/r^2 * (1 + 3L^2 / (c^2 r^2))
        L2 = (x*vy - y*vx)**2
        accel_mag = (GM / r**3) * (1 + f_sp * (3 * L2 / (c**2 * r**2)))
        return [vx, vy, -accel_mag * x, -accel_mag * y]

    # Initial conditions (at pericenter)
    r_peri = a * (1 - ecc)
    v_peri = np.sqrt(GM * (1 + ecc) / r_peri)
    w0 = [r_peri, 0, 0, v_peri]
    
    # Time steps for 5 orbital periods
    t = np.linspace(0, 100, 5000)

    # Solve for GR and TCWT
    sol_gr = odeint(equations, w0, t, args=(f_sp_gr,))
    sol_tcwt = odeint(equations, w0, t, args=(f_sp_tcwt,))

    # Visualization
    plt.figure(figsize=(10, 10))
    plt.plot(sol_gr[:, 0], sol_gr[:, 1], color='orange', lw=1, label='General Relativity (f_sp=1.0)')
    plt.plot(sol_tcwt[:, 0], sol_tcwt[:, 1], color='cyan', lw=1.5, label='TCWT Hum-Drag (f_sp=1.15)')
    
    # Plot the Black Hole (Sgr A*)
    plt.scatter([0], [0], color='black', s=100, label='Sgr A* (Saturated Phase Knot)')
    
    plt.title('S2 Star Orbital Precession: TCWT vs. General Relativity')
    plt.xlabel('Distance (Scaled)')
    plt.ylabel('Distance (Scaled)')
    plt.legend()
    plt.axis('equal')
    plt.grid(True, alpha=0.2)
    plt.savefig('s2_precession_plot.png')

if __name__ == "__main__":
    simulate_s2_orbit()
