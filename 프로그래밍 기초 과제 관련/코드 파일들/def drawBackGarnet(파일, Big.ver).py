# 빅 사이즈 버전

import turtle as t

# 사용 리스트 초기화 및  펜 설정
colorList = [["#f8f9f9","#aeaba2","#4b4c47","#180f00"],["#ffd8d8","#a76565","#893c3c","#832c2c"],["#d9dcff","#6369a6","#3d438a","#2c3382"]]
backGarnet_Color_NumList = ["black", "red", "blue"]
t.speed(0)
t.penup()
t.hideturtle()

#-------------------------------------------------------------------

def drawBackGarnet(color,isForward):

    # 색의 고유숫자 가져오기 (0==black, 1==red, 2==blue)
    backGarnet_Color_Num = backGarnet_Color_NumList.index(color.lower())

    # isForward가 False (정방향인가요? 가 False) 일때 180도 회전 (1)
    if isForward == False: t.lt(180)
    
    # 마름모 3번 그려서 정육각형 그리기
    t.lt(30)
    for i in range(3):
        t.fillcolor(colorList[backGarnet_Color_Num][i])
        t.begin_fill()
        t.fd(100)
        t.lt(120)
        t.fd(100)
        t.lt(60)
        t.fd(100)
        t.lt(120)
        t.fd(100)
        t.end_fill()
        t.lt(180)
        
    # 테두리 부분 그리기
    t.fillcolor(colorList[backGarnet_Color_Num][3])
    t.begin_fill()
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.rt(60)
    t.fd(100)
    t.rt(60)
    t.fd(100)
    t.rt(60)
    t.fd(100)
    t.rt(60)
    t.fd(100)
    t.rt(60)
    t.fd(60)
    t.rt(120)
    t.fd(40)
    t.rt(180)
    t.circle(10,120)
    t.fd(10)
    t.lt(60)
    t.fd(80)
    t.lt(60)
    t.fd(70)
    t.lt(60)
    t.fd(70)
    t.lt(60)
    t.fd(70)
    t.lt(60)
    t.fd(40)
    t.circle(10,120)
    t.fd(30)
    t.circle(40,60)
    t.end_fill()
    
    t.rt(180)
    t.fd(37)

    # 테두리에 세부적인 부분 추가
    t.rt(60)
    t.fd(100)
    t.fillcolor(colorList[backGarnet_Color_Num][2])
    t.begin_fill()
    t.rt(120)
    t.fd(100)
    t.rt(120)
    t.fd(28)
    t.rt(76)
    t.fd(87)
    t.end_fill()
    t.lt(135)
    t.fd(99)

    t.rt(60)
    t.fd(100)
    t.begin_fill()
    t.lt(121)
    t.fd(100)
    t.lt(120)
    t.fd(28)
    t.lt(76)
    t.fd(88)
    t.end_fill()

    t.fillcolor(colorList[backGarnet_Color_Num][1])
    t.begin_fill()
    t.rt(136)
    t.fd(28)
    t.lt(77)
    t.fd(93)
    t.lt(163)
    t.fd(102)
    t.end_fill()

    t.pendown()
    t.pencolor("red")
    t.fd(2)
    t.lt(120)
    t.fd(102)
    t.lt(30)

    #isForward가 False (정방향인가요? 가 False) 일때 180도 회전 (2)
    if isForward == False: t.lt(180)

#테스트
drawBackGarnet("black",True)
