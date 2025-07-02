import heapq
import sys
input = sys.stdin.readline
n = int(input())

pheap = []
mheap = []

heapq.heapify(pheap)
heapq.heapify(mheap)

for _ in range(n) : # _는 변수를 안쓰는 관행이라고 한다.
    new = int(input())
    if new == 0 :
        if not pheap and not mheap :
            print(0)
        elif not mheap :
            print(heapq.heappop(pheap))
        elif not pheap :
            print(-heapq.heappop(mheap))
        else :
            mmin = mheap[0] # 최소힙도 인덱스 접근이 가능하다.
            pmin = 0
            if mheap[0] > pheap[0] :
                print(heapq.heappop(pheap))
            else :
                print(-heapq.heappop(mheap))
    else :
        if new < 0 :
            heapq.heappush(mheap,-new)
        else :
            heapq.heappush(pheap,new)
# 가장 좋은 형태는 힙을 하나만 쓰고 튜플을 이용하여 절댓값과 원래값을 동시에 넣고 비교하는 방식이다.