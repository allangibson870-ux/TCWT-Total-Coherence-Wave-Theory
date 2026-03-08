import matplotlib.pyplot as plt
from tcwt_engine.engine import TCWTParameters, TCWTEngine
from gr_baseline import GRBaseline

# --- Run the TCWT engine ---
params = TCWTParameters(
    phi_initial=1e-2,
    phi_prime_initial=0.0,
    phi_mass=10.0,            # big increase → strong restoring force
    upsilon_breaking=0.02,   # reduce damping further
    thread_interaction=0.3,  # reduce coupling friction
)
engine = TCWTEngine(params)

hist = engine.run(t_final=1.0, n_steps=5000)
gr = GRBaseline()
gr_hist = gr.run(t_final=1.0, n_steps=5000)
t = hist["t"]

# --- Create figure ---
plt.figure(figsize=(12, 10))

# --- Scale factor ---
plt.subplot(3, 2, 1)
plt.plot(t, hist["a"], label="TimeWave")
plt.plot(gr_hist["t"], gr_hist["a"], "--", label="GR")
plt.title("Scale Factor a(t)")
plt.xlabel("t")
plt.ylabel("a")
plt.legend()


# --- Hubble rate ---
plt.subplot(3, 2, 2)
plt.plot(t, hist["H"], label="TimeWave")
plt.plot(gr_hist["t"], gr_hist["H"], "--", label="GR")
plt.title("Expansion Rate H(t)")
plt.xlabel("t")
plt.ylabel("H")
plt.legend()


# --- Knot amplitude ---
plt.subplot(3, 2, 3)
plt.plot(t, hist["phi"])
plt.title("TimeWave Knot φ(t)")
plt.xlabel("t")
plt.ylabel("phi")

# --- Knot velocity ---
plt.subplot(3, 2, 4)
plt.plot(t, hist["phi_dot"])
plt.title("TimeWave Motion φ̇(t)")
plt.xlabel("t")
plt.ylabel("phi_dot")

# --- Matter density ---
plt.subplot(3, 2, 5)
plt.plot(t, hist["rho_matter"], label="TimeWave")
plt.plot(gr_hist["t"], gr_hist["rho_m"], "--", label="GR")
plt.title("Matter Density ρ_matter(t)")
plt.xlabel("t")
plt.ylabel("rho_matter")
plt.legend()


# --- Dark sector density ---
plt.subplot(3, 2, 6)
plt.plot(t, hist["rho_dark"])
plt.title("Dark Sector Density ρ_dark(t)")
plt.xlabel("t")
plt.ylabel("rho_dark")

plt.tight_layout()
plt.savefig("/mnt/c/Users/allan/Downloads/tcwt_plot.png", dpi=200)



