import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import fsolve
# from scipy.optimize import brentq

f = lambda x: 2 * x - np.tan(x)

f_ = lambda x: 2 - (1 / np.cos(x)) ** 2

xs = np.arange(-0.2, 1.4, 0.01)
ys = [f(x) for x in xs]
plt.plot(xs, ys)
plt.plot(xs, [0 for i in xs])
plt.show()

ans1 = fsolve(f, 0.1)
ans2 = fsolve(f, 1)

print('ans', ans1, ans2)

cond1 = 1 / f_(ans1)
cond2 = 1 / f_(ans2)

print('cond', cond1, cond2)