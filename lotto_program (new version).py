#2023년 5월 23일 / 새 함수 활용 및 피드백을 고려하여 복습 (직접 제작 X)
#프로그래밍 기초1 수업때 보았던것을 복기하여 제작한것이므로 인터넷에 게시해선 안됨

import random as rn

def matchLotto(secret,guess):   # 함수 제작시 목적 (입력과 출력)을 명확하게 하기
    matchNum = []
    for num in guess:
        num = int(num)  # guess 자체를 숫자 list로 바꾸어도 되지만, 이때만 안쪽 값이 숫자가 되어 사용되므로 불필요한 변형을 하지 않아도 됨
        if num in secret: matchNum.append(num)
    return matchNum

print("복권을 맞춰보세요")
totalPrice = 0
while True:
    secret = sorted(rn.sample(range(1,10),4))   # 더 간단해질 수 있도록 다양한 함수 및 명령어 찾아보기 (sample 명령어)
    guess = input("숫자를 말해보세요").split()
    matchNum = matchLotto(secret,guess)

    print("복권 숫자는 ", secret, " 입니다.")
    print("맞춘 숫자는 ", matchNum, " 입니다.")

    prize = [0,0,0,5000,10000]  # 당첨금의 값만 변형되어서 사용되므로 리스트화 해서 활용 가능
    if len(matchNum) > 0:
        print("당첨금은 ", prize[len(matchNum)], "원 입니다.")
        totalPrice += prize[len(matchNum)]

    if input("계속 하시겠습니까?: ").lower() != "y":
        print("총 당첨금은 %d 원입니다."%totalPrice)
        break
