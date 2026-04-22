import numpy as np

arr1 = np.ones((3, 3))
arr2 = np.array([[10, 20, 30], [80, 100, 120], [210, 240, 270]])
arr = arr1 * arr2
arr = arr.astype(int)
print(arr)
