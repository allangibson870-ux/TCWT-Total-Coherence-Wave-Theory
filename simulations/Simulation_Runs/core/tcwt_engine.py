import numpy as np
from scipy.integrate import odeint

class TCWTParameters:
    def __init__(self):
        self.H_baseline = 0.05      
        self.hum_freq = 0.8         
        self.knot_initial_phi = 0.5 
        self.sync_damping = 0.2     
        self.expansion_push = 0.1   
        self.residual_hum = 0.08    # STRONGER: The eternal push of time
        # --- BALANCED MATTER ---
        self.M_matter = 0.15        # LIGHTER: Enough to see, not enough to kill
        self.M_dark = 0.70          # Baseline comparison

class TCWTEngine:
    def __init__(self, params):
        self.params = params
        class State: pass
        self.state = State()
        self.state.a = 1.0

    def derivatives(self, y, t):
        a, phi, phi_dot = y
        a_eff = max(a, 0.01) # Safety floor to prevent the 10^15 crash
        
        # 1. The Hum vs The Knot
        hum = np.sin(self.params.hum_freq * t)
        knot = np.sin(self.params.hum_freq * t + phi)
        desync = (hum - knot)**2
        
        # 2. Physics: The Battle
        rho_matter = self.params.M_matter / (a_eff**3)
        push = self.params.H_baseline + (self.params.expansion_push * np.abs(phi)) + self.params.residual_hum
        
        # We use a standard Hubble logic: H = sqrt(Push^2 - Pull^2)
        # This keeps the math stable even when matter is present
        h_squared = (push**2) - (rho_matter * 0.1)
        current_H = np.sqrt(max(h_squared, 0.001))
        
        adot = a_eff * current_H
        phiddot = -self.params.sync_damping * phi_dot - (0.5 * phi)
        
        return [adot, phi_dot, phiddot]

    def run(self, t_final=100.0, n_steps=5000):
        t = np.linspace(0, t_final, n_steps)
        y0 = [self.state.a, self.params.knot_initial_phi, 0.0]
        sol = odeint(self.derivatives, y0, t)
        return {
            't': t, 'a': sol[:, 0], 'phi': sol[:, 1],
            'H': np.gradient(sol[:, 0], t) / sol[:, 0],
            'rho_d': np.full_like(t, self.params.M_matter)
        }
