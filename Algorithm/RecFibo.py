def RecFibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return RecFibo(n-1) + RecFibo(n-2)

print(RecFibo(40))