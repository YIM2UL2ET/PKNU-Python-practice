import turtle as t

# 펜 설정
t.speed(0)
t.pendown()
t.hideturtle()

#--------------------------------------------------------

def drawTableCardBorder(t):
    t.pencolor("#57abff")
    t.pensize(5)
    for i in range(4):
        t.lt(90)
        if i % 2 == 0: t.fd(320)
        else: t.fd(480)
