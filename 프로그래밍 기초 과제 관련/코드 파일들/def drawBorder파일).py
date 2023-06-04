import turtle as t

# 펜 설정
t.speed(0)
t.penup()
t.hideturtle()

#----------------------

def drawBorder(color,size):
    t.pendown()
    t.pencolor(color)
    t.pensize(size)
    for i in range(4):
        t.circle(10,90)
        if i % 2 == 0: t.fd(402)
        else: t.fd(250)

# 테스트
drawBorder("black",5)
