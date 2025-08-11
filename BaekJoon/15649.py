def findPossibleCombinations(N, M, arr, idx):
    if 
    if len(arr) == M :
        result.append(arr)
        return
    for i in range(idx,N):
        findPossibleCombinations(i, M, arr[:], i+1)
        arr.append(i)
        findPossibleCombinations(i, M, arr[:], i+1)
result = []
N, M = map(int, input().split(),[], 0)
