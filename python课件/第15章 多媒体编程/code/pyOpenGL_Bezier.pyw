import sys
from math import pi as PI
from math import sin, cos
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class MyPyOpenGLTest:
    #重写构造函数，初始化OpenGL环境，指定显示模式以及用于绘图的函数
    def __init__(self, width = 640, height = 480, title = b'MyPyOpenGLTest'):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        self.window = glutCreateWindow(title)
        #指定绘制函数
        glutDisplayFunc(self.Draw)
        glutIdleFunc(self.Draw)
        self.InitGL(width, height)

    #根据特定的需要，进一步完成OpenGL的初始化
    def InitGL(self, width, height):
        #初始化窗口北京为白色
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        #光滑渲染
        glEnable(GL_BLEND)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_POLYGON_SMOOTH)        
        glMatrixMode(GL_PROJECTION)
        #反走样，也称抗锯齿
        glHint(GL_POINT_SMOOTH_HINT,GL_NICEST)
        glHint(GL_LINE_SMOOTH_HINT,GL_NICEST)
        glHint(GL_POLYGON_SMOOTH_HINT,GL_FASTEST)
        glLoadIdentity()
        #透视投影变换
        gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    #计算三次贝塞尔曲线上指定参数对应的点坐标
    def getBezier(self, P0, P1, P2, P3, t):
        a0 = (1-t)**3
        a1 = 3 * (1-t)**2 * t
        a2 = 3 * t**2 * (1-t)
        a3 = t**3

        x = a0*P0[0] + a1*P1[0] + a2*P2[0] + a3*P3[0]
        y = a0*P0[1] + a1*P1[1] + a2*P2[1] + a3*P3[1]
        z = a0*P0[2] + a1*P1[2] + a2*P2[2] + a3*P3[2]

        return (x, y, z)

    #定义自己的绘图函数
    def Draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        #平移
        glTranslatef(-3.0, 0.0, -8.0)
        #指定三次贝塞尔曲线的4个控制点坐标
        P0 = (-4, -2, -9)
        P1 = (-0.5, 3, 0)
        P2 = (2, -3, 0)
        P3 = (4.5, 2, 0)
        #指定模式，绘制多边形
        glBegin(GL_LINES)
        #设置顶点颜色
        glColor3f(0.0, 0.0, 0.0)
        #绘制多边形顶点
        for i in range(1001):
            t = i/1000.0
            p = self.getBezier(P0, P1, P2, P3, t)
            glVertex3f(*p)
        
        #结束本次绘制
        glEnd()       
        
        glutSwapBuffers()

    #消息主循环
    def MainLoop(self):
        glutMainLoop()

if __name__ == '__main__':
    #实例化窗口对象，运行程序，启动消息主循环
    w = MyPyOpenGLTest()
    w.MainLoop()
