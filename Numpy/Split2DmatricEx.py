import numpy as np

a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

left, right = np.hsplit(a, 2)

print("Left:")
print(left)

print("Right:")
print(right)