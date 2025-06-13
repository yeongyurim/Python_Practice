i = int(input("입력:"))
sum = 0
avg = 0
count = 0
while(0<=i<=100):
    sum += i
    count += 1
    i = int(input())
avg = sum/count
print("출력:")
print("sum :",sum)
print("avg :", avg)