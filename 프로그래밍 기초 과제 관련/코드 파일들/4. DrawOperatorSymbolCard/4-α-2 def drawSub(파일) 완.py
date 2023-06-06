import turtle as t

t.hideturtle()
t.speed(0)
t.penup()

# 사용 함수 세팅
def drawLongBar(t):
    t.lt(90)
    t.fd(9)
    t.rt(90)
    t.fd(44)
    t.fillcolor("black")
    t.begin_fill()
    for i in range(4):
        t.rt(90)
        if i % 2 == 0: t.fd(18)
        else: t.fd(88)
    t.end_fill()

def drawDot(t):
    t.lt(90)
    t.fd(9)
    t.rt(90)
    t.fd(9)
    t.fillcolor("black")
    t.begin_fill()
    for i in range(4):
        t.rt(90)
        t.fd(18)
    t.end_fill()

#-------------------------

def drawSub(t):
    drawLongBar(t.clone())

drawSub(t)
