import turtle as t

# 펜 설정
t.speed(0)
t.penup()
t.hideturtle()

# 함수 세팅

def drawFrontGarnetBody(t):
    t.lt(30)
    for bodyColor in ["#ffffff","#d6cfc9","#68645e"]:
        t.fillcolor(bodyColor)
        t.begin_fill()
        t.fd(23)
        t.lt(120)
        t.fd(23)
        t.lt(60)
        t.fd(23)
        t.lt(120)
        t.fd(23)
        t.end_fill()
        t.lt(180)

def drawFrontGarnetBorder(t):
    t.fillcolor("#000000")
    t.begin_fill()
    t.fd(23)
    t.rt(120)
    for i in range(5):
        t.fd(23)
        t.rt(60)
    t.fd(7)
    t.rt(120)
    t.fd(23)
    for i in range(3):
        t.lt(60)
        t.fd(16)
    t.lt(60)
    t.fd(6)
    t.circle(4,120)
    t.fd(3)
    t.circle(10,60)
    t.rt(180)
    t.fd(7)
    t.end_fill()

    t.fd(34)
    t.lt(170) 
    t.begin_fill()
    t.circle(11,70)
    t.fd(10)
    t.rt(120)
    t.fd(12)
    t.rt(180)
    t.circle(3,120)
    t.fd(10)
    t.end_fill()
    t.seth(0)

#--------------------------------
    
def drawFrontGarnet(t,isForward):
    if isForward == False:t.rt(180)
    drawFrontGarnetBody(t)
    drawFrontGarnetBorder(t)

#테스트
    
drawFrontGarnet(t,True)
t.setpos(100,0)
drawFrontGarnet(t,False)
