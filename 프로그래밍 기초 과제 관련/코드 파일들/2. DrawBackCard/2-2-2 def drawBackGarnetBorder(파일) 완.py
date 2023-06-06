import turtle as t

#2-2-2
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
