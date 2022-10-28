'''
By Muhammad Umar Anzar
'''
from turtle import pos
from PyQt5 import QtWidgets
from PyQt5.QtOpenGL import QGLWidget
from PyQt5.QtOpenGL import QGLFormat
from PyQt5 import QtGui

#import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#Import PyQtWindow
import PyQtWindow
import sys



class GLWidget(QGLWidget):
    
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(100, 100)
        self.setMouseTracking(False)
        #self.glInit() I think not working

        # YOUR GLOBAL ATTRIBUTES HERE IN CONSTURCTOR
        # self.abc
        # self.xyz
        self.vertices = [[]]
        self.index = 0

        self.lineWidth = 1

        #Coordinate factor
        self.xFactor = 0
        self.yFactor = 0
        


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
        self.r, self.g, self.b, self.a = 255, 253, 208, 1
        # initialize the screen to blueCalls glClearColor (in RGBA mode) 
        glClearColor(self.r/255, self.g/255, self.b/255, self.a/255)  
        #Alternate self.qglClearColor(QColor(r, g, b, a)) 

        self.x0, self.x1, self.y0, self.y1 = -1.0, 1.0, -1.0, 1.0
        gluOrtho2D(self.x0, self.x1, self.y0, self.y1)# Specify the max coordinates -x,+x,-y,+y.


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

        #glColor3f can be called in between glBegin and glEnd. When it is used this way, it can be used to give each vertex its own color.
        #glColor3f sets R,G,B and A
        
        # CODE TO DISPLAY VERTICES
        glColor3f(1.0, 0.0, 0.0) #red
        for obj in self.vertices:

            glBegin(GL_LINE_STRIP)

            for vertex in obj:
                glVertex2fv(vertex)

            glEnd()
            glFlush()





    def animate(self):
        #Any global variable You want to change to create an animation or put rotations to your Object
        #Add here
        #.
        #.
        

        #Dont change this
        self.updateGL()
        #Use updateGL() instead of update(), this does not make difference in my code here, but updateGL calls paintGL in the documentation.


    def lineWidthInc(self):
        if self.lineWidth < 10:
            self.lineWidth += 0.5
            glLineWidth(self.lineWidth)
    def lineWidthDec(self):
        if 1 < self.lineWidth:
            self.lineWidth -= 0.5
            glLineWidth(self.lineWidth)

    #this is pressed mouse event
    def mousePressEvent(self, event: QtGui.QMouseEvent):
        if event.button() == 2: #left btn
            self.clearVertices()
        else:
            self.xyFactorUpdate()
            position = event.pos()
            
            self.vertices[self.index].append([self.getX(position.x()), self.getY(position.y())])
        

    # this is pressed and drag mouse event
    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        if event.button() == 2: #left btn
            self.clearVertices()
        else:
            self.xyFactorUpdate()
            position = event.pos()
            
            self.vertices[self.index].append([self.getX(position.x()), self.getY(position.y())])

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        self.vertices.append([])
        self.index += 1

    def clearVertices(self):
        self.vertices = [[]]
        self.index = 0

    def xyFactorUpdate(self):
        self.xFactor = abs(self.x0-self.x1)/self.width()
        self.yFactor =  abs(self.y0-self.y1)/self.height()

    def centerX(self):
        return self.width()//2

    def centerY(self):
        return self.height()//2

    def getX(self, pos):
        return (pos - self.centerX()) * self.xFactor

    def getY(self, pos):
        if pos < self.centerY():
            return (pos - self.centerY()) * self.yFactor * -1
        else:
            return (pos - self.centerY()) * self.yFactor * -1
        

        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtWindow.MainWindow()
    window.show()
    sys.exit(app.exec_())
