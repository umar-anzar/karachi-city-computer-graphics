'''
By Muhammad Umar Anzar
'''

import math

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

        # YOUR GLOBAL ATTRIBUTES HERE IN CONSTURCTOR
        self.spiralObj1 = self.spiral(0, 0, 0.01, 4, 0)
        self.spiralObj2 = self.spiral(0, 0, 0.01, 4, 180)

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
        self.r, self.g, self.b, self.a = 10, 50, 10, 1
        # initialize the screen to blueCalls glClearColor (in RGBA mode) 
        glClearColor(self.r/255, self.g/255, self.b/255, self.a/255)  
        #Alternate self.qglClearColor(QColor(r, g, b, a)) 


        gluOrtho2D(-1.0, 1.0,-1.0,1.0)# Specify the max coordinates -x,+x,-y,+y.
        glViewport(10,10,300,400)
        


        #glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA) I think its not working
        self.formatGL()
        
    
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
        
        glPointSize(5.0) #The glPointSize function specifies the diameter of rasterized points
        
        
        glBegin(GL_LINES)

        #glColor3f can be called in between glBegin and glEnd. When it is used this way, it can be used to give each vertex its own color.
        #glColor3f sets R,G,B and A

        # X-AXIS--------------------------------------------------------------------------------
        glColor3f(1.0, 0.0, 0.0) #red

        glVertex2f(-1.0,0)

        glVertex2f(1.0, 0)
        

        # Y-AXIS
        glColor3f(0.0, 1.0, 0.0) #green
        glVertex2f(0, -1.0)
        glVertex2f(0, 1.0)
        glEnd()
        glFlush() #The glFlush function forces execution of OpenGL functions in finite time.
        

        self.spiralObj1.animate(-5)
        self.spiralObj2.animate(5)

    class spiral:
        def __init__(self,x1,y1,radius,spirals,rotate):
            self.x1 = x1
            self.y1 = y1
            self.radius = radius
            self.spirals = spirals
            self.rotate = rotate

        def draw(self):
            radius = self.radius
            glBegin(GL_LINE_STRIP)
            glColor3f(1,0,0)
            n = 360
            t = (2 * math.pi / n )
            for i in range(0+self.rotate, self.rotate+ n*self.spirals):
                x = self.x1 + radius * math.cos(t*i)
                y = self.y1 + radius * math.sin(t*i)
                radius += 0.0005
                glVertex2f(x,y)
            glEnd()
            glFlush()

        def animate(self, rotate):
            self.draw()
            self.rotate += rotate

    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(GLWidget)
    window.show()
    sys.exit(app.exec_())
