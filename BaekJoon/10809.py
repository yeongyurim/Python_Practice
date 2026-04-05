<<<<<<< HEAD
arr1 = input()
alphas = [-1 for i in range(26)]
for i in alphas :
    print(i)
=======
string = input()
positions = [-1] * 26
order = 0
for i in string :
    idx = ord(i) - ord('a')
    positions[idx] =  order if positions[idx] == -1 else positions[idx]
    order += 1
for i in positions :
    print(i, end=" ")
>>>>>>> 28c4ca735600c2da89239bcee3c64fb7de5ef7d6
