import sys
n, c = map(int,input().split())

nlist = [int(sys.stdin.readline()) for _ in range(n)]
nlist.sort()

start, end = 0, nlist[-1] - nlist[0]
result = 0
curr = 0
while start <= end :
    mid = (start+end) // 2
    result = mid - start
    curr *= 2
    if c > curr :
        start = mid + 1
    else :
        end = mid - 1
print(end)
    
    
