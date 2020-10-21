import math

eps = float(input())

a = 0.1
b = 0.1
i = -1
while abs(a - ((b + a) - b)) < eps:
    i += 1
    b *= 10


print(i - 1)
