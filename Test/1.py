def IterFibo(n):
    if n == 0:
        return 0
    F = [0] * (n + 1)
    F[0] = 0
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]

# 예시 실행
print(IterFibo(20))  # 출력: 55
