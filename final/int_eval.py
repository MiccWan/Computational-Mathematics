import numpy as np
from lib.complex_int import complex_integrate

complex_integrate(np.exp, 0, +(np.pi + np.pi*1j), verbose=True)