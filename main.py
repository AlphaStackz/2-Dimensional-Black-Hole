import argparse
import math
import sys
import numpy as np
import matplotlib.pyplot as plt

# Try SciPy for robust integration; fall back to RK4 if not present
try:
    from scipy.integrate import solve_ivp
    _HAS_SCIPY = True
except Exception:
    _HAS_SCIPY = False

# Schwarzschild GR:
M = 1.0 # black hole mass in solar masses

def f(r: float) -> float:
    return 1.0 - 2.0 * M / r

def V_eff(r: float, L:float) -> float:
    return f(r) * (1.0 + (L**2) / (r**2))

def dVeff_dr(r: float, L:float) -> float:
    # d/dr [ (1-2M/r) * (1 + L^2/r^2) ]
    term1 = (2.0 * M / r**2) * (1.0 + (L**2) / (r**2))
    term2 = f(r) * (-2.0 * L**2/ r**3)
    return term1 + term2

def geodesic_rhs(tau, y, E, L):
    """
    Y = [t, r, phi, ur]
    """
    t,r,phi, ur = y
    r = max(r,2.0 * M + 1e-9)
    dt_dtau = E / f(r)
    dphi_dtau = L / (r**2)
    dr_dtau = ur
    dur_dtau = -.5 * dVeff_dr(r,L)
    return np.array([dt_dtau, dr_dtau, dphi_dtau, dur_dtau], dtype=float)

