nums = []
a = -1
sum = 0
count = 0
while(1):
    a = int(input(""))
    if(a == 0) :
        break
    if(a % 2 == 0) :
        count += 1
        sum += a
print("짝수 합:",int(sum),"평균:",int(sum/count))