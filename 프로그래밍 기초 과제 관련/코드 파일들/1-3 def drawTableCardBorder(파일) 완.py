import turtle as t

# 펜 설정
t.speed(0)
t.pendown()
t.hideturtle()

#--------------------------------------------------------

def drawTableCardBorder(t):
    t.pencolor("#57abff")
    t.pensize(5)
    t.lt(90)
    t.fd(320)
    t.lt(90)
    t.fd(480)
    t.lt(90)
    t.fd(320)
    t.lt(90)
    t.fd(480)
