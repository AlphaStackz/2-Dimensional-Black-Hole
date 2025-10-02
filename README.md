# Relativistic 2-D Black Hole Orbits (Schwarzschild, Equatorial Plane)

This project simulates **general-relativistic** motion of a test particle around a non-spinning (Schwarzschild) black hole in the equatorial plane.  

The integrator reproduces effects like perihelion precession, unstable/stable circular orbits, fly-by deflection, and plunges.

> Implementation language: **Python**. Units use \(G=c=1\).  

---

## Features
- Physically correct **timelike geodesics** in Schwarzschild spacetime (equatorial).
- Integrates \((t,r,\phi,u^r)\) using `scipy.integrate.solve_ivp`.
- Helpers for exact circular-orbit invariants \(E, L\) at chosen radius \(r\).
- Ready-made scenarios: precessing bound orbit, near-plunge, and scattering fly-by.
- Simple plot of trajectory and event horizon \(r=2M\).

---

## Physics Model
Metric factor:
\[
f(r)=1-\frac{2M}{r}
\]

Conserved energy \(E\) and angular momentum \(L\):
\[
u^t=\frac{E}{f(r)},\quad u^\phi=\frac{L}{r^2}
\]

Effective potential:
\[
V_{\text{eff}}(r)=f(r)\left(1+\frac{L^2}{r^2}\right)
\]

Radial dynamics:
\[
\frac{dr}{d\tau}=u^r,\quad \frac{du^r}{d\tau}=-\tfrac12\frac{dV_{\text{eff}}}{dr},\quad
(u^r)^2+V_{\text{eff}}=E^2
\]

Stable circular orbits exist for \(r\ge 6M\) (ISCO at \(6M\)); photon sphere at \(3M\).

---

## Quick Start

### 1) Dependencies
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install numpy scipy matplotlib
