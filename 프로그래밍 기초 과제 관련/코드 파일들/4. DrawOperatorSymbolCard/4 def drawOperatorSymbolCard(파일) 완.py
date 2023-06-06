import turtle as t

# 펜 설정
t.speed(0)
t.penup()
t.hideturtle()

#사용 함수 세팅

# 4-1 (α)
def drawCardBackground(t):
    moveto_drawBackCardBorder(t)
    t.fillcolor("#ffffff")
    t.begin_fill()
    drawCardBorder(t,"#ffffff",13)
    t.end_fill()

# 4-1-1 (α-1)
def moveto_drawBackCardBorder(t):
    t.penup()
    t.fd(125)
    t.rt(90)
    t.fd(211)
    t.lt(90)
    t.pendown()

# 4-1-2 (α-2)
def drawCardBorder(t,color,size):
    t.pencolor(color)
    t.pensize(size)
    for i in range(4):
        t.circle(10,90)
        if i % 2 == 0: t.fd(402)
        else: t.fd(250)

# β-1
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

# β-2
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

# 4-2-1
def drawAdd(t):
    drawLongBar(t.clone())
    t.rt(90)
    drawLongBar(t.clone())

# 4-2-2
def drawSub(t):
    drawLongBar(t.clone())

# 4-2-3
def drawMul(t):
    t.rt(45)
    drawLongBar(t.clone())
    t.rt(90)
    drawLongBar(t.clone())

# 4-2-4
def drawDiv(t):
    drawLongBar(t.clone())
    t.rt(90)
    t.fd(30)
    drawDot(t.clone())
    t.bk(60)
    drawDot(t.clone())

# 사용 리스트 세팅
operatorSymbolDrawing_Function_List = [drawAdd, drawSub, drawMul, drawDiv]
operatiorSymbol_Number_Return_List = ["+", "-", "*", "/"]
    
#---------------------------------------------------

def drawOperatorSymbolCard(t,position,operatorSymbol):
    t.setpos(position)
    drawCardBackground(t.clone())
    operatorSymbolDrawing_Function_List[operatiorSymbol_Number_Return_List.index(operatorSymbol)](t.clone())

# 테스트
t.bgcolor("blue")
drawOperatorSymbolCard(t,(0,100),"/")
