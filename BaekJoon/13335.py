from collections import deque
import sys

n, w, L = map(int, sys.stdin.readline().split())
q1 = list(map(int, sys.stdin.readline().split()))

q2 = deque([0] * w) # 길이가 w이고 값을 0으로 deque을 초기화
t = 0
tL = 0

while q2 : # q2에 있는 원소를 모두 빼내었을 때
    t += 1
    out = q2.popleft()
    tL -= out

    if q1:
        if tL + q1[0] <= L:
            q2.append(q1[0])
            tL += q1.pop(0)
        else:
            q2.append(0)
print(t)