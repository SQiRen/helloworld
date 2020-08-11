import math
import matplotlib.pyplot as plt
nbSamples = 256
xRange = (-math.pi, math.pi)
x, y = [], []
for n in range(nbSamples):
    ratio = (n + 0.5)/nbSamples
    x.append(xRange[0] + (xRange[1] - xRange[0]) * ratio)
    y.append(math.sin(x[-1]))

plt.plot(x,y)
plt.show()