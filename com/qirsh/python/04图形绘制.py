import math
import matplotlib.pyplot as plt
import numpy as np

# 生成正弦曲线数据

nbSamples = 256
x = np.linspace(-math.pi, math.pi, 256)
y1 = np.sin(x)
y2 = np.cos(x)

# for n in range(nbSamples):
#     ratio = (n + 0.5)/nbSamples
#     x.append(xRange[0] + (xRange[1] - xRange[0]) * ratio)
#     y.append(math.sin(x[-1]))

plt.plot(x, y1, color='g', linewidth=4, linestyle='--', label=r'$y=sin(x)$')
plt.plot(x, y2, '*', markersize=8, markerfacecolor='r', markeredgecolor='k', label=r'$y=cos(x)$')

plt.legend(loc='best')
plt.show()