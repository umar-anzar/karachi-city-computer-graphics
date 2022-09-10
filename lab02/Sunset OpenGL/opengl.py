import OpenGL

from OpenGL.GL import *

from OpenGL.GLUT import *

from OpenGL.GLU import *



def init():

    glClearColor(0.0, 0.0, 0.0, 1.0)

    gluOrtho2D(-1.0, 1.0,-1.0,1.0)



def plotpoints():

    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)

    glPointSize(5.0)

    glBegin(GL_LINES)


    # X-AXIS

    glVertex2f(-1.0, 0.0)

    glVertex2f(1.0, 0.0)


    # Y-AXIS

    glVertex2f(0.0, 1.0)

    glVertex2f(0.0, -1.0)

    glEnd()

    glFlush()


    # Triangle

    x1, x2, x3 = 0.3, 0.7, 0.5

    y1, y2, y3 = 0.2, 0.5, 0.7


    glColor3f(0.5, 0.5, 0.0)

    glPointSize(3.0)

    glBegin(GL_LINES)


    glVertex2f(x1, y1)

    glVertex2f(x2, y2)


    glVertex2f(x2, y2)

    glVertex2f(x3, y3)


    glVertex2f(x3, y3)

    glVertex2f(x1, y1)


    glEnd()

    glFlush()



if __name__ == "__main__":

    glutInit()

    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)


    glutCreateWindow("X Axis, Y Axis, Triangle")

    glutDisplayFunc(plotpoints)

    init()

    glutMainLoop()