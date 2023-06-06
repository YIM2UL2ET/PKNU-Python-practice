import turtle as t

t.speed(0)
t.penup()
t.hideturtle()

def draw2(t):
    t.pensize(4)
    t.penup()
    t.fd(12)
    t.lt(90)
    t.bk(10)
    t.lt(90)
    t.fd(6)
    t.pendown()
    t.fd(10)
    t.rt(130)
    t.fd(9)
    t.circle(9,90)
    t.lt(90)
    t.fd(5)
    
draw2(t)
