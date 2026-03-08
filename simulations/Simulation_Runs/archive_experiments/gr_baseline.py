import numpy as np

class GRBaseline:
    def __init__(self, H0=67.4, rho_m0=1e-5, rho_L=1.0):
        self.H0 = H0
        self.rho_m0 = rho_m0
        self.rho_L = rho_L

    def run(self, t_final, n_steps):
        dt = t_final / n_steps

        t = 0.0
        a = 1.0
        rho_m = self.rho_m0

        history = {"t": [], "a": [], "H": [], "rho_m": [], "rho_L": []}

        for _ in range(n_steps):
            H = np.sqrt(rho_m + self.rho_L)
            rho_m = rho_m - 3 * H * rho_m * dt
            a = a + H * a * dt

            history["t"].append(t)
            history["a"].append(a)
            history["H"].append(H)
            history["rho_m"].append(rho_m)
            history["rho_L"].append(self.rho_L)

            t += dt

        return history

