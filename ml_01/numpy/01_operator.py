import numpy as np 

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
is_odd = np.mod(arr, 2) != 0
print(np.extract(is_odd, arr))