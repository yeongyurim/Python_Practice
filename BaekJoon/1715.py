import sys, heapq

input = sys.stdin.readline

n = int(input())

heap = []

result = 0
heapq.heapify(heap)
for _ in range(n) :
    heapq.heappush(heap, int(input()))
while len(heap) > 1 :
    op1 = heapq.heappop(heap)
    op2 = heapq.heappop(heap)
    result += op1 + op2
    heapq.heappush(heap, op1 + op2)
print(result)