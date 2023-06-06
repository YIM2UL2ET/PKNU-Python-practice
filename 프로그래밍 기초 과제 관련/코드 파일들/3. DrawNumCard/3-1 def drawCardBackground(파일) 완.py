import turtle as t

#함수 세팅
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
    t.fd(211)
    t.lt(90)
    t.pendown()

#----------------------------
def drawCardBackground(t):
    moveto_drawBackCardBorder(t)
    t.fillcolor("#ffffff")
    t.begin_fill()
    drawCardBorder(t,"#ffffff",13)
    t.end_fill()

#테스트
drawCardBackground(t)
