from PyQt5 import QtWidgets
from PyQt5.QtOpenGL import QGLWidget, QGLFormat
import sys
import math

import OpenGL.GL as gl

import OpenGL.GLUT as glut

import OpenGL.GLU as glu

class GLWidget(QGLWidget):
    
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.setMinimumSize(100, 100)
        self.setMaximumSize(800,800)
        self.setMouseTracking(False)
        
    def formatGL(self):
        fmt = QGLFormat()
        fmt.setDoubleBuffer(True)                 # Double Buffering
        QGLFormat.setDefaultFormat(fmt) 

    def initializeGL(self):
        
        #print("Intial")
        # initialize the screen to blueCalls glClearColor (in RGBA mode) 
        r, g, b, a = 35, 39, 42, 1
        gl.glClearColor(r/255, g/255, b/255, a/255) 

        #glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA) I think its not working
        self.formatGL()
        
    
    def resizeGL(self, width, height):
        #print("resizeGL")
        gl.glViewport(0, 0, width, height)    
        glu.gluOrtho2D(-1.0, 1.0,-1.0, 1.0)# Specify the max coordinates -x,+x,-y,+y.

    def paintGL(self):
        #print("paingGl").

        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) #refresh screen : clear color array buffer
        gl.glPointSize(5.0) 
        gl.glBegin(gl.GL_LINES)

        # X-AXIS------------------------------------------------------
        gl.glColor3f(1.0, 1.0, 0.0) 
        gl.glVertex2f(1.0, .0)
        gl.glVertex2f(-1.0, .0)
        
        # Y-AXIS------------------------------------------------------
        gl.glColor3f(0.0, 1.0, 0.0) 
        gl.glVertex2f(.0, 1.0)
        gl.glVertex2f(.0, -1.0)
        gl.glEnd()
        gl.glFlush()

        # Shapes------------------------------------------------------
        self.rectangle(-0.3,0.2,-0.8,0.2,-0.8,0.6,-0.3,0.6)
        self.triangle(0.3,0.6,0.1,0.2,0.5,0.2)
        self.circle(0.2,-0.5,-0.5)
        self.triangleFan()
        self.heart(0.01,0,0)
        
    def rectangle(self,x1,y1,x2,y2,x3,y3,x4,y4):
        gl.glBegin(gl.GL_QUADS)
        gl.glColor3f(0.0, 1.0, 0.0) 
        gl.glVertex2f(x1,y1)#Order matters
        gl.glVertex2f(x2,y2)
        gl.glColor3f(0.5, .5, 0.5) 
        gl.glVertex2f(x3,y3)
        gl.glVertex2f(x4,y4)
        gl.glEnd()
        gl.glFlush()

    def triangle(self,x1,y1,x2,y2,x3,y3):
        gl.glBegin(gl.GL_TRIANGLES)
        gl.glColor3f(1.0, 0.0, 0.0) 
        gl.glVertex2f(x1,y1)
        gl.glVertex2f(x2,y2)
        gl.glColor3f(0.0, 1.0, 0.0) 
        gl.glVertex2f(x3,y3)
        gl.glEnd()
        gl.glFlush()

    def circle(self,radius,x1,y1):
        gl.glBegin(gl.GL_POLYGON)
        gl.glColor3f(0.08, 0.0, 1.0) 
        n = 360
        j = 0.01
        for i in range(0,n):
            t = (2 * math.pi / n)*i
            x = x1 + radius * math.cos(t)
            y = y1 + radius * math.sin(t)
            gl.glVertex2f(x, y)
            gl.glColor3f(0.05+j, 0.0+j, 0.8-j)
            j += 0.01
        gl.glEnd()
        gl.glFlush()


    def triangleFan(self):
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glColor3f(0.08, 0.2, 1.0) 
        gl.glVertex2f(0.5,-0.8)
        gl.glVertex2f(.3,-.9)
        gl.glVertex2f(0.35,-0.7)
        gl.glColor3f(0.28, 0, 1.0) 
        gl.glVertex2f(0.4,-0.6)
        gl.glVertex2f(0.5,-0.5)
        gl.glEnd()

    def heart(self,radius,x1,y1):

        gl.glBegin(gl.GL_POLYGON)
        gl.glColor3f(0.08, 0.0, 1.0) 

        radian = 0
        while radian<2*math.pi:
            x = x1 + radius * 16 * math.pow(math.sin(radian),3)
            y = y1 + radius * (13*math.cos(radian) - 5*math.cos(2*radian) - 2*math.cos(3*radian) -math.cos(4*radian))
            gl.glVertex2f(x, y)
            radian += 0.01
            
        gl.glEnd()
        gl.glFlush()

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setMinimumSize(500,500)
layout = QtWidgets.QHBoxLayout(window)
GL = GLWidget(window)
layout.addWidget(GL)



window.show()
sys.exit(app.exec_())
