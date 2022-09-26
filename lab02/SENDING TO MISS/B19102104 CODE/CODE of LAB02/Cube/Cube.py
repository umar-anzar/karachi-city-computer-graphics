import time
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

    

class GL_Window:
    
    def __init__(self) -> None:
        self.vertices= (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
        )
        self.edges = (
        (0,1),
        (0,3),
        (0,4),
        (2,1),
        (2,3),
        (2,7),
        (6,3),
        (6,4),
        (6,7),
        (5,1),
        (5,4),
        (5,7)
        )
        glut.glutInit() #glutInit will initialize the GLUT library and negotiate a session with the window system
        display = (800,600)
        glut.glutCreateWindow("B19102104")
        glut.glutReshapeWindow(display[0], display[1])
        glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB)#/Bit mask to select a double buffered window. This overrides GLUT_SINGLE if it is also specified.
        
        
        
        
        
        glu.gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
        gl.glTranslatef(0.0,0.0, -5)


        #gl.glClearColor(0.0, 0.0, 0.0, 1.0) # background Color

        
        glut.glutDisplayFunc(self.plotPoints) #This display on screen

        glut.glutIdleFunc(self.spin)##this idle function recalls will post display function
        glut.glutMainLoop()
        
        #glutMainLoop enters the GLUT event processing loop. This routine should be called at most once in a GLUT program. Once called, this routine will never return.
        
    def spin(self):
        time.sleep(0.01)
        glut.glutPostRedisplay() #here I am recalling post redisplay function

    def plotPoints(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

        gl.glColor3f(1.0, 0.0, 1.0)

        gl.glPointSize(5.0)
        gl.glRotatef(1, 3, 1, 1)

        gl.glBegin(gl.GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                gl.glVertex3fv(self.vertices[vertex])
        gl.glEnd()
        gl.glFlush()

        

GL_Window()

    