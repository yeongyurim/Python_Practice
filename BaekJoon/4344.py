n = int(input())
for i in range(n) :
    arr = list(map(int,input().split()))
    sum = 0
    count = 0
    for i in range(1,len(arr)):
        sum += arr[i]
    avg = sum/arr[0]
    for i in range(1,len(arr)):
        if arr[i] > avg :
            count += 1
    print( round(count / arr[0] * 100,3),end="")
    print('%')