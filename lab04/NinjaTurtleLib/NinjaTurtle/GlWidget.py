'''
By Muhammad Umar Anzar
'''
from PyQt5 import QtWidgets
from PyQt5.QtOpenGL import QGLWidget
from PyQt5.QtOpenGL import QGLFormat

#import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#Import PyQtWindow
from NinjaTurtle import PyQtWindow




class GlWidget(QGLWidget):
    
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(100, 100)
        self.setMouseTracking(False)
        #self.glInit() I think not working
        self.backGroundColor = (10, 50, 10, 1)
        self.r, self.g, self.b, self.a = self.backGroundColor
        self.isBgColorChange = False

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
        
        # initialize the screen to blueCalls glClearColor (in RGBA mode) 
        glClearColor(self.r/255, self.g/255, self.b/255, self.a/255)  
        
        #Alternate self.qglClearColor(QColor(r, g, b, a)) 
        gluOrtho2D(-1.0, 1.0,-1.0,1.0)# Specify the max coordinates -x,+x,-y,+y.

        #glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA) I think its not working
        self.formatGL()

        # YOUR GLOBAL ATTRIBUTES HERE IN initializeGL Function
        # self.abc
        # self.xyz
        self.object_vertex = []
        
    
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

    def setBackgroundColor(self):
        if self.isBgColorChange:
            glClearColor(self.backGroundColor[0]/255, 
            self.backGroundColor[1]/255, 
            self.backGroundColor[2]/255, 
            self.backGroundColor[3]/255) 
            self.isBgColorChange = False

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
        self.setBackgroundColor()


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



        for obj in self.object_vertex:
            
            glColor3fv(obj.color)
            glBegin(obj.type)
            for v in obj.vertices:
                glVertex2fv(v)
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

