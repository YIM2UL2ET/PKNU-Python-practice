import turtle as t

t.speed(0)
t.penup()
t.hideturtle()

def draw1(t):
    t.pensize(4)
    t.penup()
    t.lt(90)
    t.bk(10)
    t.pendown()
    t.fd(20)
    t.lt(150)
    t.fd(5)

draw1(t)
