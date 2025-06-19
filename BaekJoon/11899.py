s = list(input(""))
stack = []
result = 0
for i in s:
    if(i == '('):
        stack.append(i)
    elif(i == ')') : 
        if not stack : # 열린 것이 없는 경우 + 1
            result += 1
            continue
        else : 
            stack.pop()
if len(stack) > 0 : 
    result += len(stack) # 닫힌 것이 없는 경우 + 1
print(result)