def findPossibleCombinations(S, M, sum, idx):
    global result
    if idx == len(S) :
        if M == sum :
            result += 1
        return
    findPossibleCombinations(S, M, sum + S[idx], idx+1)
    findPossibleCombinations(S, M, sum, idx+1)
result = 0
N, M = map(int, input().split())
S = list(map(int, input().split()))
findPossibleCombinations(S, M, 0 ,0)
if M == 0 : # M이 0이면 들어가자마자 공집합에 대해서도 계수를 하기 때문에 빼줘야 함
    result -= 1
print(result)