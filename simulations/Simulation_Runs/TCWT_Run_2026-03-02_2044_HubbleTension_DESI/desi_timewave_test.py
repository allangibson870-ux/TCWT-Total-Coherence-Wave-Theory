import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../../hubble_tension_data.csv")
z_data = df["redshift"].values
H_lcdm_data = df["H_z_lcdm"].values
H_pred_data = df["H_z_predicted"].values

H_err_now = np.full_like(H_pred_data, 1.5)
H_err_future = H_err_now / 2.0

H0 = 67.4
Omega_m = 0.315
Omega_r = 0.0
Omega_de = 1.0 - Omega_m - Omega_r

w0 = -1.0
wa = 0.0

Aw = float(os.getenv("AW", "0.02"))
Pw = 0.8

def w_of_z(z):
    return w0 + wa * z/(1.0 + z) + Aw * np.sin(2.0 * np.pi * z / Pw)

def E_of_z(z):
    z = np.atleast_1d(z)
    Ez2 = Omega_m * (1.0 + z)**3 + Omega_r * (1.0 + z)**4
    z_grid = np.linspace(0.0, z.max(), 2000)
    w_grid = w_of_z(z_grid)
    integrand = (1.0 + w_grid) / (1.0 + z_grid)
    integral_grid = np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(z_grid))
    rho_de_ratio = np.zeros_like(z)
    for i, zi in enumerate(z):
        idx = np.searchsorted(z_grid, zi)
        if idx == 0:
            I = 0.0
        elif idx >= len(integral_grid):
            I = integral_grid[-1]
        else:
            I = integral_grid[idx-1]
        rho_de_ratio[i] = np.exp(3.0 * I)
    Ez2 += Omega_de * rho_de_ratio
    return np.sqrt(Ez2)

def H_of_z(z):
    return H0 * E_of_z(z)

def E_of_z_lcdm(z):
    z = np.atleast_1d(z)
    Ez2 = Omega_m * (1.0 + z)**3 + Omega_r * (1.0 + z)**4
    z_grid = np.linspace(0.0, z.max(), 2000)
    w_grid = w0 + wa * z_grid/(1.0 + z_grid)
    integrand = (1.0 + w_grid) / (1.0 + z_grid)
    integral_grid = np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(z_grid))
    rho_de_ratio = np.zeros_like(z)
    for i, zi in enumerate(z):
        idx = np.searchsorted(z_grid, zi)
        if idx == 0:
            I = 0.0
        elif idx >= len(integral_grid):
            I = integral_grid[-1]
        else:
            I = integral_grid[idx-1]
        rho_de_ratio[i] = np.exp(3.0 * I)
    Ez2 += Omega_de * rho_de_ratio
    return np.sqrt(Ez2)

def H_of_z_lcdm(z):
    return H0 * E_of_z_lcdm(z)

H_tw_data = H_of_z(z_data)
H_lcdm_model = H_of_z_lcdm(z_data)

delta_H = H_tw_data - H_lcdm_model
R_future = delta_H / H_err_future

chi2_future = np.sum(R_future**2)
max_sigma = np.max(np.abs(R_future))

print("=== TCWT TimeWave vs future-DESI-like test ===")
print(f"w0 = {w0}, wa = {wa}, Aw = {Aw}, Pw = {Pw}")
print(f"chi2 (future-like errors) = {chi2_future:.3f}")
print(f"max |ΔH| / σ_future       = {max_sigma:.3f}")

