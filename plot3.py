import matplotlib.pyplot as plt
import numpy as np

x_ = np.linspace(-10, 10, 1000)
y_ = np.linspace(-10, 10, 1000)

X, Y = np.meshgrid(x_, y_)

radius = 8
disk_mask = (X**2) + (Y**2) < radius ** 2

plt.matshow(disk_mask, cmap='gray', extent=[-10, 10, -10, 10])
plt.show()