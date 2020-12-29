import numpy as np
from numpy.linalg import norm

def QRfact(A, m, n):
    A = A.copy().astype(float)
    Q = np.eye(m)

    for i in range(n):
        z = A[i:m, i]
        v = -np.copy(z)
        v[0] = (-np.sign(z[0]) * norm(z, 2) - z[0])

        if norm(v, 2) == 0:
            continue
        
        v = v / norm(v, 2)

        for j in range(n):
            A[i:m, j] = A[i:m, j] - 2 * (v.T @ A[i:m, j]) * v

        for j in range(m):
            Q[i:m, j] = Q[i:m, j] - 2 * (v.T @ Q[i:m, j]) * v

    return Q.T, np.triu(A)

s = int(input())
np.random.seed(s)
m = np.random.randint(9,12)
n = np.random.randint(6,9)
A = np.random.randint(0,10,(m,n))

Q, R = QRfact(A, m, n)

print(Q@R - A)
print(Q@Q.T)

ans = np.hstack((Q[0,:], R[0,:]))
for a in ans:
    print(round(a, 3),end=' ')
