# -*- coding:utf-8 -*-
# Filename: TextureMapping.py
# --------------------
# Function description:
# PyOpenGL demo
# --------------------
# Author: Dong Fuguo
# QQ: 306467355
# Email: dongfuguo2005@126.com
#--------------------
# Date: 2014-12-29, Updated on 2016-5-1
# --------------------

import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

class MyPyOpenGLTest:
    def __init__(self, width=640, height=480, title=b'MyPyOpenGLTest'):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        self.window = glutCreateWindow(title)
        glutDisplayFunc(self.Draw)
        #指定键盘事件处理函数
        glutKeyboardFunc(self.KeyPress)
        glutIdleFunc(self.Draw)
        self.InitGL(width, height)
        #绕各坐标轴旋转的角度
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    def KeyPress(self, key, x, y):        
        if key==b'a':
            self.x += 0.3
        elif key==b's':
            self.x -= 0.3
        elif key==b'j':
            self.y += 0.3
        elif key==b'k':
            self.y -= 0.3
        elif key==b'g':
            self.z += 0.3
        elif key==b'h':
            self.z -= 0.3

    #绘制图形
    def Draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        #沿z轴平移
        glTranslate(0.0, 0.0, -5.0)
        #分别绕x,y,z轴旋转
        glRotatef(self.x, 1.0, 0.0, 0.0)
        glRotatef(self.y, 0.0, 1.0, 0.0)
        glRotatef(self.z, 0.0, 0.0, 1.0)

        #开始绘制立方体的每个面，同时设置纹理映射
        #绘制四边形
        glBegin(GL_QUADS)
        #设置纹理坐标
        glTexCoord2f(0.0, 0.0)
        #绘制顶点
        glVertex3f(-1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)

        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)

        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)

        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)

        #结束绘制
        glEnd()
        #刷新屏幕，产生动画效果
        glutSwapBuffers()

    #加载纹理
    def LoadTexture(self):
        img = Image.open('sample_texture.bmp')
        width, height = img.size
        img = img.tobytes('raw', 'RGBX', 0, -1)
        glBindTexture(GL_TEXTURE_2D, glGenTextures(1))
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0, GL_RGBA,
                     GL_UNSIGNED_BYTE,img)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        
    def InitGL(self, width, height):
        self.LoadTexture()
        glEnable(GL_TEXTURE_2D)
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glShadeModel(GL_SMOOTH)
        #背面剔除，消隐
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glEnable(GL_POINT_SMOOTH)
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_POLYGON_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glHint(GL_POINT_SMOOTH_HINT,GL_NICEST)
        glHint(GL_LINE_SMOOTH_HINT,GL_NICEST)
        glHint(GL_POLYGON_SMOOTH_HINT,GL_FASTEST)
        glLoadIdentity()
        gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
    def MainLoop(self):
        glutMainLoop()

if __name__ == '__main__':
    w = MyPyOpenGLTest()
    w.MainLoop()
