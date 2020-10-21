import numpy as np

import matplotlib.pyplot as plt

def e (x):
    return sum(map(lambda i: x**i/np.math.factorial(i), range(18)))

x = np.linspace(-1, 1, 1001)
y1 = (np.exp(x) - 1) / x
y2 = (e(x) - 1) / x
# plt.plot(x, (y1 - y2)/y1)
plt.plot(x, y1 - y2)
plt.show()