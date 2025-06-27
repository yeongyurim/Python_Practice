import heapq
import sys
input = sys.stdin.readline
n = int(input())

li = []
heapq.heapify(li)
for i in range(n) :
    new = int(input())
    if new == 0 :
        if li :
            print(-heapq.heappop(li))
        else : 
            print(0)
    else :
        heapq.heappush(li, -new)