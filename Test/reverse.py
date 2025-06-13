n = int(input())
list = ""
for i in range(n) :
    stack = input().split()
    for j in range(len(stack)) :
        list += stack.pop() + " "
    if(i != n-1):
        list += (",")
count = 1
for i in list.split(","):
    print("Case #"+str(count)+":",i)
    count += 1