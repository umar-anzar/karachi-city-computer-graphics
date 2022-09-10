
from PyQt5 import QtWidgets
from PyQt5.QtOpenGL import QGLWidget
from PyQt5.QtOpenGL import QGLFormat
import PyQt5.QtCore as QtCore

import OpenGL
import OpenGL.GL as gl
import OpenGL.GLU as glu

import math
import random
import sys

class Vertex:
    def __init__(self, x, y):
        self.x = x/100
        self.y = y/100

def cv(x):
    return x/100

class GLWidget(QGLWidget):
    
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(100, 100)
        self.setMouseTracking(False)
        #self.glInit() I think now working

        #Rain
        self.rainDrops = []
        for i in range(200):
            self.rainDrops.append(self.RainParticles(x=random.uniform(-2, 2),y=random.uniform(-1, 1), length=0.05, increment=0.1))

        #Sun
        self.sun_y = -1
        self.sun_move_y = -1

    
        
    def formatGL(self):
        fmt = QGLFormat()
        fmt.setDoubleBuffer(True)                 # Double Buffering
        QGLFormat.setDefaultFormat(fmt) 

    def initializeGL(self):
        #print("Intial")
        self.once = True

        self.r, self.g, self.b, self.a = 228, 151, 89, 1
        self.r_c, self.g_c, self.b_c, self.a_c = 228, 151, 89, 1
        # initialize the screen to blueCalls glClearColor (in RGBA mode) 
        gl.glClearColor(self.r/255, self.g/255, self.b/255, self.a/255) #Alternate self.qglClearColor(QColor(r, g, b, a)) 

        #glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA) I think its not working
        self.formatGL()
        
    
    def resizeGL(self, width, height):
        #print("resizeGL")
        gl.glViewport(0, 0, width, height)    
        glu.gluOrtho2D(-1.0, 1.0,-1.0,1.0)# Specify the max coordinates -x,+x,-y,+y.

        
    def checkingFunction(self):
        
        if self.once:
            self.once = False
            #If widget is using a double-buffered format, the background and foreground GL buffers will automatically be swapped 
            # after each paintGL() call. The buffer auto-swapping is on by default.
            print("\nStatus\tAttribute")
            print(self.doubleBuffer(),"\tDouble Buffer")
            print(self.autoBufferSwap(),"\tBuffer Swap")

    class RainParticles:
        def __init__(self, x, y, length, increment) -> None:
            self.x = x
            self.y = y
            self.x_move = x
            self.length = length
            self.increment = increment
        
        def simulateRain(self):
            if self.y < -1:
                self.y = 1
                self.x_move = self.x
            gl.glBegin(gl.GL_LINES)
            gl.glColor3f(0.0, 0.0, 1.0) 
            gl.glVertex2f(self.x_move, self.y)
            gl.glVertex2f(self.x_move-0.02, self.y+self.length)
            self.y-= self.increment
            self.x_move += 0.05
            gl.glEnd()
            gl.glFlush()        

    def paintGL(self):
        #print("paingGl").
        
        self.checkingFunction()

        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) #refresh screen : clear color array buffer
        
        gl.glPointSize(5.0) #The glPointSize function specifies the diameter of rasterized points
        
        # gl.glBegin(gl.GL_LINES)

        # #glColor3f can be called in between glBegin and glEnd. When it is used this way, it can be used to give each vertex its own color.
        # #glColor3f sets R,G,B and A

        # # X-AXIS--------------------------------------------------------------------------------
        # gl.glColor3f(1.0, 1.0, 0.0)

        # gl.glVertex2f(cv(-100),0)

        # gl.glVertex2f(cv(100), 0)
        

        # # Y-AXIS
        # gl.glColor3f(0.0, 1.0, 0.0)
        # gl.glVertex2f(0, cv(-100))
        # gl.glVertex2f(0, cv(100))
        # gl.glEnd()
        # gl.glFlush() #The glFlush function forces execution of OpenGL functions in finite time.
        
        #SUNSET--------------------------------------------------------------------------------
        gl.glColor3f(1.0, 1.0, 0.0)
        gl.glBegin(gl.GL_POLYGON)
        t = 0

        while t < math.pi:
            gl.glVertex2f(0.5*math.cos(t),self.sun_move_y+0.5*math.sin(t))
            t += 0.01
        gl.glEnd()
        gl.glFlush()
        self.sun_move_y -= 0.001

        self.r_c, self.g_c, self.b_c = self.r_c-0.5, self.g_c-0.5, self.b_c-0.5

        gl.glClearColor(self.r_c/255, self.g_c/255, self.b_c/255, self.a_c/255) #Gets night

        if self.sun_move_y < -1.4: #sun comebacks
            self.sun_move_y  = self.sun_y
            self.r_c, self.g_c, self.b_c, self.a_c = self.r, self.g, self.b, self.a


        #Land--------------------------------------------------------------------------------
        gl.glColor3f(0.0, 1.0, 0.0)
        gl.glBegin(gl.GL_POLYGON)
        t = 0
        while t < math.pi:
            gl.glVertex2f(0.5*math.cos(t),-1.2+0.35*math.sin(t))
            t += 0.01
        gl.glEnd()
        gl.glFlush()

        gl.glBegin(gl.GL_POLYGON)
        t = 0
        while t < math.pi:
            gl.glVertex2f(-0.5+0.5*math.cos(t),-1.2+0.35*math.sin(t))
            t += 0.01
        gl.glEnd()
        gl.glFlush()

        gl.glBegin(gl.GL_POLYGON)
        t = 0
        while t < math.pi:
            gl.glVertex2f(0.5+0.5*math.cos(t),-1.2+0.35*math.sin(t))
            t += 0.01
        gl.glEnd()
        gl.glFlush()

        gl.glBegin(gl.GL_POLYGON)
        t = 0
        while t < math.pi:
            gl.glVertex2f(-1.0+0.5*math.cos(t),-1.2+0.35*math.sin(t))
            t += 0.01
        gl.glEnd()
        gl.glFlush()

        gl.glBegin(gl.GL_POLYGON)
        t = 0
        while t < math.pi:
            gl.glVertex2f(1.0+0.5*math.cos(t),-1.2+0.35*math.sin(t))
            t += 0.01
        gl.glEnd()
        gl.glFlush()

        #Rain drop falling function
        for drop in self.rainDrops:
            drop.simulateRain()

        
    

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self) -> QtWidgets.QMainWindow:
        super().__init__()
        self.windowSetting()

        self.windowObject()
        self.GL_window.show()
        self.setCentralWidget(self.central_widget)

        #For multiThreading
        self.timer = QtCore.QTimer()
        self.animate = True

        #Button functions
        self.Btn_clear.clicked.connect(self.closeEvent)
        self.Btn_draw.clicked.connect(self.animation)

    def windowSetting(self) -> None:
        self.setWindowTitle("B19102104 Muhammad Umar Anzar")
        self.resize(800,600)
        self.center()

    def center(self) -> None:
        #Determines the center of screen
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        x,y = cp.x() , cp.y()
        #Center the window
        x = x - self.width()//2
        y = y - self.height()//2
        #apply new axis
        self.move(x,y)


    def windowObject(self) -> None:
       
        self.central_widget = QtWidgets.QWidget(self)
        self.GL_window = GLWidget(self.central_widget)
        self.Btn_clear = QtWidgets.QPushButton("STOP",self.central_widget)
        self.Btn_draw = QtWidgets.QPushButton("SIMULATE",self.central_widget)

        self.verticalLayout1 = QtWidgets.QVBoxLayout(self.central_widget)
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()

        self.verticalLayout1.addWidget(self.GL_window)
        self.verticalLayout1.addLayout(self.horizontalLayout1)
        self.horizontalLayout1.addWidget(self.Btn_draw)
        self.horizontalLayout1.addWidget(self.Btn_clear)
        


    def animation(self):
        if self.animate:
            self.timer.timeout.connect(self.GL_window.update)
            self.timer.start(20)
            self.animate = False

    def closeEvent(self, event):
        self.animate = True
        self.timer.stop()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

