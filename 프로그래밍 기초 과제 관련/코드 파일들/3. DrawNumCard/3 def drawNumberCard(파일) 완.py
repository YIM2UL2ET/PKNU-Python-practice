import turtle as t

# 펜 설정
t.speed(0)
t.penup()
t.hideturtle()


#사용할 함수 설정

# 3-1 (α)
def drawCardBackground(t):
    moveto_drawBackCardBorder(t)
    t.fillcolor("#ffffff")
    t.begin_fill()
    drawCardBorder(t,"#ffffff",13)
    t.end_fill()

# 3-1-1 (α-1)
def moveto_drawBackCardBorder(t):
    t.penup()
    t.fd(125)
    t.rt(90)
    t.fd(211)
    t.lt(90)
    t.pendown()
    
# 3-1-2 (α-2)
def drawCardBorder(t,color,size):
    t.pencolor(color)
    t.pensize(size)
    for i in range(4):
        t.circle(10,90)
        if i % 2 == 0: t.fd(402)
        else: t.fd(250)

# 3-2
def move_NumCard_Garnet_Coord(t,numCoord):
    t.penup()
    t.seth(0)
    t.fd(real_FrontGarnet_CoordList[numCoord][0])
    t.lt(90)
    t.fd(real_FrontGarnet_CoordList[numCoord][1])
    t.rt(90)

# 3-3
def drawFrontGarnet(t,isForward):
    if isForward == False:t.rt(180)
    drawFrontGarnetBody(t)
    drawFrontGarnetBorder(t)

# 3-3-1
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

# 3-3-2
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

# 3-4
def moveto_drawNum(t):
    t.penup()
    t.fd(115)
    t.rt(90)
    t.fd(185)
    t.rt(90)

# 3-5-0 
def drawZero(t):
    t.pensize(2)
    t.fillcolor("#000000")
    t.lt(90)
    t.fd(24)
    t.rt(135)
    t.fd(44)
    t.lt(90)
    t.bk(66)
    t.pendown()
    t.begin_fill()
    t.fd(33)
    t.circle(55,90)
    t.rt(90)
    t.fd(11)
    t.rt(180)
    t.fd(33)
    t.circle(55,90)
    t.end_fill()
    t.penup()

    t.lt(90)
    t.fd(11)
    t.fillcolor("#ffffff")
    t.begin_fill()
    t.circle(55,90)
    t.lt(90)
    t.circle(55,90)
    t.end_fill()

# 3-5-1
def draw1(t):
    t.pensize(4)
    t.penup()
    t.lt(90)
    t.bk(10)
    t.pendown()
    t.fd(20)
    t.lt(150)
    t.fd(5)

# 3-5-2
def draw2(t):
    t.pensize(4)
    t.penup()
    t.fd(12)
    t.lt(90)
    t.bk(10)
    t.lt(90)
    t.fd(6)
    t.pendown()
    t.fd(10)
    t.rt(130)
    t.fd(9)
    t.circle(9,90)
    t.lt(90)
    t.fd(5)

# 3-5-3
def draw3(t):
    t.pensize(4)
    t.penup()
    t.lt(90)
    t.bk(10)
    t.rt(90)
    t.bk(3)
    t.pendown()
    t.fd(3)
    t.circle(6,180)
    t.rt(180)
    t.circle(4,180)
    t.fd(2)

# 3-5-4
def draw4(t):
    t.pensize(4)
    t.penup()
    t.lt(90)
    t.bk(10)
    t.pendown()
    t.fd(20)
    t.lt(145)
    t.fd(14)
    t.lt(125)
    t.fd(10)

# 3-5-5
def draw5(t):
    t.pensize(4)
    t.penup()
    t.lt(90)
    t.bk(10)
    t.rt(90)
    t.bk(2)
    t.pendown()
    t.fd(2)
    t.circle(8,90)
    t.circle(6,120)
    t.rt(140)
    t.fd(7)
    t.rt(60)
    t.fd(6)

