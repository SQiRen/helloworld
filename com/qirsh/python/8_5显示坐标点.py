import numpy as np
import  matplotlib.pyplot as plt

x = np.arange(0, 10, 1)
y = 2 * x

for a, b in zip(x, y):
    plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=10)

plt.plot(x, y, 'bo-')
plt.show()