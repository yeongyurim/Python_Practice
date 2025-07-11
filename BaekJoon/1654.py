import sys
line = sys.stdin.readline

K, N = map(int, line().split())
Ks = [int(line()) for _ in range(K)] #리스트 컴프리핸션을 통해 바로 리스트를 초기화 시킬 수 있다.

start, end = 1, max(Ks) # 설정할 수 있는 가장 긴 길이는 Ks중 가장 긴 랜선의 길이 이므로

while start <= end : #1에서 가장 긴 길이 사이에서 조사
    mid = (start + end) // 2
    lines = 0 # 잘린 랜선의 수
    for i in Ks :
        lines += i // mid # 현재 길이로 잘른 랜선의 수
    
    if lines >= N : # 랜선의 길이가 더 길어질 수 있다면
        start = mid + 1 # 더 긴 길이를 조사한다.
    else : #랜선의 길이가 더 길어질 수 없다면
        end = mid -1 # 더 짧은 길이를 조사한다.
print(end)
    
