import numpy as np

a = np.array([
    [4, 2],
    [3, 1]
])

det = np.linalg.det(a)

print("Determinant:", det)