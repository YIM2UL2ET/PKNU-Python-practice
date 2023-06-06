import turtle as t

t.speed(0)
t.penup()
t.hideturtle()

def draw8(t):
    t.pensize(4)
    t.penup()
    t.lt(90)
    t.bk(10)
    t.rt(90)
    t.pendown()
    t.circle(6,360)
    t.penup()
    t.lt(90)
    t.fd(12)
    t.rt(90)
    t.pendown()
    t.circle(5,360)

draw8(t)
