from queue import Queue
queue = Queue()
n ,k = map(int, input().split())
for i in range(1,n+1) :
    queue.put(i)
while queue.qsize() > 1 :
    top = queue.get()
    for i in range(k-1) :
        if not queue.empty() :
            queue.get()
    queue.put(top)
print(queue.get())
