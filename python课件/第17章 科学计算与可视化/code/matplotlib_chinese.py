import numpy as np
import pylab as pl
import matplotlib.font_manager as fm

myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf')

t = np.arange(0.0, 2.0*np.pi, 0.01)
s = np.sin(t)
z = np.cos(t)
pl.plot(t, s, label='正弦')
pl.plot(t, z, label='余弦')
pl.xlabel('x-变量', fontproperties='STKAITI', fontsize=24)
pl.ylabel('y-正弦余弦函数值', fontproperties='STKAITI', fontsize=24)
pl.title('sin-cos函数图像', fontproperties='STKAITI', fontsize=32)
pl.legend(prop=myfont)
pl.show()
