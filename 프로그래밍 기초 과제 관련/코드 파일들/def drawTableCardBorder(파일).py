import turtle as t

# 펜 설정
t.speed(0)
t.pendown()
t.hideturtle()

#--------------------------

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

drawTableCardBorder()
