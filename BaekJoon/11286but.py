import queue
import sys

q = queue.PriorityQueue()
n = int(sys.stdin.readline().rstrip())

class _abs :
    def __init__(self, num):
        self.num = num
    
    def __lt__(self,other) :
        if abs(self.num) == abs(other.num) :
            return self.num < other.num
        else :
            return abs(self.num) < abs(other.num)

for _ in range(n) : # _는 변수를 안쓰는 관행이라고 한다.
    new = int(sys.stdin.readline().rstrip())
    if new == 0 :
        if q.empty() :
            print(0)
        else :
            inst = q.get()
            print(inst.num)
    else :
        q.put(_abs(new))