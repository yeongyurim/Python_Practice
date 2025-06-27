import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n) :
    for j in input().split() :
        heapq.heappush(heap, int(j))
        if len(heap) > n :
            heapq.heappop(heap)
print(int(heapq.heappop(heap)))
