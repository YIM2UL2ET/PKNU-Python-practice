import turtle as t

t.speed(0)
t.penup()
t.hideturtle()

def draw6(t):
    t.pensize(4)
    t.bk(3)
    t.penup()
    t.lt(90)
    t.bk(10)
    t.pendown()
    t.rt(90)
    t.circle(7,180)
    t.penup()
    t.rt(90)
    t.bk(14)
    t.pendown()
    t.lt(16)
    t.fd(7)
    t.rt(24)
    t.fd(13)
    t.rt(30)
    t.fd(5)
    t.rt(70)
    t.fd(3)
    
draw6(t)
