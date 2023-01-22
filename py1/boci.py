from turtle import*
speed(4)
shape("turtle")
pensize(5)
color("black")
setheading(90)
def teglalap(m,sz):
    forward(m)
    right(90)
    forward(sz)
    right(90)
    forward(m)
    right(90)
    forward(sz)
    right(90)

def boci1(sz):
    m=3*sz/4
    teglalap(m,sz)
    forward(m/2)
    teglalap(m/2, sz/2)
    teglalap(m/4,sz/2)
    up()
    setpos(xcor()+sz/8,ycor()+3*m/8)
    down()
    pensize(sz/20)
    forward(0)
    up()
    home()
    



boci1(200)
teglalap(200)

