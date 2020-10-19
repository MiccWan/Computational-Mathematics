import math

eps = float(input())

a = 0.1
b = 0.1
i = -1
while True:
    i += 1
    b *= 10
    a_comp = (b + a) - b
    if abs(a - a_comp) >= eps:
        break


print(i - 1)
