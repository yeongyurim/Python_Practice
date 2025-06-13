num = int(input("입력: "))
sum = 0
count = 0
while(num != 0):
    if(num % 2 == 1):
        sum += num
        count += 1
    num = int(input())
print("출력:",sum,int(sum/count))