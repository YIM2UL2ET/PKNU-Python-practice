import turtle as t

# 펜 설정
t.speed(0)
t.pendown()
t.hideturtle()

#--------------------------------------------------------
def drawTableBorder(t):
    t.pencolor("#57abff")
    t.pensize(20)
    for difference in [300,-300]:
        t.penup()
        t.setpos(-1200, difference)
        t.seth(0)
        t.pendown()
        t.fd(2400)
