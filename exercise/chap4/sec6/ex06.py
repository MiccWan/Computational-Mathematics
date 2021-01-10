import numpy as np

def f(x): return np.array([
    x[0] * x[1] + x[1] ** 2 - 1,
    x[0] + x[1] ** 3 + x[0] ** 2 * x[1] ** 2 + 1
])


def J(x): return np.array([
    [x[1], x[0] + 2 * x[1]],
    [2 * x[0] * x[1] ** 2 + x[1] ** 3, 3 * x[0] * x[1] ** 2 + 2 * x[0] ** 2 * x[1]]
])


def levenberg(f, J, x0, max_iter=1000, tol=10 ** (-12)):
    f0 = f(x0)
    A = J(x0)
    xs = [x0]
    fs = [np.linalg.norm(f0)]
    for i in range(max_iter):
        lamb = 0.01 * i
        xs.append(x0 + np.linalg.solve((A.T @ A + lamb * np.eye(2)), - A.T @ f0))
        fs.append(np.linalg.norm(f(xs[i + 1])))

        if fs[-1] < fs[0]:
            return xs, fs

    print('max_iter reached')
    print(xs[:100])
    print(fs[:100])
    return None, None


xs, fs = levenberg(f, J, np.array([-2, 1]))

print(fs[0], fs[1], fs[0] < fs[1])

for i in range(len(xs)):
    print(f'x_{i + 1} = {xs[i]}, ||f_{i + 1}|| = {fs[i]}')
