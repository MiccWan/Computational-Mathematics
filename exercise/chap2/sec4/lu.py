import numpy as np

def lu(A):
    n = A.shape[0]
    A = np.copy(A)

    L = np.eye(n)

    for j in range(n):
        for i in range(j + 1, n):
            L[i, j] = A[i, j] / A[j, j]
            A[i, j:] = A[i, j:] - A[j, j:] * L[i, j]
    
    # print(L, A)
    # print(L@A)
    return L, A

# A = np.array([
#     [2, 3, 4],
#     [4, 5, 10],
#     [4, 8, 2]
# ])

# lu(A)