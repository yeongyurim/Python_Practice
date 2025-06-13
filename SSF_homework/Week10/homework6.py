prices = {"apple":1000, "banana":500, "cherry": 1500, "orange": 1200}
max = -1000000
fruit = ""
for name in prices :
    if (prices[name] > max):
        max = prices[name]
        fruit = name
print("가장 비싼 과일:",fruit,"("+str(prices[fruit])+"원)")