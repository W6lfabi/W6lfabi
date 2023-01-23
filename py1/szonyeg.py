from turtle import *

def tl(m):
    forward(m)
    left(90)
    forward(m/2)
    left(90)
    forward(m)
    left(90)
    forward(m/2)
    left(90)  

up()
setpos(-200, -100)
down()

tl(400)
exitonclick()