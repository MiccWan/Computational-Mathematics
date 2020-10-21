from lu import lu
from backwardSub import backwardSub
from forwardSub import forwardSub
import numpy as np

def solve(A, y):
    L, U = lu(A)
    Ux = forwardSub(L, y)
    x = backwardSub(U, Ux)
    return x

A = np.array([
    [2, 3, 4],
    [4, 5, 10],
    [4, 8, 2]
])

y = A @ np.array([4,5,6])

print(solve(A,y))