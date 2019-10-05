import numpy as np

np.random.seed(100)
a = np.random.randint(0, 5, 10)
a_unique = np.full((10), True)
a_unique[np.unique(a, return_index=True)[1]] = False
print(a_unique)
