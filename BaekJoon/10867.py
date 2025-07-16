n = int(input())
dic = {}
for i in map(int,input().split()) :
    dic[i] = 0
key_list = sorted(dic.keys())
print(' '.join(map(str,key_list)))
