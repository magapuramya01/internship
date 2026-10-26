import numpy as np

a = np.array([
    [10, 30, 90],
    [40, 70, 100],
    [20, 80, 50]
])

print(a[(a >= 20) & (a <= 80)])