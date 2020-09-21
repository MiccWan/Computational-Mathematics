import sys
eps = sys.float_info.epsilon
print((1 + eps / 2) - 1)
print(1 + (eps / 2 - 1))

print((1 - eps/2) + eps/2)
print((1 + eps/2) - eps/2)
# print(-(eps/2 - 1))
# print(1 + eps / 2)
