
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_ = np.linspace(-5, 5, 100)
y_ = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x_, y_)

gaussian = np.exp(-((X**2) / 2 + (Y**2) / 2))

fig = plt.figure()

ax = fig.add_subplot(121)
# Show matrix in two dimensions
ax.matshow(gaussian, cmap="jet")

ax = fig.add_subplot(122, projection="3d")
# Show three-dimensional surface
ax.plot_surface(X, Y, gaussian, cmap="jet")
plt.show()