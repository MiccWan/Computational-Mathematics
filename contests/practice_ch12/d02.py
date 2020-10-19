import numpy as np

name, year = input().split(' ')
year = int(year)

nameToIndex = {
    "U": 0,
    "C": 1,
    "G": 2
}

Y = np.array([
    [227.225,  984.736, 78.298],
    [249.623, 1148.364, 79.380],
    [282.172, 1263.638, 82.184],
    [308.282, 1330.141, 81.644]
])

y = Y[:, nameToIndex[name]]
A = np.vander([0, 10, 20, 30])
x = np.linalg.solve(A, y)

pred = np.polyval(x, year - 1980)
print(int(pred))
