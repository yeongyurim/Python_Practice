a = tuple(map(int,input("입력 :").split(' ')))
b = tuple(map(int,input("       ").split(' ')))
c = []
for i in range(len(a)) :
    c.append(a[i] * b[i])
c = tuple(c)
print(c)
