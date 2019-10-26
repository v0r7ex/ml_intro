import numpy as np
import matplotlib.pyplot as plt

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.bar(y_pos, performance)
plt.title("Programming language usage")
plt.ylabel("Usage")
plt.xticks(y_pos, objects)
plt.show()