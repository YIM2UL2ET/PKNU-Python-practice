import turtle as t

# 펜 설정
t.speed(0)
t.penup()
t.hideturtle()

# 사용 리스트 t설정
colorList = [["#f8f9f9","#aeaba2","#4b4c47","#180f00"],["#ffd8d8","#a76565","#893c3c","#832c2c"],["#d9dcff","#6369a6","#3d438a","#2c3382"]]
backGarnet_Color_NumList = ["black", "red", "blue"]

# 2-1
def moveto_drawPattern(t):
    t.bk(122)
    t.lt(90)
    t.fd(205)
    t.rt(90)

# 2-2
def drawBackGarnet(t,color,isForward):
    backGarnet_Color_Num = backGarnet_Color_NumList.index(color.lower())
    if isForward == False: t.lt(180)
    drawBackGarnetBody(t,colorList[backGarnet_Color_Num])
    drawBackGarnetBorder(t,colorList[backGarnet_Color_Num][3])
    drawBackGarnetDetails(t,colorList[backGarnet_Color_Num])

# 2-2-1
def drawBackGarnetBody(t,colorList):
    t.lt(30)
    for i in range(3):
        t.fillcolor(colorList[i])
        t.begin_fill()
        t.fd(10)
        t.lt(120)
        t.fd(10)
        t.lt(60)
        t.fd(10)
        t.lt(120)
        t.fd(10)
        t.end_fill()
        t.lt(180)
# 2-2-2
def drawBackGarnetBorder(t,color):
    t.fillcolor(color)
    t.begin_fill()
    t.fd(10)
    t.rt(120)
    for i in range(5):
        t.fd(10)
        t.rt(60)
    t.fd(6)
    t.rt(120)
    t.fd(4)
    t.rt(180)
    t.circle(1,120)
    t.fd(1)
    t.lt(60)
    t.fd(8)
    t.lt(60)
    for i in range(3):
        t.fd(7)
        t.lt(60)
    t.fd(4)
    t.circle(1,120)
    t.fd(3)
    t.circle(4,60)
    t.end_fill()
    
    t.rt(180)
    t.fd(3.7)

# 2-2-3
def drawBackGarnetDetails(t,colorList):
    t.rt(60)
    t.fd(10)
    t.fillcolor(colorList[2])
    t.begin_fill()
    t.rt(120)
    t.fd(10)
    t.rt(120)
    t.fd(2.8)
    t.rt(76)
    t.fd(8.7)
    t.end_fill()
    t.lt(135)
    t.fd(9.9)

    t.rt(60)
    t.fd(10)
    t.begin_fill()
    t.lt(121)
    t.fd(10)
    t.lt(120)
    t.fd(2.8)
    t.lt(76)
    t.fd(8.8)
    t.end_fill()

    t.fillcolor(colorList[1])
    t.begin_fill()
    t.rt(136)
    t.fd(2.8)
    t.lt(77)
    t.fd(9.3)
    t.lt(163)
    t.fd(10.2)
    t.end_fill()

# 2-3
def moveOneSellDown(t):
    t.bk(270)
    t.rt(90)
    t.fd(15)
    t.lt(90)

# 2-4
def drawBackCardBorder(t):
    moveto_drawBackCardBorder(t)
    drawCardBorder(t,"white",13)
    drawCardBorder(t,"grey",1)
    t.penup()

# 2-4-1 (α-1)
def moveto_drawBackCardBorder(t):
    t.penup()
    t.fd(125)
    t.rt(90)
    t.fd(211)
    t.lt(90)
    t.pendown()

# 2-4-2 (α-2)
def drawCardBorder(t,color,size):
    t.pencolor(color)
    t.pensize(size)
    for i in range(4):
        t.circle(10,90)
        if i % 2 == 0: t.fd(402)
        else: t.fd(250)

#------------------------------
    
def drawBackCard(t,position,color,answer):
    if answer.lower() == "no": isForward = False
    else: isForward = True
    t.setpos(position)
    moveto_drawPattern(t)
    for lengthCount in range(28):
        for widthCount in range(15):
            drawBackGarnet(t.clone(),color,isForward)
            t.fd(18)
        moveOneSellDown(t)
        if lengthCount % 2 == 0: t.bk(9)
        else: t.fd(9)
    t.setpos(position)
    drawBackCardBorder(t)

# 테스트
drawBackCard(t,(0,0),"black","yes")
