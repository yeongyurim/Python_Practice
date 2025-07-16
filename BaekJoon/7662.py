import sys
import heapq

T = int(input())
for _ in range(T) :
    min_heap = []
    max_heap = []
    dic = dict()
    k = int(input())

    for _ in range(k) :
        ch, num = sys.stdin.readline().rstrip().split()
        num = int(num)
        if ch == 'I' :
            if num in dic :
                dic[num] += 1
            else :
                dic[num] = 1
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)
        else :
            if dic :
                if num == 1 :
                    max = -max_heap[0]
                    if dic.get(max,0) > 1 :
                        dic[max] -= 1
                    else :
                        del dic[max]
                        heapq.heappop(max_heap)
                else :
                    min = min_heap[0]
                    if dic[min] == 1 :
                        del dic[min]
                        heapq.heappop(min_heap)
                    else :
                        dic[min] -= 1
            else :
                pass
    if dic :
        print(dic[-heapq.heappop(max_heap)],dic[heapq.heappop(min_heap)])
    else :
        print("EMPTY")