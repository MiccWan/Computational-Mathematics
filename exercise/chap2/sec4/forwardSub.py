import numpy as np

def forwardSub(A, y):
    x = np.zeros_like(y)
    n = A.shape[0]

    for i in range(n):
        x[i] = (y[i] - x[:i] @ A[i, :i]) / A[i, i]

    return x

# A = np.array([
#     [2, 0, 0],
#     [4, 5, 0],
#     [4, 8, 2]
# ])

# y = np.array([4, 13, 18])

# x = forwardSub(A, y)
# print(x)
# print(A@x)