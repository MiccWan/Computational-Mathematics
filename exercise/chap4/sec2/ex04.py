import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import fsolve

def solve(f, x0, max_iter = 100):
    x = x0
    for i in range(max_iter):
        x_next = f(x)
        err = np.abs(x_next - x)
        print(err)
        if err < 10 ** -15:
            return x_next
        else:
            x = x_next
    return None

f = lambda x: (x ** 2 + 3.5) / 4

x1 = solve(f, 1)
x2 = solve(f, 2.5)


xs = np.linspace(1, 3, num=100)
plt.plot(xs, f(xs))
plt.plot(xs, xs)
plt.show()

print(x1, x2)