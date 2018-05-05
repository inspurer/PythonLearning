from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

#定义绘图指令与控制点坐标
#其中MOVETO表示将绘制起点移动到指定坐标
#CURVE4表示使用4个控制点绘制3次贝塞尔曲线
#CURVE3表示使用3个控制点绘制2次贝塞尔曲线
#LINETO表示从当前位置绘制直线到指定位置
#CLOSEPOLY表示从当前位置绘制直线到指定位置，并闭合多边形
path_data = [
           (Path.MOVETO, (1.58, -2.57)),
           (Path.CURVE4, (0.35, -1.1)),
           (Path.CURVE4, (-1.75, 2.0)),
           (Path.CURVE4, (0.375, 2.0)),
           (Path.LINETO, (0.85, 1.15)),
           (Path.CURVE4, (2.2, 3.2)),
           (Path.CURVE4, (3, 0.05)),
           (Path.CURVE4, (2.0, -0.5)),
           (Path.CURVE3, (3.5, -1.8)),
           (Path.CURVE3, (2, -2)),
           (Path.CLOSEPOLY, (1.58, -2.57)),
          ]
codes, verts = zip(*path_data)
path = Path(verts, codes)
#按指令和坐标进行绘图
patch = PathPatch(path, facecolor='r', alpha=0.9)
ax.add_patch(patch)

# 绘制控制多边形和连接点
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')

#显示网格
ax.grid()
#设置坐标轴刻度大小一致，可以更真实地显示图形
ax.axis('equal')
plt.show()
