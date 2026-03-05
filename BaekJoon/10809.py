string = input()
positions = [-1] * 26
order = 0
for i in string :
    idx = ord(i) - ord('a')
    positions[idx] =  order if positions[idx] == -1 else positions[idx]
    order += 1
for i in positions :
    print(i, end=" ")