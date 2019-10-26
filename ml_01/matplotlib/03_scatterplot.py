import matplotlib.pyplot as plt
import numpy as np

N = 500
x = np.random.rand(N)
y = np.random.rand(N)
colors = [[0,0,0]]
area = np.pi*3

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Scatter plot')
plt.ylabel('y')
plt.xlabel('x')
plt.show()
