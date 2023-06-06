import turtle as t

# 3-4-2
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
