'''
By Muhammad Umar Anzar
'''

import math
import time

from PyQt5 import QtWidgets
from PyQt5.QtOpenGL import QGLWidget
from PyQt5.QtOpenGL import QGLFormat

#import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#Import PyQtWindow
from PyQtWindow import MainWindow
import sys

class GLWidget(QGLWidget):
    
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(100, 100)
        self.setMouseTracking(False)
        #self.glInit() I think not working

        

    def formatGL(self):
        fmt = QGLFormat()
        #Double Buffering
        fmt.setDoubleBuffer(True)
        QGLFormat.setDefaultFormat(fmt) 

    def initializeGL(self):
        self.once = True


        '''
        Background color, values b/w 0-1 that is why I divided RGB by 255
        '''
        self.r, self.g, self.b, self.a = 35, 39, 42, 1
        # initialize the screen to blueCalls glClearColor (in RGBA mode) 
        glClearColor(self.r/255, self.g/255, self.b/255, self.a/255)  
        #Alternate self.qglClearColor(QColor(r, g, b, a)) 


        gluPerspective(80, (self.width()/self.height()), 0.01, 50.0)
        # gluPerspective(	GLdouble fovy,
        # GLdouble aspect,
        # GLdouble zNear,
        # GLdouble zFar);
        glTranslatef(0.0,0.0, -5)

        # YOUR GLOBAL ATTRIBUTES HERE IN INITIALIZE FUNCTION
        #FPS
        self.current_time = time.time()
        self.last_time = 0
        self.fps = 50
        self.delta_time = 1 / self.fps

        # HELIX VERTEX POINTS
        self.vertex1 = []
        self.vertex2 = []
        n = 360

        #Helix EQUATION
        loops = 10
        for i in range(n+n):
            t = ((loops*math.pi - 0 ) / n ) * i
            x = math.cos(t)
            y = math.sin(t)
            z = 0.01*t
            self.vertex1.append([x,y,z])

        #Torodial Spiral
        R = 6/4
        r = 2/4
        loops = 10
        for i in range(n+n):
            t = ((5*math.pi - 0 ) / n ) * i
            x = (r*math.sin(loops*t)+R)*math.cos(t)
            y = (r*math.sin(loops*t)+R)*math.sin(t)
            z = R*math.cos(loops*t)
            self.vertex2.append([x,y,z])


        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
        self.formatGL()
        glRotatef(140, 1, 0, 0)
        
    
    def resizeGL(self, width, height):
        #Necessary to make the world space resizable as widget size is changed
        glViewport(0, 0, width, height)
        
    def checkingFunction(self):
        if self.once:
            self.once = False
            #If widget is using a double-buffered format, the background and foreground GL buffers will automatically be swapped 
            # after each paintGL() call. The buffer auto-swapping is on by default.
            print("\nStatus\tAttribute")
            print(self.doubleBuffer(),"\tDouble Buffer")
            print(self.autoBufferSwap(),"\tBuffer Swap")


    def paintGL(self):
        self.checkingFunction() #Just to check whether FormatGL is working

        '''
        This is the Draw function where You code OpenGl Graphics
        Here You code Whatever You want to draw on the OpenGl Widget
        '''

        '''
        Example Code
        of X AND Y AXIS
        '''
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #refresh screen : clear color array buffer
        
        glLineWidth(2.0) #The glPointSize function specifies the diameter of rasterized points
        
        


        #glColor3f can be called in between glBegin and glEnd. When it is used this way, it can be used to give each vertex its own color.
        #glColor3f sets R,G,B and A
        glColor3f(0.25, 0.4, 0.88)

        glPointSize(5.0)
        

        glBegin(GL_LINE_STRIP) # GL_LINE_STRIP make continuous line in 3d
        for v in self.vertex1:
            glVertex3fv(v)  #v in 3fv means u can pass array in function
        glEnd()
        glFlush()

        glColor3f(0.823, 0.41, 0.117)

        glBegin(GL_LINE_STRIP) # GL_LINE_STRIP make continuous line in 3d
        for v in self.vertex2:
            glVertex3fv(v)  #v in 3fv means u can pass array in function
        glEnd()
        glFlush()

        
    def animate(self):
        

        glRotatef(0.01, 0, 0, 1)
        
        self.current_time = time.time()
        if (self.current_time - self.last_time >= self.delta_time):
            self.last_time = self.current_time
            self.updateGL()

    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(GLWidget)
    window.show()
    sys.exit(app.exec_())
