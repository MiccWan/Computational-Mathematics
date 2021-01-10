import numpy as np
import matplotlib.pyplot as plt

# from scipy.optimize import fsolve
from scipy.optimize import brentq

f = lambda x: x * x - np.exp(-x)

f_ = lambda x: 2 * x + np.exp(-x)

def newton(f, f_, x0, x_exact, max_iter = 40, threshold = 10 ** -15):
    rates = []
    x_next = x0
    y_next = f(x_next)
    for i in range(max_iter):
        x = x_next
        y = y_next
        x_next = x  - y / f_(x)
        y_next = f(x_next)
        rates.append(np.abs(x_next - x_exact) / (x - x_exact) ** 2)

        if np.abs(x_next - x) < threshold:
            return x_next, rates
        if np.abs(y_next - y) < threshold:
            return x_next, rates
    
    return None, rates

x_exact = brentq(f, -2, 2)

ans, rates = newton(f, f_, 100, x_exact)
print(rates)

rates = rates[:-2]


plt.plot(range(len(rates)), rates)
plt.show()

print('x_exact\n', x_exact)
print('ans\n', ans)

