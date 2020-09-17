n = int(input())

primeTable = [False] + [True] * n
for i in range(2, int(n ** 0.5) + 1):
    if primeTable[i]:
        for j in range(i * i, n + 1, i):
            primeTable[j] = False
            
print(' '.join([str(x) for x in range(2, n + 1) if primeTable[x]]))