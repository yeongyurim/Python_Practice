import sys, heapq

input = sys.stdin.readline
n ,k = map(int,input().split())

jewel = [] 
bag = []
jewel2 = [] 
result = 0

for _ in range(n) :
    m ,v = map(int,input().split())
    heapq.heappush(jewel,(m,v))
for _ in range(k) :
    heapq.heappush(bag,int(input()))

while bag :
    max = 0
    c = heapq.heappop(bag)

    while jewel and jewel[0][0] <= c :
        heapq.heappush(jewel2,-heapq.heappop(jewel)[1])
    if jewel2:
        result += -heapq.heappop(jewel2)

print(result)