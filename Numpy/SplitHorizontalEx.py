import numpy as np

a = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

top, bottom = np.vsplit(a, 2)

print("Top:")
print(top)

print("Bottom:")
print(bottom)