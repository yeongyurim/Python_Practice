s = list(input(""))
stack = []
result = 0
for i in s:
    if(i == '(' or i == '['):
        stack.append(i)
    elif(i == ')' or i == ']') :
        if not stack :
            result += 1
            continue
        if(i == ')'):
            if (stack.pop() != '(') :
                result += 1
        elif(i == ']'):
            if (stack.pop() != '[') :
                result = "no"
if len(stack) > 0 :
    result += len(stack)
print(result)