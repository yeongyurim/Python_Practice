import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = [-1 for _ in range(n)]
s = 9999
def finder(t) :
    global n, arr
    if n == t :
        return 0
    if n < t :
        return s
    
    if arr[t] != -1 :
        return arr[t]
    path1 = 1 + finder(t+3)
    path2 = 1 + finder(t+5)

    arr[t] = min(path1, path2)
    return arr[t]

result = finder(0)
print(arr)
if result >= s:
    print(-1)
else :
    print(result)