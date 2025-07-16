import sys
N, M = map(int,input().split())
dic = dict()
li = []
for i in range(N+M) :
    line = sys.stdin.readline().rstrip()
    if line in dic :
       li.append(line)
    else :
        dic[line] = 0
li = sorted(li)
print(len(li))
for i in li :
    print(i)