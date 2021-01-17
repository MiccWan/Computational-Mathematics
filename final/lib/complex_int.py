import numpy as np
from scipy import integrate

def complex_integrate(f, a, b, verbose=False):
    #  f(z) * dz = f(z(t)) * (z2-z1) * dt
    z = b - a

    def real_f(t):
        p = (t * b + a * (1-t))
        return np.real(f(p) * z)

    def imag_f(t):
        p = (t * b + a * (1-t))
        return np.imag(f(p) * z)
    real_int = integrate.quad(real_f, 0, 1)
    imag_int = integrate.quad(imag_f, 0, 1)

    if verbose:
        print(f'error: {real_int[1]} {imag_int[1]}')

    return real_int[0] + 1j*imag_int[0]