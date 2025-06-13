matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,1,2,3],
    [4,5,6,7]
    ]
sum = 0

for i in range(len(matrix)) :
    for j in range(len(matrix[i])) :
        if(i==j) :
            sum += matrix[i][j]
matrix = matrix[::-1]
for i in range(len(matrix)) :
    for j in range(len(matrix[i])) :
        if(i==j) :
            sum += matrix[i][j]

print(sum)