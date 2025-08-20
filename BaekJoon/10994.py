def printStars(n, x, y) :
    global arrD2
    length = n * 4 - 3
    if n == 1 :
        arrD2[x][y] = "*"
        return
    else :
        for i in range(length) :
            arrD2[x][y+i] = "*"
            arrD2[x+i][y] = "*"
            arrD2[x+length-1][y+i] = "*"
            arrD2[x+i][y+length-1] = "*"
    n -= 1
    x = x+2
    y = y+2
    printStars(n,x,y)

n = int(input())
length = n * 4 - 3
arrD2 = [[' ' for _ in range(length)] for _ in range(4*n-3)]
printStars(n, 0, 0)
for i in arrD2 :
    print(''.join(i))