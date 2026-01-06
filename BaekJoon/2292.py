n = int(input())
lev = 1
c = 1
while n>c :
    c = c + lev * 6 + 1
    lev += 1
print(lev)