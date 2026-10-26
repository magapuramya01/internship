import numpy as np

arr = np.array([10, -5, 20, -10, 30])

arr[arr < 0] = 0

print("Updated array:", arr)