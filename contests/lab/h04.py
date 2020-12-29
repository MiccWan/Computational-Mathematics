import numpy as np

f = lambda x: np.exp(x)
I_f = np.e - 1          # integral from 0 to 1
a, b = [0, 1]

m, n = list(map(int, input().split(',')))


#### your code
def method1(f, a, b, n):
    xs = np.linspace(a, b, num=n)
    x_bars = (xs[1:] + xs[:-1])/2
    h  = xs[1] - xs[0]

    print(x_bars)

    return h * np.sum([f(x_bar) for x_bar in x_bars])

def method2(f, a, b, n):
    xs = np.linspace(a, b, num=n)
    h  = xs[1] - xs[0]

    def I(f, a, b):
        return f(a) + 4 * f((a + b) / 2) + f(b)

    return h / 6 * np.sum([I(f, xs[i], xs[i+1]) for i in range(n-1)])
#### your code


err = 1
if m == 1:
    err = abs(method1(f, a, b ,n) - I_f)
if m == 2:
    err = abs(method2(f, a, b ,n) - I_f)

print(round(np.log10(err),3))
