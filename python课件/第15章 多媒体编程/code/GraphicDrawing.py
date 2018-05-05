# -*- coding:utf-8 -*-
# Filename: GraphicDrawing.py
# --------------------
# Function description:
# PyOpenGL demo
# --------------------
# Author: Dong Fuguo
# QQ: 306467355
# Email: dongfuguo2005@126.com
#--------------------
# Date: 2014-12-29
# --------------------

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from PIL import Image

class MyPyOpenGLTest:
    def __init__(self, width = 640, height = 480, title = b'MyPyOpenGLTest'):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        self.window = glutCreateWindow(title)
        glutDisplayFunc(self.Draw)
        glutIdleFunc(self.Draw)
        self.InitGL(width, height)

    #default drawing function
    def Draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(-2.0, 0.0, -8.0)
        #draw 2D graphic, leaving z to be 0
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 3.0, 0.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(2.0, -2.0, 0.0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-2.0, -2.0, 0.0)
        glEnd()
        glTranslatef(2.5, 0.0, 0.0)
        #draw a 3D colored line
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(0.0, 3.0, -1.0)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, 3.0)
        glEnd()
        glutSwapBuffers()
        
    def InitGL(self, width, height):
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glShadeModel(GL_SMOOTH)
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
