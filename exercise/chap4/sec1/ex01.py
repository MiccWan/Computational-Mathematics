import numpy as np
import matplotlib.pyplot as plt

# from scipy.optimize import fsolve
from scipy.optimize import brentq

f = lambda x: x * x - np.exp(-x)

f_ = lambda x: 2*x + np.exp(-x)

xs = np.arange(-2, 2, 0.01)
ys = [f(x) for x in xs]
plt.plot(xs, ys)
plt.plot(xs, [0 for i in xs])
plt.show()

# ans = fsolve(f, 0)
ans = brentq(f, -2, 2)

print('ans', ans)

cond = 1 / f_(ans)

print('cond', cond)