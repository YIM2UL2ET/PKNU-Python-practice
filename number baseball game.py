import random as rn

def matching (secret, guess):
    i=0
    strike = 0
    ball = 0
    for num in guess:
        num = int(num)
        if num in secret:
            if num == secret[i]: strike +=1
            else: ball +=1
        i +=1
    return [strike, ball]

def playGame(): # 성공이면 1, 실패하면 0
    secret = rn.sample(range(1,10),3)
    for chance in range(10,0,-1):
        print("\n남은 기회는  %d번 입니다."%chance)
        guess = input("서로 중복되지 않는 숫자 3개를 입력해주세요: ").split()
        matchList = matching(secret, guess)
        if matchList == [3,0]:
            print("추측 성공입니다!")
            return 1
        elif matchList == [0,0]: print("OUT 입니다.")
        else: print("%s스트라이크, %s볼 입니다,"%(matchList[0],matchList[1]))
    else:
        print("비밀 숫자는 %s였습니다."%secret)
        return 0


print("숫자 야구 게임입니다.")
playCount = 0
successCount = 0
while True:
    playCount +=1
    successCount += playGame()
    if input("\n게임을 %d번 했고, 그중에서 %d번 성공하셨습니다. 계속 하시겠습니까?: "%(playCount, successCount)).lower() !="y": break
