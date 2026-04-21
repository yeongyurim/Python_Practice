my_list = [1, 2, 3, 4, 5]
del my_list[0] # 첫 번째 요소 삭제 -> [2, 3, 4, 5]
print(my_list)
del my_list[1:3] # 인덱스 1부터 2까지 삭제 -> [2, 5]
print(my_list)

x=10
del x
#print(x) NameError: name 'x' is not defined

class MyClass:
    def __init__(self):
        self.a = 1
        self.b = 2

obj = MyClass()
del obj.a
# print(obj.a) # AttributeError: 'MyClass' object has no attribute 'a'