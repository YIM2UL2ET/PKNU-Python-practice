import turtle as t

# 사용 리스트 초기화
cardCoordList = [-800,-480,-160,160,480,800]

# 펜 설정
t.speed(0)
t.pendown()
t.hideturtle()

# 사용 함수 설정

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
    
def moveto_drawTableCardBorder(t,position):
    t.penup()
    t.setpos(position)
    t.seth(0)
    t.fd(160)
    t.lt(90)
    t.fd(240)
    t.pendown()

def drawTableBorder(t):
    t.pencolor("#57abff")
    t.pensize(20)
    for difference in [300,-300]:
        t.penup()
        t.setpos(-1200, difference)
        t.seth(0)
        t.pendown()
        t.fd(2400)


#--------------------------------------------------------
    
def drawTable(t):

    # 배경 색 설정 및 펜 설정
    t.bgcolor("#1e4e95")
    drawTableBorder(t)
    for location in range(6):
        moveto_drawTableCardBorder(t,(cardCoordList[location],0))
        drawTableCardBorder(t)

# 테스트
drawTable(t)
    

