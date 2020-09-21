*cs, x = list(map(int, input().split(',')))

s = 0
xn = 1

for c in cs:
    s += c * xn
    xn *= x

print(s)