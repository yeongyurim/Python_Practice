F = []
def IterFibo(n):
    F.append(0)
    F.append(1)
    for i in range(2,n+1):
        F.append(F[i-1] + F[i-2])
    return F[len(F)-1]

print(IterFibo(int(input())))
