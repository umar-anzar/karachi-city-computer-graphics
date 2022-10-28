from turtle import RawTurtle, TurtleScreen
from tkinter import *


class Window(Tk):
    def __init__(self, title, geometry):
        super().__init__()
        self.running = True
        self.geometry(geometry)
        self.title(title)
        self.protocol("WM_DELETE_WINDOW", self.destroy_window)
        self.canvas = Canvas(self)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)
        self.turtle = RawTurtle(TurtleScreen(self.canvas))

    def update_window(self):
        if self.running:
            self.update()

    def destroy_window(self):
        self.running = False
        self.destroy()


def forward_rotate(t: RawTurtle,amount,angle,start,stop,step,color_linkList=[]):
    t.pendown()
    index = 0

    if amount <= 0:
        amount = 1
    if len(color_linkList) == 0:
        color = 'black'
        t.color(color)
        for i in range(start,stop,step):
            t.forward(amount * i)
            t.left(angle)
            yield
    else:
        for i in range(start,stop,step):
            color, index = color_linkList[index]
            t.color(color)
            t.forward(amount * i)
            t.left(angle)
            yield


def circle_rotate(t: RawTurtle,radi,angle,start,stop,step,color='black'):
    t.pendown()
    t.color(color)
    if radi <= 0:
        amount = 1
    for i in range(start,stop,step):
        t.circle(i*radi)
        t.left(angle)
        yield



def condition(windows):
    for win in windows:
        if not(win.running):
            return False
    return True

def update_window(windows):
    for win in windows:
        win.update_window()

def draw(drawList):
    for draw in draw_list:
        try:
            next(draw)
        except StopIteration:
            pass

def speed(windows):
    for win in windows:
        win.turtle.speed(500)


# create windows
win1 = Window('Turtle Window 1', '400x350+0+0')
win2 = Window('Turtle Window 2', '400x350+400+0')
win3 = Window('Turtle Window 3', '400x350+800+0')
win4 = Window('Turtle Window 4', '400x350+0+420')
win5 = Window('Turtle Window 5', '400x350+400+420')
win6 = Window('Turtle Window 6', '400x350+800+420')
windows = [win1,win2,win3,win4,win5,win6]



t1Draw = forward_rotate(win1.turtle,2,91, 0,100,1 ,color_linkList=[('orange',1),('blue',0)])
t2Draw = forward_rotate(win2.turtle,2,190, 0,100,1 ,color_linkList=[('red',1),('green',2),('blue',0)])
t3Draw = forward_rotate(win3.turtle,2,-90, 0,100,1 )
t4Draw = circle_rotate(win4.turtle,1,360/6, 0,100,1 ,'red')
t5Draw = circle_rotate(win5.turtle,1,10, 0,100,1 ,'purple')
t6Draw = circle_rotate(win6.turtle,1,360/3, 0,100,1 ,'green')

draw_list = [t1Draw,t2Draw,t3Draw,t4Draw,t5Draw,t6Draw]

speed(windows)
    
# update windows (the mainloop)
while condition(windows):
    draw(draw_list)

    update_window(windows)