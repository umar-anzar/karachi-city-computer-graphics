import turtle as t
t.screensize(canvwidth=100, canvheight=40,
                  bg="yellow")
z = t.Turtle()

def lineTo(t,x,y):
    t.pendown()
    t.goto(x,y)    
def moveTo(t,x,y):
    t.penup()
    t.goto(x,y)  



point_arr = [
    [0,0],
    [100,30],
    [70,60],
    [10,50],
    [0,0]
]
n = len(point_arr)
for i in range(0,n-1):
    for j in range(i+1, n):
        lineTo(z,x=point_arr[j][0],y=point_arr[j][1])
t.done()
