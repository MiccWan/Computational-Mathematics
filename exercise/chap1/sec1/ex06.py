import random
import math

random.seed(12345)


def generateRandomWalk(n=10000):
    x = 0
    for i in range(n):
        x += (random.random() > 0.5) * 2 - 1
    return x

    # l = [0]
    # for i in range(n):
    #     l.append(l[-1] + ((random.random() > 0.5) * 2) - 1)
    # return l


alpha = []
beta = []
times = 10000
n = 10000

for i in range(times):
    x = generateRandomWalk(n)
    alpha.append(x)
    beta.append(abs(x))

print(sum(alpha) / times, sum(beta) / times)

print(0, (2 * n / math.pi) ** (1 / 2))
