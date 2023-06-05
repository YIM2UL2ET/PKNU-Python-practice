import turtle as t

# 2-2-1
def drawBackGarnetBody(t,colorList):
    t0.lt(30)
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
