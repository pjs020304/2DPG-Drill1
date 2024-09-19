import turtle
import random
 
turtle.speed(0)
turtle.pensize(5) 
turtle.shape("turtle")

def up():
    turtle.setheading(90)
    turtle.forward(50)
 
def down():
    turtle.setheading(270)
    turtle.forward(50)
 
 
def left():
    turtle.setheading(180)
    turtle.forward(50)
 
def right():
    turtle.setheading(0)
    turtle.forward(50)
 
def esc():
    turtle.clear()   
    turtle.home() 
 
turtle.listen()
 
 
turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(left, 'a')
turtle.onkey(right, 'd')
turtle.onkey(esc, 'Escape')
 
turtle.mainloop()