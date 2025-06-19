from collections import deque
q = deque()
q2 = deque()

n = int(input())

for i in range(n) :
    temp = int(input())
    if temp != 0 :
        q.append(temp)
    else :
        if q :
            min = 100000
            while q :
                p = q.pop()
                if min > p :
                    min = p
                q2.append(p)
            q2.remove(min)
            while q2 :
                q.append(q2.pop())
            print(min)
        else :
            print('0')
