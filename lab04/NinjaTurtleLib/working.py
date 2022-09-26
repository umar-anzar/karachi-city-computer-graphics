import NinjaTurtle.myTurtle as myTurtle
import time



Turtle_Window = myTurtle.ninjaTurtle()
t = myTurtle.Turtle(Turtle_Window)
t.pendown()
t.color(50,100,255)
t.lineTo(3,8)
t.penup()
time.sleep(1)
Turtle_Window.bgcolor((255, 255, 255, 1))
t.goto(30,20)
t.pendown()
t.lineTo(10,-10)
t.penup()
t.goto(-4,20)
t.pendown()
t.color(255,255,0)
time.sleep(1)
Turtle_Window.bgcolor((0, 0, 0, 1))
t.lineTo(-5,-5)


