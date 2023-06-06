import turtle as t

# 펜 설정
t.speed(0)
t.penup()
t.hideturtle()


def drawZero(t):
    t.pensize(2)
    t.fillcolor("#000000")
    t.lt(90)
    t.fd(24)
    t.rt(135)
    t.fd(44)
    t.lt(90)
    t.bk(66)
    t.pendown()
    t.begin_fill()
    t.fd(33)
    t.circle(55,90)
    t.rt(90)
    t.fd(11)
    t.rt(180)
    t.fd(33)
    t.circle(55,90)
    t.end_fill()
    t.penup()

    t.lt(90)
    t.fd(11)
    t.fillcolor("#ffffff")
    t.begin_fill()
    t.circle(55,90)
    t.lt(90)
    t.circle(55,90)
    t.end_fill()
    
drawZero(t)
