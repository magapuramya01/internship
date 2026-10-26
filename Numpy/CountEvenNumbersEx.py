import numpy as np

arr = np.array([10, 15, 20, 25, 30, 35])

count = np.sum(arr % 2 == 0)

print("Even numbers count:", count)