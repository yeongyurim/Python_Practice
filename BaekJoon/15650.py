def findPossibleCombinations(N, M, arr, idx):
    if len(arr) == M :
        result.append(arr[:])
        return
    for i in range(1,N + 1):
        if arr and arr[-1] >= i:
            continue
        arr.append(i)
        findPossibleCombinations(N, M, arr[:], i+1)
        arr.pop()
result = []
N, M = map(int, input().split())
findPossibleCombinations(N, M,[],1)
for i in result :
    print(*i)