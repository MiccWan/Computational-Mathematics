import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import fsolve

f = lambda x: np.pi + np.sin(x) / 4

xs = [np.pi / 2]
max_iter = 100

for i in range(max_iter - 1):
    x_i = f(xs[i])
    xs.append(x_i)
    if np.log(np.abs(x_i - np.pi)) < -20:
        break

n = len(xs)
xs = np.array(xs)
x_axis = np.arange(0, n, 1)
y_axis = np.log(np.abs(xs - np.pi))
plt.plot(x_axis, y_axis)
plt.show()

log_sigma, c = np.polyfit(x_axis, y_axis, 1)

print('sigma', np.exp(log_sigma))