# 3-5-6
def draw6(t):
    t.pensize(4)
    t.bk(3)
    t.penup()
    t.lt(90)
    t.bk(10)
    t.pendown()
    t.rt(90)
    t.circle(7,180)
    t.penup()
    t.rt(90)
    t.bk(14)
    t.pendown()
    t.lt(16)
    t.fd(7)
    t.rt(24)
    t.fd(13)
    t.rt(30)
    t.fd(5)
    t.rt(70)
    t.fd(3)

# 3-5-7
def draw7(t):
    t.pensize(4)
    t.penup()
    t.lt(90)
    t.bk(10)
    t.pendown()
    t.rt(20)
    t.fd(21)
    t.lt(110)
    t.fd(10)

# 3-5-8
def draw8(t):
    t.pensize(4)
    t.penup()
    t.lt(90)
    t.bk(10)
    t.rt(90)
    t.pendown()
    t.circle(6,360)
    t.penup()
    t.lt(90)
    t.fd(12)
    t.rt(90)
    t.pendown()
    t.circle(5,360)

# 3-5-9
def draw9(t):
    t.pensize(4)
    t.penup()
    t.rt(175)
    t.lt(90)
    t.bk(10)
    t.pendown()
    t.rt(90)
    t.circle(7,180)
    t.penup()
    t.rt(90)
    t.bk(14)
    t.pendown()
    t.lt(16)
    t.fd(7)
    t.rt(24)
    t.fd(13)
    t.rt(30)
    t.fd(5)
    t.rt(70)
    t.fd(3)
    t.rt(30)
    t.fd(2)

# 3-5-10
def draw10(t):
    t.pensize(4)
    t.penup()
    t.bk(5)
    t.lt(90)
    t.bk(10)
    t.pendown()
    t.fd(20)
    t.rt(30)
    t.bk(5)
    t.rt(60)
    t.penup()
    t.fd(13)
    t.lt(90)
    t.bk(16)
    t.rt(90)
    t.pendown()
    t.circle(6,80)
    t.fd(5)
    t.lt(20)
    t.fd(5)
    t.circle(6,160)
    t.fd(5)
    t.lt(20)
    t.fd(5)
    t.circle(6,80)

# 사용 리스트 세팅
temporary_FronGarnet_CoordList =  [0,[9],[7,11],[7,9,11],[1,5,13,17],[1,5,9,13,17],[0,3,6,12,15,18],[0,3,6,8,12,15,18],[0,3,6,8,10,12,15,18],[0,2,4,6,9,12,14,16,18],[0,2,4,6,19,20,12,14,16,18]]
real_FrontGarnet_CoordList = [[-45,120],[-45,80],[-45,40],[-45,0],[-45,-40],[-45,-80],[-45,-120],[0,100],[0,60],[0,0],[0,-60],[0,-100],[45,120],[45,80],[45,40],[45,0],[45,-40],[45,-80],[45,-120],[0,80],[0,-80]]
numberDrawing_Function_List = [drawZero, draw1, draw2, draw3, draw4, draw5, draw6, draw7, draw8, draw9, draw10]

#----------------------------------
def drawNumCard(t,position,num):
    t.setpos(position)
    drawCardBackground(t.clone())
    t.setpos(position)
    if int(num) == 0: drawZero(t)
    else:
        for numCoord in temporary_FronGarnet_CoordList[int(num)]:
            tClone = t.clone()
            move_NumCard_Garnet_Coord(tClone,numCoord)
            if numCoord in [4,5,6,10,11,16,17,18,20]: drawFrontGarnet(tClone,False)
            else: drawFrontGarnet(tClone,True)
        for i in [0,180]:
            t.setpos(position)
            t.seth(i)
            moveto_drawNum(t)
            numberDrawing_Function_List[int(num)](t.clone())
        
#테스트
t.bgcolor("blue")
drawNumCard(t,(0,0),6)
