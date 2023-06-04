# 스몰 사이즈 (실제 사용하는) 버전

import turtle as t

# 사용 리스트 초기화 및  펜 설정
colorList = [["#f8f9f9","#aeaba2","#4b4c47","#180f00"],["#ffd8d8","#a76565","#893c3c","#832c2c"],["#d9dcff","#6369a6","#3d438a","#2c3382"]]
backGarnet_Color_NumList = ["black", "red", "blue"]
t.speed(0)
t.penup()
t.hideturtle()

#-------------------------------------------------------------------

def drawBackGarnet(color,isForward):

    # 거북이 복사
    t0 = t.clone()

    # 색의 고유숫자 가져오기 (0==black, 1==red, 2==blue)
    backGarnet_Color_Num = backGarnet_Color_NumList.index(color.lower())

    # isForward가 False (정방향인가요? 가 False) 일때 180도 회전 (1)
    if isForward == False: t0.lt(180)
    
    # 마름모 3번 그려서 정육각형 그리기
    t0.lt(30)
    for i in range(3):
        t0.fillcolor(colorList[backGarnet_Color_Num][i])
        t0.begin_fill()
        t0.fd(10)
        t0.lt(120)
        t0.fd(10)
        t0.lt(60)
        t0.fd(10)
        t0.lt(120)
        t0.fd(10)
        t0.end_fill()
        t0.lt(180)
        
    # 테두리 부분 그리기
    t0.fillcolor(colorList[backGarnet_Color_Num][3])
    t0.begin_fill()
    t0.fd(10)
    t0.rt(120)
    for i in range(5):
        t0.fd(10)
        t0.rt(60)
    t0.fd(6)
    t0.rt(120)
    t0.fd(4)
    t0.rt(180)
    t0.circle(1,120)
    t0.fd(1)
    t0.lt(60)
    t0.fd(8)
    t0.lt(60)
    for i in range(3):
        t0.fd(7)
        t0.lt(60)
    t0.fd(4)
    t0.circle(1,120)
    t0.fd(3)
    t0.circle(4,60)
    t0.end_fill()
    
    t0.rt(180)
    t0.fd(3.7)

    # 테두리에 세부적인 부분 추가
    t0.rt(60)
    t0.fd(10)
    t0.fillcolor(colorList[backGarnet_Color_Num][2])
    t0.begin_fill()
    t0.rt(120)
    t0.fd(10)
    t0.rt(120)
    t0.fd(2.8)
    t0.rt(76)
    t0.fd(8.7)
    t0.end_fill()
    t0.lt(135)
    t0.fd(9.9)

    t0.rt(60)
    t0.fd(10)
    t0.begin_fill()
    t0.lt(121)
    t0.fd(10)
    t0.lt(120)
    t0.fd(2.8)
    t0.lt(76)
    t0.fd(8.8)
    t0.end_fill()

    t0.fillcolor(colorList[backGarnet_Color_Num][1])
    t0.begin_fill()
    t0.rt(136)
    t0.fd(2.8)
    t0.lt(77)
    t0.fd(9.3)
    t0.lt(163)
    t0.fd(10.2)
    t0.end_fill()

#테스트
drawBackGarnet("black",False)
    

