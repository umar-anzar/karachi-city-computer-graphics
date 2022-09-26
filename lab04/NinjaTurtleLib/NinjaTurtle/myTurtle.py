from locale import normalize
from typing import Tuple
from NinjaTurtle.PyQtWindow import MainWindow
from PyQt5 import QtWidgets
import threading
import time
import sys


import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def ninjaTurtle():
    global queue

    class Queue:
        def __init__(self) -> None:
            self.arr = []
        def enqueue(self,val):
            self.arr.append(val)
        def isEmpty(self):
            return len(self.arr) == 0
        def returnWindow(self) -> MainWindow:
            return self.arr[0]

    queue = Queue()

    def f():
        x = TurtleWindow()

        queue.enqueue(x)

        x.end()

    t = threading.Thread(target=f)
    t.start()

    while queue.isEmpty():
        pass
    window = queue.returnWindow()
    time.sleep(1)
    print("A")
    return window
################################################################################################################



class TurtleWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = MainWindow()
        self.window.show()

    def end(self):
        sys.exit(self.app.exec_())

    def Initialize(self):
        self.vertex = []

    def bgcolor(self,color:list):
        self.window.GL_window.backGroundColor= color
        self.window.GL_window.isBgColorChange = True


class Point:
    """Coordinates of pen
    """
    def __init__(self) -> None:
        self.x = 0 
        self.y = 0

class GlObject:
    def __init__(self, type:OpenGL.constant, color:list, vertices:list) -> None:
        
        self.type =  type
        self.color = color
        self.vertices = vertices


class Pen:

    def __init__(self) -> None:
        self.status = False
        self.width = 1
        self.color = [1, 1, 1]
        self.pos = Point()
        

class Turtle:
    def __init__(self,turtleWindow:TurtleWindow) -> None:
        """_summary_

        Args:
            window (TurtleWindow): _description_
        """
        self.pen = Pen()
        self.vertices = []
        self.window = turtleWindow.window #PyqtWindow
        

    def createGlObject(self, vertices):
        self.window.GL_window.object_vertex.append(GlObject(GL_LINE_STRIP,self.pen.color,vertices))

    def penup(self) -> None:
        """Pen is up so no drawing will take place
        """
        self.pen.status = False
    def pendown(self) -> None:
        """Pen is down so drawing will take place
        """
        self.pen.status = True

    def getPos(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        return [self.pen.pos.x , self.pen.pos.y]

    def goto(self, x, y) -> None:
        self.lineTo(x,y)
        x, y = self.normalize(x,y)
        self.pen.pos.x = x
        self.pen.pos.y = y

    def color(self, r:float, g:float, b:float):
        """Set color of pen

        Args:
            r (float): Red
            g (float): Green
            b (float): Blue
        """        
        self.pen.color = [r/255, b/255, g/255]


    def setWidth(self, width:float):
        """Set Width

        Args:
            width (float): thickness of the pen marker
        """
        if self.pen.width <= 0:
            self.pen.width = 1
        else:
            self.pen.width = width


    def lineTo(self, x:float, y:float):
        if self.pen.status:
            x, y = self.normalize(x,y)
            vertices = []
            vertices.append(self.getPos())
            vertices.append([x, y])
            self.createGlObject(vertices)

        # for i in range(100):
        #     t = ((x - current.x) / 100) * i;
        #     a = x - current.x
        #     b = y - current.y
        #     vertices.append ([current.x + a * t , current.y + b * t])

    def normalize(self, x:float, y:float) -> Tuple:
        """_summary_

        Args:
            x (float): _description_
            y (float): _description_

        Returns:
            Tuple: _description_
        """
        return x/100, y/100