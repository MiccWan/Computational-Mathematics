import numpy as np
from lib.complex_int import complex_integrate
from lib.generate import generate
from lib.basic_plot import basic_plot

basic_plot(*generate(lambda z: 1 + z ** 2, lambda z: 1 - z ** 2, du=1, dv=1)) # butterfly, shuriken
basic_plot(*generate(lambda z: 1 - z + z**2, lambda z: 1 + z + z ** 2, du=1, dv=1)) # 
basic_plot(*generate(np.sin, np.cos, du=np.pi, dv=np.pi, step=0.1)) # enneper?
basic_plot(*generate(lambda z: z*np.sin(z), lambda z: z*np.cos(z), du=1, dv=1)) # 
basic_plot(*generate(np.exp, lambda z: np.exp(-z), du=1.5, dv=np.pi, step=0.1))
basic_plot(*generate(lambda z: np.sinh(z), lambda z: np.cosh(z), du=np.pi, dv=np.pi)) # 

basic_plot(*generate(lambda z: 1 - z + z**2, lambda z: 1 + z + z ** 2, du=1, dv=1))