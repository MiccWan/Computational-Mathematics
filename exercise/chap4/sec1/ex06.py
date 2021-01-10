import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import fsolve

f = lambda x: x * np.exp(x)

def f_inverse(y):
    return fsolve(lambda x: f(x) - y, 2)

xs = np.linspace(0, 4, num = 500)
# plt.plot(xs, [f(x) for x in xs])
plt.plot(xs, [f_inverse(x) for x in xs])
plt.plot(xs, [0 for i in xs])
plt.show()

xs = [-1, 0, 1]

print('check inv xs', [f_inverse(f(x)) for x in xs])
