n = int(input())

factors = []
i = 2
while i <= n:     
    if n % i == 0:      
        factors.append(i)
        n /= i
    else:
        i += 1

print(' '.join(map(str, factors)))