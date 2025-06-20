import sys
line = sys.stdin.readline

st = line()
result = []
while st[0] != "-":
    stack = []
    count = 0
    for i in st :
        if i == '{' :
            stack.append(i)
        else :
            if stack :
                popped = stack.pop()
                if popped != '{' :
                    count += 1
            else :
                count += 1
    if stack :
        count += len(stack)
    result.append(count)
    st = line()

for idx, i in enumerate(result) :
    print(str(idx+1)+".",i)
