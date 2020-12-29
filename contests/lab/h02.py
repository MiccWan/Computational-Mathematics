import numpy as np
x0, x1 = [float(x) for x in input().split(' ')]


def f(x):
    x = np.array(x, dtype=float)
    y = x.copy()
    x_nonzero = x[x != 0]
    y[x != 0] = x_nonzero*np.log(np.abs(x_nonzero)) - x_nonzero
    return y

# your code


def find_root_range(f, x0, x1, th=1e-2):
    if np.abs(x0-x1) < th:
        return x0, x1
    else:
        x2 = (x0 + x1) / 2
        f0 = f(x0)
        f2 = f(x2)
        if f0 * f2 < 0:
            return find_root_range(f, x0, x2, th)
        else:
            return find_root_range(f, x2, x1, th)


def secant_method(f, x0, x1, max_iter=40, eps=1e-12):
    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)
        x = -f0 * (x1 - x0) / (f1 - f0) + x0
        x0 = min(x1, x)
        x1 = max(x1, x)
        if np.abs(x0-x1) < eps:
            break

    return x

a, b = find_root_range(f, x0, x1)
r = secant_method(f, a, b)
# your code

print(round(r, 5))
