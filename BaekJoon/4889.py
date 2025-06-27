import sys
line = sys.stdin.readline

st = line().rstrip()
j = 0
while st[0] != "-":
    stack = []
    count = 0
    for i in st :
        if i == '{' :
            stack.append(i)
        else :
            if stack :
                stack.pop()
            else :
                count += 1
                stack.append('{')
    if stack :
        count += len(stack) // 2
    j += 1
    print(str(j)+".",str(count))
    st = line().rstrip()
