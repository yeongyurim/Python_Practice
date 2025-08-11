import sys

def getPossibleCombinations(arr, path, idx):     
    if len(path) == 6 :
        print(*path) # *을 사용하면 리스트를 공백으로 구분하여 출력한다.
        return
    
    for i in range(idx, len(arr)):
        path.append(arr[i])
        getPossibleCombinations(arr, path, i+1)
        path.pop()

while True:
    line = sys.stdin.readline().rstrip()
    if line == '0' : # 입력의 끝을 알리는 '0'이 들어오면 루프 종료
        break
    
    testCase = list(map(int, line.split()))
    k = testCase[0]
    numbers = testCase[1:]
    
    getPossibleCombinations(numbers, [], 0)
    
    print()