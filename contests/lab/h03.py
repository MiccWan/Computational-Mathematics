import numpy as np

f = lambda x: np.exp(np.sin(7*x))

# observed points
ob_xs = np.array([0, 0.075, 0.25, 0.55, 0.7, 1])
ob_ys = f(ob_xs)

# input
x = float(input())

#### your code

n = len(ob_ys) - 1
hs = ob_xs[1:] - ob_xs[:-1]

# s(x_k) = y_k => (n)
I = np.eye(n)
Z = np.zeros((n,n))
M1 = np.hstack([I, Z, Z])
ys1 = ob_ys[:-1].reshape(-1,1)

# s(x_{k+1}) = y_{k+1} => (n)
H = np.diag(hs)
M2 = np.hstack([I, H, H**2])
ys2 = ob_ys[1:].reshape(-1,1)

# s_k'(t_{k+1}) = s_{k+1}'(t_{k+1}) => (n-1)
E = np.eye(n-1, n)
J = np.eye(n)
J[:-1, 1:] -= np.eye(n-1)
Z = np.zeros((n,n))

M3 = E @ np.hstack([Z, J, 2*H])
ys3 = np.zeros((n-1, 1))

# s''(t_0) = s''(t_1) => (1)
M4 = np.hstack([np.zeros((1, 2*n)), np.array([[1,-1]]) , np.zeros((1, n-2))] )
ys4 = np.zeros((1,1))

# solve ss
M = np.vstack([M1, M2, M3, M4])
ys = np.vstack([ys1, ys2, ys3, ys4])

ss = np.linalg.solve(M, ys)

# solve y for x
n = len(ob_xs) - 1
for k in range(n):
    if x >= ob_xs[k] and x <= ob_xs[k + 1]:
        a = ss[k, 0]
        b = ss[n+k, 0]
        c = ss[2*n+k, 0]
        t = ob_xs[k]
        y = a + b*(x-t) + c*((x-t)**2)
        break

#### your code

# output
print(round(y, 3))
