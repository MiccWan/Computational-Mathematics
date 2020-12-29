import numpy as np

s = input()

def getPi(k):
    x = 2 * k + 1
    for i in reversed(range(1, k + 1)):
        x = i*i/x + (2 * i - 1)
    return 4 / x


eps = float(input())
k = 0
while abs(np.pi - getPi(k)) >= eps:
    k += 1

print(k)

# print(getPi(20))
