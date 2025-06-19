import sys
from queue import Queue
queue = Queue()

n = int(input())
results= [[],[],[]] # 출력과정에서 학생이 없는 경우를 검사하기 위해 리스트로 묶었다.
for i in range(n) :
    line = list(map(int,sys.stdin.readline().strip().split())) # input 보다 훨씬 빠르게 동작
    if line[0] == 1 : # 1번 유형에 대한 분기
        id, menu = line[1:]  # 학생 번호와 메뉴 번호에 대한 전처리
        queue.put([id,menu]) 
    else : # 2번 유형에 대한 분기
        menu = line[1] # 도착한 메뉴 번호에 대한 전처리
        id, id_menu = queue.get()
        if id_menu == menu : # 좋아하는 메뉴를 먹은 경우
            results[0].append(id)
        else : # 좋아하는 메뉴를 먹지 못한 경우
            results[1].append(id)
            
while not queue.empty() : # 아무 메뉴도 먹지 못한 경우
    results[2].append(queue.get()[0])

for result in results : # 결과에 대한 출력
    if not result : # 학생 목록에 학생이 없는 경우
        print("None")
    else :
        result.sort() # 오름차 순 출력을 위한 정렬
        print(' '.join(map(str,result)))