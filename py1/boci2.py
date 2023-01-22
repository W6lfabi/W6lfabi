from turtle import*
import math
speed(0)
shape("turtle")
pensize(5)
color("green")
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
    m=3/4*sz
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
    setpos(xcor()+sz/4,ycor())
    down()
    pensize(sz/20)
    forward(0)
    up()
    setpos(xcor(),ycor()-3*m/16)
    down()
    pensize(3)
    backward(m/8)
    up()
    setpos(xcor()-sz/4,ycor())
    down()
    forward(m/8)
    up()

    setpos(0,m) # Balfül
    setheading(195)
    down()
    right(60)
    forward(m/5)
    left(-90)
    forward(m/5)
    up()

    setpos(sz/2,m)  # Jobbfül
    setheading(-15)
    down()
    forward(m/5)
    right(-90)
    forward(m/5)
    up()

    setpos(sz/10,0)
    setheading(0)
    down()
    teglalap(sz/10,m/5)
    teglalap(sz/10,4*m/25)
    forward(sz/10)
    teglalap(sz/10,m/4)
    teglalap(sz/10,21*m/100)
    forward(sz/2)
    teglalap(sz/10,m/5)
    teglalap(sz/10,4*m/25)
    forward(sz/10)
    teglalap(sz/10,m/4)
    teglalap(sz/10,21*m/100)
    up()

    setpos(sz,m/2)
    setheading(15)
    down()
    forward(m/5)
    left(-90)
    forward(m/5)
    up()
    home()
    
    
    
    
    



    



def kor(x,y,r):
    up()
    setpos(x,y)
    forward(r)
    left(90)
    down()
    begin_fill()
    for i in range(40):
        forward(2*r*math.pi/40)
        left(9)
    end_fill()
    
    
    
    
    
boci1(500)
color("blue")
kor(200,110,50)
color("brown")
kor(400, 250, 50)
hideturtle()
exitonclick()
