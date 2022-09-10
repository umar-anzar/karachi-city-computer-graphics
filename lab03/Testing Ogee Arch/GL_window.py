'''
By Muhammad Umar Anzar
'''
import math
from re import X
from PyQt5 import QtWidgets
from PyQt5.QtOpenGL import QGLWidget
from PyQt5.QtOpenGL import QGLFormat

#import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#Import PyQtWindow
import PyQtWindow
import sys

#Import matrix lib
import omermatrix as mat

class Circle:
    def __init__ (self,x,y,limit,radius,points,n,rotate=0):
        self.x=x
        self.y=y
        self.limit=[(limit[0]*math.pi/180),(limit[1]*math.pi/180)]
        self.radius=radius
        self.points = points
        self.n = n
        self.rotate = rotate
        self.vertex = []

    def draw(self):
        glBegin(GL_LINE_STRIP)
        for i in range(self.rotate ,self.points+self.rotate):
            t = ((self.limit[1]-self.limit[0])/self.n)  * i
            x= self.radius*math.cos(t) + self.x
            y = self.radius*math.sin(t) + self.y
            self.vertex.append([x,y])
            glVertex2f(x,y) 
        glEnd()
        glFlush()
    def redraw(self):
        glBegin(GL_LINE_STRIP)
        for arr in self.vertex:
            glVertex2fv(arr)
        glEnd()
        glFlush()

class Rect:
    from math import cos,sin,pi
    def __init__ (self,x,y,length,breadth):
        self.x=x
        self.y=y
        self.length = length
        self.breadth = breadth
        self.vertex = []
        self.vertex.append([self.x,self.y])
        self.vertex.append([self.x+self.length,self.y])
        self.vertex.append([self.x+self.length,self.y+self.breadth])
        self.vertex.append([self.x,self.y+self.breadth])

    def draw(self):
        glBegin(GL_QUADS)
        glVertex2f(self.x,self.y) 
        glVertex2f(self.x+self.length,self.y) 
        glVertex2f(self.x+self.length,self.y+self.breadth) 
        glVertex2f(self.x,self.y+self.breadth) 
        glEnd()
        glFlush()

    def redraw(self):
        glBegin(GL_QUADS)
        for arr in self.vertex:
            glVertex2fv(arr)
        glEnd()
        glFlush()
    
    def rotation(self,angle):
        rad = (angle * self.pi) / 180
        rotationMatrix = [
            [self.cos(rad),self.sin(rad)],
            [-self.sin(rad),-self.cos(rad)]
        ]
        self.vertex =  mat.multiplyMatrix(self.vertex,rotationMatrix)
        self.redraw()


class GLWidget(QGLWidget):
    
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(100, 100)
        self.setMouseTracking(False)
        #self.glInit() I think not working

        # YOUR GLOBAL ATTRIBUTES HERE IN CONSTURCTOR
        # self.abc
        # self.xyz
        self.i = 0 #EXAMPLE MOVING POINT


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


        ## CIRCL A AND B
        r = 0.5
        x2 = 0.3
        x3 = 0.3+2*r
        x1 = 0.3+r
        y1 = 0.1
        y2 = y1+math.sqrt((2*r)**2-r**2)
        B = self.Bullet(0.3,0.1,0.08)
        B.draw()
        B.rotation(int(self.i))
        RE = Rect(0,0,0.2,0.2)
        RE.rotation(int(self.i))
        RE.redraw()


    class Bullet:
        from math import cos,sin,pi
        def __init__ (self,x,y,size):
            self.r = size
            self.x2 = x
            self.x3 = x+2*size
            self.x1 = x+size
            self.y1 = y
            self.y2 = y+math.sqrt((2*size)**2-size**2)
            self.A = Circle(self.x1,self.y1,[0,180],self.r,360,360)
            self.B = Circle(self.x2,self.y2,[0,60],self.r,360,360,-360)
            self.C = Circle(self.x3,self.y2,[0,60],self.r,360,360,1100)
            self.D = Rect(self.x2,self.y1-2*self.r+0.01,2*self.r,0.15)
        def draw(self):
            self.A.draw()
            self.B.draw()
            self.C.draw()
            self.D.draw()

        def rotation(self,angle):
            rad = (angle * self.pi) / 180
            rotationMatrix = [
                [self.cos(rad),self.sin(rad)],
                [-self.sin(rad),-self.cos(rad)]
            ]
            self.A.vertex =  mat.multiplyMatrix(self.A.vertex,rotationMatrix)
            self.A.redraw()



    def animate(self):
        #Any global variable You want to change to create an animation or put rotations to your Object
        #Add here
        #.
        #.
        self.i += 1 #EXAMPLE MOVING POINT

        #Dont change this
        self.updateGL()
        #Use updateGL() instead of update(), this does not make difference in my code here, but updateGL calls paintGL in the documentation.


    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = PyQtWindow.MainWindow()
    window.show()
    sys.exit(app.exec_())
