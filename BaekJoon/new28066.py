n ,k = map(int, input().split())
queue = [i for i in range(1,n+1)]
top = 0
while len(queue) > 1 :
    top = queue[0]
    if len(queue) > k:
        queue = queue[k:]
    else : 
        break
    queue.append(top)
print(top)