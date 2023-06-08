import turtle as t
#프로그래밍기초1 104분반 3조 과제 (202313431 임승호)

#펜 설정==========================================================

t.speed(0)
t.pendown()
t.hideturtle()

# 사용 함수 설정==================================================

# 1
def drawTable(t):
    t.bgcolor("#1e4e95")
    drawTableBorder(t)
    for location in range(6):
        moveto_drawTableCardBorder(t,(cardsXCoordList[location],0))
        drawTableCardBorder(t)

#1-1
def drawTableBorder(t):
    t.pencolor("#57abff")
    t.pensize(20)
    for difference in [300,-300]:
        t.penup()
        t.setpos(-1200, difference)
        t.seth(0)
        t.pendown()
        t.fd(2400)

#1-2
def moveto_drawTableCardBorder(t,position):
    t.penup()
    t.setpos(position)
    t.seth(0)
    t.fd(160)
    t.lt(90)
    t.fd(240)
    t.pendown()

# 1-3
def drawTableCardBorder(t):
    t.pencolor("#57abff")
    t.pensize(5)
    t.lt(90)
    t.fd(320)
    t.lt(90)
    t.fd(480)
    t.lt(90)
    t.fd(320)
    t.lt(90)
    t.fd(480)

#---------------------------------------------------------------------

# 2
def drawBackCard(t,position,color,answer):
    if answer.lower() == "no": isForward = False
    else: isForward = True
    t.setpos(position)
    t.seth(0)
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

# 2-1
def moveto_drawPattern(t):
    t.bk(122)
    t.lt(90)
    t.fd(205)
    t.rt(90)

# 2-2
def drawBackGarnet(t,color,isForward):
    backGarnet_Color_Num = ["black", "red", "blue"].index(color.lower())
    if isForward == False: t.lt(180)
    drawBackGarnetBody(t,backGarnet_Color_List[backGarnet_Color_Num])
    drawBackGarnetBorder(t,backGarnet_Color_List[backGarnet_Color_Num][3])
    drawBackGarnetDetails(t,backGarnet_Color_List[backGarnet_Color_Num])

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

# 2-4-2 (α-2)

#---------------------------------------------------------------------

# 3
def drawNumCard(t,position,num):
    t.setpos(position)
    t.seth(0)
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

# 3-1 (α)

# 3-1-1 (α-1)
    
# 3-1-2 (α-2)

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
    t.pencolor("black")
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
    t.pencolor("black")
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
    t.pencolor("black")
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
    t.pencolor("black")
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
    t.pencolor("black")
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
    t.pencolor("black")
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
    t.pencolor("black")
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
    t.pencolor("black")
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
    t.pencolor("black")
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
    t.pencolor("black")
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
    t.pencolor("black")
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

#---------------------------------------------------------------------

# 4
def drawOperatorSymbolCard(t,position,operatorSymbol):
    t.setpos(position)
    t.seth(0)
    drawCardBackground(t.clone())
    operatorSymbolDrawing_Function_List[["+", "-", "*", "/"].index(operatorSymbol)](t.clone())

# 4-1 (α)

# 4-1-1 (α-1)

# 4-1-2 (α-2)

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

#---------------------------------------------------------------------

# α(3-1, 4-1)
def drawCardBackground(t):
    moveto_drawBackCardBorder(t)
    t.fillcolor("#ffffff")
    t.begin_fill()
    drawCardBorder(t,"#ffffff",13)
    t.end_fill()

# α-1 (2-4-1, 3-1-1, 4-1-1)
def moveto_drawBackCardBorder(t):
    t.penup()
    t.fd(125)
    t.rt(90)
    t.fd(211)
    t.lt(90)
    t.pendown()

# α-2 (2-4-2, 3-1-2, 4-1-2)
def drawCardBorder(t,color,size):
    t.pencolor(color)
    t.pensize(size)
    for i in range(4):
        t.circle(10,90)
        if i % 2 == 0: t.fd(402)
        else: t.fd(250)

# β-1 (4-2-1, 4-2-2, 4-2-3, 4-2-4)
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

# β-2 (4-2-1, 4-2-2, 4-2-3, 4-2-4)
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

#사용 리스트 초기화===============================================
    
cardTypeList = []
cardDetailList = []
hiddenAnswerList = []
listOfQuestionWords = ["카드뒷면: Black, Red, Blue 중 하나의 색 입력","숫자카드: 0~10 중 하나의 숫자 입력","연산기호카드: +,-,*,/ 중 하나의 연산기호 입력"]

cardsXCoordList = [-800,-480,-160,160,480,800]
temporary_FronGarnet_CoordList =  [0,[9],[7,11],[7,9,11],[1,5,13,17],[1,5,9,13,17],[0,3,6,12,15,18],[0,3,6,8,12,15,18],[0,3,6,8,10,12,15,18],[0,2,4,6,9,12,14,16,18],[0,2,4,6,19,20,12,14,16,18]]
real_FrontGarnet_CoordList = [[-45,120],[-45,80],[-45,40],[-45,0],[-45,-40],[-45,-80],[-45,-120],[0,100],[0,60],[0,0],[0,-60],[0,-100],[45,120],[45,80],[45,40],[45,0],[45,-40],[45,-80],[45,-120],[0,80],[0,-80]]
numberDrawing_Function_List = [drawZero, draw1, draw2, draw3, draw4, draw5, draw6, draw7, draw8, draw9, draw10]
operatorSymbolDrawing_Function_List = [drawAdd, drawSub, drawMul, drawDiv]
backGarnet_Color_List = [["#f8f9f9","#aeaba2","#4b4c47","#180f00"],["#ffd8d8","#a76565","#893c3c","#832c2c"],["#d9dcff","#6369a6","#3d438a","#2c3382"]]

#=================================================================


# 0 drawPicture(cardTypeList, cardDetailList, HiddenAnswerList)
def drawPicture(cardTypeList, cardDetailList, HiddenAnswerList):
    drawTable(t)
    t.penup()
    for count in range(6):
        if cardTypeList[count].lower() != "p": 
            position = (cardsXCoordList[count],0)
            if cardTypeList[count].lower() == "b":
                drawBackCard(t,position,cardDetailList[count],HiddenAnswerList[0])
                del HiddenAnswerList[0]
            elif cardTypeList[count].lower() == "n": drawNumCard(t,position,cardDetailList[count])
            else: drawOperatorSymbolCard(t,position,cardDetailList[count])
        else: continue

# 전체 시스템
for count in range(6):
    while True:
        cardTypeList .append(input("\n%d번 칸에 들어갈 카드의 종류를 입력하세요. B=카드뒷면, N=숫자카드, O=연산기호카드, P=넣지않음 : " %(count+1)).lower())
        if cardTypeList[count] in ["b","n","o","p"]: break
        del cardTypeList[count]
        print(" 다시 입력하세요.")
    if cardTypeList[count] == "p": cardDetailList.append("Pass")
    else: cardDetailList.append(input("\n방금 입력한 카드에 대한 데이터를 입력하세요. (방금 넣은 카드:%s) : "%(listOfQuestionWords[["b","n","o"].index(cardTypeList[count])])))
    if cardTypeList[count] == "b": hiddenAnswerList.append(input("\n이대로 하시겠습니까? (Yes or No) : "))
try: drawPicture(cardTypeList, cardDetailList, hiddenAnswerList)
except: print("\n그림을 그리는 도중 오류가 발생했습니다. 카드 데이터 정보를 제대로 입력하지 않았을 수도 있습니다.")
else: print("\n그림이 완성되었습니다.")
finally: print("\n프로그램 실행이 종료되었습니다.")
