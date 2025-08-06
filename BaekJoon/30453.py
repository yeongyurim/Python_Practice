import sys

n = int(input())

def getPoint(x1,x2,y1,y2) :
    x = (x1 + x2)/2
    y = (y1 + y2)/2
    return (x,y)

S = []
P = {}
max = -999999
for i in range(n) :
    x,y = map(int,sys.stdin.readline().rstrip().split())
    S.append((x,y))

for i in S :
    x1, y1 = i
    for j in S :
        x2, y2 = j
        p = getPoint(x1,x2,y1,y2)
        if p not in P :
            P[p] = set() # 중복 방지용
        P[p].add(i)
        if i != j :
            P[p].add(j)

for key in P.keys() :
    if len(P[key]) > max :
        max = len(P[key])
print(max)