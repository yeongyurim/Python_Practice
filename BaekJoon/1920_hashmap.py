n = int(input())
nlist = [i for i in map(int,input().split())]

d = dict(zip(nlist,[1 for _ in range(len(nlist)) ]))
m = int(input())
mlist = [i for i in map(int,input().split())]

for i in mlist :
    print(d.get(i,0))