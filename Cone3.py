from pylab import *
#import time
import numpy as np
import matplotlib.pyplot as plt

z = np.arange(0, 1, 0.02)
theta = np.arange(0, 2 * pi + pi / 50, pi / 50)

fig = plt.figure()
axes1 = fig.add_subplot(111, projection='3d')
for zval in z:
    x = zval * np.array([cos(q) for q in theta])
    y = zval * np.array([sin(q) for q in theta])
    axes1.plot(x, y, -zval, 'b-')
axes1.set_xlabel("x label")
axes1.set_ylabel("y label")
axes1.set_zlabel("z label")

plt.show()

