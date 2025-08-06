import queue

q = queue.PriorityQueue()

class Data :
    def __init__(self, number, name, nickname) :
        self.number = number
        self.name = name
        self.nickname = nickname
        
    def __lt__(self,other) :
        return self.name < other.name # 객체의 name을 비교한다.

q.put(Data(5, '도롱뇽', '바보'))
q.put(Data(2, '개구리', '쩜프'))
q.put(Data(3, '효도르', '주먹'))
q.put(Data(1, '박효신', '신'))

while not q.empty() :
    inst = q.get()
    print((inst.number, inst.name, inst.nickname))