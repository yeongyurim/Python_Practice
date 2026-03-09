n = int(input())
for i in range(n) :
    r,s = input().split()
    r = int(r)
    p = ""
    for idx in range(len(s)) :
        for j in range(r) :
            p += s[idx]
    print(p)
