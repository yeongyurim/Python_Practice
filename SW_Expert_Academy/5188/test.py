import sys
sys.setrecursionlimit(10000)
sys.stdin = open("SW_Expert_Academy/5188/sample_input.txt", "r")

def is_pos_valid(pos,n):
    flag = True
    x,y = map(int,pos)
    if x<0 or x>=n :
        return False
    if y<0 or y>=n :
        return False
    return flag

def recur(lis, x, y, total):
    global min
    n = len(lis)
    total += lis[x][y]

    if x == n-1 and y == n-1:
        if min > total:
            min = total
    if is_pos_valid([x,y+1],n):
        recur(lis,x,y+1,total)
    if is_pos_valid([x+1,y],n):
        recur(lis,x+1,y,total)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    lis = [list(map(int, input().split())) for i in range(n)]
    min = float('inf')
    recur(lis,0,0,0)
    print(min)




