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
import PyQtWindow
import sys
import numpy as np

class Wall:
    def __init__(self, x, y, length, width):
        x,y = x + width/2, y - length/2

        self.A = [ x - (width/2),  y + (length/2)]
        self.B = [ x + (width/2),  y + (length/2)]
        self.C = [ x + (width/2),  y - (length/2)]
        self.D = [ x - (width/2),  y - (length/2)]
        
    def coor(self):
        return [self.A, self.B, self.C, self.D]
    def draw(self):
        glBegin(GL_QUADS)
        glVertex2fv(self.A)
        glVertex2fv(self.B)
        glVertex2fv(self.C)
        glVertex2fv(self.D)
        glEnd()
        glFlush()

class GLWidget(QGLWidget):
    
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(100, 100)
        self.setMouseTracking(False)
        #self.glInit() I think not working

        # YOUR GLOBAL ATTRIBUTES HERE IN CONSTURCTOR
        # self.abc
        # self.xyz
        

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
        #255, 140, 0
        self.r, self.g, self.b, self.a = 255, 140, 0, 1
        # initialize the screen to blueCalls glClearColor (in RGBA mode) 
        glClearColor(self.r/255, self.g/255, self.b/255, self.a/255)  
        #Alternate self.qglClearColor(QColor(r, g, b, a)) 


        self.x0, self.x1, self.y0, self.y1 = -1.0, 1.0, -1.0, 1.0
        gluOrtho2D(self.x0, self.x1, self.y0, self.y1)# Specify the max coordinates -x,+x,-y,+y.

        #Attributes
        
        # self.maze_arr = [
        #     [1,1,1,1,1,1,1,1,1,1,1,1,1],
        #     [1,0,1,0,1,0,1,0,0,0,0,0,1],
        #     [1,0,1,0,0,0,1,0,1,1,1,0,1],
        #     [1,0,0,0,1,1,1,0,0,0,0,0,1],
        #     [1,0,1,0,0,0,0,0,1,1,1,0,1],
        #     [1,0,1,0,1,1,1,0,1,0,0,0,1],
        #     [1,0,1,0,1,0,0,0,1,1,1,0,1],
        #     [1,0,1,0,1,1,1,0,1,0,1,0,1],
        #     [1,0,0,0,0,0,0,0,0,0,1,0,1],
        #     [1,0,1,1,1,1,1,1,1,1,1,1,1]
        # ]

        self.maze_arr = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1],
            [1,0,1,0,0,1,0,1,1,0,1,1,0,1,0,0,0,1,0,1,0,1],
            [1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1],
            [1,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,1,0,0,1],
            [1,0,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]

        self.maze_arr2 = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
            [1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
            [1,0,1,0,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1],
            [1,0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1],
            [1,0,1,0,1,0,0,0,0,0,1,1,1,0,0,0,0,1,0,1],
            [1,1,1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,1],
            [1,0,1,1,1,1,1,0,1,0,0,0,0,0,0,1,0,1,0,1],
            [1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1],
            [1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1],
            [1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1],
            [1,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1],
            [1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1],
            [1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,1],
            [1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1],
            [1,0,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]
        #self.box = Wall(0,0,self.Width,self.Length)
        self.xFactor = 0
        self.yFactor = 0
        self.Width,self.Length = self.xyFactorUpdate()

        self.walls = []
        self.mazeMap= self.mazeMapper()
        self.once_run = True

        #self.mazeGenerator()

        #glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA) I think its not working
        self.formatGL()
        
    def mazeGenerator(self):
        if not(self.once_run):
            
            self.maze_arr = np.random.binomial(1,.3, size=(18,18))
            self.maze_arr[:,0] = 1  #Borders
            self.maze_arr[:,-1] = 1 #Borders
            self.maze_arr[0,:] = 1  #Borders
            self.maze_arr[-1,:] = 1 #Borders
            self.maze_arr[0][-4:-2] = 0 #Gate
            self.maze_arr[-1][1:3] = 0 #Gate

        else:
            self.maze_arr = self.maze_arr2
            self.once_run = False

        self.walls = []
        self.mazeMap= self.mazeMapper()
        self.xFactor = 0
        self.yFactor = 0
        self.Width,self.Length = self.xyFactorUpdate()

        self.walls = []
        self.mazeMap= self.mazeMapper()

    def mazeMapper(self):
        for y, row in enumerate(self.maze_arr):
            for x,flag in enumerate(row):
                if flag != 0:
                    yield Wall(self.getX(x),self.getY(y),self.Width,self.Length).coor()

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
        
        glColor3f(30/255,144/255,255/255)
        
        for wall in self.walls:
            glBegin(GL_QUADS)
            for coor in wall:
                glVertex2fv(coor)
            glEnd()
            glFlush()

        


    def animate(self):
        #Any global variable You want to change to create an animation or put rotations to your Object
        #Add here
        #.
        #.
        try:
            self.walls.append(next(self.mazeMap))
        except StopIteration:
            pass

        #Dont change this
        self.updateGL()
        #Use updateGL() instead of update(), this does not make difference in my code here, but updateGL calls paintGL in the documentation.

    def xyFactorUpdate(self) -> list:
        if len(self.maze_arr) > len(self.maze_arr[0]):
            size = len(self.maze_arr)
        else:
            size = len(self.maze_arr[0])

        self.xFactor = abs(self.x0-self.x1)/size
        self.yFactor =  abs(self.y0-self.y1)/size
        return [self.xFactor,self.yFactor]
    
    def centerX(self):
        return len(self.maze_arr[0])/2

    def centerY(self):
        return len(self.maze_arr)/2

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
