import sys

print(float.hex(float(1)))

print(float.hex(float(1 + sys.float_info.epsilon)))

print(float.hex(float(1 + 16 * sys.float_info.epsilon)))

print(float.hex(1+64206*sys.float_info.epsilon))