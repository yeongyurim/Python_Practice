from collections import deque
queue = deque()
n = 0
st = input()
prev = ''
for i in st:
    if i == '(' :
        queue.append(i)
    else :
        if prev == ')' : # 쇠막대기 끝부분
            n += 1
            queue.popleft()
        else : # 레이저
            queue.popleft() 
            n += len(queue) 
    prev = i
print(n)