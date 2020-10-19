import math

eps = float(input())

n1 = 0
n2 = 0

a = [1]
i = 0
while True:
    i += 1
    a.append(a[-1] + (-5) ** i / math.factorial(i))
    if abs(a[-1] - a[-2]) < eps:
        n1 = i
        break

b = [1]
i = 0
while True:
    i += 1
    b.append(b[-1] + 5 ** i / math.factorial(i))
    if (1/b[-2] - 1/b[-1]) < eps:
        n2 = i
        break


print(n1, n2)
