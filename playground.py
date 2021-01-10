
#4.6.6 Quasi-Newton Broden Levenberg
#finding Jacobian

import numpy as np

def fdjac(f , x, y):
    delta = 10**(-10)
    m = len(y)
    n = len(x)
    J = np.zeros((m,n))
    I = np.eye(n)
    
    for j in range(n):
        x_delta = x + delta*I[:,j]
        J[:,j] = (f(*x_delta) - y)/delta
        
    return J

f = lambda u,v: np.array([u*v + v**2 -1, u*v**3 + u**2*v**2 + 1])
A = np.array([[1 ,0], [-3,2]])
x = np.array([-2 , 1])
fk = f(*x)
I = np.eye(2)
Lambda = 10

while np.linalg.norm(fk)>10**(-10):
    B = A.T@A + Lambda*I
    z = A.T@fk
    s = -np.linalg.solve(B,z)
    x_new = x + s
    f_new = f(*x_new)
    
    if np.linalg.norm(f_new,2) < np.linalg.norm(fk,2):
        #Newton good
        Lambda = Lambda/10
        print(s.T@s)
        A = A + 1/(s.T@s) * (f_new - fk - A@s)@s.T
        x = x_new
        fk = f_new
        #print(x)
    
    else:
        #steepest descent
        Lambda = Lambda*4
        A = fdjac(f, x, fk)
        
u,v = x
print(x, f(u,v))