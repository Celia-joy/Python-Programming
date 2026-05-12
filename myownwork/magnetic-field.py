import numpy as np
from scipy.integrate import quad

mu0 = 4*np.pi*1e-7
I = 10.0
x = 0.05
a = 0.5

def integrand(y, x):
    r_squared = x**2 + y**2
    sin_phi = x / np.sqrt(r_squared)
    return sin_phi / r_squared

integral, error = quad(integrand, -a, a, args=(x,))
B = (mu0 * I / (4 * np.pi)) * integral
print(f"Integral value : {integral:.6f}")
print(f"Magnetic field B : {B:.8e} Tesla")
print(f"Estimated error : {error:.2e}")
