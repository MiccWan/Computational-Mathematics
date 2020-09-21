n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        s = ' '.join([(' ' * (n - j) + '*' * (2 * j - 1) + ' ' * (n - j))]*i)
        pad = ' ' * ((2 * n * n - len(s)) >> 1)
        print(pad + s + pad)
