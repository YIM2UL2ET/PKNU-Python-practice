import turtle as t

# 사용 리스트 초기화
cardCoordList = [-800,-480,-160,160,480,800]

# 펜 설정
t.speed(0)
t.pendown()
t.hideturtle()

# 사용 함수 초기화 (1개)
def drawTableCardBorder():
    
    # 펜 설정
    t.pencolor("#57abff")
    t.pensize(5)

    # 그릴 위치로 이동
    t.penup()
    t.fd(160)
    t.lt(90)
    t.fd(240)
    t.pendown()
    
    # 그리기
    t.lt(90)
    t.fd(320)
    t.lt(90)
    t.fd(480)
    t.lt(90)
    t.fd(320)
    t.lt(90)
    t.fd(480)


#--------------------------------------------------------
    
def drawTable():

    # 배경 색 설정 및 펜 설정
    t.bgcolor("#1e4e95")
    t.pencolor("#57abff")
    t.pensize(20)
    
    # 테이블 테두리 그리기
    t.penup()
    t.setpos(-1200, 300)
    t.seth(0)
    t.pendown()
    t.fd(2400)

    t.penup()
    t.setpos(-1200, -300)
    t.seth(0)
    t.pendown()
    t.fd(2400)

    for location in range(6):

        # drawTableCardBorder() 함수를 사용할 위치로 이동
        t.penup()
        t.setpos(cardCoordList[location],0)
        t.seth(0)
        t.pendown()
        
        drawTableCardBorder()

# 테스트
drawTable()
    

