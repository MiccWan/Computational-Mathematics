import numpy as np

def backwardSub(A, y):
    x = np.zeros_like(y)
    n = A.shape[0]

    for i in reversed(range(n)):
        x[i] = (y[i] - x[i+1:] @ A[i, i+1:]) / A[i, i]

    return x

# A = np.array([
#     [2, 8, 4],
#     [0, 5, 4],
#     [0, 0, 2]
# ])

# y = np.array([18, 13, 4])

# x = backwardSub(A, y)
# print(x)
# print(A@x)