import numpy as np


def FDJacob(f, x0, f0, delta=10 ** -6):
    # suit for m * n matrix
    m = f0.shape[0]
    n = x0.shape[0]
    I = np.eye(n)
    J = np.zeros((m, n))
    for j in range(n):
        J[:, j] = (f(x0 + delta * I[:, j]) - f0) / delta

    return J


def levenberg(f, x0, max_iter=10000, tol=10 ** (-12)):
    # only for squre matrix
    xs = [x0]
    fs = [f(x0)]
    lamb = 1
    I = np.eye(x0.shape[0])
    A = FDJacob(f, xs[0], fs[0])
    for i in range(max_iter):
        lamb = 0.01 * i

        s = np.linalg.solve(A.T @ A + lamb * I, -(A.T @ fs[-1]))
        x_new = xs[-1] + s
        f_new = f(x_new)


        if np.linalg.norm(f_new) < np.linalg.norm(fs[-1]):
            # accepted
            lamb *= 0.1
            A = A + (f_new - fs[-1] - A@s) @ s.T / (s.T @s)
            xs.append(x_new)
            fs.append(f_new)
            if np.linalg.norm(f_new) < tol:
                return xs, fs
        else:
            lamb *= 4
            A = FDJacob(f, xs[-1], fs[-1])

    print('max_iter reached')
    print(xs[-20:])
    print(fs[-20:])
    return None, None

# ###########################################################################
#  test
# ###########################################################################


def f(x): return np.array([
    x[0] * x[1] + x[1] ** 2 - 1,
    x[0] + x[1] ** 3 + x[0] ** 2 * x[1] ** 2 + 1
])


xs, fs = levenberg(f, np.array([-2, 1]))

print(xs[-1], fs[-1])
