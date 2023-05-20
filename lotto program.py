import random as rn

def lottoNum(): # 복권 번호 추첨
    lotto = []                              # 1.변수 초기화
    i=4
    while i>0:
        n = rn.randint(0,9)                 # 2.번호 추첨
        if n in lotto: continue
        else:
            lotto.append(n)
            i-=1
    lotto.sort()                            # 3.번호 정렬
    return lotto                            # 4.번호 출력


def matchLotto(sel): #복권 번호 맞추기
    global price
    sel.sort()              # 1.입력값 정렬
    num = lottoNum()        # 2.복권 번호 추첨
    i=0
    while i<len(sel):       # 3.못 맞춘 번호 제거
        if sel[i] in num: i+=1
        else: del sel[i]
    print("복권 번호는 %s 입니다."%(num))   # 4.로또 번호 출력
    print("맞춘 숫자는 %s 입니다."%(sel))   # 5.맞춘 숫자 출력

    if len(sel)==4:         # 6. 당첨금 출력
        print("4개를 맞춰 당첨금은 10000원 입니다.")
        return 10000
    elif len(sel)==3:
        print("3개를 맞춰 당첨금은 5000원 입니다.")
        return 5000
    else: return 0

def lottos(): #복권 프로그램
    print("복권 번호를 맞추어보세요")
    price = 0   # 1.상금 초기화

    while True: # 3 에서 'Y'을 입력한 경우 프로그램 반복
        sel = list(map(int,input("\n네 개의 숫자를 입력하세요: ").split())) # 1.값 입력

        price += matchLotto(sel)    # 2. 당첨금 추가

        while True: # 3. 추가 질문
            ask = input("또 하시겠습니까? (네:Y 아니오:N)")
            if ask.lower() == "y" or ask.lower() == "n": break
            print("다시 한번 입력하세요.")  # 3 에서 'Y' 나 'N' 이 아닌 다른것을 입력한 경우
            continue
        if ask.lower() == "y": continue
        break

    print("\n총 당첨금은 %d원 입니다."%(price)) # 3 에서 'N'를 입력한 경우 당첨금 출력

lottos()
