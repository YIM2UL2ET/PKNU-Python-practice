import turtle as t

t.speed(0)
t.penup()
t.hideturtle()

def draw3(t):
    t.pensize(4)
    t.penup()
    t.lt(90)
    t.bk(10)
    t.rt(90)
    t.bk(3)
    t.pendown()
    t.fd(3)
    t.circle(6,180)
    t.rt(180)
    t.circle(4,180)
    t.fd(2)

draw3(t)
