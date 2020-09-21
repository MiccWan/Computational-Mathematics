import numpy as np

n = int(input())
fab_mat = np.array([[1, 1], [1, 0]])
# use this for large integer
# fab_mat = np.array([[1, 1], [1, 0]], dtype='object')
print(np.linalg.matrix_power(fab_mat, n)[0, 1])