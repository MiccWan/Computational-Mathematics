d = {0: 0, 1: 1}

def fab(n):
    if not n in d:
        d[n] = fab(n-1) + fab(n-2)
    return d[n]

print(fab(int(input())))