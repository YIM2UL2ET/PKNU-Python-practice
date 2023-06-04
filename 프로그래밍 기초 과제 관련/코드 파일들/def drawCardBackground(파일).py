import turtle as t

# 펜 설정
t.speed(0)
t.penup()
t.hideturtle()

def drawCardBackground():

    # 그릴 위치로 이동
    t.fd(125)
    t.rt(90)
    t.fd(200)
    t.lt(90)

    # 채움색 설정 및 그리기
    t.fillcolor("grey")
    t.begin_fill()
    for i in range(4):
        t.circle(10,90)
        if i % 2 == 0: t.fd(402)
        else: t.fd(250)
    t.end_fill()

# 테스트
drawCardBackground()
