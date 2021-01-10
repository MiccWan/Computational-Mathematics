import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.array([
    x[0] * np.log(x[0]) + x[1] * np.log(x[1]) + 0.3,
    x[0] ** 4 + x[1] ** 2 - 1
])

J = lambda x: np.array([
    [np.log(x[0]) + 1, np.log(x[1]) + 1],
    [4 * (x[0] ** 3), 2 * x[1]]
])

def newtonSystem(f, J, x0, max_iter = 40, threshold = 10 ** (-10)):
    xs = [x0]
    x = x0
    for i in range(max_iter):
        x = x + np.linalg.solve(J(x), -f(x))
        if np.linalg.norm(f(x)) < threshold:
            return x
    print(xs)
    return None

ans = newtonSystem(f, J, np.array([1, 0.1]))

print(ans, f(ans))

ans = newtonSystem(f, J, np.array([0.1, 1]))

print(ans, f(ans))
