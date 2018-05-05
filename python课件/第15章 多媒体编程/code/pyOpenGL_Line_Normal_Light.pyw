import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class MyPyOpenGLTest:
    #重写构造函数，初始化OpenGL环境，指定显示模式以及用于绘图的函数
    def __init__(self, width = 640, height = 480, title = b'Normal_Light'):
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
        #设置灯光与材质属性
        mat_sp = (1.0, 1.0, 1.0, 1.0)
        mat_sh = [50.0]
        light_position = (-0.5, 1.5, 1, 0)
        yellow_l = (1, 1, 0, 1)
        ambient = (0.1, 0.8, 0.2, 1.0)
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_sp)
        glMaterialfv(GL_FRONT, GL_SHININESS, mat_sh)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, yellow_l)
        glLightfv(GL_LIGHT0, GL_SPECULAR, yellow_l)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
        #启用光照模型
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_DEPTH_TEST)
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
        glTranslatef(-1.5, 2.0, -8.0)                
        #绘制三维图形，三维线段
        glBegin(GL_LINES)
        #设置顶点颜色
        glColor3f(1.0, 0.0, 0.0)
        #设置顶点法向量
        glNormal3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glColor3f(0.0, 1.0, 0.0)
        glNormal3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 3.0)
        glEnd()

        #球
        glColor3f(0.8, 0.3, 1.0)
        glTranslatef(0, -1.5, 0)
        #第一个参数是球的半径，后面两个参数是分段数
        glutSolidSphere(1.0,40,40)
        
        glutSwapBuffers()

    #消息主循环
    def MainLoop(self):
        glutMainLoop()

if __name__ == '__main__':
    #实例化窗口对象，运行程序，启动消息主循环
    w = MyPyOpenGLTest()
    w.MainLoop()
