import turtle as t

# 3-4-1
def drawFrontGarnetBody(t):
    t.lt(30)
    for bodyColor in ["#ffffff","#d6cfc9","#68645e"]:
        t.fillcolor(bodyColor)
        t.begin_fill()
        t.fd(23)
        t.lt(120)
        t.fd(23)
        t.lt(60)
        t.fd(23)
        t.lt(120)
        t.fd(23)
        t.end_fill()
        t.lt(180)
