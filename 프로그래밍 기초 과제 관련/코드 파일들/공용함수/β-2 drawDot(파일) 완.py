import turtle as t

# 4-β-2
def drawDot(t):
    t.lt(90)
    t.fd(9)
    t.rt(90)
    t.fd(9)
    t.fillcolor("black")
    t.begin_fill()
    for i in range(4):
        t.rt(90)
        t.fd(18)
    t.end_fill()
