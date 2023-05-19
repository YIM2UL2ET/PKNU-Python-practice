import turtle as t

def colorChange(colorNum):                 #숫자에 따른 펜의 색 변경
    if colorNum==0: t.pencolor("red")
    elif colorNum==1: t.pencolor("orange")
    elif colorNum==2: t.pencolor("yellow")
    elif colorNum==3: t.pencolor("green")
    elif colorNum==4: t.pencolor("blue")
    elif colorNum==5: t.pencolor("purple")
    else: t.pencolor("pink")


def drawPicture(lineSize,pictureSize,firstColorNum):
    t.speed(0)              #그리는 속도 지정
    t.bgcolor("black")      #배경색 설정
    t.pensize(lineSize)     #선 굵기 설정

    colorNum=firstColorNum  #색 초깃값 설정
    i=1                     #선 길이 초깃값 설정
    while pictureSize>0:
        colorChange(colorNum)       #색 변경
        if colorNum>0: colorNum-=1  #색 넘버값 변경
        else: colorNum+=6
        t.rt(360/7-0.5)             #펜의 각도 변경
        t.fd(i)                     #선 긋기
        i+=1                        #다음에 그릴 선의 길이 늘이기
        pictureSize-=1

drawPicture(1,260,3)

#아이디어 참조:https://blog.naver.com/PostView.naver?blogId=python_math&logNo=221214850769&parentCategoryNo=&categoryNo=8&viewDate=&isShowPopularPosts=true&from=search
