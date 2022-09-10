import math
import time
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

    

class GL_Window:
    
    def __init__(self) -> None:
        self.obj_list = []
        self.display = (800,600)   
        r, g, b, a = 35, 39, 42, 1

        self.ImportObj("parametricVertexList.txt")

        glut.glutInit() #glutInit will initialize the GLUT library and negotiate a session with the window system
        
        glut.glutCreateWindow("B19102104")
        glu.gluOrtho2D(-10, 10,-10, 10)# Specify the max coordinates -x,+x,-y,+y.
        glut.glutReshapeWindow(self.display[0], self.display[1])
        glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)#/Bit mask to select a double buffered window. This overrides GLUT_SINGLE if it is also specified.
        
        gl.glClearColor(r/255, g/255, b/255, a/255) # background Color

        glut.glutDisplayFunc(self.plotPoints) #This display on screen

        glut.glutMainLoop()
        
        #glutMainLoop enters the GLUT event processing loop. This routine should be called at most once in a GLUT program. Once called, this routine will never return.
    
    class Obj:
        def __init__(self,name) -> None:
            self.name = name
            self.vertices = []

    def plotPoints(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

        
        for obj in self.obj_list:
            gl.glBegin(gl.GL_LINES)
            for vertex in obj.vertices:
                gl.glVertex2f(vertex[0],vertex[1])
            gl.glEnd()
            gl.glFlush()


        # #y= math.sin(x+1.5*math.pi)
        # #HELIX
        # gl.glBegin(gl.GL_LINES)
        # t = 0
        # for degree in range(-320,320):
        #     radian = degree * math.pi/180
        #     gl.glVertex2f( degree/36, -2 + 4*math.cos(radian))
        #     t += 0.01
        # gl.glEnd()
        # gl.glFlush()

        # gl.glBegin(gl.GL_LINES)
        # t = 0
        # for degree in range(-320,320):
        #     radian = degree * math.pi/180
        #     gl.glVertex2f( degree/36, -2 + 4*math.sin(radian+1.5*math.pi))
        #     t += 0.01
        # gl.glEnd()
        # gl.glFlush()


        
    
    def ImportObj(self,location):
        with open(location,'r') as file:
            i = 0
            for line in file.readlines():
                line = line[:-1]
                try:

                    if line[0] == 'o':
                        self.obj_list.append(self.Obj(line.split()[1]))
                        i += 1
                    if line[0] == 'v':
                        self.obj_list[i-1].vertices.append(list(map(float,line.split()[1:])))

                except IndexError as e:
                    pass
                    

        for i in self.obj_list:
            if i.name not in ('Circle','Cos','sin'):
                print(i.name,i.vertices,'\n')
            
 


GL_Window()

    