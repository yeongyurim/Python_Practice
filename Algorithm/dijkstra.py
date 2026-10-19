import heapq

def dijkstra(graph, start):
    # 1. 출발지로부터의 거리를 모두 무한대로 초기화
    # 인덱스를 노드 번호와 맞추기 위해 (노드 개수 + 1) 크기로 생성
    distances = {node: float('inf') for node in graph}
    
    # 출발 노드까지의 거리는 0으로 설정
    distances[start] = 0
    
    # 2. 우선순위 큐 생성 및 (거리, 노드) 형태로 시작 노드 삽입
    # heapq는 튜플의 첫 번째 원소(거리)를 기준으로 최소 힙을 구성함
    queue = []
    heapq.heappush(queue, (distances[start], start))
    
    while queue:
        # 3. 가장 거리가 짧은 노드 정보를 꺼냄 (수식에서의 argmin 역할)
        current_distance, current_node = heapq.heappop(queue)
        
        # 큐에서 꺼낸 거리가 이미 기록된 최단 거리보다 크다면 무시 (이미 방문 처리된 효과)
        if distances[current_node] < current_distance:
            continue
            
        # 4. 현재 노드와 인접한 이웃 노드들을 확인 (Relaxation 단계)
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 더 짧은 경로를 발견한 경우 최단 거리 테이블 업데이트
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                # 변경된 최단 거리를 우선순위 큐에 삽입
                heapq.heappush(queue, (distance, adjacent))
                
    return distances

# --- 테스트를 위한 그래프 세팅 ---
# 딕셔너리를 활용해 인접 리스트 형태로 그래프를 표현합니다.
# 예: 'A': {'B': 5, 'C': 1} -> A에서 B로 가는 거리는 5, C로 가는 거리는 1
my_graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3, 'F': 2},
    'F': {'D': 6, 'E': 2}
}

# 'A' 노드를 출발지로 설정하여 다익스트라 실행
result = dijkstra(my_graph, 'A')

# 결과 출력
print("출발지 'A'로부터 각 노드까지의 최단 거리:")
for node, dist in result.items():
    print(f"노드 {node} : {dist}")