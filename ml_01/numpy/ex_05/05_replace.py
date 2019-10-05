import numpy as np 

myList = [[1, 2, 3, 4],[3, 4, 5, 6], [5, 6, 7, 8]]
arr = np.array(myList, dtype='float')
arr[1,1] = np.nan # not a number
arr[1,2] = np.inf # infinite

np.nan_to_num(arr, False, -1, -1)
print(arr)
