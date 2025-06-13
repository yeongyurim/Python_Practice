from collections import deque
queue = deque()

n = int(input())
result = ""
for i in range(1,n+1) :
    queue.append(i)
while(len(queue) >= 2) :
    result += (str(queue.popleft()) + " ")
    queue.append(queue.popleft())
result += (str(queue.popleft()) + " ")
print(result.strip())