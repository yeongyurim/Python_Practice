from collections import deque

n ,k = map(int, input().split())
li = [i for i in range(1,n+1)]
deq = deque(li)

while len(deq) > 1 :
    deq.rotate(-1) # 양의 정수시 뒤에 것이 앞으로 음의 정수시 앞의 것이 뒤로
    for i in range(k-1) :
        if len(deq) == 1 : # queue에 하나 밖에 안남으면 break
            break
        deq.popleft()
print(deq.pop())    