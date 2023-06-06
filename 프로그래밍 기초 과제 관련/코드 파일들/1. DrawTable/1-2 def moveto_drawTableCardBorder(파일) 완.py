import turtle as t

# 펜 설정
t.speed(0)
t.pendown()
t.hideturtle()

#--------------------------------------------------------
def moveto_drawTableCardBorder(t,position):
    t.penup()
    t.setpos(position)
    t.seth(0)
    t.fd(160)
    t.lt(90)
    t.fd(240)
    t.pendown()
