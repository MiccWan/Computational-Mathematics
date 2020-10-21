import numpy as np

def backsub(U, b):
    n = len(b)
    x = np.zeros((n, 1))

    for i in range(n-1, -1, -1):
        s = U[i, i+1:] @ x[i+1:]
        x[i] = (b[i] - s) / U[i, i]

    return x

x_exact = np.ones((5, 1))
alpha = 0.1
b = np.array([alpha, 0, 0, 0, 1])

def getA(k):
    beta = 10**k
    return np.array([
        [1, -1, 0, alpha - beta, beta],
        [0, 1, -1, 0, 0],
        [0, 0, 1, -1, 0],
        [0, 0, 0, 1, -1],
        [0, 0, 0, 0, 1]
    ])


eps = float(input())
k = 0
while np.linalg.norm(backsub(getA(k), b) - x_exact, 2) < eps:
    k += 1

print(k - 1)
