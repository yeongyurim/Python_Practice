def add() :
    print("Empty") # 1 매개변수 X, 반환값 X

def add(x, y) : # 2 매개변수 O, 반환값 X
    print(x+y)

def add() : # 3 매개변수 X, 반환값 O
    return 5

def add(x, y) : # 4 매개변수 O, 반환값 O
    return x+y

def print_args(*args) :
    print(args)

print_args(1, 2, 3) # 인자의 개수를 모를 떄 유용 튜플처럼 동작

def print_kwargs(**kwargs) :
    print(kwargs)
    
print_kwargs(a=1, b=2, c=3) # key=value 형태의 인자 전달하고 딕셔너리로 받는다.

add = lambda x, y : x + y
# 한 줄로 작성할 수 있는 간단한 함수
# lamda 키워드 다음에 매개변수를 적고 : (콜론) 뒤에 반환할 표현식을 쓴다.

class Member :
    
    # 속성 생성
    def __init__(self, name, age, address) :
        self.name = name
        self.age = age
        self.address = address
    
    # 메소드 생성
    def info(self):
        print("저의 이름은 {0}이고, 나이는 {1}, 사는곳은 {2} 입니다".format(self.name, self.age, self.address))

# Member의 introduce 인스턴스 생성
introduce = Member('ssf', 25, '수원시')

# introduce 인스턴스의 info 메서드 호출
introduce.info()

class Animal:
    def speak(self):
        print('동물이 소리를 냅니다.')
    
class Dog(Animal) :
    def speak(self): # 오버라이딩
        print("멍멍!")
    
class Cat(Animal) :
    def speak(self): # 오버라이딩
        print("야옹~")
        
#사용예
a = Animal()
a.speak() # 출력: 동물이 소리를 냅니다.

d = Dog()
d.speak() # 출력: 멍멍!

c = Cat()
c.speak() # 출력: 야옹~