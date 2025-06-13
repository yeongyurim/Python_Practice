menu = 0
machine = dict()
while menu != 3 :
    print("[메뉴]")
    print("1. 과일 등록")
    print("2. 과일 가격 조회")
    print("3. 종료")
    try :
        menu = int(input("메뉴 번호를 선택하세요: "))
    except ValueError :
        print("숫자만을 입력해주세요!")
        print()
        continue
    if menu == 1 :
        name = input("과일 이름: ")
        price = int(input("가격: "))
        machine[name] = price
        script = name+"이(가) 등록되었습니다."
        print(script)
    elif menu == 2 :
        name = input("조회할 과일 이름: ")
        if name in machine :
            script = name + "의 가격은 " + str(machine[name])+"원입니다."
            print(script)
        else :
            print("해당 과일은 등록되어 있지 않습니다.")
    elif menu == 3 :
        pass
    else :
        print("잘못된 메뉴 번호입니다.")
        