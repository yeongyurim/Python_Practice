def hannoi(n, s, d) :
    global k, results
    if n == 1 :
        results.append((s,d))
        k += 1
        return
    # 보조 기둥의 계산공식 1 + 2 + 3 = 6 이므로 출발과 도착기둥이 정해지면 보조 기둥의 위치를 찾을 수 있다.
    a = 6 - s - d
    hannoi(n-1, s, a)
    hannoi(1  , s, d)
    hannoi(n-1, a, d)
k = 0
results = []
n = int(input())
hannoi(n,1,3)
print(k)
for i in results :
    print(*i)
