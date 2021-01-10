import numpy as np
import matplotlib.pyplot as plt

# from scipy.optimize import fsolve
# from scipy.optimize import brentq

f = lambda x: x ** (-2) - np.sin(x)

f_ = lambda x: - 2 * (x ** (-3)) - np.cos(x)

def newton(f, f_, x0, max_iter = 40, threshold = 10 ** (-10)):
    xs = [x0]
    x = x0
    for i in range(max_iter):
        x = x  - f(x) / f_(x)
        xs.append(x)

        if np.abs(f(x)) < threshold:
            return x
    print(xs)
    return None

x0s = [1.5, 2, 3.2, 4, 5, 2 * np.pi]
ans = [newton(f, f_, x0) for x0 in x0s]

print(ans)

# for x0 in x0s:
#     ans = newton(f, f_, x0)
#     print(x0, ans)

xs = np.linspace(0.1, 4 * np.pi)
plt.plot(xs, f(xs))
plt.plot(xs, [0 for x in xs])
plt.show()