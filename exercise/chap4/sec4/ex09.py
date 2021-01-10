import numpy as np
import matplotlib.pyplot as plt


f = lambda x: x * np.exp(x) - 2

def iqi(f, x_i, max_iter = 40, threshold = 10 ** (-10)):
    xs = x_i.copy()
    ys = [f(x) for x in xs]
    for i in range(max_iter):
        poly = np.polyfit(ys[-3:], xs[-3:], 2)
        x = np.polyval(poly, 0)
        xs.append(x)
        ys.append(f(x))

        if np.abs(ys[-1]) < threshold:
            return xs
    return None

ans = iqi(f, [4, 5, 6])

print(ans[-1], f(ans[-1]))

# xs = np.linspace(0.1, 4 * np.pi)
# plt.plot(xs, f(xs))
# plt.plot(xs, [0 for x in xs])
# plt.show()