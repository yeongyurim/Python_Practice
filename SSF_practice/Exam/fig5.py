year = int(input("에제 입력: "))
while(year != 0):
    if(year % 400 == 0):
        print(1)
    elif(year % 4 == 0 and year % 100 != 0):
        print(1)
    else:
        print(0)
    year = int(input("예제 입력: "))