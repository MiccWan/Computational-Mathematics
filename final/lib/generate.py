import numpy as np
from .complex_int import complex_integrate

def generate(h, l, ori_u=0, ori_v=0, du=4, dv=4, step=0.1, verbose=False):
    origin = ori_u + ori_v * 1j

    def phi_to_X(u, v, phi):
        return np.real(complex_integrate(phi, origin, u + v * 1j))

    def phi_x(z):
        return (h(z) * (1 - l(z) ** 2)) / 2

    def phi_y(z):
        return 1j * (h(z) * (1 + l(z) ** 2)) / 2

    def phi_z(z):
        return h(z) * l(z)

    u, v = np.mgrid[ori_u - du:ori_u + du:(2 * du / step) * 1j, ori_v - dv:ori_v + dv:(2 * dv / step) * 1j]
    x = np.zeros_like(u)
    y = np.zeros_like(u)
    z = np.zeros_like(u)
    last_progress = 0
    for i in range(u.shape[0]):
        for j in range(u.shape[1]):
            progress = (i + j/u.shape[1]) / u.shape[0]
            if verbose and progress - last_progress > 0.1:
                print(f'progress: {(progress//0.1) * 10}%')
                last_progress = progress
            x[i, j] = phi_to_X(u[i, j], v[i, j], phi_x)
            y[i, j] = phi_to_X(u[i, j], v[i, j], phi_y)
            z[i, j] = phi_to_X(u[i, j], v[i, j], phi_z)

    if verbose:
        print('progress: 100%!')

    return x, y, z