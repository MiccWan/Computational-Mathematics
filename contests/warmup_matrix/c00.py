import numpy as np

n = int(input())
fab_mat = np.array([[1, 1], [1, 0]])
print(np.linalg.matrix_power(fab_mat, n)[0, 1])