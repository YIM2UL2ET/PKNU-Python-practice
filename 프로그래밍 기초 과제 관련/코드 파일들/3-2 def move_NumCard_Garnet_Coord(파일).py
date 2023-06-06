import turtle as t

#리스트 설정
real_FrontGarnet_CoordList = [[-45,120],[-45,90],[-45,60],[-45,30],[-45,0],[-45,-30],[-45,-60],[-45,-90],[-45,-120],[0,90],[0,45],[0,0],[0,-45],[0,-90],[45,120],[45,90],[45,60],[45,30],[45,0],[45,-30],[45,-60],[45,-90],[45,-120]]

def move_NumCard_Garnet_Coord(t,numCoord):
    t.penup()
    t.seth(0)
    t.fd(real_FrontGarnet_CoordList[numCoord][0])
    t.lt(90)
    t.fd(real_FrontGarnet_CoordList[numCoord][1])
    t.rt(90)
    t.pendown()
