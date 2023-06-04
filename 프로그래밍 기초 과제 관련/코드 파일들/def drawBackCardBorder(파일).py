import turtle as t

# 펜 설정
t.speed(0)
t.penup()
t.hideturtle()

# 사용 함수 설정 (1개)

def drawBorder(color,size):
    t.pencolor(color)
    t.pensize(size)
    for i in range(4):
        t.circle(10,90)
        if i % 2 == 0: t.fd(402)
        else: t.fd(250)

#------------------------------

def drawBackCardBorder():

    # 그릴 위치로 이동
    t.fd(125)
    t.rt(90)
    t.fd(200)
    t.lt(90)
    t.pendown()

    # 테두리 그리기
    drawBorder("white",10)
    drawBorder("grey",1)
    t.penup()

# 테스트
drawBackCardBorder()
