import numpy as np


def getPi(k):
    x = 6
    for i in range(k):
        x = (2 * (k - i) - 1) ** 2 / x + 6
    return x - 3


eps = float(input())
k = 0
while abs(np.pi - getPi(k)) >= eps:
    k += 1

print(k)
