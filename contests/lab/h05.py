import numpy as np
s = int(input())
np.random.seed(s)
A = np.random.rand(5,5)
A = A + A.T

lams = []

#### your code
def power_iter(A, max_iter=30):
    x = np.random.randn(5, 1)
    x = x/np.linalg.norm(x)
    
    for _ in range(max_iter):
        y = A@x
        x = y/np.linalg.norm(y)
    
    lam = (x.T @ (A @ x))[0, 0]

    return lam, x

for _ in range(3):
    l, v = power_iter(A)
    lams.append(l)
    A = A - (v @ (A@v).T)
#### your code

ans = ' '.join([ str(round(lam,2)) for lam in lams ])
print(ans)
