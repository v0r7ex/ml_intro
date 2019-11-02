import numpy as np
import matplotlib.pyplot as plt

# Create data
N = 60
g1 = (0.6 + 0.6 * np.random.rand(N), np.random.rand(N))
g2 = (0.4+0.3 * np.random.rand(N), 0.5*np.random.rand(N))
g3 = (0.3*np.random.rand(N),0.3*np.random.rand(N))
data = (g1, g2, g3)
colors = ("red", "green", "blue")
groups = ("coffee", "tea", "water")

for data, colors, groups in zip(data, colors, groups):
    x, y = data
    print(x)
    plt.scatter(x, y, c=colors, label=groups)
    plt.legend(loc='best')
    plt.title("Grouped Scatter Plot")

plt.show()