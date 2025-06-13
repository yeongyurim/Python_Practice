a, b = map(int,input("예제 입력:\n").split(' '))
list = [i for i in list(map(int,input().split(' '))) if i < b]
print(list)