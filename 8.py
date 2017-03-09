from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-1,1, 0.01)
Y = np.arange(-1,1, 0.01)
X, Y = np.meshgrid(X, Y)
T = 0
#https://en.wikipedia.org/wiki/Rosenbrock_function
#Z = -((1 + np.cos(12 * np.sqrt(X**2 + Y**2))) / (0.5*(X**2 + Y**2) + 2))
#Z = -X * np.sin(np.sqrt(np.abs(X)) - Y * np.sin(np.sqrt(np.abs(Y))))
Z= np.abs(X)**2 + np.abs(Y)**3
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_stern,
                       linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
