n = int(input())
arr = list(map(int,input().split()))

# 2가지를 선택하고 배열에서 제외하여야 함
def findMax(idx,C):
    global arr
    arr[idx]