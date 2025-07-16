import sys
tree_map = {}
N = int(input())
for i in range(N) :
    ext = sys.stdin.readline().rstrip().split('.')[1]
    if ext in tree_map :
        tree_map[ext] = tree_map[ext] + 1
    else :
        tree_map[ext] = 1
key_list = sorted(tree_map.keys())

for i in key_list :
    print(i,tree_map[i])