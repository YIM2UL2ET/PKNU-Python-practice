import turtle as t

# 펜 설정
t.speed(0)
t.penup()
t.hideturtle()

# 사용 함수 설정 (2개)

def drawCardBorder(t,color,size):
    t.pencolor(color)
    t.pensize(size)
    for i in range(4):
        t.circle(10,90)
        if i % 2 == 0: t.fd(402)
        else: t.fd(250)

def moveto_drawBackCardBorder(t):
    t.penup()
    t.fd(125)
    t.rt(90)
    t.fd(200)
    t.lt(90)
    t.pendown()

#------------------------------

def drawBackCardBorder(t):
    moveto_drawBackCardBorder(t)
    drawCardBorder(t,"white",10)
    drawCardBorder(t,"grey",1)
    t.penup()

# 테스트
drawBackCardBorder(t)
