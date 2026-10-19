arr = [2,3,4,5]
for i in range(1 << len(arr)) :
    print([arr[j] for j in range(len(arr)) if i & (1 << j)])