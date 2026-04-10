import numpy as np

arr = np.array([1.2, 2.5, 3.8, 4.1])
arr_int = arr.astype("int64")
print(f"Исходный массив: {arr}")
print(f"Тип данных: {arr.dtype}")
print(f"Массив округленных целых чисел: {arr_int}")
print(f"Тип данных: {arr_int.dtype}")
