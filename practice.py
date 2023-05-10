import turtle as t


def colorChange():          #색 바꾸기 함수
    global i
    if i<=6:
        if i==2: t.pencolor("orange")
        elif i==3: t.pencolor("yellow")
        elif i==4: t.pencolor("green")
        elif i==5: t.pencolor("blue")
        else: t.pencolor("purple")
        i+=1
    else:
        t.pencolor("red")
        i-=5

t.speed(0)          #그리는 속도
t.pensize(2)        #선 굵기
t.bgcolor("black")  #배경 색
n=150               #선 개수
j=10                #처음 선길이
i=3                 #색 초기값
while n>0:
    colorChange()
    t.fd(j)
    t.rt(91)
    j+=5
    n-=1
