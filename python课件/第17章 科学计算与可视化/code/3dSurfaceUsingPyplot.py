import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
x,y = np.mgrid[-2:2:20j, -2:2:20j]
z = 50 * np.sin(x+y)
ax = plt.subplot(111, projection='3d')
ax.plot_surface(x,y,z,rstride=2, cstride=1, cmap=plt.cm.Blues_r)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
