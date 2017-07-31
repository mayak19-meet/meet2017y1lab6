import turtle
##turtle.shape('turtle')
##square=turtle.clone()
##square.shape('square')
##square.goto(100,100)
##square.goto(300,300)
##square.stamp()
##square.goto(100,100)
##square.penup()
##square.goto(0,0)
##square.pendown()
##square.goto(0,100)
##square.goto(100,100)
##square.goto(100,0)
##square.goto(0,0)
##square=turtle.clone()
##square.shape('triangle')
##square.goto(100,100)
##square.goto(0,200)
##square.goto(0,0)
##square=turtle.clone()
##square.shape('triangle')
##square=turtle.clone()
up_arrow="Up"
left_arrow="Left"
DOWN_arrow="Down"
right_arrow="right"
spacebar="space"

UP=0
DOWN=1
LEFT=2
RIGHT=3

direction=up

def up():
    global direction
    directon =UP
    print('you pressed up')

def down():
    global direction
    directon =DOWN
    print('you pressed down')
    
def left():
    global direction
    directon =LEFT
    print('you pressed left')
    
def right():
    global direction
    directon =RIGHT
    print('you pressed right')
    
#tutrle.mineloop()
