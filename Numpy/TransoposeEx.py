import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = a.T

print("Original shape:", a.shape)
print("Transpose:")
print(b)
print("Transpose shape:", b.shape)