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
        #初始化窗口背景为白色
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

    #定义自己的绘图函数
    def Draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        #平移
        glTranslatef(-3.0, 2.0, -8.0)
        #绘制二维图形，z坐标为0
        #指定模式，绘制多边形
        glBegin(GL_POLYGON)
        #设置顶点颜色
        glColor3f(1.0, 0.0, 0.0)
        #绘制多边形顶点
        glVertex3f(0.0, 1.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-1.0, -1.0, 0.0)
        #结束本次绘制
        glEnd()
        
        glTranslatef(3, -1, 0.0)
        
        #绘制三维图形，三维线段
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(1.0, 1.0, -1.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 3.0)
        glEnd()

        glTranslatef(-0.3, 1, 0)

        #使用折线段绘制圆
        glBegin(GL_LINE_LOOP)
        n = 100
        theta = 2*PI/n
        r = 0.8
        for i in range(100):
            x = r*cos(i*theta)
            y = r*sin(i*theta)
            glVertex3f(x, y, 0)
        glEnd()
        
        glutSwapBuffers()

    #消息主循环
    def MainLoop(self):
        glutMainLoop()

if __name__ == '__main__':
    #实例化窗口对象，运行程序，启动消息主循环
    w = MyPyOpenGLTest()
    w.MainLoop()
