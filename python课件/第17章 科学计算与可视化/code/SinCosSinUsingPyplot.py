import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 500)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x*x)
#create figure
plt.figure(1)
#create three axes
#first line,first column
ax1 = plt.subplot(2,2,1)
#first line,second column
ax2 = plt.subplot(2,2,2)
#the whole second line
ax3 = plt.subplot(2,1,2)
#choose ax1
plt.sca(ax1)
#draw the curve in ax1
plt.plot(x,y1,color='red')
plt.ylim(-1.2,1.2)
#choose ax2
plt.sca(ax2)
plt.plot(x,y2,'b--')
plt.ylim(-1.2,1.2)
#choose ax3
plt.sca(ax3)
plt.plot(x,y3,'g--')
plt.ylim(-1.2,1.2)

plt.legend()
plt.show()
