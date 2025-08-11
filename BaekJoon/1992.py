import sys

def grouper(A, r, c, N) :
    global result
    if N <= 1 :
        if A[r][c] == 1 :
            result.append('1')
        else :
            result.append('0')
        return
    flag = A[r][c]
    for i in range(r, r+N) :
        for j in range(c , c+N) :
            if flag != A[i][j] :
                result.append('(')
                grouper(A,r     ,c     ,N//2)
                grouper(A,r     ,c+N//2,N//2)
                grouper(A,r+N//2,c     ,N//2)
                grouper(A,r+N//2,c+N//2,N//2)
                result.append(')')
                return
    if flag == 1 :
        result.append('1')
    else :
        result.append('0')
    
n = int(input())
result = []
arr = []
for i in range(n) :
    arr.append(list(map(int,sys.stdin.readline().rstrip())))
grouper(arr, 0, 0, n)
print(''.join(result))