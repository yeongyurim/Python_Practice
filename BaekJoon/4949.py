resultList = []

while True :
    s = list(input(""))
    if s[0] == '.':
        break
    stack = []
    result = "yes"
    for i in s:
        if(i == '(' or i == '['):
            stack.append(i)
        elif(i == ')' or i == ']') :
            if not stack :
                result = "no"
                break
            if(i == ')'):
                if (stack.pop() != '(') :
                    result = "no"
            elif(i == ']'):
                if (stack.pop() != '[') :
                    result = "no"
    if len(stack) > 0 :
        result = "no"
    resultList.append(result)
for i in resultList:
    print(i)