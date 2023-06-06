import turtle as t

#리스트 설정
real_FrontGarnet_CoordList = [[-45,120],[-45,80],[-45,40],[-45,0],[-45,-40],[-45,-80],[-45,-120],[0,100],[0,60],[0,0],[0,-60],[0,-100],[45,120],[45,80],[45,40],[45,0],[45,-40],[45,-80],[45,-120],[0,80],[0,-80]]

def move_NumCard_Garnet_Coord(t,numCoord):
    t.penup()
    t.seth(0)
    t.fd(real_FrontGarnet_CoordList[numCoord][0])
    t.lt(90)
    t.fd(real_FrontGarnet_CoordList[numCoord][1])
    t.rt(90)
