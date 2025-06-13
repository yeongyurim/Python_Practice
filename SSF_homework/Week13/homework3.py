class Order :
    def __init__(self, name, price, quantity) :
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total(self) :
        return self.price * self.quantity
    
def analyze_orders(orders) :
    totalPrice = 0
    totalOrder = 0
    avgPrice = 0
    
    for order in orders :
        totalPrice += order.total()
        totalOrder += 1
    
    avgPrice = totalPrice / totalOrder
    print("총 주문 금액: {0}원".format(totalPrice))
    print("주문 개수: {0}건".format(totalOrder))
    print("평균 주문 금액: {:.2f}원".format(avgPrice))
    
order1 = Order("키보드", 30000, 2)
order2 = Order("마우스", 15000, 3)
order3 = Order("모니터", 1200000, 1)

orders = [order1, order2, order3]
analyze_orders(orders)