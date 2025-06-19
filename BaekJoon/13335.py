from collections import deque

q1 = deque()
q2 = deque()

n, w, L = map(int,input().split())
t = 0
tL = 0
for i in map(int,input().split()) :
    q1.append(i)
    

while 1 :
    if q1 :
        item = q1.popleft()
    else :
        if L >= tL : # 다리에 트럭이 들어갈 수 있는 경우
            t += w
            break
        else : # 다리에 트럭이 들어갈 수 없는 경우
            t += w-len(q2) # 현재 도로 위에 존재하는 트럭 수만큼 제외하고 더한다.
            tL -= q2.popleft()
            continue

    tL += item
    t += 1 # 트럭이 진입하는 시간
    if L >= tL : # 다리에 트럭이 들어갈 수 있는 경우
        q2.append(item)
    else : # 다리에 트럭이 들어갈 수 없는 경우
        t += w-len(q2) # 현재 도로 위에 존재하는 트럭 수만큼 제외하고 더한다.
        tL -= q2.popleft()
        q2.append(item)
        
print(t)