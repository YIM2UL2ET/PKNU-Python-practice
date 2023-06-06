import turtle as t

t.speed(0)
t.penup()
t.hideturtle()

def draw5(t):
    t.pensize(4)
    t.penup()
    t.lt(90)
    t.bk(10)
    t.rt(90)
    t.bk(2)
    t.pendown()
    t.fd(2)
    t.circle(8,90)
    t.circle(6,120)
    t.rt(140)
    t.fd(7)
    t.rt(60)
    t.fd(6)

draw5(t)
